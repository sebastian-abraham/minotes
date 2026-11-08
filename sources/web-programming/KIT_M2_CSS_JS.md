# MODULE 2 — CSS and JavaScript · Complete Study Kit

> 20CST461 Web Technologies · ESE Part A = 3 marks, Part B = 14 marks · **2 Part-A questions and 1 of 2 Part-B questions come from this module**
> Sources: `module2_fixed.md` (page refs `2:p11`; the old `WEB PROGRAMMING MOD-2.md` was a duplicate of Module 1 — ignore it), faculty `Question Bank.pdf` (Q37–Q67, Q186–Q202, Q222–Q228). Items marked **(standard, not in your deck)** are exam-standard but not on your slides.

---

## 0. How to use this kit

Part 1 = understand (read once). Part 2 = what you write in the exam (3 marks = 3–4 numbered lines). Part 3 = code by hand. §5 = night-before list. §6 = figures to go look at.

---

## 1. Module map + question coverage

### 1.1 Coverage table

| Q# | What it asks (short) | Marks | Answered at |
|---|---|---|---|
| 37 | CSS rule syntax and structure | 3 | §2.2 |
| 38 | Inline vs external — application and scope | 3 | §2.3 |
| 39 | Embedded stylesheet, when to prefer it | 3 | §2.3 |
| 40 | Link an external stylesheet | 3 | §2.3 |
| 41 | Two advantages of external over inline | 3 | §2.3 |
| 42 | Absolute vs relative positioning | 3 | §2.8 |
| 43 | Box model and layout | 3 | §2.9 |
| 44 | Media queries and responsive design | 3 | §2.11 |
| 45 | Background position and repeat | 3 | §2.7 |
| 46 | Purpose of `prompt()` | 3 | §2.13 |
| 47 | Arithmetic in JS + expression example | 3 | §2.14 |
| 48 | JS control statements + switch example | 3 | §2.15 |
| 49 | Arrays in JS + example | 3 | §2.16 |
| 50 | Objects in JS + define/access | 3 | §2.17 |
| 51 | DOM role + JS interaction | 3 | §2.18 |
| 52 | Array index vs object key | 3 | §2.16 |
| 53 | Update element content with `getElementById`/`innerHTML` | 3 | §2.18 |
| 54 | Add a property to an object | 3 | §2.17 |
| 55 | Inline vs embedded vs external (compare) | 3 | §2.3 |
| 56 | Absolute vs relative positioning (compare) | 3 | §2.8 |
| 57 | Callback function vs normal function | 3 | §2.19 |
| 58 | Pseudo-classes with examples | 3 | §2.6 |
| 59 | Explain the DOM | 3 | §2.18 |
| 60 | CSS3 syntax + inline style example | 3 | §2.2 |
| 61 | Embedded vs external with examples | 3 | §2.3 |
| 62 | CSS selector types with properties/values | 3 | §2.5 |
| 63 | Absolute and relative positioning with examples | 3 | §2.8 |
| 64 | Box model with diagram | 3 | §2.9 |
| 65 | What is JavaScript + `prompt()` example | 3 | §2.13 |
| 66 | Arithmetic operators + if/else | 3 | §2.14 |
| 67 | JS arrays and objects, simple example | 3 | §2.16, §2.17 |
| 186 | Inline/embedded/external + pros and cons of external | 14 | §3.1 |
| 187 | CSS2 vs CSS3 + border-radius/box-shadow/transition button | 14 | §3.2 |
| 188 | Cascading and precedence + conflicting-rule scenario | 14 | §3.3 |
| 189 | Box model + padding/border/margin example | 14 | §3.4 |
| 190 | Three ways to apply CSS, compared | 14 | §3.5 |
| 191 | `background-image`/`-position`/`-repeat` + snippet | 14 | §3.6 |
| 192 | Ways to obtain user input + `prompt()` with validation | 14 | §3.7 |
| 193 | Decision statements if/if-else/switch + day-of-week switch | 14 | §3.8 |
| 194 | JS fundamentals + for/while/do-while | 14 | §3.9 |
| 195 | Array manipulation methods + demo | 14 | §3.10 |
| 196 | Objects + function that prints an object's properties | 14 | §3.11 |
| 197 | Arrays vs objects + form processing | 14 | §3.12 |
| 198 | CSS: hover/active, lower-alpha list, Boat.gif bg, dotted border; JS control statements | 14 | §3.13 |
| 199 | Event handlers + Welcome/Click demo; class selectors + two styles | 14 | §3.14 |
| 200 | Box model diagram + padding/margin effect | 14 | §3.4 |
| 201 | DOM + change paragraph background/text on click | 14 | §3.15 |
| 202 | Pseudo-classes + JS digital clock | 14 | §3.16 |
| 222 | CSS3 syntax with inline styles; embedded vs external + advantages | 14 | §3.5 |
| 223 | Selectors (type, class, ID, attribute, pseudo-class) + properties | 14 | §3.17 |
| 224 | Positioning + backgrounds; list styles + table layouts | 14 | §3.18 |
| 225 | Box model and text flow; responsive CSS with viewport + media queries | 14 | §3.19 |
| 226 | JS fundamentals + `prompt()`; arithmetic + if-else/switch | 14 | §3.9, §3.8 |
| 227 | JS arrays/objects + methods; DOM and form processing | 14 | §3.20 |
| 228 | JS prime check; JS form validation via DOM | 14 | §3.21 |

### 1.2 Master themes (55 questions → five)

