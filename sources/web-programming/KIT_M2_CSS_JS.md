# Module 2 — CSS and JavaScript

**20CST461 Web Technologies · ESE:** Part A = 3 marks, Part B = 14 marks · this module supplies 2 Part-A questions and one of two Part-B questions.
Sources: `module2_fixed.md` (`2:p11`; the old `WEB PROGRAMMING MOD-2.md` was a duplicate of Module 1 — ignore it), `question_bank.md` (Q37–Q67, Q186–Q202, Q222–Q228).

---

## 1. Coverage — every bank question

| Q | Asks | Marks | Answer at |
|---|---|---|---|
| 37 | CSS rule syntax | 3 | §2.2 |
| 38 | Inline vs external | 3 | §3.1 B |
| 39 | Embedded stylesheet, when | 3 | §3.1 B |
| 40 | Link an external sheet | 3 | §3.1 B |
| 41 | Two advantages of external | 3 | §3.1 B |
| 42 | Absolute vs relative | 3 | §3.1 C |
| 43 | Box model and layout | 3 | §3.1 D |
| 44 | Media queries | 3 | §3.1 E |
| 45 | Background position/repeat | 3 | §2.7 |
| 46 | Purpose of `prompt()` | 3 | §3.1 G |
| 47 | Arithmetic + expression | 3 | §2.14 |
| 48 | Control statements + switch | 3 | §3.1 I |
| 49 | Arrays + example | 3 | §2.16 |
| 50 | Objects + access | 3 | §2.17 |
| 51 | DOM role | 3 | §3.1 L |
| 52 | Index vs key | 3 | §3.1 J |
| 53 | Update content via DOM | 3 | §2.18 |
| 54 | Add an object property | 3 | §2.17 |
| 55 | Inline vs embedded vs external | 3 | §3.1 B |
| 56 | Absolute vs relative (2) | 3 | §3.1 C |
| 57 | Callback vs normal function | 3 | §2.19 |
| 58 | Pseudo-classes | 3 | §3.1 M |
| 59 | Explain the DOM | 3 | §3.1 L |
| 60 | CSS3 syntax + inline | 3 | §3.1 A |
| 61 | Embedded vs external | 3 | §3.1 B |
| 62 | Selector types | 3 | §3.1 N |
| 63 | Position with examples | 3 | §3.1 C |
| 64 | Box model + diagram | 3 | §3.1 D |
| 65 | JS + `prompt()` | 3 | §3.1 G |
| 66 | Arithmetic + if/else | 3 | §3.1 H |
| 67 | Arrays and objects | 3 | §3.1 J |
| 186 | Three methods + external pros/cons | 14 | §3.2.1 |
| 187 | CSS2 vs CSS3 + button | 14 | §3.2.2 |
| 188 | Cascade + conflicting rules | 14 | §3.2.3 |
| 189 | Box model + padding/border/margin | 14 | §3.2.4 |
| 190 | Apply CSS three ways | 14 | §3.2.5 |
| 191 | Backgrounds + snippet | 14 | §3.2.6 |
| 192 | User input + prompt validation | 14 | §3.2.7 |
| 193 | Decision statements + day switch | 14 | §3.2.8 |
| 194 | Fundamentals + loops | 14 | §3.2.9 |
| 195 | Array manipulation | 14 | §3.2.10 |
| 196 | Objects + print properties | 14 | §3.2.11 |
| 197 | Arrays vs objects; forms | 14 | §3.2.12 |
| 198 | CSS specifics; JS control | 14 | §3.2.13 |
| 199 | Events; class selectors | 14 | §3.2.14 |
| 200 | Box model diagram | 14 | §3.2.4 |
| 201 | DOM colour/text change | 14 | §3.2.15 |
| 202 | Pseudo-classes; digital clock | 14 | §3.2.16 |
| 222 | CSS3 + inline; embedded vs external | 14 | §3.2.5 |
| 223 | Selectors + properties | 14 | §3.2.17 |
| 224 | Positioning/backgrounds; lists/tables | 14 | §3.2.18 |
| 225 | Box model/text flow; responsive | 14 | §3.2.19 |
| 226 | JS fundamentals; arithmetic/if | 14 | §3.2.9 |
| 227 | Arrays/objects; DOM forms | 14 | §3.2.20 |
| 228 | Prime check; form validation | 14 | §3.2.21 |

