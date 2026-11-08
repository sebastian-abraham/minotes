# 📚 20CST461 Web Programming — Study Tracker

> **ACTIVE TARGET: ESE — all 5 modules** (3 hrs · 100 marks)
> Set up 24 Sep 2026 for Internal Test II (M3–M4); **re-scoped 08 Nov 2026 to the full ESE** now that the faculty Question Bank (286 questions) is in the folder.
> **Per-module study kits are built** — see §"Module kits" below. Modules 1 & 2 were previously "done"; they now have kits too, because the ESE pulls 2 Part-A + 1 Part-B from every module.

## ▶️ How to start a session (new chat)

Paste this into a fresh chat:

> **Web Programming exam prep — read /home/haze/study/Web Programming/wp_study_tracker.md, then start Session 2.**

**My side of the loop:** read this tracker → read the relevant line ranges of `module3.md` / `module4.md` (line refs below) → **PART 1** Deep Dive (notes-first, every term from scratch) → **PART 2** Exam Kit (skeletons for all possible questions + 🔴 memorize lists) → **PART 3** code drills (write-it / predict-the-output, with answers) → grade with specific corrections → append to `wp_revision.md` + `wp_code_drills.md` → update tables and Session Log here.

---

## Exam profile

**ESE (end-semester, official — from `Web Programming Syllabus.pdf` p4):** 3 hrs · 100 marks
- **Part A:** 10 questions × **3 marks** (2 per module, all compulsory) → 30
- **Part B:** 5 questions × **14 marks** (2 per module, answer any **one**) → 70
- CIE 50 = Internal Test I 12.5 + **Internal Test II 12.5** + assignments 15 + attendance 10
- Internal tests: **2-hour duration** (syllabus p2, "Course Implementation Clock")
- ⚠️ No internal-test paper for this course exists in the folder — internal format unconfirmed. ESE pattern above is the official one. **Marks split drives skeleton length: 3-mark = 3 points; 14-mark = full program + explanation.**

**🎯 Exam intel for this course (from Haze, Sep 2026):**
1. **Modules 3 & 4 are CODE-heavy** — both modules are mostly syntax and programs. Expect *write a PHP program / predict the output / write the form-processing script / write the connect-query-loop-render page*.
2. **Haze is a first-time PHP learner** — read the slides once, no practice yet. Every term gets explained from zero; no assumed PHP familiarity (C is a pre-requisite, so C-shape analogies are fine and welcome).
3. Priority = **syntax you can reproduce by hand** (no interpreter in the exam): exact tags, `$`, `;`, `.` vs `+`, `->`, `=>`, `==` vs `===`, `$_POST` vs `$_GET`, connect → query → loop → render.

**Depth:** 🔵 understand · 🔴 memorize · **Confidence:** 🔴 weak · 🟡 okay · 🟢 strong

**Study method (my preferences):**
- Notes-first (module .md), PYQ/syllabus only set *priority*
- 3 parts per session: Deep Dive → Exam Kit → code drills
- Answer skeletons: numbered, attribution-free, matching the mark allocation
- Question prediction = **syllabus × PYQ cross-analysis**. Here: **no PYQs exist** → syllabus + the official ESE pattern + the deck's own slide titles are the only signals (see Prediction Map).

---

## 📁 Materials & tooling (this machine)