1. **How CSS is attached and how conflicts resolve** — inline/embedded/external, cascade, specificity (37–41, 55, 60, 61, 186, 188, 190, 222).
2. **Selectors and styling surface** — selector types, pseudo-classes, properties/values, backgrounds, lists, tables (45, 58, 62, 198, 202a, 223, 224b).
3. **Layout** — box model, positioning, text flow, responsive CSS (42, 43, 44, 56, 63, 64, 189, 191, 200, 225).
4. **JavaScript language core** — variables, types, operators, control flow, loops, arrays, objects, callbacks (46–50, 52, 54, 57, 65–67, 193–197, 226, 227a).
5. **DOM + events + forms** — selecting nodes, changing content, event handlers, validation (51, 53, 59, 199, 201, 227b, 228).

---

## 2. PART 1 — Deep dive, from zero

### 2.1 What CSS is (`2:p2`)

**Story:** HTML is the skeleton, CSS is the skin and clothing, JavaScript is the muscles. CSS = *Cascading Style Sheets*: a separate language whose only job is to say how HTML should *look*.

- Separating structure (HTML) from presentation (CSS) means one stylesheet can skin a hundred pages, and the same markup can be restyled for print/mobile/dark mode without touching content (`2:p2`).
- **"Cascading"** = the set of rules that decides which declaration wins when several could apply: importance → specificity → source order.
- History: proposed by Håkon Wium Lie 1994, CSS1 Recommendation 1996, CSS2 1998 (positioning + media types), CSS3 from the early 2000s **split into independent modules** (Selectors, Flexbox, Grid, Media Queries, Animations…) each evolving at its own speed — that is why you say "CSS3 modules" rather than one spec (`2:p2`).

### 2.2 CSS rule syntax (`2:p2–3`)

```css
/* selector { property: value; property: value; } */
h1 {
  color: #5E3E8E;
  font-size: 28px;
  text-align: center;
}
```

| Part | Meaning |
|---|---|
| Selector | Pattern choosing which elements the rule hits (`h1`, `.card`, `#logo`) |
| Declaration block | Everything inside `{ }` |
| Property | What aspect is being set (`color`, `font-size`) |
| Value | The setting (`#5E3E8E`, `28px`) |
| Declaration | One `property: value;` pair — semicolon required |

Comments are `/* ... */` only (no `//`). Property names are case-insensitive but written lowercase-with-hyphens (`font-size`, never `fontSize`).

**CSS3 modularity** (`2:p2`): Selectors L3/4 (attribute, pseudo-class, combinators), Box Model (`box-sizing`), Backgrounds & Borders (`border-radius`, `box-shadow`, multiple backgrounds), Flexbox (1-D layout), Grid (2-D), Media Queries, Transitions & Animations.

### 2.3 The three ways to attach CSS (`2:p3–5`)

**Story:** inline = writing the colour on each individual object; embedded = a note pinned inside one room; external = one master instruction sheet everybody shares.

| | Inline | Embedded (`<style>` in `<head>`) | External (`<link>` to `.css`) |
|---|---|---|---|
| Where | `style=""` on one element | `<style>` block in the document | separate file |
| Scope | one element | one document | every page that links it |
| Reusability | none | low (copy per page) | high |
| Specificity | highest | medium | lowest of the three |
| Can do `:hover`, `::before`, media queries? | **No** | yes | yes |
| Typical use | quick one-off, JS-generated styles | single-page demo, page-specific override | production sites |

```html
<!-- inline -->
<p style="color:red; font-weight:bold; margin-top:10px;">Inline styled</p>
<!-- embedded -->
<style> body{font-family:Arial,sans-serif} h1{color:#5E3E8E} </style>
<!-- external -->
<link rel="stylesheet" href="styles/main.css">
```

`<link>` attributes: `rel="stylesheet"` (required), `href` (path/URL), `type="text/css"` (optional in HTML5), `media="print"` (restrict to print) (`2:p4`).

**Why external wins in practice** (`2:p5`): one file styles unlimited pages consistently; the browser caches it, so repeat visits are faster; content stays cleanly separated from presentation — the whole reason CSS exists. Disadvantages: an extra HTTP request on first load, and a failure in that one file breaks styling everywhere.

### 2.4 Cascade, inheritance and specificity (`2:p5–7`)

- **Cascade order** (lowest → highest priority): browser defaults → external → embedded → inline → `!important`.
- **Specificity score** (a,b,c): inline style (1,0,0) > ID (0,1,0) > class/attribute/pseudo-class (0,0,1) > element/type (0,0,0). Universal `*` counts zero.
- **Equal specificity → later rule wins** (source order).
- **Inheritance**: text properties (`color`, `font-family`, `line-height`) inherit from parent; box properties (margin, border, padding) do not.

Worked scenario for Q188b: `<p class="note" id="intro" style="color:red">` with embedded `.note{color:blue}` and external `#intro{color:green}` → inline red wins; remove the inline style → the ID rule (`green`) beats the class rule.

### 2.5 Selectors (`2:p6–7`)

| Selector | Example | Matches |
|---|---|---|
| Universal | `* { margin:0 }` | every element |
| Type/element | `p { line-height:1.5 }` | all `<p>` |
| Class | `.card { padding:10px }` | all `class="card"` |
| ID | `#header { height:60px }` | the one `id="header"` |
| Grouping | `h1, h2, h3 { font-family:serif }` | all listed |
| Descendant | `nav a { color:white }` | `<a>` anywhere inside `<nav>` |
| Child | `ul > li { list-style:none }` | direct `<li>` children |
| Adjacent sibling | `h2 + p` | the `<p>` right after an `<h2>` |
| General sibling | `h2 ~ p` | all `<p>` siblings after an `<h2>` |
| Attribute | `input[type="text"]`, `a[href^="https"]`, `a[href$=".pdf"]`, `a[href*="saintgits"]` | by attribute value: exact / starts / ends / contains |

