#!/usr/bin/env python3
"""style_check.py — mechanical checks for the note-writing voice.

The three failure modes that made the first drafts unreadable, made countable:

  1. SENTENCE BLOAT   — sentences written for compression, not comprehension.
  2. UNGLOSSED JARGON — a technical term used before it is explained.
  3. GLOSSING         — sections wildly uneven in depth, because the source was
                        thin, not because the topic is small.

Usage: style_check.py FILE...    (exit 1 if any file breaches a limit)
"""
import re
import sys
import statistics

LIMITS = {
    "long_sentence": 30,     # words
    "very_long": 45,         # words — always a rewrite
    "bloat_ratio": 0.12,     # share of sentences over long_sentence
    "unglossed": 8,          # per 1000 sentences, roughly per file
    "section_words": 120,    # a concept section under this is probably glossed
    "section_ratio": 3.5,    # max/min concept size within a kit
}

# words that look technical: morphology of medical/engineering vocabulary
TECH = re.compile(
    r"\b\w+(?:osis|itis|pathy|genic|plasia|aemia|emia|uria|ectomy|plasty|"
    r"static|tropic|lytic|philic|phobic|metry|scopy|oidal)\b", re.I)

GLOSS = re.compile(r"—|–|\bmeans\b|\bi\.e\.|\bthat is\b|\bwhich is\b|\bcalled\b|\bknown as\b|\(|\bthink of\b|\bimagine\b", re.I)


def prose(raw):
    """Body prose only: headings, tables and rules dropped; each bullet becomes
    its own paragraph so a list is not read as one long sentence."""
    raw = re.sub(r"```.*?```", "", raw, flags=re.S)
    out, buf = [], []

    def flush():
        if buf:
            out.append(" ".join(buf))
            buf.clear()

    for line in raw.split("\n"):
        s = line.strip()
        if not s or s.startswith(("#", "|", "---", ">", "!")):
            flush()
            continue
        if re.match(r"^\*\*[^*]+\*\*$", s):      # a bare label line
            flush()
            continue
        if re.match(r"^([-*]|\d+\.)\s+", s):       # a bullet starts a new thought
            flush()
            buf.append(re.sub(r"^([-*]|\d+\.)\s+", "", s))
            continue
        buf.append(s)
    flush()
    return "\n\n".join(out)


def sentences(text):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.split()) > 2]


def concept_sizes(raw):
    sizes, cur = {}, None
    for line in raw.split("\n"):
        m = re.match(r"^### (\d+\.\d+[^\n]*)", line)
        if m:
            cur = m.group(1)[:70]
            sizes[cur] = 0
        elif cur:
            sizes[cur] += len(line.split())
    return {k: v for k, v in sizes.items() if v > 20}


def analyse(path):
    raw = open(path, encoding="utf-8").read()
    sents = sentences(prose(raw))
    lens = [len(s.split()) for s in sents]
    long_s = [s for s in sents if len(s.split()) > LIMITS["long_sentence"]]
    very_s = [s for s in sents if len(s.split()) > LIMITS["very_long"]]

    unglossed, seen = [], set()
    for s in sents:
        if GLOSS.search(s):
            continue
        for m in TECH.finditer(s):
            w = m.group(0).lower()
            if w not in seen:
                seen.add(w)
                unglossed.append((w, s[:80]))
    # a term glossed later is still a first-use problem, so we do not re-scan

    sizes = concept_sizes(raw)
    vals = list(sizes.values())
    ratio = (max(vals) / min(vals)) if vals and min(vals) else 0

    return dict(
        path=path, n=len(sents),
        mean=statistics.mean(lens) if lens else 0,
        median=statistics.median(lens) if lens else 0,
        long_n=len(long_s), very=very_s,
        bloat=(len(long_s) / len(sents)) if sents else 0,
        unglossed=unglossed, sizes=sizes, ratio=ratio,
        small=sorted([(k, v) for k, v in sizes.items() if v < LIMITS["section_words"]], key=lambda x: x[1]),
    )


def main(paths):
    bad = 0
    print(f"{'file':46s} {'sent':>5s} {'med':>4s} {'mean':>5s} {'>30':>4s} {'>45':>4s} {'bloat':>6s} {'ungl':>4s} {'size':>6s}")
    for p in paths:
        r = analyse(p)
        if not r["n"]:
            print(f"{p.split('/')[-1]:46s}  (no prose found)")
            continue
        fail = (r["bloat"] > LIMITS["bloat_ratio"] or len(r["unglossed"]) > LIMITS["unglossed"]
                or r["ratio"] > LIMITS["section_ratio"] or len(r["very"]) > 0)
        bad += bool(fail)
        print(f"{p.split('/')[-1]:46s} {r['n']:5d} {r['median']:4.0f} {r['mean']:5.1f} "
              f"{r['long_n']:4d} {len(r['very']):4d} {r['bloat']*100:5.0f}% {len(r['unglossed']):4d} "
              f"{r['ratio']:5.1f}x {'FAIL' if fail else 'ok'}")
        if fail:
            for s in r["very"][:3]:
                print(f"   {len(s.split())}w: {s[:150]}…")
            for w, ctx in r["unglossed"][:5]:
                print(f"   unglossed '{w}': {ctx}…")
            for k, v in r["small"][:3]:
                print(f"   thin section {v}w: {k}")
    print(f"\n{len(paths)} files, {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