- Folder: `/home/haze/study/Web Programming`
- **PRIMARY TEACHING SOURCES:** `module3.md` (773 lines, 26 slides, PHP) · `module4.md` (858 lines, 26 slides, PHP+MySQL)
- `module3.pdf` / `module4.pdf` — source decks, **both have full text layers** (16.7k / 18.8k chars, 26 pp each). Conversion verdict (24 Sep 2026): all 26 slides of each deck are present in the .md with matching titles and code blocks — **nothing missing**. The only content the .md drops is the repeated slide chrome ("MODULE III · 1 HR TOPIC / 20CST461 / slide no."), which is correct.
- `Web Programming Syllabus.pdf` — **pure scan (0 extractable text)**. Read via rendered-page vision; modules III & IV transcribed into this tracker + the module tables below. To re-render: `~/.venvs/study/bin/python ~/.hermes/skills/study/study-tutor-sessions/scripts/render_pages.py "Web Programming Syllabus.pdf" /tmp/wpscan 1 2 3 4` (or pymupdf `get_pixmap(dpi=170)`).
- `S7_QuestionPapers.pdf/.md` — scanned bundle; contains **20CST401 AI, 20CST421 Cloud Computing, 20CET453 EHS, 20MCN401 Industrial Safety only. ❌ No Web Programming paper.** → there is no PYQ evidence for this course; the Prediction Map is syllabus-derived only.
- **`phprun.py` — online PHP runner (3v4l.org). DORMANT — the exam is written, so we no longer verify outputs.** Kept only for the case where a claim is genuinely uncertain: `python3 phprun.py snippet.php`. **PHP is NOT installed locally** (needs sudo password); `sudo pacman -S php` would fix that (log it to `~/system-tweaks.md`). ✅ *(3v4l)* tags already in `wp_revision.md` came from this.
- `wp_revision.md` — **append-only revision notes** (I append; you read; never read back into context)
- `wp_code_drills.md` — **append-only drill workbook: answer key** (model answers for every drill set)
- **`answers.php` — YOUR fill-in worksheet.** Questions live in comment blocks with all scaffolding pre-typed; you fill only the blanks on the `// >>> FILL:` lines, then say "done" in chat and I grade it in place (Part A = graded feedback, Part B = current set). Never put the answer key in here.
- Line-ref legend: `3:L275` = `module3.md` line 275 · `4:L431` = `module4.md` line 431

---

## 📦 Module kits (built 08 Nov 2026 — these are the primary study artefacts now)

Every kit follows the same shape: **§1 coverage table (every bank question + where it is answered) → §2 Part-1 deep dive from zero → §3 Part-2 exam answer bank (3-mark masters + 14-mark skeletons with full code) → §4 Part-3 hand-writable drills → §5 night-before memorize table → §6 diagram index → §7 "say this if grilled" lines.**

| Module | Kit file | Lines | Bank questions covered | ESE value |
|---|---|---|---|---|
| 1 · WWW & HTML5 | `KIT_M1_WWW_HTML.md` | 61 (Q1–36, Q161–185) | 100% | ~20 marks |
| 2 · CSS & JavaScript | `KIT_M2_CSS_JS.md` | 55 (Q37–67, Q186–202, Q222–228) | 100% | ~20 marks |
| 3 · Introduction to PHP | `KIT_M3_PHP.md` | 43 (Q68–91, Q203–221) | 100% | ~20 marks |
| 4 · PHP + MySQL | `KIT_M4_PHP_MYSQL.md` | 63 (Q92–129, Q229–253) | 100% | ~20 marks |
| 5 · JSON & Laravel | `KIT_M5_JSON_LARAVEL.md` | 64 (Q130–160, Q254–286) | 100% | ~20 marks |
| — | `START_HERE.md` | — | plan + how to use the kits | — |

**Coverage verified programmatically on 08 Nov 2026:** all 286 bank questions appear in exactly one kit's coverage table, no duplicates, no gaps.

⚠️ **Question-bank numbering quirk (faculty typo, confirmed):** the bank's module headings for Q122–160 and Q203–286 are shifted by one — "Module 3: JSON and Laravel" actually holds PHP questions, "Module 4: PHP" holds PHP+MySQL, "Module 5: PHP and MySQL Database Operations" holds JSON/Laravel. The kits use the **content** mapping, which matches the syllabus:
- **M3 = PHP**, **M4 = PHP+MySQL**, **M5 = JSON+Laravel**.