**Pseudo-class** = styles an element in a *state*: `:hover`, `:focus`, `:active`, `:visited`, `:first-child`, `:nth-child(2n)`. **Pseudo-element** = styles a *part* of an element: `::first-line`, `::first-letter`, `::before`, `::after` (`2:p6`).

**Value types** (`2:p6–7`): keyword (`bold`, `solid`), length (`16px`, `2em`, `1.5rem`, `100vh`), percentage (`50%`), colour (`red`, `#5E3E8E`, `rgb()`, `rgba()`, `hsl()`), URL (`url('bg.png')`), number (`1.5` unitless for opacity/line-height).

### 2.6 Pseudo-classes in depth (Q58, Q202a)

```css
a:link    { color: blue; }     /* not yet visited */
a:visited { color: purple; }   /* already visited */
a:hover   { color: yellow; }   /* pointer over it */
a:active  { color: red; }      /* being clicked */
input:focus { border: 2px solid #5E3E8E; }
li:nth-child(2) { font-weight: bold; }
p::first-letter { font-size: 2em; }   /* pseudo-ELEMENT */
```
Notes worth a mark: LVHA order matters (`:link :visited :hover :active`) because later rules of equal specificity win; `:hover` needs a pointing device; pseudo-class = one colon, pseudo-element = two.

### 2.7 Backgrounds, list styles, table CSS (`2:p8–10`)

```css
.hero{
  background-color:#f0f0f0;
  background-image:url('banner.jpg');
  background-repeat:no-repeat;      /* repeat | no-repeat | repeat-x | repeat-y */
  background-position:center top;   /* center | top right | 20px 10px */
  background-size:cover;            /* cover | contain | 300px 200px */
  background-attachment:fixed;      /* scroll (default) | fixed = parallax */
}
/* shorthand */
.hero{ background:#f0f0f0 url('banner.jpg') no-repeat center top / cover; }
```

| Property | Controls |
|---|---|
| `list-style-type` | `disc circle square decimal upper-alpha lower-roman none` |
| `list-style-position` | `outside` (default) / `inside` |
| `list-style-image` | `url('bullet.png')` |
| `border-collapse` | `collapse` merges cell borders; `separate` (default) keeps them |
| `table-layout` | `auto` (content-driven) / `fixed` (first-row widths, faster) |
| `tr:nth-child(even)` | zebra striping |

### 2.8 Positioning (`2:p8`)

**Story:** `relative` = nudging your own chair; `absolute` = leaving the room and standing exactly where a named landmark tells you; `fixed` = floating above the room, unaffected by scrolling.

| Value | Behaviour |
|---|---|
| `static` | Default; `top/left` do nothing |
| `relative` | Offset from its own normal spot; **space stays reserved** |
| `absolute` | Removed from flow (others close the gap); positioned against the nearest ancestor whose `position` ≠ static, else the viewport |
| `fixed` | Relative to the viewport; stays put when scrolling |
| `sticky` | `relative` until a scroll threshold, then `fixed` within its container |

```css
.container{ position:relative; width:400px; height:200px; }
.badge{ position:absolute; top:10px; right:10px; }  /* pinned to container corner */
```

Common pattern (say this and you look competent): wrapper `relative`, child `absolute` — precise placement without disturbing layout. `z-index` controls stacking when positioned boxes overlap **(standard)**.

### 2.9 The box model (`2:p11`)

**Story:** a framed photo — picture (content), mat (padding), frame (border), gap to the next frame (margin).

```
┌─────────────── margin ───────────────┐
│  ┌──────────── border ───────────┐   │
│  │  ┌────── padding ───────┐     │   │
│  │  │     content          │     │   │
│  │  └──────────────────────┘     │   │
│  └───────────────────────────────┘   │
└──────────────────────────────────────┘
```

`.box{width:300px;padding:20px;border:5px solid;margin:15px}` → rendered width = 300 + 2(20) + 2(5) + 2(15) = **380px** by default (`content-box`).

`box-sizing:border-box` makes `width` include padding+border → declared width *is* rendered width; the near-universal reset is `*{box-sizing:border-box}`. Margins **collapse** between adjacent block elements; padding never does. `padding`/`margin` shorthands: `10px` all, `10px 20px` vertical/horizontal, `10px 20px 30px 40px` top/right/bottom/left.

### 2.10 Text flow (`2:p12`)

`display` (`block|inline|inline-block|flex|grid|none`) selects the layout model. `float:left|right` pushes a box aside so text wraps around it (still valid for wrapping text around an image, superseded for page layout); `clear:both` stops wrapping. `text-align` aligns inline content; `white-space` controls wrapping/collapse; `overflow` decides what happens when content exceeds the box.

### 2.11 Responsive CSS, viewport, media queries (`2:p12–13`)

**Story:** one suit that resizes itself instead of a different suit per customer.

Three techniques: **fluid units** (`%`, `vw`, `vh`, `em`, `rem`), **flexible images** (`img{max-width:100%;height:auto}`), **media queries** + **mobile-first** authoring (base styles for small screens, then `min-width` rules add complexity).