---

## 2. Core concepts

### 2.1 What CSS is (`2:p2`)

**CSS** = styling language: decides colour, font, spacing, layout; HTML keeps structure. One stylesheet can skin any number of pages, and the same markup can be restyled for print, mobile or dark mode without edits.
**Cascading** = the conflict-resolution algorithm: importance → specificity → source order.
History: proposed 1994 (Håkon Wium Lie), CSS1 1996, CSS2 1998 (positioning, media types), CSS3 split into independently versioned modules (Selectors, Flexbox, Grid, Media Queries, Animations).

### 2.2 Rule syntax (`2:p2–3`)

```css
h1 {
  color: #5E3E8E;
  font-size: 28px;
}
```
- **Selector** chooses elements, **declaration block** `{ }` holds **declarations** of `property: value;`.
- Semicolon required after every declaration; comments `/* … */` only — no `//`.
- Property names are case-insensitive but written lowercase-hyphenated (`font-size`, never `fontSize`).

### 2.3 The three attachment methods (`2:p3–5`)

| | Inline `style=""` | Embedded `<style>` | External `<link>` |
|---|---|---|---|
| Scope | one element | one document | every page that links it |
| Reuse | none | none (copied per page) | full |
| Specificity | highest | medium | lowest |
| Pseudo-classes, media queries | no | yes | yes |
| Example | `style="color:red"` | `h1{color:#5E3E8E}` | `#logo{height:60px}` |
| Use | one-off, JS-set styles | single-page demo | production |

```html
<p style="color:red; font-weight:bold">Inline</p>
<style> h1 { color:#5E3E8E } </style>
<link rel="stylesheet" href="styles/main.css">
```
- `<link>` attributes: `rel="stylesheet"` (required), `href`, optional `type="text/css"`, `media="print"`.
- External wins in practice: one file for unlimited pages, browser caching on repeat visits, clean split of content and presentation. Costs: one extra request, and a broken stylesheet breaks every page.

### 2.4 Cascade, inheritance, specificity (`2:p5–7`)

Priority, lowest → highest: browser default → external → embedded → inline → `!important`.
Specificity (a,b,c): inline (1,0,0) > id (0,1,0) > class/attribute/pseudo-class (0,0,1) > type (0,0,0). Equal specificity → later rule wins.
Inheritance: text properties (`color`, `font-family`, `line-height`) inherit; box properties (margin, border, padding) do not.

### 2.5 Selectors (`2:p6–7`)

| Selector | Example | Matches |
|---|---|---|
| Universal | `*` | every element |
| Type | `p` | all `<p>` |
| Class | `.card` | `class="card"` |
| ID | `#header` | the element with that id |
| Group | `h1, h2` | all listed |
| Descendant | `nav a` | `<a>` anywhere inside `<nav>` |
| Child | `ul > li` | direct children only |
| Adjacent | `h2 + p` | the `<p>` right after |
| General sibling | `h2 ~ p` | all later `<p>` siblings |
| Attribute | `input[type="text"]`, `a[href^="https"]`, `a[href$=".pdf"]`, `a[href*="saints"]` | exact / starts / ends / contains |

Value types (`2:p6–7`): keyword (`bold`, `solid`), length (`16px`, `2em`, `1.5rem`, `100vh`), percentage, colour (`red`, `#5E3E8E`, `rgb()`, `rgba()`, `hsl()`), URL, unitless number.

### 2.6 Pseudo-classes and pseudo-elements (`2:p6`)

