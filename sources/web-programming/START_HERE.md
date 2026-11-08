# START HERE — 20CST461 Web Technologies · ESE kit

Built 08 Nov 2026 from the faculty Question Bank (286 questions). Every question in the bank is covered by exactly one kit.

## What you study

| Module | Kit | Bank questions | Coverage |
|---|---|---|---|
| 1 · WWW & HTML5 | `KIT_M1_WWW_HTML.md` | Q1–36 · Q161–185 (61) | 100% |
| 2 · CSS & JavaScript | `KIT_M2_CSS_JS.md` | Q37–67 · Q186–202 · Q222–228 (55) | 100% |
| 3 · Introduction to PHP | `KIT_M3_PHP.md` | Q68–91 · Q203–221 (43) | 100% |
| 4 · PHP + MySQL | `KIT_M4_PHP_MYSQL.md` | Q92–129 · Q229–253 (63) | 100% |
| 5 · JSON & Laravel | `KIT_M5_JSON_LARAVEL.md` | Q130–160 · Q254–286 (64) | 100% |

(Each kit's §1 table lists every question number and the section that answers it, so you can jump straight to any question.)

Each kit has the same seven sections: coverage table → deep dive → 3-mark answers → 14-mark answers → hand-writable drills → night-before memorize table → "say this if grilled" lines.

## Exam pattern this is built for

**ESE: 3 hours, 100 marks.**
- **Part A — 10 × 3 = 30 marks.** Exactly **2 questions per module**, all compulsory, short answers.
- **Part B — 5 × 14 = 70 marks.** One question per module, **choose 1 of 2**. This is where the paper is won: 5 answers, ~35 minutes each.

So each module is worth ~20 marks and *cannot be skipped* — a module you haven't touched costs you both of its Part-A marks and its whole Part-B choice.

## How to use a kit (per module, ~2 hours)

1. **§2 deep dive** — read once. Don't memorise; just make the story click (analogy → term → code).
2. **§3.1 Part-A masters** — cover the right column and say the 3 points out loud. These are the exact 3-mark answers; there are only ~15–25 of them per module because the bank repeats itself.
3. **§3.2 Part-B skeletons** — read the *Structure* line first, then the code. You are memorising the **shape** (what goes in which order, what to draw), not the prose.
4. **§4 drills** — write each one on paper, closed book, then compare. This is the only step that converts reading into marks in a 3-hour writing exam.
5. **§5 memorize table** — final 20 minutes before you sleep, and again on exam morning.

## Order of attack (highest return first)

1. **M4 PHP+MySQL** — the most predictable block in the paper: connect → query → fetch loop → render, plus session/cookie. Its 14-mark questions are near-identical variants of five programs. Do this first; it also feeds M3's form questions.
2. **M3 PHP** — code-heavy, same five program shapes each year (factorial/prime/palindrome/Armstrong/vowels, arrays, regex validation, form processing). Synergy with M4 is large.
3. **M5 JSON + Laravel** — most *memorisation*-heavy and least code-risk: JSON syntax + types + schema keywords, then a fixed Laravel vocabulary (MVC, routing, middleware, route model binding, Blade, redirects). Two hours of vocabulary drilling buys ~20 marks.
4. **M1 HTML** — easy marks, but the volume of small facts (attributes, entities, input types) is where careless 3-mark answers leak. Learn the memorize table cold.
5. **M2 CSS + JS** — the box model, positioning, selector specificity, three attachment methods, plus JS fundamentals + DOM + form validation. The CSS half is mechanical; the JS half needs the 20 drills written once.

## Cross-module links that examiners love to exploit

- **Forms:** HTML `<form action method>` (M1) → `$_GET`/`$_POST` + validation (M3) → insert into MySQL (M4). One storyline across three modules; if they ask a 14-mark "user registration system", it is all three.
- **State:** HTTP is stateless (M1) → cookies/sessions (M4) → login state recommendation (M4 Q247).
- **Client vs server validation:** JS validates in the browser (M2 Q228) but the server must validate again (M3 Q208/Q229).
- **Data shapes:** JS objects/arrays (M2) → JSON syntax and types (M5) → JSON Schema validation (M5) → `json_encode`/`json_decode` (M5).
- **From raw to framework:** `mysqli_query` + loop (M4) → MVC + Eloquent/Laravel (M5). A good "why Laravel" answer cites the M4 pain points.

## Known facts about your source files

- `question_bank.md` — converted from `Question Bank.pdf` (14 pages, full text layer).
- `module2_fixed.md` — **the real Module 2 deck**. `WEB PROGRAMMING MOD-2.md` is a corrupted copy of Module 1 (identical file, same headings) — never study from it.
- `module5.md` — converted from `module 5.pdf` (28 pages). The M5 kit cites `5:pN` page numbers.
- `module3.md` / `module4.md` — unchanged; the M3/M4 kits cite `3:L…` / `4:L…` line numbers.
- The faculty bank's **module headings are shifted by one** from Q122 onward (its "Module 3: JSON and Laravel" section actually holds PHP questions). The kits use the syllabus mapping: M3 = PHP, M4 = PHP+MySQL, M5 = JSON+Laravel.
- Slide content the deck does not cover (JSON Schema keywords, responsive images, HTTP message format, file uploads) is present in the kits but **marked "(standard, not in your deck)"** — safe to write in the exam, but you were not taught it from these slides.

## How to continue in a new chat

> Web Programming ESE prep — read /home/haze/study/Web Programming/wp_study_tracker.md and START_HERE.md, then drill me on Module 4 Part B.

Ask for a **mock paper** when you have covered all five: 2 Part-A questions per module + one 14-mark paper per module drawn from the bank, timed at 3 hours.