The viewport meta is mandatory or mobile browsers lay out at ~980px and zoom out, defeating everything:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```css
.container{ display:block; padding:10px; }            /* base: mobile */
@media (min-width:768px){ .container{ display:flex; padding:20px; } }
@media (min-width:1200px){ .container{ max-width:1140px; margin:0 auto; } }
@media print { nav, footer { display:none; } }
```
Queries can test width, orientation, resolution (`min-resolution:2dppx`) and media type (`screen`/`print`). Breakpoints are guidelines (≤576 phones, 577–768 small tablets, 769–992 tablets, ≥993 desktop) — real ones go where the design breaks.

### 2.12 What JavaScript is (`2:p14`)

Lightweight, interpreted, dynamically typed scripting language that runs mainly in browsers and gives pages behaviour: react to clicks, validate forms, update content without reload. Third pillar next to HTML (structure) and CSS (presentation). Brendan Eich, 1995, Netscape; standardised as ECMAScript; unrelated to Java despite the name. Client-side by default; Node.js later took it server-side.

Inclusion (`2:p14`): inline handler `onclick="alert('Hi')"` (avoid), embedded `<script>...</script>`, external `<script src="app.js" defer></script>`. `defer` = download in parallel, execute after parsing, order preserved; `async` = execute as soon as ready, order not guaranteed; neither → parsing blocks.

### 2.13 Variables, types, `prompt()` (`2:p14–16`)

`let` (block-scoped, reassignable), `const` (block-scoped, no reassignment), `var` (function-scoped, legacy). Types: Number, String, Boolean, Undefined, Null, Object, Array (specialised object). Dynamically typed — a variable's type follows its current value.

```js
let name = prompt("What is your name?", "Enter name here");
if (name !== null && name.trim() !== "") {
  alert("Hello, " + name + "!");
}
```
| Function | Purpose | Returns |
|---|---|---|
| `prompt(msg, default)` | modal text input | the string, or `null` on Cancel |
| `alert(msg)` | message + OK | `undefined` |
| `confirm(msg)` | yes/no | `true` / `false` |

Key trap: **`prompt()` always returns a string** — `Number(x)` or `parseInt(x,10)` before arithmetic. Dialogs are blocking and modal; fine for teaching, dated for production UIs.

### 2.14 Operators and arithmetic (`2:p15, p17`)

`+ - * / % **` plus `++ --`; `+` doubles as string concatenation (`5+3=8`, `"a"+"b"="ab"`, `"5"+3="53"`). Precedence follows BODMAS: `( )` → `**` → `* / %` → `+ -`, left to right. `(10+5)*2-3**2 = 21`.

Comparison `== === != !== < > <= >=`; **`==` converts types** (`"5"==5` is true), `===` compares value *and* type (`"5"===5` false) — always prefer `===`. Logical `&& || !`; assignment `= += -= *= /=`; type operators `typeof`, `instanceof`.

### 2.15 Control statements (`2:p17–19`)

```js
if (marks >= 90) grade = "A+";
else if (marks >= 75) grade = "A";
else grade = "F";

switch (day) {
  case 1: name = "Monday"; break;
  case 2: name = "Tuesday"; break;
  default: name = "Invalid";
}

let category = (age >= 18) ? "Adult" : "Minor";
```
`break` prevents fall-through; `default` is the else-branch. Loops: `for (init; test; update)`, `while (test)` (may run zero times), `do{...}while(test)` (**runs at least once**), plus `break`/`continue` and `for...of` / `for...in` **(standard)**.

### 2.16 Arrays (`2:p20`)

Ordered, zero-indexed list, mixed types allowed: `let s = ["HTML","CSS","JS"]; s[0] // "HTML"; s.length // 3`.

| Method | Job |
|---|---|
| `push(x)` / `pop()` | add / remove at end |
| `unshift(x)` / `shift()` | add / remove at start |
| `indexOf(x)` | position, `-1` if absent |
| `slice(a,b)` | copy of a portion, original unchanged |
| `splice(start,count,...)` | remove/insert in place, original changed |
| `map(fn)` / `filter(fn)` / `forEach(fn)` | transform / select / iterate with a callback |
| `join(sep)` / `sort()` / `reverse()` / `concat()` | string, order, combine **(standard)** |

**Index vs key** (Q52): arrays use numeric indices `arr[0]` (order matters, `length` exists); objects use named keys `obj["name"]`/`obj.name` (order irrelevant, no `length`).

### 2.17 Objects (`2:p20–21`)

An unordered collection of key–value pairs modelling one entity.

```js
let student = { name:"Anjali", age:20, courses:["Web Programming","DBMS"], isActive:true };
console.log(student.name);       // dot notation
console.log(student["age"]);     // bracket notation
student.branch = "CSE";          // add a property dynamically
delete student.isActive;         // remove a property
```
Bracket notation is required when the key is dynamic (`student[key]`) or contains spaces. Objects hold arrays and arrays hold objects — nesting freely is exactly the shape JSON later formalises (Module 5).

### 2.18 The DOM (`2:p21`)

**Story:** the browser reads your HTML file once and builds a live family tree in memory. JavaScript never edits the file — it edits that tree, and the screen updates.

Every element, attribute and text becomes a **node**; `document` is the root.

```
document
 └── html
     ├── head → title
     └── body → h1, p
```

| Task | Code |
|---|---|
| Select by id | `document.getElementById("main-title")` |
| By class | `document.getElementsByClassName("card")` |
| First match / all matches | `document.querySelector(".card")` / `querySelectorAll(".card")` |
| Read/write text | `el.textContent = "New"` |
| Write HTML | `el.innerHTML = "<em>New</em>"` |
| Style | `el.style.color = "purple"` |
| Attribute | `el.setAttribute("class","highlighted")` |