```css
a:link    { color: blue; }
a:visited { color: purple; }
a:hover   { color: yellow; }
a:active  { color: red; }
li:nth-child(even) { background: #f7f5fa; }
li:nth-child(2n+1) { font-weight: 600; }
p::first-letter { font-size: 2em; }
```
- Pseudo-class = a **state or position**: `:hover`, `:focus`, `:first-child`, `:nth-child()`.
- Pseudo-element = a **part of the element**: `::first-line`, `::first-letter`, `::before`, `::after`.
- One colon vs two. Write link states in LVHA order — `:link :visited :hover :active` — because later equal-specificity rules win.

### 2.7 Backgrounds, lists, tables (`2:p8–10`)

```css
.hero{
  background:#f0f0f0 url('banner.jpg') no-repeat center top / cover;
  background-attachment: fixed;
}
```
`background-repeat` repeat|no-repeat|repeat-x|repeat-y · `background-position` center|top right|20px 10px · `background-size` cover (fills, may crop) | contain (fits, may letterbox) | explicit.
`list-style-type` disc|circle|square|decimal|upper-alpha|lower-roman|none · `list-style-position` outside|inside · `list-style-image: url()`.
Tables: `border-collapse: collapse` merges borders, `table-layout: fixed` uses first-row widths, `tr:nth-child(even)` for zebra rows.

### 2.8 Positioning (`2:p8`)

| Value | Behaviour |
|---|---|
| `static` | default; offsets ignored |
| `relative` | offset from its own spot; **space stays reserved** |
| `absolute` | out of flow; placed against nearest positioned ancestor, else viewport |
| `fixed` | pinned to the viewport while scrolling |
| `sticky` | relative until a threshold, then fixed in its container |

```css
.container{ position:relative; }
.badge{ position:absolute; top:10px; right:10px; }
```
Pattern: `relative` wrapper + `absolute` child for corner badges and captions without disturbing layout. `z-index` orders overlapping positioned boxes **(standard)**.

### 2.9 Box model (`2:p11`)

Four layers inside-out: content → padding → border → margin.

```
margin
 └ border
    └ padding
       └ content
```
`.box{width:300px;padding:20px;border:5px solid;margin:15px}` → rendered width 300 + 40 + 10 + 30 = **380px**.
`box-sizing:border-box` makes the declared width the final width (padding and border inside); the usual reset is `*{box-sizing:border-box}`.
Margins collapse between block siblings; padding never collapses.

### 2.10 Text flow (`2:p12`)

`display` block|inline|inline-block|flex|grid|none · `float:left|right` pushes a box aside so text wraps (still valid around images) · `clear:both` stops wrapping · `text-align` aligns inline content · `white-space` controls wrapping · `overflow` visible|hidden|scroll|auto.

### 2.11 Responsive CSS (`2:p12–13`)

Three parts: fluid units (`%`, `vw`, `em`, `rem`), flexible images (`img{max-width:100%;height:auto}`), media queries written mobile-first.
Without the viewport meta, mobile browsers lay out at ~980px and zoom out — responsive CSS does nothing:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
```css
.container{ display:block; padding:10px; }
@media (min-width:768px){ .container{ display:flex; padding:20px; } }
@media (min-width:1200px){ .container{ max-width:1140px; margin:0 auto; } }
@media print { nav, footer { display:none; } }
```
Queries can test width, orientation, resolution (`2dppx`) and media type. Breakpoints are guidelines (≤576 phone, 577–768 small tablet, 769–992 tablet, ≥993 desktop) — choose where the design breaks.

### 2.12 What JavaScript is (`2:p14`)

Lightweight, interpreted, dynamically typed scripting language that runs in the browser and gives pages behaviour. Standardised as ECMAScript; unrelated to Java.
Include it three ways: inline handler `onclick="fn()"` (avoid), embedded `<script>…</script>`, external `<script src="app.js" defer></script>`.
`defer` = parallel download, runs after parsing, order kept; `async` = runs as soon as ready, order not guaranteed; neither = parsing blocks.

### 2.13 Variables, types, dialogs (`2:p14–16`)

`let` block-scoped and reassignable · `const` block-scoped, no reassignment · `var` function-scoped, legacy.
Types: Number, String, Boolean, Undefined, Null, Object, Array. Dynamically typed — the type follows the current value.