⚠️ **Source-file fix:** `WEB PROGRAMMING MOD-2.md` was a byte-identical copy of Module 1 (same 33,332 bytes, same headings). The real Module 2 deck was re-converted to **`module2_fixed.md`** (22 pages, 985 lines) on 08 Nov 2026 — that is the file the M2 kit cites (`2:pN`). Treat the old MOD-2.md as dead.

---

## Syllabus scope (verbatim, from the scanned syllabus pp. 3–4)

**Module III — Introduction to PHP** (CO5 · 6 hrs · 20% ESE)
| Syllabus line | Hrs |
|---|---|
| Building blocks of PHP – Variables – Data Type – simple PHP program | 1 |
| Converting between Data Types – Operators and Expressions – Flow Control functions | 1 |
| Control Statements – Working with Functions | 1 |
| Initialising and Manipulating Arrays – Objects | 1 |
| Working with Strings – String processing with Regular expression – Pattern Matching | 1 |
| Form Processing and Business Logic | 1 |

**Module IV — PHP–MySQL** (CO4 · 6 hrs · 20% ESE)
| Syllabus line | Hrs |
|---|---|
| Cookies – Sessions | 1 |
| PHP and MySQL Integration – Connecting to MySQL with PHP | 1 |
| Working with MySQL data | 1 |
| Performing CREATE – DELETE – INSERT operations on MySQL table from PHP Program | 1 |
| Performing SELECT and UPDATE operations on MySQL table from PHP Program | 1 |
| Building Dynamic Content in PHP application | 1 |

**Coverage sweep (checked 24 Sep 2026): every syllabus line of M3 and M4 maps to ≥1 topic row below. Nothing skipped.** Module V (JSON–Laravel) is out of scope for this test; Modules I & II already done.

---

## Module 3 — Introduction to PHP

Source: `module3.md`. Slides per topic in brackets.