`textContent` inserts literal text (safe); `innerHTML` parses markup (powerful, an injection risk with user data).

### 2.19 Events and callbacks (`2:p21–22`)

An **event handler** is a function that runs when something happens. Register it with `addEventListener(type, fn)` (preferred), an element property (`btn.onclick = fn`), or an inline attribute (`onclick="fn()"` — avoid). Events asked about: `click`, `submit`, `change`, `input`, `load`, `keydown`/`keyup`.

```js
document.querySelector("#submitBtn").addEventListener("click", function(){
  alert("Button was clicked!");
});
```

**Callback vs normal function** (Q57): a normal function is called by *you*; a **callback** is a function *you pass as an argument* so something else can call it later (an event, `setTimeout`, `map`). Same syntax, different contract — the caller is the browser or the library, and it decides *when*.

```js
function greet(name){ console.log("Hi " + name); }   // normal
setTimeout(() => greet("Anjali"), 1000);             // greet passed as a callback
[1,2,3].forEach(n => console.log(n));                // callback per element
```

---

## 3. PART 2 — Answer bank

### 3.1 3-mark answers (Part A)

**MASTER A — CSS rule syntax (Q37, Q60, Q222a).** (1) A rule = selector + declaration block: `selector { property: value; }`; (2) the selector picks elements, each declaration is one `property:value;` pair terminated by a semicolon, the block is `{ }`; (3) example `h1{color:#5E3E8E;font-size:28px}` — CSS comments are `/* */` only, and property names are lowercase-hyphenated.

**MASTER B — Three attachment methods (Q38, Q39, Q40, Q41, Q55, Q61, Q186a, Q190, Q222b).** (1) Inline (`style=""`) — one element, highest specificity, no `:hover`/media queries, no reuse; (2) embedded (`<style>` in `<head>`) — whole document, medium specificity, not reusable across pages; (3) external (`<link rel="stylesheet" href="main.css">`) — any page that links it, lowest specificity, cached, best separation. Two advantages of external over inline: reuse across all pages from one file + browser caching (and clean separation of content/presentation).

**MASTER C — Positioning (Q42, Q56, Q63, Q224a).** (1) `relative` offsets the element from its own normal position and **keeps its space reserved**; (2) `absolute` removes it from flow and positions it against the nearest positioned ancestor (else the viewport), so siblings close the gap; (3) pattern: `relative` wrapper + `absolute` child to pin a badge; `fixed` is viewport-anchored, `static` is the default.

**MASTER D — Box model (Q43, Q64, Q189, Q200).** (1) Every element is a box of four layers: content → padding (inside, transparent, background shows through) → border → margin (outside, separates neighbours); (2) rendered width = width + 2(padding) + 2(border) + 2(margin) under `content-box`, and `box-sizing:border-box` makes the declared width inclusive; (3) margins collapse between block siblings, padding never does — so the box model explains all spacing and "why is my element wider than I said".

**MASTER E — Media queries (Q44, Q225b).** (1) A media query wraps rules in a condition: `@media (min-width:768px){ ... }`; (2) conditions can test width, orientation, resolution and media type (`print`); (3) responsive design = fluid units + flexible images (`max-width:100%`) + mobile-first `min-width` queries, and it only works with `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.

**MASTER F — Backgrounds (Q45, Q191).** (1) `background-image:url('x.jpg')` draws an image behind content; (2) `background-repeat` (`repeat|no-repeat|repeat-x|repeat-y`) and `background-position` (`center top`, `20px 10px`) place it; (3) add `background-size:cover|contain` to fit it, `background-attachment:fixed` for parallax; shorthand `background:#f0f0f0 url('x') no-repeat center/cover`.

**MASTER G — `prompt()` and JS input (Q46, Q65, Q192a).** (1) `prompt(message, default)` opens a modal dialog and returns the typed text as a **string**, or `null` if Cancel is pressed; (2) because it is always a string, convert with `Number()` / `parseInt()` before arithmetic; (3) other inputs: `confirm()` (true/false), `alert()` (output only), and real form fields read via the DOM (`input.value`) — prefer forms for production UIs since dialogs block the page.

**MASTER H — Arithmetic (Q47, Q66).** (1) `+ - * / % **` plus `++`/`--`, with `+` also concatenating strings; (2) precedence BODMAS — parentheses, exponent, `* / %`, `+ -`, left to right; `(10+5)*2-3**2 = 21`; (3) divisions are floating point (`5/2 = 2.5`), unlike C.

**MASTER I — Control statements (Q48, Q193a, Q226b).** (1) `if / else if / else` selects one branch by condition; (2) `switch(expr){case v: ...; break; default: ...}` compares one value against many, and `break` prevents fall-through; (3) ternary `cond ? a : b` is a one-line if/else; loops `for`, `while`, `do...while` repeat.

**MASTER J — Arrays (Q49, Q52, Q67).** (1) `let a = ["HTML","CSS","JS"]` — ordered, zero-indexed, mixed types allowed, `a.length` gives the count; (2) access/assign `a[0]`, iterate `forEach`, add/remove with `push/pop/unshift/shift`, transform with `map/filter`; (3) an array is index-addressed; an object is key-addressed — `a[0]` vs `o["name"]`.

**MASTER K — Objects (Q50, Q54, Q67).** (1) `let s = {name:"Anjali", age:20}` — unordered key–value pairs; (2) access with dot (`s.name`) or brackets (`s["name"]`, required for dynamic keys); (3) add dynamically `s.branch = "CSE"`, remove with `delete s.age` — no class declaration needed.