```js
let name = prompt("Your name?", "Anjali");
if (name !== null && name.trim() !== "") alert("Hello, " + name);
```
| Call | Returns |
|---|---|
| `prompt(msg, default)` | entered string, or `null` on Cancel |
| `alert(msg)` | `undefined` |
| `confirm(msg)` | `true` / `false` |

`prompt()` always returns a string — `Number(x)` / `parseInt(x,10)` before arithmetic. Dialogs are modal and blocking.

### 2.14 Operators (`2:p15, p17`)

`+ - * / % **` plus `++ --`. `+` also concatenates: `5+3=8`, `"a"+"b"="ab"`, `"5"+3="53"`.
Precedence BODMAS: `()` → `**` → `* / %` → `+ -`, left to right. `(10+5)*2-3**2 = 21`.
`==` converts types (`"5"==5` true); `===` compares value and type (`"5"===5` false) — prefer `===`.
Logical `&& || !`; assignment `= += -= *= /=`; `typeof`, `instanceof`.

### 2.15 Control statements and loops (`2:p17–19`)

```js
if (marks >= 90) grade = "A+";
else if (marks >= 75) grade = "A";
else grade = "F";

switch (day) { case 1: d = "Monday"; break; default: d = "Invalid"; }
let category = (age >= 18) ? "Adult" : "Minor";
```
`break` prevents fall-through; `default` is the else branch; `switch` compares strictly.
Loops: `for (init; test; update)`, `while` (test first, may run zero times), `do…while` (**runs at least once**), `break`/`continue`.

### 2.16 Arrays (`2:p20`)

```js
let s = ["HTML", "CSS", "JS"];
s[0];          // "HTML"
s.length;      // 3
s.push("DOM"); // add at end
```
| Method | Job |
|---|---|
| `push`/`pop` | add/remove at end |
| `unshift`/`shift` | add/remove at start |
| `indexOf` | position or `-1` |
| `slice(a,b)` | copy of a portion, original intact |
| `splice(i,n,…)` | remove/insert in place |
| `map`/`filter`/`forEach` | transform / select / iterate with a callback |

Array = index-addressed and ordered; object = key-addressed and unordered.

### 2.17 Objects (`2:p20–21`)

```js
let student = { name: "Anjali", age: 20, courses: ["WP", "DBMS"] };
student.name;            // dot
student["age"];          // bracket — required for dynamic keys
student.branch = "CSE";  // add a property
delete student.age;      // remove one
```
Objects hold arrays and arrays hold objects — this nesting is the shape JSON formalises in Module 5.

### 2.18 DOM (`2:p21`)

The browser parses HTML into a live tree of nodes; JavaScript edits the tree, never the file.

```
document
 └ html
    ├ head → title
    └ body → h1, p
```
| Task | Code |
|---|---|
| By id | `document.getElementById("x")` |
| By class | `document.getElementsByClassName("card")` |
| First / all matches | `querySelector(".card")` / `querySelectorAll(".card")` |
| Text | `el.textContent = "New"` |
| Markup | `el.innerHTML = "<em>New</em>"` |
| Style | `el.style.color = "purple"` |
| Attribute | `el.setAttribute("class","hi")` |

`textContent` is literal and safe; `innerHTML` parses markup and is an injection risk with user data.

### 2.19 Events and callbacks (`2:p21–22`)

```js
document.querySelector("#submitBtn").addEventListener("click", function(){
  alert("Clicked");
});
```
Register with `addEventListener` (preferred), element property (`btn.onclick = fn`), or inline attribute (avoid).
Events: `click`, `submit`, `change`, `input`, `load`, `keydown`/`keyup`.
**Callback** = a function passed as an argument so something else calls it later (a listener, `setTimeout`, `map`); a normal function is called by your own code. Same syntax, different caller.

---

## 3. Answer bank

### 3.1 Three-mark answers