| # | Topic (syllabus ↔ slides) | Src (file:line) | Depth | Status | Conf | Notes |
|---|---|---|---|---|---|---|
| M3.1 | What PHP is; server-side vs client-side; the request–response cycle (browser → server → PHP engine → MySQL → plain HTML) | 3:L27–77 | 🔵 | ☐ | 🔴 | Know the 3-box flow diagram (3:L57) — a likely 3-mark "explain how PHP works" |
| M3.2 | **Embedding + variables + data types + simple program** — `<?php ?>`, `$var`, int/float/string/bool/array/NULL, `echo`, `;`, `gettype()`, `var_dump()` | 3:L84–127 | 🔴 | ☐ | 🔴 | The absolute base layer — must be automatic |
| M3.3 | Converting between data types — casts `(int)` `(float)` `(string)` `(bool)` `(array)`, `intval()`/`floatval()`/`strval()`/`boolval()`, `settype()`, `is_int()`/`is_string()`/`is_array()` | 3:L136–158 | 🔴 | ☐ | 🔴 | High-yield output-prediction fodder |
| M3.4 | Operators & expressions — arithmetic incl. `**`, assignment, `.` / `.=`, precedence, expression = anything with a value | 3:L166–189 | 🔴 | ☐ | 🔴 | `.` vs `+` is THE classic trap |
| M3.5 | Comparison & logical operators — `==` vs `===`, `!=` vs `!==`, `<` `>`, `&&` `\|\|` `!`, loose-typing comparison rules | 3:L197–219 | 🔴 | ☐ | 🔴 | "One of PHP's most exam-relevant quirks" — the deck says so itself |
| M3.6 | Flow control functions — `if/elseif/else`, `exit()`/`die()`, `return` | 3:L227–246 | 🔵 | ☐ | 🔴 | 4 named points = a 3-mark question |
| M3.7 | Control statements — `if`/`elseif`/`else`, `switch`/`case`/`break`/`default`, nesting, ternary | 3:L255–282 | 🔴 | ☐ | 🔴 | Write-a-program target |
| M3.8 | Loops — `for`, `while`, `do…while`, `foreach` (and `foreach … as $k => $v`) | 3:L291–315 | 🔴 | ☐ | 🔴 | Every 14-mark program needs a loop |
| M3.9 | Functions — declaration, call, `return`, hoisting, no-return → NULL | 3:L324–349 | 🔴 | ☐ | 🔴 | |
| M3.10 | Function parameters — default values, **scope** (`local` / `global` / `static`), **pass by value vs `&` by reference**, variadics `...$nums` | 3:L358–377 | 🔴 | ☐ | 🔴 | 4 named sub-points = ready-made exam question |
| M3.11 | Indexed arrays — init `[]` vs `array()`, access, append `$arr[] =`, `count()` | 3:L386–409 | 🔴 | ☐ | 🔴 | |
| M3.12 | Associative & multidimensional arrays — `key => value`, nested records, `foreach` with key | 3:L419–441 | 🔴 | ☐ | 🔴 | `=>` is a syntax must |
| M3.13 | Common array functions — `count`, `array_push`, `sort`/`rsort`, `array_map`, `array_filter`, `in_array`, (+`array_keys`, `array_values`, `array_merge`, `array_search`) | 3:L450–461 | 🔴 | ☐ | 🔴 | Table on 3:L452 = a 3-mark "list the functions" question |
| M3.14 | Objects & classes — `class`, `public`, `new`, `->`, `$this`, `__construct()`, methods | 3:L471–498 | 🔴 | ☐ | 🔴 | Write-a-class target; `->` not `.` |
| M3.15 | Strings — `strlen`, `strtoupper`/`strtolower`, `trim`, `substr` (+ single vs double quotes, interpolation, escaping) | 3:L508–529 | 🔴 | ☐ | 🔴 | |
| M3.16 | String manipulation — `.` / `.=`, `str_replace`, `explode`, `implode` (+ `strpos`, `strrev`, `ucfirst`, `sprintf`) | 3:L538–556 | 🔴 | ☐ | 🔴 | Fine |
| M3.17 | Regular expressions — PCRE, `preg_match`, `preg_replace`, `preg_split`, `/delimiters/` | 3:L568–586 | 🔴 | ☐ | 🔴 | |
| M3.18 | Pattern matching for validation — the 5-pattern table (`^`,`$`,`\d`,`\w`,`{n}`, char classes, quantifiers) | 3:L597–609 | 🔴 | ☐ | 🔴 | Memorize the 5 patterns verbatim |
| M3.19 | Reading form data — `$_GET` vs `$_POST`, `$_REQUEST`, `$_SERVER["REQUEST_METHOD"]`, `isset()` | 3:L619–637 | 🔴 | ☐ | 🔴 | The bridge to M4 |
| M3.20 | Validating & sanitizing input — `trim`, `htmlspecialchars`, `empty`, `preg_match`, `??` null-coalescing, `die()` | 3:L650–671 | 🔴 | ☐ | 🔴 | |
| M3.21 | Business logic — validation vs business rule, why separate, examples (eligibility/fee/grade) | 3:L684–705 | 🔵 | ☐ | 🔴 | |
| M3.22 | **Full form-processing script** (the 5-step pipeline: method check → read+trim → validate → business logic → respond) | 3:L718–740 | 🔴 | ☐ | 🔴 | **Prime 14-mark program candidate** |
| M3.23 | Module 3 recap's 8 takeaways (3:L754–770) | 3:L752–773 | 🔴 | ☐ | 🔴 | Fast revision list the night before |

## Module 4 — PHP–MySQL

Source: `module4.md`.