**MASTER L — DOM (Q51, Q53, Q59).** (1) The DOM is the browser's in-memory tree of nodes for the loaded HTML — the live structure JS reads and modifies; (2) select with `getElementById`, `querySelector(All)`, `getElementsByClassName`; (3) change with `el.textContent`, `el.innerHTML`, `el.style.x`, `setAttribute` — the page re-renders immediately, the source file is untouched.

**MASTER M — Pseudo-classes (Q58, Q202a).** (1) A pseudo-class styles an element in a state or position: `a:hover`, `a:visited`, `input:focus`, `li:first-child`, `li:nth-child(even)`; (2) written with one colon, unlike pseudo-elements (`::before`) which style a part; (3) classic uses: hover feedback, zebra table rows, focus outlines — and order matters (`:link :visited :hover :active`).

**MASTER N — Selectors + properties (Q62, Q223).** Type/element (`p`), universal (`*`), class (`.card`), ID (`#header`), grouping (`h1,h2`), attribute (`input[type="text"]`), pseudo-class (`:hover`), combinator (`nav a`, `ul>li`, `h2+p`); properties examples: `color:#333`, `font-size:18px`, `margin:10px auto`, `padding:8px 12px`, `background:#f5f5f5`.

**MASTER O — Callback vs normal function (Q57).** A normal function is invoked directly by your code; a callback is passed *as an argument* and invoked later by whoever receives it (an event listener, `setTimeout`, `map`). Same syntax; the difference is control of *when*. Example: `btn.addEventListener("click", handleClick)` — the browser calls `handleClick`, not you.

### 3.2 14-mark answers (Part B)

#### §3.1 Q186 / Q190 / Q222 — Three methods of applying CSS
**Structure:** (a) 7: three methods with code, scope, specificity, reuse. (b) 7: advantages/disadvantages of external.
Method table (see §2.3) + one code block per method + precedence line: browser default < external < embedded < inline (with `!important` overriding all).
External advantages: single source of truth, browser caching, easier maintenance/teamwork, clean separation, supports media queries and pseudo-classes. Disadvantages: extra request on first load; if the file fails, every page loses styling; requires correct relative paths; harder to override locally (lowest specificity).

#### §3.2 Q187 — CSS2 vs CSS3 + a styled button
(a) CSS2 (1998): single monolithic spec, added positioning and media types. CSS3: modular, each module versioned separately (Selectors, Flexbox, Grid, Media Queries, Animations); new features: `border-radius`, `box-shadow`, gradients, `rgba()`, transitions/animations, transforms, flexbox/grid, web fonts, multiple backgrounds.
(b)
```css
.btn{
  background:#5E3E8E; color:#fff; padding:10px 22px; border:none;
  border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,.3);
  transition:background .3s ease, transform .15s;
}
.btn:hover{ background:#7a5aa8; transform:translateY(-1px); }
```
Explain each: `border-radius` rounds corners; `box-shadow` (x y blur colour) lifts it; `transition` animates property changes over time so hover is smooth, not a jump.

#### §3.3 Q188 — The cascade and conflicts
(a) The cascade is the conflict-resolution algorithm: (1) **importance** (`!important` beats normal), (2) **origin/specificity** (inline > ID > class/attr/pseudo-class > type > universal), (3) **source order** (later wins when tied); inheritance fills in unset inheritable properties.
(b) Scenario: `<p id="intro" class="note" style="color:red">` with external `#intro{color:green}`, embedded `.note{color:blue}`, and the inline style. Trace it out loud: inline wins → red. Remove inline → compare ID (0,1,0) vs class (0,0,1) → green. Remove the ID rule → blue. Show the same link/p element at each step so the marker sees the mechanism, not just the answer.

#### §3.4 Q189 / Q200 — Box model with numbers
(a) Draw the nested-box figure, name the four layers, give the formula, mention `box-sizing`, margin collapse.
(b) Code `.box{width:300px;padding:20px;border:5px solid #5E3E8E;margin:15px}` → explain each layer and compute rendered width 380px; then `box-sizing:border-box` → 300px total with 250px content. Add a two-box example proving margin collapse (20px + 30px margins → 30px gap).

#### §3.5 Q191 / Q224a — Backgrounds and positioning in practice
Give the shorthand plus longhand, `cover` vs `contain` (fill/may crop vs fit/may letterbox), `background-attachment:fixed` parallax, multiple backgrounds (`url(a), url(b)` with comma separation) **(standard)**. Combine with §2.8 positioning: a `relative` hero with an `absolute` caption pinned bottom-left.

#### §3.6 Q192 — User input in JS
(a) `prompt()` for one-off text; `confirm()` for yes/no; form fields (`<input>`, `<select>`, `<textarea>`) read through the DOM; event-driven input (`input`, `change` events). Discuss blocking/modal nature and why forms are preferred in production.
(b) Code: `prompt` → validate not null and not empty after `trim()` → `alert` greeting → else re-prompt / show error. Include numeric conversion for a second prompt.

#### §3.7 Q193 — Decision making
(a) `if`, `if...else`, `else if` ladder, `switch`, ternary — with a one-line example each.
(b) Day-of-week function:
```js
function dayName(n){
  switch(n){
    case 1: return "Monday";
    case 2: return "Tuesday";
    case 3: return "Wednesday";
    case 4: return "Thursday";
    case 5: return "Friday";
    case 6: return "Saturday";
    case 7: return "Sunday";
    default: return "Invalid day";
  }
}
```
Explain `default` (no match, e.g. 0 or 8), `break` vs `return` (return leaves the function immediately), and that `switch` uses strict comparison.