**A — Rule syntax (Q37, Q60).** 1. **Shape** — `selector { property: value; }`. 2. **Parts** — selector, declaration block, declarations each ending in `;`. 3. **Example** — `h1{color:#5E3E8E;font-size:28px}`; comments `/* */` only.

**B — Three methods (Q38–41, Q55, Q61, Q186a, Q190, Q222b).** 1. **Inline** — `style=""`, one element, highest specificity, no pseudo-classes or media queries. 2. **Embedded** — `<style>` in `<head>`, one document, medium. 3. **External** — `<link rel="stylesheet" href>`; reuse across pages + browser caching + separation of concerns.

**C — Positioning (Q42, Q56, Q63, Q224a).** 1. **relative** — offset from its normal position, space kept. 2. **absolute** — out of flow, anchored to the nearest positioned ancestor. 3. **Others** — `fixed` viewport-anchored, `sticky` hybrid, `static` default.

**D — Box model (Q43, Q64, Q189, Q200).** 1. **Layers** — content → padding → border → margin. 2. **Width** — declared width + 2·padding + 2·border (+margins for outer size). 3. **`box-sizing`** — `content-box` default vs `border-box` inclusive.

**E — Media queries (Q44, Q225b).** 1. **Syntax** — `@media (min-width:768px){ … }`. 2. **Conditions** — width, orientation, resolution, media type (`print`). 3. **Responsive trio** — fluid units + `max-width:100%` images + viewport meta.

**F — Backgrounds (Q45, Q191).** 1. **`background-image`** — `url('x.jpg')`. 2. **Repeat/position** — `no-repeat`, `center top`, `20px 10px`. 3. **Fit** — `background-size:cover|contain`; shorthand `background:#eee url() no-repeat center/cover`.

**G — prompt (Q46, Q65, Q192a).** 1. **Signature** — `prompt(msg, default)` returns a string or `null`. 2. **Convert** — `Number()`/`parseInt()` before arithmetic. 3. **Alternatives** — `confirm()` yes/no, form fields read through the DOM.

**H — Arithmetic (Q47, Q66).** 1. **Operators** — `+ - * / % **`, `++`/`--`; `+` also concatenates. 2. **Precedence** — parentheses, exponent, `* / %`, `+ -`. 3. **Example** — `(10+5)*2-3**2 = 21`; `5/2 = 2.5` (floating point).

**I — Control statements (Q48, Q193a).** 1. **if/else** — one branch by condition; ternary `c ? a : b` for two values. 2. **switch** — one expression against many cases, `break` stops fall-through. 3. **Loops** — `for`, `while`, `do…while` (always runs once).

**J — Arrays and objects (Q49, Q52, Q67).** 1. **Array** — ordered, zero-indexed, `length`, `push`/`pop`. 2. **Object** — key–value pairs, dot or bracket access. 3. **Difference** — index vs key; `arr[0]` vs `obj["name"]`.

**K — Objects (Q50, Q54).** 1. **Literal** — `{name:"Anjali", age:20}`. 2. **Access** — `o.name`, `o["name"]`. 3. **Mutate** — `o.branch = "CSE"`, `delete o.age`.

**L — DOM (Q51, Q53, Q59).** 1. **Definition** — live in-memory tree of the loaded HTML. 2. **Select** — `getElementById`, `querySelector(All)`. 3. **Change** — `textContent`, `innerHTML`, `style`, `setAttribute`; the page updates immediately.

**M — Pseudo-classes (Q58, Q202a).** 1. **Definition** — styles an element in a state or position. 2. **Examples** — `:hover`, `:focus`, `:visited`, `:nth-child(even)`. 3. **Markup distinction** — one colon for classes, two for pseudo-elements (`::first-line`).

**N — Selectors and properties (Q62, Q223).** 1. **Selectors** — type, universal, class, id, grouping, attribute, pseudo-class, combinator. 2. **Properties** — `color`, `font-size`, `margin`, `padding`, `background`. 3. **Values** — keywords, lengths, percentages, colours, URLs, numbers.

### 3.2 Fourteen-mark answers