| # | Topic (syllabus ↔ slides) | Src (file:line) | Depth | Status | Conf | Notes |
|---|---|---|---|---|---|---|
| M4.1 | Why state management — HTTP is stateless, cookies (client) vs sessions (server), why both exist | 4:L27–53 | 🔵 | ☐ | 🔴 | 4 named points = 3-mark question |
| M4.2 | Cookies — `setcookie(name, value, expiry)`, `$_COOKIE`, delete via past expiry, must precede output, security limit, 4KB | 4:L63–88 | 🔴 | ☐ | 🔴 | Write-a-cookie script |
| M4.3 | Sessions — `session_start()`, `$_SESSION[key] = value`, persistence, `session_destroy()`, plus `unset()`/`session_unset()` | 4:L102–124 | 🔴 | ☐ | 🔴 | |
| M4.4 | Cookies vs sessions comparison table (storage, size, security, lifetime, good-for) | 4:L136–160 | 🔴 | ☐ | 🔴 | 5-row compare = 3-mark certain |
| M4.5 | Why pair PHP with MySQL — no persistence in plain PHP, relational tables, MySQL reasons (free, LAMP), the bridge `mysqli` vs `PDO` | 4:L170–195 | 🔵 | ☐ | 🔴 | |
| M4.6 | Connecting — procedural `mysqli_connect(host,user,pass,db)`, failure check, `mysqli_connect_error()`, `mysqli_close()` | 4:L206–230 | 🔴 | ☐ | 🔴 | **Memorize exact signature** |
| M4.7 | Connecting — OO style `new mysqli(...)`, `$conn->connect_error`, `$conn->query()`, `$conn->close()` | 4:L244–268 | 🔴 | ☐ | 🔴 | Both styles; know which is which |
| M4.8 | Connection best practices — no hardcoded creds, always check failure, close when done, prepared statements ahead | 4:L280–305 | 🔵 | ☐ | 🔴 | 4 points = 3-mark |
| M4.9 | Running queries — `mysqli_query($conn,$sql)` return type (result handle vs bool), `mysqli_error($conn)`, injection risk | 4:L316–337 | 🔴 | ☐ | 🔴 | |
| M4.10 | Fetching — `mysqli_fetch_assoc()` one row at a time, returns NULL at end, `while` loop, `mysqli_num_rows()` | 4:L351–370 | 🔴 | ☐ | 🔴 | The canonical loop |
| M4.11 | Other fetch styles — `fetch_array`, `fetch_row`, `fetch_object`, internal pointer advance | 4:L383–393 | 🔴 | ☐ | 🔴 | 5-row table = 3-mark "list" |
| M4.12 | The full cycle — build SQL → `mysqli_query()` → result handle → `while`+`fetch_assoc()` → echo HTML → browser table | 4:L405–419 | 🔴 | ☐ | 🔴 | Know the 5-step diagram (4:L399) |
| M4.13 | CREATE TABLE — syntax, `AUTO_INCREMENT PRIMARY KEY`, column types `INT`/`VARCHAR(n)`/`TEXT`/`DATE`/`DECIMAL`, run once at setup | 4:L431–453 | 🔴 | ☐ | 🔴 | |
| M4.14 | INSERT — `INSERT INTO t (cols) VALUES (vals)`, quote strings not numbers, `mysqli_insert_id($conn)` | 4:L468–490 | 🔴 | ☐ | 🔴 | |
| M4.15 | DELETE — `DELETE FROM t WHERE cond`, never omit WHERE, `mysqli_affected_rows($conn)`, SELECT-preview first | 4:L505–525 | 🔴 | ☐ | 🔴 | |
| M4.16 | CREATE/INSERT/DELETE quick-ref table + "all three are write ops" | 4:L538–546 | 🔴 | ☐ | 🔴 | |
| M4.17 | SELECT — `SELECT *` vs named columns, `WHERE`, SQL comparison ops incl. `LIKE` | 4:L558–580 | 🔴 | ☐ | 🔴 | |
| M4.18 | SELECT refinement — `ORDER BY col ASC/DESC`, `LIMIT n`, `LIMIT offset, count` (pagination) | 4:L595–615 | 🔴 | ☐ | 🔴 | |
| M4.19 | UPDATE — `UPDATE t SET col = val WHERE cond`, multi-column SET, missing WHERE = whole table, `affected_rows` | 4:L630–652 | 🔴 | ☐ | 🔴 | |
| M4.20 | Safe practices — SELECT-test the WHERE, `(int)` cast input, `mysqli_prepare()` with `?`, always check `affected_rows` | 4:L665–689 | 🔵 | ☐ | 🔴 | 4 points = 3-mark |
| M4.21 | Dynamic content — static vs dynamic, mixing PHP in HTML, separating data/logic/presentation (MVC precursor) | 4:L699–726 | 🔵 | ☐ | 🔴 | |
| M4.22 | **Looping rows into HTML** — `while (...):` … `endwhile;` alternative syntax, `<?= ?>`, `htmlspecialchars()` | 4:L735–755 | 🔴 | ☐ | 🔴 | Syntax must: `:` + `endwhile` |
| M4.23 | **Complete dynamic page** — connect → query → loop → render (4:L782 block) | 4:L770–792 | 🔴 | ☐ | 🔴 | **Prime 14-mark program candidate** |
| M4.24 | Looking ahead to Module V — JSON exchange, Laravel/Eloquent replacing raw `mysqli_query`, MVC | 4:L805–829 | 🔵 | ☐ | 🔴 | Only if asked "how does this scale" |
| M4.25 | Module 4 recap's 8 takeaways (4:L841–855) | 4:L839–858 | 🔴 | ☐ | 🔴 | Fast revision list |