#### §3.8 Q194 / Q226 — Fundamentals + control statements
(a) Variables (`let`/`const`), data types table, functions (declaration, parameters, `return`), `typeof`, dynamic typing.
(b) `for` (known count), `while` (test first), `do...while` (test last → at least one iteration), `break`/`continue`, and a nested-loop example (a 3×3 table built with `for`).

#### §3.9 Q195 — Array manipulation
(a) `push/pop`, `unshift/shift`, `indexOf`, `slice` vs `splice`, `map/filter/forEach`, `length`.
(b) Live demo code with `console.log` after each op and the resulting array written as a comment — examiners give marks for the *result* of each operation, so write the before/after array next to each line.

#### §3.10 Q196 — Objects + printing properties
```js
let student = { name:"Anjali", age:20, course:"CSE" };
function printValues(obj){
  for (let key in obj){ console.log(key + ": " + obj[key]); }
}
printValues(student);
```
Explain `for...in` iterates keys, `obj[key]` is required because `key` is dynamic, and output order follows insertion order for string keys.

#### §3.11 Q197 / Q227 — Arrays vs objects; form processing
(a) Table: ordered vs keyed, index vs key, `length` vs none, use for lists vs records, methods differ.
(b) Form processing: `getElementById` on fields, read `.value`, validate, `event.preventDefault()` to stop the default reload, then either `form.submit()` or `fetch()`; and the reminder that client-side validation never replaces server-side validation.

#### §3.12 Q198 — CSS specifics + JS control statements
Four separate CSS answers (write them as labelled items — each is worth ~1.5):
```css
a:hover, a:active { background-color: yellow; }
ol { list-style-type: lower-alpha; }
body { background-image: url('Boat.gif'); }
body { border: 1px dotted #000; }
```
Note the trap: `lower case alphabet` = `lower-alpha` (not `lower-case`); the border shorthand order is width style colour.
Then control statements: if/else, switch, for, while, do-while with one example each.

#### §3.13 Q199 — Event handlers + class selectors
(a) Three registration methods (inline attribute, element property, `addEventListener`) and why the third is preferred (multiple handlers, removable, cleaner). Code the Welcome→"Hello from JavaScript" demo:
```html
<p id="msg">Welcome</p><button id="btn">Click</button>
<script>
  document.getElementById("btn").addEventListener("click", function(){
    document.getElementById("msg").innerHTML = "<b>Hello from JavaScript</b>";
  });
</script>
```
(b) `.style1{color:blue;text-align:right;text-decoration:underline;font-style:italic;word-spacing:2cm}` and `.style2{background-color:yellow;border:1px solid blue;padding:1.5cm}` applied to `<p class="style1">` / `<p class="style2">`. Note `word-spacing` accepts lengths and `1.5cm` is legal CSS.

#### §3.14 Q201 — DOM interaction
(a) Explain the DOM tree and node selection; then the two snippets: change `p.style.backgroundColor` on click; change `p.textContent`/`innerHTML` on click. Use `addEventListener`, not inline `onclick`, and mention `document.querySelector`.
(b) Same page with separate buttons for colour and text — shows you understand that handlers are independent functions.

#### §3.15 Q202 — Pseudo-classes + digital clock
(a) §2.6 with runnable examples (link states, `:focus`, `:nth-child`, `::first-letter`).
(b)
```html
<p id="clock"></p>
<script>
  function tick(){
    const d = new Date();
    const p = n => String(n).padStart(2,'0');
    document.getElementById("clock").textContent =
      p(d.getHours()) + ":" + p(d.getMinutes()) + ":" + p(d.getSeconds());
  }
  tick();
  setInterval(tick, 1000);
</script>
```
Explain `Date`, `getHours/Minutes/Seconds`, `padStart` for two digits, `setInterval(fn, 1000)` repeating every second, and why `tick()` is called once immediately (otherwise the clock is blank for a second).

#### §3.16 Q223 / Q224 / Q225 — The CSS sweep
Compose from MASTER N (selectors + properties), MASTER C (positioning) + MASTER F (backgrounds) + list/table CSS, and MASTER D + MASTER E. Each sub-part gets its own labelled block and one short code block; do not merge them into one essay.

#### §3.17 Q228 — Two programs
Prime check: loop `i` from 2 to `Math.sqrt(n)`, return false on divisibility, handle `n < 2`.
Form validation: `submit` listener, `preventDefault()`, check `.value.trim() === ""`, regex `/^[^@\s]+@[^@\s]+\.[a-z]{2,}$/i` for email, write the error into a `<span id="err">` rather than `alert` (better marks — shows DOM manipulation).

---

## 4. PART 3 — Code you must be able to write by hand