#### 3.2.1 Q186 / Q190 — Three methods of applying CSS
**Structure (7 + 7).** (a) three methods with code, scope, specificity, reuse. (b) external advantages and disadvantages.
(a) Table from §2.3 + one snippet per method; precedence browser default < external < embedded < inline, `!important` on top.
(b) Pros: single source of truth, caching, easier maintenance, media queries and pseudo-classes, separation. Cons: extra first-load request, one failure breaks every page, lowest specificity needs care.

#### 3.2.2 Q187 — CSS2 vs CSS3 + styled button
**Structure (6 + 8).** (a) monolithic vs modular, new features. (b) button with three CSS3 properties explained.
(a) CSS2 (1998) was one specification with positioning and media types; CSS3 is a set of modules versioned separately — Selectors, Flexbox, Grid, Media Queries, Animations. New: `border-radius`, `box-shadow`, gradients, `rgba()`, transitions, transforms, web fonts, multiple backgrounds.
(b)
```css
.btn{background:#5E3E8E;color:#fff;padding:10px 22px;border:none;
     border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,.3);
     transition:background .3s ease}
.btn:hover{background:#7a5aa8}
```
`border-radius` rounds corners; `box-shadow: x y blur colour` lifts the button; `transition` animates the property change so hover is smooth.

#### 3.2.3 Q188 — The cascade and conflicts
**Structure (6 + 8).** (a) the three decision levels. (b) trace a conflict.
(a) Importance (`!important`), then specificity (inline > id > class/attr/pseudo-class > type > universal), then source order; inheritance fills unset inheritable properties.
(b) `<p id="intro" class="note" style="color:red">` with external `#intro{color:green}`, embedded `.note{color:blue}` → red. Remove inline → id beats class → green. Remove the id rule → blue. Show every step, not just the answer.

#### 3.2.4 Q189 / Q200 — Box model with numbers
**Structure (7 + 7 / 8 + 6).** (a) layers and arithmetic. (b) worked padding/margin effect.
(a) Draw the nested boxes; width = 300 + 40 + 10 + 30 = 380px; `border-box` makes it 300px total with 250px of content; margins collapse (20 + 30 → 30px gap).
(b) Code the four properties, then a two-box demo showing that padding pushes content and border, while margin only moves neighbours.

#### 3.2.5 Q191 / Q224a — Backgrounds and positioning
**Structure (7 + 7).** Longhand, shorthand, and the `relative`/`absolute` pairing.
Cover: `background-image`, `-repeat`, `-position`, `-size` (cover vs contain), `-attachment:fixed` for parallax, multiple backgrounds separated by commas **(standard)**. Then a `relative` hero with an `absolute` caption pinned bottom-left.

#### 3.2.6 Q192 — User input in JS
**Structure (7 + 7).** (a) the four input channels. (b) prompt with validation.
(a) `prompt()` one-off text, `confirm()` yes/no, form controls read through the DOM, event-driven input (`input`, `change`); dialogs are modal and dated for production.
(b) Prompt → reject `null` and empty after `trim()` → show greeting or error; second prompt for a number, convert with `Number()`.

#### 3.2.7 Q193 — Decision making
**Structure (7 + 7).** (a) if / if-else / else-if / switch / ternary. (b) day-of-week function.
(b)
```js
function dayName(n){
  switch(n){
    case 1: return "Monday";
    case 2: return "Tuesday";
    case 6: return "Saturday";
    case 7: return "Sunday";
    default: return "Invalid day";
  }
}
```
`default` catches 0 and 8; `return` leaves the function immediately, unlike `break`; `switch` uses strict comparison. (Write all seven cases in the exam.)

#### 3.2.8 Q194 / Q226 — Fundamentals and control statements
**Structure (7 + 7).** (a) variables, types, functions, `typeof`. (b) `for`, `while`, `do…while`, `break`/`continue`.
(a) `let`/`const`, seven types, function declaration with parameters and `return`, dynamic typing.
(b) One example each plus a nested loop building a 3×3 table; state that `do…while` tests last.