---

## Prediction Map (syllabus × structure of the deck — ⚠️ no PYQs available)

| Topic | Probability | Evidence |
|---|---|---|
| Form processing script (`$_POST` + validate + sanitize + business logic) | **Staple (14-mark)** | M3.5 syllabus line "Form Processing and Business Logic" is a whole hour; deck builds to it (3:L718) and calls it "the full pipeline this module has built up to" |
| Complete dynamic page (connect → query → loop → render) | **Staple (14-mark)** | M4.6 "Building Dynamic Content in PHP application"; deck's own "exact shape … backbone of almost every PHP page" (4:L780) |
| CRUD from PHP: CREATE/INSERT/DELETE/SELECT/UPDATE program | **Staple (14-mark)** | M4.3+M4.4+M4.5 syllabus lines are each a separate hour — 3 of the 6 module hours are pure CRUD |
| Cookies vs sessions (+ write a cookie/session script) | **Staple (3+ or 14)** | M4.1 is its own hour; the deck gives 2 full slide sets + a 5-row compare table |
| `==` vs `===` (with output prediction) | **Staple (3)** | Deck literally flags it as "one of PHP's most exam-relevant quirks" (3:L199) and the recap repeats it |
| Data types / type conversion | **Strong (3)** | Two dedicated slides (3:L113, 3:L136) |
| Arrays: indexed/associative/multidim + array functions | **Strong (3 or 14)** | Two slides + a function table (3:L450) |
| Write a class with constructor and method | **Strong (14)** | "Objects" is a named syllabus line under M3.4 |
| Regex validation (`preg_match` patterns) | **Strong (3 or 4)** | A named syllabus line; deck hands over a 5-pattern table |
| String functions (`strlen`/`trim`/`substr`/`explode`/`implode`/`str_replace`) | **Strong (3)** | Named syllabus line, two slides |
| Functions: default args / by-reference / variadic / scope | **Strong (3)** | Slide 3:L358 lists exactly 4 sub-points |
| Loops + control statements | **Possible (inside a program)** | Not a standalone syllabus line — always appears *inside* the bigger programs |
| mysqli connect (both styles) + connect-failure check | **Strong (3 or inside 14)** | Two dedicated slides |
| Fetch family (`fetch_assoc`/`array`/`row`/`object`, `num_rows`) | **Strong (3)** | Table on 4:L385 |
| Escape / SQL-injection / prepared statements / safe WHERE practice | **Strong (3)** | Two dedicated slides (4:L280, 4:L665) |
| Static vs dynamic content | **Possible (3)** | One slide, 4 points |
| JSON / Laravel | **Low for M3–M4 test** | Module V content; only touched in the "looking ahead" slide |