**D1.** CSS rule with selector/declarations + comment syntax.
**D2.** Same `<p>` styled inline, embedded, and external — plus the `<link>` line.
**D3.** Specificity demo: inline vs `#id` vs `.class` vs `p` on one element.
**D4.** Selector zoo: universal, type, class, id, group, descendant, child, adjacent, attribute (all four operators).
**D5.** Link states in LVHA order, `:focus`, `:nth-child(even)` zebra rows, `::first-letter`.
**D6.** Background hero: image + `no-repeat` + `center` + `cover`, and the shorthand version.
**D7.** Positioning: `relative` parent + `absolute` badge top-right; then a `fixed` header.
**D8.** Box model numbers: compute rendered width, then re-compute with `border-box`.
**D9.** List styling: `lower-alpha`, `square`, `none`, `inside`.
**D10.** Table CSS: `border-collapse`, cell padding, zebra striping, caption styling.
**D11.** Mobile-first responsive: base + two `min-width` queries + `max-width:100%` image.
**D12.** `prompt()` with empty-check and numeric conversion, output via `innerHTML`.
**D13.** if/else-if ladder + `switch` day-of-week + ternary.
**D14.** Loops: `for` 1–10, `while`, `do...while`, and a `for` that builds a table row.
**D15.** Array ops demo: push/pop/unshift/shift/indexOf/slice/splice/map/filter with printed results.
**D16.** Object ops: literal, dot + bracket access, add property, `for...in` print.
**D17.** DOM update: `getElementById` + `innerHTML` + `style.color`, on button click via `addEventListener`.
**D18.** Welcome→Hello button demo (Q199a) verbatim.
**D19.** Prime check function + a form-validation handler with `preventDefault` and an error `<span>`.
**D20.** Digital clock with `setInterval` and `padStart`.

---

## 5. 🔴 Night-before memorize sheet

| Item | Exact thing to recall | Why |
|---|---|---|
| Rule anatomy | `selector { property: value; }` | Q37, Q60 |
| Comment | `/* ... */` only | Q37 |
| Attachment | inline `style=""` > embedded `<style>` > external `<link rel="stylesheet" href="">` | Q38–41, Q55, Q186 |
| Specificity | inline > ID > class/attr/pseudo-class > type > universal; tie → later rule | Q188 |
| Specificity scores | (1,0,0) (0,1,0) (0,0,1) (0,0,0) | Q188 |
| Position values | static, relative, absolute, fixed, sticky | Q42, Q63, Q224 |
| Box layers | content → padding → border → margin | Q43, Q64, Q200 |
| Box formula | width + 2·padding + 2·border (+ margins for outer size) | Q189, Q200 |
| `box-sizing` | `content-box` default vs `border-box` inclusive | Q189 |
| Background props | image, repeat, position, size (`cover`/`contain`), attachment | Q45, Q191 |
| List props | `list-style-type` (`lower-alpha`, `square`, `none`), `-position`, `-image` | Q198, Q224 |
| Table CSS | `border-collapse:collapse`, `nth-child(even)` | Q224 |
| Viewport meta | `width=device-width, initial-scale=1.0` | Q44, Q225 |
| Media query | `@media (min-width:768px){ }` | Q44, Q225 |
| JS vars | `let` / `const` / `var` scope difference | Q194 |
| JS types | Number, String, Boolean, Undefined, Null, Object, Array | Q194 |
| `==` vs `===` | `"5"==5` true, `"5"===5` false | Q194, Q226 |
| `prompt()` | returns string or `null`; always convert | Q46, Q65, Q192 |
| Array methods | push pop shift unshift indexOf slice splice map filter forEach | Q49, Q195 |
| Object access | `o.key`, `o["key"]`, `o.newKey = v`, `delete o.key` | Q50, Q54 |
| DOM selectors | getElementById, querySelector(All), getElementsByClassName | Q51, Q199 |
| DOM writes | `textContent`, `innerHTML`, `style.x`, `setAttribute` | Q53, Q201 |
| Events | click, submit, change, input, load, keydown | Q199 |
| `preventDefault` | stops the default submit/reload | Q227, Q228 |
| Clock | `new Date()`, `getHours()`, `setInterval(fn,1000)`, `padStart(2,'0')` | Q202 |

---

## 6. 📐 Diagram + figure index

| Figure | Where | What to draw |
|---|---|---|
| CSS rule structure | `2:p2–3` | selector + block + declarations labelled |
| Three attachment methods table | `2:p5` | scope/reuse/specificity grid |
| Selector specificity ladder | `2:p7` | inline > ID > class > type |
| Position property table | `2:p8` | five values and behaviour |
| Box model | `2:p11` (ASCII figure in the deck) | four nested labelled boxes + width sum |
| Media query breakpoints | `2:p13` | mobile → tablet → desktop |
| DOM tree | `2:p21` | document → html → head/body → nodes |
| Event table | `2:p21` | event → when it fires |

---

## 7. Say-this-if-grilled defence lines

1. "CSS is a separate language so presentation can change without touching content — that separation is the reason it exists."
2. "Inline styles win on specificity but lose on everything else — no reuse, no media queries, no pseudo-classes."
3. "`!important` beats specificity; that is why it is a last resort and not a fix."
4. "`relative` reserves the space; `absolute` does not — that one sentence explains most positioning bugs."
5. "`box-sizing:border-box` exists because padding and border used to silently add to the declared width."
6. "Margins collapse vertically between blocks; padding never collapses — that is why padding is used for inner spacing."
7. "`prompt()` returns a string or null — `"5" + 3` gives `"53"`, so convert before arithmetic."
8. "`===` avoids the coercion surprises of `==`; `"5" == 5` is true and that is a bug factory."
9. "An array is index-addressed and ordered; an object is key-addressed and unordered — that is the whole difference."
10. "The DOM is the live tree, not the HTML file — JavaScript mutates the tree and the screen follows."
11. "A callback is not a different kind of function; it is a function handed to someone else to call."
12. "Client-side validation is UX only — disable JavaScript and it is gone, so the server must validate again."
13. "A media query without the viewport meta tag is wasted on phones, because the browser assumes a 980px desktop."