#### 3.2.9 Q195 — Array manipulation
**Structure (7 + 7).** (a) the method table. (b) live demo with results.
(a) `push/pop`, `unshift/shift`, `indexOf`, `slice` vs `splice`, `map/filter/forEach`, `length`.
(b) Show the array after **each** operation as a comment — marks are for the resulting array, not the call.

#### 3.2.10 Q196 — Objects + printing properties
**Structure (7 + 7).**
```js
let student = { name:"Anjali", age:20, course:"CSE" };
function printValues(obj){
  for (let key in obj) console.log(key + ": " + obj[key]);
}
printValues(student);
```
`for…in` yields keys; `obj[key]` is required because the key is a variable; string keys keep insertion order.

#### 3.2.11 Q197 / Q227 — Arrays vs objects; form processing
**Structure (7 + 7).** (a) comparison table. (b) validate then submit.
(a) ordered/indexed/`length` vs keyed/no order; lists vs records; different methods.
(b) `getElementById` per field → `.value` → validate → `event.preventDefault()` to stop the reload → `form.submit()` or `fetch()`. Repeat the rule: client validation never replaces server validation.

#### 3.2.12 Q198 — CSS specifics + JS control
**Structure (6 + 8).** Four labelled CSS answers, then control statements.
```css
a:hover, a:active { background-color: yellow; }
ol { list-style-type: lower-alpha; }
body { background-image: url('Boat.gif'); }
body { border: 1px dotted #000; }
```
Traps: `lower case alphabet` = `lower-alpha`; border shorthand order is width, style, colour. Then if/else, switch, `for`, `while`, `do…while` with one example each.

#### 3.2.13 Q199 — Event handlers; class selectors
**Structure (8 + 6).** Three registration methods, then the demo and two class rules.
```html
<p id="msg">Welcome</p><button id="btn">Click</button>
<script>
document.getElementById("btn").addEventListener("click", function(){
  document.getElementById("msg").innerHTML = "<b>Hello from JavaScript</b>";
});
</script>
```
`addEventListener` is preferred: multiple handlers, removable, no markup mixing.
```css
.style1{color:blue;text-align:right;text-decoration:underline;font-style:italic;word-spacing:2cm}
.style2{background-color:yellow;border:1px solid blue;padding:1.5cm}
```

#### 3.2.14 Q201 — DOM interaction
**Structure (7 + 7).** (a) tree + selection, colour change on click. (b) text change on click.
Explain nodes and `querySelector`; then `p.style.backgroundColor = "yellow"` in one handler and `p.textContent = "…"` in another; two buttons show independent handlers.

#### 3.2.15 Q202 — Pseudo-classes; digital clock
**Structure (7 + 7).**
```html
<p id="clock"></p>
<script>
function tick(){
  const d = new Date(), p = n => String(n).padStart(2, "0");
  document.getElementById("clock").textContent =
    p(d.getHours()) + ":" + p(d.getMinutes()) + ":" + p(d.getSeconds());
}
tick(); setInterval(tick, 1000);
</script>
```
`Date` + `getHours/Minutes/Seconds`, `padStart` for two digits, `setInterval(fn,1000)` repeats; call `tick()` once or the clock is blank for a second.

#### 3.2.16 Q223 / Q224b / Q225 — CSS sweep
**Structure (7 + 7 each).** Compose from §3.1 N (selectors and properties), §3.1 C + F (positioning, backgrounds), list and table CSS, §3.1 D (box model) and §3.1 E (responsive). One labelled block per sub-part.

#### 3.2.17 Q228 — Two programs
**Structure (7 + 7).** Prime check, then validation.
```js
function isPrime(n){ if(n<2) return false;
  for(let i=2;i*i<=n;i++) if(n%i===0) return false; return true; }
```
Validation: `submit` listener → `preventDefault()` → `trim() === ""` checks → `/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i` → write the message into a `<span id="err">` rather than `alert` (shows DOM skill).

---

## 4. Code to write from memory

