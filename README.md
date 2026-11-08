# minotes

Lecture notes, exam kits and trackers — written in Markdown, published as a static site.

Live: **https://minotes.vercel.app** (once the Vercel project is imported)

```
index.html                  hub — one card per subject
web-programming/
  index.html                library for that subject (filterable)
  start-here.html           plan + how to use the kits
  m1-html.html … m5-json-laravel.html   the five study kits
  question-bank.html        all 286 faculty questions
  notes-m1.html … notes-m5.html         lecture notes
  tracker.html, revision-log.html, drill-key.html
sources/web-programming/    the Markdown these pages were rendered from
tools/build.py              renderer: Markdown → HTML
tools/build.sh              sync sources + rebuild
```

Everything is plain static HTML with inline CSS and JS — no framework, no
runtime dependencies, no build step on the host.

## Features

- Sidebar table of contents per document, with the current section highlighted
- Reading progress bar, hover copy buttons on code blocks
- Light / dark theme (remembers your choice; follows the OS on first visit)
- Scrollable tables with sticky headers
- Print stylesheet — Ctrl+P gives clean pages without the chrome
- Fully offline: no CDN, no web fonts, no tracking

## Adding notes

**A new document in an existing subject**

1. Drop the `.md` file into `sources/web-programming/`.
2. Add a row to that subject's `docs` list in `tools/build.py`:
   `("my-note.md", "Sidebar label", "sub line", "card blurb", "Card title", "kits", "my-note")`
   (the last field is the output filename without `.html`; `group` is one of
   `start`, `kits`, `source`, `progress`).
3. Rebuild, commit, push.

```bash
./tools/build.sh
git add -A && git commit -m "add my-note" && git push
```

**A new subject**

Create `sources/<subject>/`, copy the subject dict in `tools/build.py` and
change `slug`, `title`, `code`, `tagline`, `blurb` and `docs`. The hub picks it
up automatically.

## Build requirements

Python 3 with [`markdown`](https://pypi.org/project/Markdown/) (the notes were
built with the venv at `~/.venvs/study`):

```bash
uv venv ~/.venvs/study && uv pip install --python ~/.venvs/study/bin/python markdown
```

`tools/build.sh` also copies the Markdown from the working folder
(`~/study/Web Programming`) into `sources/web-programming/` before building, so
the published copy always matches what is being studied. Skip that step on a
machine without the folder — the build falls back to the committed sources.

## Practice drills

`/<subject>/practice.html` — a small self-contained app page (no Markdown source).

Ten combined tasks, two per module:

| Type | What you do | Checked by |
|---|---|---|
| **fill** | scaffolds with inline blanks (`{{1}}`…); you type only the missing syntax | instant, per-blank, in the browser |
| **write** | full answer from scratch | “Grade with tutor” → `/api/chat`, marks lost and exact fixes |
| **output** | predict what a snippet prints | normalised text compare |
| **mcq** | one of four | instant, with the reasoning |

The fill drills are deliberately wide — one HTML page with 19 blanks, one PHP
script with 9 — so each attempt touches most of a module instead of 30 tiny
questions. Progress is kept in `localStorage`; “Mark done” ticks a drill.

Adding a drill: edit `tools/drills.py` (schema in the docstring), rebuild. No
other file needs touching.

## Ask-this-page assistant

Every document page has a small assistant: **select any text → "Ask about this"**, or press the ✳ button to ask about the section you are reading. Answers stream in from `api/chat.js` (a Vercel function) using the opencode-go endpoint.

**Context sent per question:** the selected text, the section it sits in (≤3 000 chars), the page outline, and the page title. No index, no vector store — the page is the context, which keeps it fast and cheap.

**Required env var on the host** (Vercel → Project → Settings → Environment Variables):

| Name | Value |
|---|---|
| `OPENCODE_GO_API_KEY` | your opencode-go key |

Optional:

| Name | Default | Notes |
|---|---|---|
| `CHAT_MODEL` | `deepseek-v4.1-flash` | `glm-5.3-flash` answers in ~1.3 s vs ~5.8 s (measured), same provider |
| `OPENCODE_GO_BASE_URL` | `https://opencode.ai/zen/go/v1` | |
| `CHAT_ALLOW_ORIGINS` | same-origin + `*.vercel.app` | comma-separated allowlist if you add a custom domain |

**Abuse limits** (the endpoint is public): origin check, 20 requests/minute per IP per warm instance, 500 output tokens. It is a convenience guard, not a security boundary — if the URL gets hammered, rotate the key.

Local test:

```bash
OPENCODE_GO_API_KEY=... node tools/dev-server.js      # static site + /api/chat
node tools/test-chat.js "why is $_POST safer than $_GET?" "some selected text"
```

## Deploying

Vercel → **Add New → Project → Import** `sebastian-abraham/minotes`:

- Framework preset: **Other**
- Build command: *(empty)*
- Output directory: *(empty — the repo root is the site)*
- Root directory: *(empty)*

Every push to `main` redeploys automatically. GitHub Pages works too: Settings →
Pages → Deploy from branch → `main` / `/ (root)`.