---

## Diagram Index (converted lecture md)

| Module | Figure | md line |
|---|---|---|
| M3 | PHP request–response cycle (browser → server → PHP engine → MySQL → plain HTML) | `module3.md` L57 (described) + L59–70 (labels) |
| M3 | PHP logo / `</>` / "A" typography slide furniture (no content) | `module3.md` L1, 22, 79, 131, 161, 192, 250, 286, 319, 353, 381, 414, 466, 503, 533, 563, 614, 645, 679, 713, 748 |
| M4 | Query → browser full cycle (5 steps + browser table) | `module4.md` L399 (described) + L407–417 (labels) |
| M4 | Database-cylinder / PHP slide furniture (no content) | `module4.md` L1, 57, 96, 200, 238, 310, 345, 425, 462, 499, 552, 589, 624, 729, 764 |
| — | Syllabus pages (scans, no .md) | `Web Programming Syllabus.pdf` pp. 1–4 → render with `render_pages.py` |

---

## Session Plan

| # | Covers | Syllabus | Drill focus |
|---|---|---|---|
| ✅ **1** | M3.1–M3.6: what PHP is, embedding, variables, types, casts, operators, `==` vs `===`, flow-control functions | M3 hrs 1–2 | write/predict: tags, `$`, `.` vs `+`, juggling, casts |
| **2** | M3.7–M3.10: control statements, loops, functions (defaults, `&`, variadic, scope) | M3 hr 3 | write a function; trace a loop; predict `global`/`static` |
| **3** | M3.11–M3.14: arrays (indexed/assoc/multi-dim, functions) + classes & objects | M3 hr 4 | build a record array; write a class with `__construct` |
| **4** | M3.15–M3.18: strings, string functions, regex, pattern matching | M3 hr 5 | write 5 validation patterns from memory |
| **5** | M3.19–M3.23: form processing, validation/sanitization, business logic, full script | M3 hr 6 | **write the 14-mark form script cold** |
| **6** | M4.1–M4.12: cookies, sessions, connecting (both styles), `mysqli_query`, fetch family, full cycle | M4 hrs 1–3 | write cookie + session scripts; the fetch loop |
| **7** | M4.13–M4.25: CREATE/INSERT/DELETE/SELECT/UPDATE from PHP + dynamic content page | M4 hrs 4–6 | **write the 14-mark dynamic page cold** |
| **8** | Full code-answer drill: 6 exam-style programs, timed, no notes, graded | M3+M4 all | exam simulation |

---

## Session Log

| Date | Session | Covered | Drill score | Notes |
|---|---|---|---|---|
| 2026-09-24 | 1 | M3.1–M3.6 (PHP basics → operators → `==` vs `===` → flow control) + tracker setup | D1 ✅ · D2 ⏭️ · D3 ✅ · D4 ❌ missing `;` · D5 ❌ tautology | Set up tracker; verified both deck conversions (26/26 slides present); syllabus read via vision; **no PYQs exist for this course**. Drill mode changed to fill-in worksheet in `answers.php` at Haze's request. |
| 2026-11-08 | — | **ESE kit build, all 5 modules** against the new faculty Question Bank (286 Q) | not drilled yet | Converted `Question Bank.pdf` → `question_bank.md`, `module 5.pdf` → `module5.md`, and re-converted the real Module 2 deck → `module2_fixed.md`. Wrote 5 kits (M1–M5), each with full question coverage, 3-mark masters, 14-mark skeletons, hand-writable drills, memorize sheet. ESE is the live target now. |