1. Rule with selector and declarations.
2. Same `<p>` inline, embedded, external — plus the `<link>` line.
3. Specificity demo: inline vs `#id` vs `.class` vs `p`.
4. Selector zoo: universal, type, class, id, group, descendant, child, adjacent, four attribute forms.
5. Link states LVHA, `:focus`, `:nth-child(even)`, `::first-letter`.
6. Hero background with `no-repeat`, `center`, `cover` — longhand and shorthand.
7. `relative` parent + `absolute` badge; then a `fixed` header.
8. Box model arithmetic, then the same box with `border-box`.
9. List styles: `lower-alpha`, `square`, `none`, `inside`.
10. Table CSS: collapse, padding, zebra rows, caption.
11. Mobile-first media queries + `max-width:100%` image.
12. `prompt()` with empty check, numeric conversion, `innerHTML` output.
13. if/else-if ladder + `switch` + ternary.
14. Loops: `for`, `while`, `do…while`, table-row builder.
15. Array ops demo with printed results.
16. Object literal, both access forms, add property, `for…in`.
17. DOM update on click via `addEventListener`.
18. Welcome→Hello button.
19. Prime check + form validation with an error `<span>`.
20. Digital clock.

---

## 5. Night-before memorize

| Item | Recall |
|---|---|
| Rule anatomy | `selector { property: value; }` |
| Comments | `/* … */` only |
| Attachment order | inline > embedded `<style>` > external `<link>` |
| Specificity | inline > id > class > type; tie → later rule |
| Position values | static, relative, absolute, fixed, sticky |
| Box layers | content, padding, border, margin |
| Box math | width + 2·padding + 2·border |
| `box-sizing` | content-box vs border-box |
| Background props | image, repeat, position, size, attachment |
| List props | `list-style-type/position/image` |
| Table CSS | `border-collapse:collapse`, `nth-child(even)` |
| Viewport | `width=device-width, initial-scale=1.0` |
| Media query | `@media (min-width:768px){ }` |
| JS variables | `let`, `const`, `var` scope |
| JS types | Number, String, Boolean, Undefined, Null, Object, Array |
| Equality | `"5"==5` true, `"5"===5` false |
| `prompt()` | string or `null` |
| Array methods | push pop shift unshift indexOf slice splice map filter forEach |
| Object access | `o.k`, `o["k"]`, add, `delete` |
| DOM selectors | getElementById, querySelector(All), getElementsByClassName |
| DOM writes | textContent, innerHTML, style, setAttribute |
| Events | click, submit, change, input, load, keydown |
| `preventDefault` | stops the default submit/reload |
| Clock | `new Date()`, `getHours()`, `setInterval`, `padStart(2,"0")` |

---

## 6. Diagram index

| Figure | Where | Draw |
|---|---|---|
| Rule structure | `2:p2–3` | selector + block + declarations |
| Three methods | `2:p5` | scope/reuse/specificity grid |
| Specificity ladder | `2:p7` | inline > id > class > type |
| Position table | `2:p8` | five values |
| Box model | `2:p11` | four nested boxes + width sum |
| Breakpoints | `2:p13` | mobile → tablet → desktop |
| DOM tree | `2:p21` | document → html → head/body |
| Event table | `2:p21` | event → when it fires |

---

## 7. Say-this-if-grilled

1. "CSS exists so presentation changes without touching content."
2. "Inline wins specificity and loses everything else — no reuse, no media queries, no pseudo-classes."
3. "`!important` beats specificity; it is a last resort, not a fix."
4. "`relative` reserves the space, `absolute` does not — that one line explains most positioning bugs."
5. "`border-box` exists because padding and border used to silently add to the declared width."
6. "Margins collapse vertically; padding never does."
7. "`prompt()` returns a string or null — `\"5\" + 3` is `\"53\"`."
8. "`===` avoids the coercion surprises of `==`."
9. "An array is index-addressed and ordered; an object is key-addressed and unordered."
10. "The DOM is the live tree, not the HTML file."
11. "A callback is not a different kind of function — it is one handed to someone else to call."
12. "Client-side validation is UX only; the server must validate again."
13. "A media query without the viewport meta is wasted on phones."
