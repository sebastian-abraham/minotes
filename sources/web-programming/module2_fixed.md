# WEB PROGRAMMING MOD-2.pdf -> markdown

Converted from the PDF text layer (pymupdf). Page markers `### p<N>` map 1:1 to PDF pages. `[Image Description: ...]` blocks are placeholders: the page is diagram/figure-heavy and must be rendered and viewed, not guessed.


### p1

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 1 of 22 
WEB PROGRAMMING 
Module 2 — Lecture Notes 
Introduction to Cascading Style Sheets (CSS) and JavaScript 
 
Topics Covered 
# 
Topic 
Hrs 
1 
Introduction to CSS — Introduction to CSS3; Basic Syntax and Structure; Inline Styles 
3 
2 
Embedded Style Sheets; Linking External Style Sheets 
3 
3 
Exploring CSS Selectors — Properties and Values 
3 
4 
Positioning Elements — Absolute/Relative Positioning; Backgrounds; List Styles; Table Layouts 
3 
5 
Box Model and Text Flow; Basics of Responsive CSS; Viewport and Media Queries 
3 
6 
Introduction to JavaScript — Scripting; Programming Fundamentals; prompt Dialogs 
3 
7 
Arithmetic; Decision Making; Control Statements 
3 
8 
Arrays; Objects; Document Object Model (DOM); Form Processing 
3 
 
ESE Weightage: 20% (Module 2)


### p2

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 2 of 22 
1. Introduction to CSS, CSS3, Basic Syntax and Structure, Inline Styles 
1.1 What is CSS? 
CSS (Cascading Style Sheets) is a style-sheet language used to describe the presentation of an HTML document 
— colours, fonts, spacing, layout — while HTML remains responsible only for structure and meaning. Separating 
structure (HTML) from presentation (CSS) makes sites easier to maintain, lets one stylesheet skin many pages 
consistently, and lets the same HTML be restyled for print, mobile, or accessibility needs without touching 
markup. 
• Cascading refers to the algorithm that resolves conflicts when multiple rules could apply to the same 
element, based on specificity, source order, and importance (see Module 1 recap: inline > id > class > 
element). 
• CSS was first proposed by Håkon Wium Lie in 1994 and became a W3C Recommendation (CSS1) in 1996. 
• CSS2 (1998) added positioning and media types; CSS3, from the early 2000s onward, split the specification 
into independent modules (Selectors, Flexbox, Grid, Animations, etc.), each versioned and evolving 
separately — this is why we now speak of individual CSS3 modules rather than one single CSS3 document. 
1.2 CSS3 — Modular Evolution 
Unlike CSS1/CSS2 which were single monolithic specifications, CSS3 is organised as a collection of independent 
modules that can progress through standardisation at their own pace. This is why browsers can support one 
CSS3 feature (e.g. Flexbox) fully while another (e.g. a newer Grid feature) is still experimental. 
CSS3 Module 
Adds 
Selectors Level 3/4 
Attribute, pseudo-class and combinator selectors (see Section 3) 
Box Model 
box-sizing property to change how width/height are calculated 
Backgrounds and Borders 
Multiple backgrounds, rounded corners (border-radius), box-shadow 
Flexible Box Layout (Flexbox) 
One-dimensional flexible layouts 
Grid Layout 
Two-dimensional grid-based layouts 
Media Queries 
Responsive styling based on viewport/device characteristics 
Transitions & Animations 
Smooth property changes and keyframe-based animation without JavaScript 
1.3 Basic CSS Syntax 
A CSS rule (rule-set) consists of a selector, which targets HTML element(s), followed by a declaration block in 
curly braces containing one or more declarations. 
selector { 
 property: value; 
 property: value; 
}


### p3

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 3 of 22 
/* Example */ 
h1 { 
 color: #5E3E8E; 
 font-size: 28px; 
 text-align: center; 
} 
Part 
Meaning 
Selector 
Pattern identifying which element(s) the rule applies to (h1, .card, #logo, etc.) 
Declaration Block 
The { ... } portion containing the rules 
Property 
The style aspect being set (color, font-size, margin, etc.) 
Value 
The setting applied to that property 
Declaration 
A single property: value; pair, always terminated with a semicolon 
• CSS comments use /* ... */ (no // single-line comment syntax, unlike JavaScript). 
• Property names are case-insensitive but conventionally written in lowercase with hyphens (kebab-case): 
font-size, not fontSize. 
1.4 Inline Styles 
An inline style is applied directly to a single element using its style attribute, mixing presentation into the HTML 
markup itself. 
<p style="color: red; font-weight: bold; margin-top: 10px;"> 
 This paragraph has an inline style. 
</p> 
• Highest specificity of the three CSS application methods (inline, embedded/internal, external) — it 
overrides rules from <style> blocks and external stylesheets for that one element. 
• Cannot use pseudo-classes/pseudo-elements (:hover, ::before), nor media queries, since it is scoped to one 
element only. 
• Best avoided for anything beyond a quick one-off tweak or dynamically generated styles from JavaScript, 
because it defeats the separation-of-concerns benefit of CSS and is hard to maintain across a whole site.


### p4

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 4 of 22 
2. Embedded Style Sheets and Linking External Style Sheets 
2.1 Embedded (Internal) Style Sheets 
An embedded stylesheet is placed inside a <style> element within the <head> of the HTML document. Rules 
apply to the whole document (or the elements matched by their selectors), not just a single tag. 
<head> 
 <meta charset="UTF-8"> 
 <title>My Page</title> 
 <style> 
 body { 
 font-family: Arial, sans-serif; 
 background-color: #f5f5f5; 
 } 
 h1 { 
 color: #5E3E8E; 
 } 
 .highlight { 
 background-color: yellow; 
 } 
 </style> 
</head> 
• Useful for single-page documents or page-specific overrides, but the CSS is not reusable across multiple 
pages — every page needs its own copy. 
2.2 External Style Sheets 
An external stylesheet is a separate .css file linked into the HTML document using the <link> element, placed in 
the <head>. This is the recommended approach for real projects. 
<!-- In every HTML page that should use these styles --> 
<link rel="stylesheet" href="styles/main.css"> 
 
/* Contents of styles/main.css */ 
body { 
 font-family: Arial, sans-serif; 
 margin: 0; 
} 
h1 { 
 color: #5E3E8E; 
} 
Attribute 
Purpose 
rel="stylesheet" 
Tells the browser this linked resource is a stylesheet. 
href 
Path/URL to the .css file (relative or absolute). 
type="text/css" 
Optional in HTML5 (text/css is assumed by default). 
media 
Restricts when the stylesheet applies, e.g. media="print" for print-only styles.


### p5

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 5 of 22 
2.3 Comparing the Three Methods 
Method 
Scope 
Reusability 
Specificity 
Typical Use 
Inline (style="") 
Single element 
None 
Highest 
Quick one-off / 
dynamic JS styling 
Embedded (<style>) 
One document 
Low (copy-paste 
per page) 
Medium 
Single-page demos, 
page-specific 
overrides 
External (<link>) 
Any page that 
links it 
High 
Lowest (of the 
three, but easiest 
to override with 
cascade rules) 
Whole websites, 
production projects 
Why external wins in practice: 
One CSS file can style an unlimited number of pages consistently, is cached by the browser across 
page loads (faster repeat visits), and keeps content (HTML) cleanly separated from presentation 
(CSS) — the core design principle CSS was built for.


### p6

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 6 of 22 
3. Exploring CSS Selectors — Properties and Values 
3.1 Basic Selectors 
Selector 
Example 
Matches 
Universal 
* { margin: 0; } 
Every element on the page 
Type/Element 
p { line-height: 1.5; } 
All <p> elements 
Class 
.card { padding: 10px; } 
All elements with class="card" 
ID 
#header { height: 60px; } 
The single element with id="header" 
Grouping 
h1, h2, h3 { font-family: serif; } 
All elements listed, comma-separated 
3.2 Combinators 
Combinator 
Example 
Matches 
Descendant (space) 
nav a { color: white; } 
Any <a> nested anywhere inside <nav> 
Child (>) 
ul > li { list-style: none; } 
<li> that is a direct child of <ul> 
Adjacent sibling (+) 
h2 + p { margin-top: 0; } 
The <p> immediately following an <h2> 
General sibling (~) 
h2 ~ p { color: gray; } 
All <p> siblings after an <h2> 
3.3 Attribute Selectors 
input[type="text"] { border: 1px solid #ccc; } 
a[href^="https"] { color: green; } /* starts with */ 
a[href$=".pdf"] { color: red; } /* ends with */ 
a[href*="saintgits"] { font-weight: bold; } /* contains */ 
3.4 Pseudo-classes and Pseudo-elements 
Type 
Example 
Meaning 
Pseudo-class 
a:hover { text-decoration: underline; 
} 
Styles an element in a particular state (:hover, 
:focus, :visited, :nth-child(2), :first-child) 
Pseudo-element 
p::first-line { font-weight: bold; } 
Styles a specific part of an element's content 
(::before, ::after, ::first-letter, ::first-line) 
3.5 Properties and Values 
A property names what aspect of the element to style; a value specifies the setting. CSS values come in several 
data types: 
Value Type 
Examples 
Keyword 
bold, center, none, solid


### p7

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 7 of 22 
Length 
16px, 2em, 1.5rem, 100vh 
Percentage 
50%, 100% 
Colour 
red, #5E3E8E, rgb(94,62,142), rgba(94,62,142,0.5), hsl(261,39%,40%) 
URL 
url('images/bg.png') 
Number 
1.5 (used unitless for line-height, opacity, etc.) 
.card { 
 color: #333333; 
 font-size: 1.2rem; 
 background-image: url('images/pattern.png'); 
 border: 2px solid rgba(94, 62, 142, 0.6); 
} 
3.6 Selector Specificity (Quick Recap) 
When multiple rules target the same element, the browser calculates a specificity score to decide which one 
wins: inline styles beat ID selectors, which beat class/attribute/pseudo-class selectors, which beat type selectors. 
Equal specificity is resolved by source order — the later rule wins.


### p8

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 8 of 22 
4. Positioning Elements, Backgrounds, List Styles, Table Layouts 
4.1 The position Property 
Value 
Behaviour 
static 
Default. Element follows normal document flow; top/left/right/bottom have no effect. 
relative 
Positioned relative to its own normal position, using top/left/right/bottom offsets; the 
original space it occupied is preserved (other elements don't move in to fill it). 
absolute 
Removed from normal flow and positioned relative to its nearest ancestor that has a 
position other than static (its 'positioned' ancestor); if none exists, relative to the <html> 
root/viewport. 
fixed 
Positioned relative to the browser viewport; stays in place even when the page is 
scrolled. 
sticky 
Behaves like relative until the scroll position crosses a threshold, then behaves like fixed 
within its container. 
.container { 
 position: relative; /* establishes positioning context */ 
 width: 400px; 
 height: 200px; 
} 
 
.badge { 
 position: absolute; 
 top: 10px; 
 right: 10px; /* pinned to top-right of .container */ 
} 
4.1.1 Absolute vs Relative Positioning — Key Difference 
• relative: the element is offset from where it would normally sit; the layout still 'reserves' its original spot. 
• absolute: the element is taken out of the normal flow entirely; other elements behave as if it isn't there, 
and it's placed according to its nearest positioned ancestor. 
Common pattern: 
Give a wrapper position: relative and its child position: absolute so the child can be precisely placed (e.g. a 
badge/icon in a card corner) without affecting the rest of the layout. 
4.2 Backgrounds 
.hero { 
 background-color: #f0f0f0; 
 background-image: url('banner.jpg'); 
 background-repeat: no-repeat; 
 background-position: center top; 
 background-size: cover; 
 /* Shorthand equivalent: */


### p9

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 9 of 22 
 background: #f0f0f0 url('banner.jpg') no-repeat center top / cover; 
} 
Property 
Purpose 
background-color 
Solid fill colour behind the content. 
background-image 
Image (or gradient) drawn behind the content. 
background-repeat 
repeat (default), no-repeat, repeat-x, repeat-y 
background-position 
Where the image starts, e.g. center, top right, 20px 10px 
background-size 
cover (fills, may crop), contain (fits fully, may letterbox), or explicit dimensions 
background-attachment 
scroll (default) or fixed (parallax-style, stays put while page scrolls) 
4.3 List Styles 
ul { 
 list-style-type: square; 
 list-style-position: inside; 
} 
ol { 
 list-style-type: upper-roman; 
} 
li.no-marker { 
 list-style: none; 
} 
Property 
Common Values 
list-style-type 
disc, circle, square, decimal, upper-alpha, lower-roman, none 
list-style-position 
outside (default, marker sits outside content box) / inside 
list-style-image 
url('bullet.png') — custom bullet graphic 
list-style (shorthand) 
list-style: square inside url('bullet.png'); 
4.4 Table Layouts (CSS for Tables) 
table { 
 width: 100%; 
 border-collapse: collapse; /* merges double borders into one */ 
} 
th, td { 
 border: 1px solid #999; 
 padding: 8px 12px; 
 text-align: left; 
} 
tr:nth-child(even) { 
 background-color: #f7f5fa; /* zebra striping */ 
} 
caption {


### p10

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 10 of 22 
 caption-side: bottom; 
 font-style: italic; 
} 
Property 
Purpose 
border-collapse 
collapse merges adjacent cell borders into a single line; separate (default) keeps them 
distinct with border-spacing between. 
table-layout 
auto (default, column widths follow content) or fixed (widths follow the first row / 
explicit CSS, faster rendering for large tables). 
:nth-child(even/odd) 
Commonly used with tr to create alternating row colours (zebra striping) for readability.


### p11

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 11 of 22 
5. Box Model and Text Flow, Responsive CSS, Viewport and Media 
Queries 
5.1 The CSS Box Model 
Every HTML element is rendered as a rectangular box made of four nested layers, from the inside out: content, 
padding, border, and margin. 
┌─────────────────────────────┐ 
│ margin │ 
│ ┌───────────────────────┐ │ 
│ │ border │ │ 
│ │ ┌─────────────────┐ │ │ 
│ │ │ padding │ │ │ 
│ │ │ ┌───────────┐ │ │ │ 
│ │ │ │ content │ │ │ │ 
│ │ │ └───────────┘ │ │ │ 
│ │ └─────────────────┘ │ │ 
│ └───────────────────────┘ │ 
└─────────────────────────────┘ 
Layer 
Purpose 
content 
The actual text/image/etc.; sized by width and height. 
padding 
Transparent space between the content and the border (inside the element's background). 
border 
A visible (or invisible) line surrounding the padding: border-width, border-style, border-color. 
margin 
Transparent space outside the border, separating this element from its neighbours; margins can 
collapse between adjacent block elements. 
.box { 
 width: 300px; 
 padding: 20px; 
 border: 5px solid #5E3E8E; 
 margin: 15px; 
} 
/* Rendered total width = 300 + 20*2 + 5*2 + 15*2 = 380px by default */ 
5.1.1 box-sizing 
* { 
 box-sizing: border-box; 
} 
• content-box (default): width/height apply to the content only; padding and border are added on top, 
making the rendered box larger than the declared width. 
• border-box: width/height include padding and border, so the declared width IS the final rendered width — 
much easier to reason about, and the near-universal modern default via a * { box-sizing: border-box; } 
reset.


### p12

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 12 of 22 
5.2 Text Flow 
Text flow describes how inline content (text, inline images) wraps and flows within the space defined by its 
containing block box. 
Property 
Purpose 
display 
block, inline, inline-block, flex, grid, none — governs how the box participates in layout. 
float 
left/right — lets an element be pushed to one side while text flows around it (classic 
technique now largely superseded by Flexbox/Grid for layout, but still valid for text-
wrap-around-image). 
clear 
Stops an element from wrapping around a floated element (clear: both;). 
text-align 
left, right, center, justify — horizontal alignment of inline content within its box. 
white-space 
normal, nowrap, pre — controls whitespace collapsing and line wrapping. 
overflow 
visible, hidden, scroll, auto — behaviour when content exceeds its box. 
5.3 Basics of Responsive CSS 
Responsive design means a page automatically adapts its layout to different screen sizes and devices (desktop, 
tablet, phone) using flexible units, flexible layout models, and conditional CSS rather than building separate sites 
per device. 
• Fluid layouts: use relative units (%, vw, vh, em, rem) instead of fixed pixels so elements scale with the 
viewport. 
• Flexible images: img { max-width: 100%; height: auto; } so images shrink to fit their container instead of 
overflowing. 
• Mobile-first approach: write base styles for small screens first, then progressively add rules for larger 
screens inside min-width media queries. 
5.4 The Viewport meta Tag 
Before applying responsive CSS, the HTML document must declare its viewport, or mobile browsers will render 
the page at a fixed desktop-like width (e.g. 980px) and then zoom out — defeating responsive CSS entirely. 
<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
Directive 
Meaning 
width=device-width 
Sets the layout viewport width to match the device's actual screen width in CSS pixels. 
initial-scale=1.0 
Sets the initial zoom level when the page first loads (1.0 = no zoom). 
maximum-scale / user-scalable 
Can restrict pinch-zoom (use cautiously — restricting zoom can harm accessibility). 
5.5 Media Queries 
A media query applies a block of CSS rules only when the browser/device matches given conditions (viewport 
width, orientation, resolution, print vs screen).


### p13

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 13 of 22 
/* Base (mobile-first) styles */ 
.container { 
 display: block; 
 padding: 10px; 
} 
 
/* Tablets and up */ 
@media (min-width: 768px) { 
 .container { 
 display: flex; 
 padding: 20px; 
 } 
} 
 
/* Desktops and up */ 
@media (min-width: 1200px) { 
 .container { 
 max-width: 1140px; 
 margin: 0 auto; 
 } 
} 
 
/* Print stylesheet */ 
@media print { 
 nav, footer { display: none; } 
} 
Feature Queried 
Example 
Width 
@media (min-width: 600px) { ... } 
Orientation 
@media (orientation: landscape) { ... } 
Resolution 
@media (min-resolution: 2dppx) { ... } — for high-DPI/Retina screens 
Media type 
@media screen { ... } / @media print { ... } 
Common breakpoints (not a hard standard, but widely used): 
≤ 576px phones, 577–768px small tablets, 769–992px tablets/small laptops, 993px+ desktops. These are 
guidelines — real breakpoints should be chosen based on where a specific design actually breaks, not 
memorised numbers.


### p14

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 14 of 22 
6. Introduction to JavaScript — Scripting, Programming Fundamentals, 
prompt Dialogs 
6.1 What is JavaScript? 
JavaScript (JS) is a lightweight, interpreted, dynamically-typed scripting language that runs primarily in web 
browsers, giving HTML pages behaviour and interactivity — reacting to clicks, validating forms, updating content 
without reloading the page, and much more. Alongside HTML (structure) and CSS (presentation), JavaScript is 
the third pillar of front-end web development. 
• Created by Brendan Eich in 1995 (originally named Mocha, then LiveScript, then JavaScript) for Netscape 
Navigator. 
• Standardised as ECMAScript (ES) by ECMA International; 'JavaScript' is the common name, 'ECMAScript' is 
the formal specification name. 
• Despite the similar name, JavaScript is unrelated to Java — the naming was a marketing decision in the 
mid-1990s. 
• Client-side scripting: JS traditionally executes in the user's browser (as opposed to server-side languages 
like PHP); Node.js later extended JS to run outside the browser as well. 
6.2 Including JavaScript in a Web Page 
<!-- Inline (avoid for anything beyond trivial handlers) --> 
<button onclick="alert('Hi')">Click</button> 
 
<!-- Embedded, inside <script> tags --> 
<script> 
 console.log("Page loaded"); 
</script> 
 
<!-- External file (recommended) --> 
<script src="app.js" defer></script> 
• defer: script downloads in parallel with HTML parsing and executes only after parsing finishes, preserving 
order — the recommended default for most scripts. 
• async: downloads in parallel but executes as soon as it's ready, potentially before HTML parsing finishes — 
order relative to other scripts is not guaranteed. 
• Without defer/async, a <script> in the middle of the page blocks HTML parsing until the script finishes 
downloading and executing. 
6.3 Programming Fundamentals of JavaScript 
6.3.1 Variables 
let age = 20; // block-scoped, reassignable 
const name = "Justin"; // block-scoped, cannot be reassigned 
var legacy = true; // function-scoped, older syntax (avoid in new code)


### p15

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 15 of 22 
6.3.2 Data Types 
Type 
Example 
Number 
42, 3.14, -7 
String 
"Hello", 'World' 
Boolean 
true, false 
Undefined 
A declared variable with no assigned value 
Null 
An intentional absence of value 
Object 
{ name: "Justin", age: 20 } 
Array 
[1, 2, 3] (a specialised object) 
JavaScript is dynamically typed: a variable's type is determined at run time by its current value and can change, 
unlike statically typed languages like Java or C. 
6.3.3 Operators (Overview) 
Category 
Operators 
Assignment 
=, +=, -=, *=, /= 
Comparison 
==, ===, !=, !==, <, >, <=, >= 
Logical 
&& (and), || (or), ! (not) 
Type 
typeof, instanceof 
=== vs ==: 
=== (strict equality) compares value AND type without conversion; == (loose equality) converts 
types before comparing, which can produce surprising results (e.g. "5" == 5 is true, but "5" === 5 is 
false). Best practice: always prefer === / !== . 
6.4 Obtaining User Input with prompt Dialogs 
The prompt() function displays a modal dialog box asking the user for text input, and returns whatever the user 
types (as a string) once they click OK, or returns null if they click Cancel. 
let userName = prompt("What is your name?", "Enter name here"); 
 
if (userName !== null) { 
 alert("Hello, " + userName + "!"); 
} 
Function 
Purpose 
Returns 
prompt(message, default) 
Asks the user for text input via a modal 
dialog 
The entered string, or null if 
cancelled 
alert(message) 
Shows a message with only an OK button 
undefined


### p16

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 16 of 22 
confirm(message) 
Asks a yes/no question with OK/Cancel 
buttons 
true (OK) or false (Cancel) 
• prompt() always returns a string, even if the user types digits — numeric input typically needs conversion, 
e.g. Number(userInput) or parseInt(userInput, 10), before arithmetic is performed on it. 
• These dialogs are blocking/modal — script execution pauses until the user responds — and are considered 
old-fashioned for production UIs (custom HTML forms are preferred), but remain useful for teaching 
fundamentals and quick debugging/demos.


### p17

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 17 of 22 
7. Arithmetic, Decision Making and Control Statements 
7.1 Arithmetic Operators 
Operator 
Meaning 
Example 
+ 
Addition (also string concatenation) 
5 + 3 → 8; "a" + "b" → "ab" 
- 
Subtraction 
5 - 3 → 2 
* 
Multiplication 
5 * 3 → 15 
/ 
Division 
5 / 2 → 2.5 
% 
Modulus (remainder) 
5 % 2 → 1 
** 
Exponentiation 
2 ** 3 → 8 
++ / -- 
Increment / decrement 
let x = 5; x++; // x is 6 
Operator precedence follows standard mathematical rules (BODMAS/PEMDAS): parentheses first, then 
exponentiation, then * / %, then + -, evaluated left to right within the same precedence level. Parentheses can 
always be used to make evaluation order explicit and readable. 
let result = (10 + 5) * 2 - 3 ** 2; 
// (10+5)=15, 3**2=9, 15*2=30, 30-9=21 
console.log(result); // 21 
7.2 Decision Making — Conditional Statements 
7.2.1 if / else if / else 
let marks = 72; 
 
if (marks >= 90) { 
 console.log("Grade: A+"); 
} else if (marks >= 75) { 
 console.log("Grade: A"); 
} else if (marks >= 60) { 
 console.log("Grade: B"); 
} else { 
 console.log("Grade: F"); 
} 
7.2.2 switch Statement 
let day = 3; 
switch (day) { 
 case 1: 
 console.log("Monday"); 
 break; 
 case 2: 
 console.log("Tuesday");


### p18

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 18 of 22 
 break; 
 case 3: 
 console.log("Wednesday"); 
 break; 
 default: 
 console.log("Another day"); 
} 
• break exits the switch after a matching case executes; omitting it causes 'fall-through' into the next case 
(occasionally intentional, but usually a bug). 
• default acts like the final else — runs if no case matches (optional, but good practice to include). 
7.2.3 Ternary Operator 
let age = 20; 
let category = (age >= 18) ? "Adult" : "Minor"; 
A compact single-line alternative to a simple if/else that returns one of two values based on a condition. 
7.3 Control (Looping) Statements 
7.3.1 for Loop 
for (let i = 1; i <= 5; i++) { 
 console.log("Count: " + i); 
} 
7.3.2 while Loop 
let i = 1; 
while (i <= 5) { 
 console.log(i); 
 i++; 
} 
7.3.3 do...while Loop 
let i = 1; 
do { 
 console.log(i); 
 i++; 
} while (i <= 5); 
Key difference: a do...while loop always executes its body at least once, checking the condition afterwards, 
whereas a while loop checks the condition first and may never execute its body at all. 
7.3.4 break and continue 
for (let i = 1; i <= 10; i++) { 
 if (i === 5) break; // exits the loop entirely 
 if (i % 2 === 0) continue; // skips to the next iteration 
 console.log(i);


### p19

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 19 of 22 
}


### p20

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 20 of 22 
8. Arrays, Objects, the Document Object Model (DOM) and Form 
Processing 
8.1 Arrays 
An array is an ordered, zero-indexed list that can hold multiple values (of any type, even mixed) under a single 
variable name. 
let subjects = ["HTML", "CSS", "JavaScript"]; 
 
console.log(subjects[0]); // "HTML" (first element, index 0) 
console.log(subjects.length); // 3 
 
subjects.push("DOM"); // adds to the end 
subjects.pop(); // removes the last element 
subjects.forEach(function(subject) { 
 console.log(subject); 
}); 
Method 
Purpose 
push(item) / pop() 
Add / remove an element at the end 
shift() / unshift(item) 
Remove / add an element at the beginning 
indexOf(item) 
Finds the index of an item (-1 if not found) 
slice(start, end) 
Returns a shallow copy of a portion, without modifying the original 
splice(start, count) 
Adds/removes elements, modifying the original array 
map(fn) / filter(fn) / forEach(fn) 
Iterate/transform/select elements using a callback function 
8.2 Objects 
An object is an unordered collection of key–value pairs (properties), used to model real-world entities with 
multiple related attributes. 
let student = { 
 name: "Anjali", 
 age: 20, 
 courses: ["Web Programming", "DBMS"], 
 isActive: true 
}; 
 
console.log(student.name); // dot notation 
console.log(student["age"]); // bracket notation 
 
student.branch = "CSE"; // add a new property dynamically 
• Dot notation (object.property) is more common and readable; bracket notation (object["property"]) is 
required when the key is dynamic/stored in a variable or contains special characters.


### p21

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 21 of 22 
• Objects can contain arrays, and arrays can contain objects — nesting freely models complex, structured 
data (this is the foundation of JSON, also covered in this course's textbooks). 
8.3 The Document Object Model (DOM) 
The DOM is a tree-structured, in-memory representation of an HTML document that the browser builds when it 
loads a page. Every HTML element, attribute, and piece of text becomes a node in this tree, which JavaScript can 
read and modify — this is how JavaScript makes pages interactive: it doesn't edit the HTML file, it manipulates 
the live DOM tree that the browser is currently rendering. 
document 
 └── html 
 ├── head 
 │ └── title 
 └── body 
 ├── h1 
 └── p 
8.3.1 Selecting Elements 
let title = document.getElementById("main-title"); 
let cards = document.getElementsByClassName("card"); 
let firstCard = document.querySelector(".card"); 
let allCards = document.querySelectorAll(".card"); 
8.3.2 Reading and Changing Content 
title.textContent = "New Heading"; 
title.innerHTML = "<em>New</em> Heading"; 
title.style.color = "purple"; 
title.setAttribute("class", "highlighted"); 
8.3.3 Responding to Events 
let button = document.querySelector("#submitBtn"); 
 
button.addEventListener("click", function() { 
 alert("Button was clicked!"); 
}); 
Common Event 
Fires When 
click 
An element is clicked 
submit 
A form is submitted 
change 
An input/select value changes and loses focus 
input 
An input's value changes on every keystroke 
load 
A page/resource finishes loading 
keydown / keyup 
A key is pressed / released


### p22

Web Programming — Module 2 Lecture Notes 
Introduction to CSS and JavaScript 
Page 22 of 22 
8.4 Form Processing with JavaScript 
JavaScript can read submitted values, validate them, and prevent submission if something is wrong — all client-
side, before the data reaches the server. 
<form id="regForm"> 
 <input type="text" id="username" required> 
 <input type="email" id="email" required> 
 <button type="submit">Register</button> 
</form> 
 
<script> 
 const form = document.getElementById("regForm"); 
 
 form.addEventListener("submit", function(event) { 
 event.preventDefault(); // stop the default page-reload submission 
 
 const username = document.getElementById("username").value; 
 const email = document.getElementById("email").value; 
 
 if (username.trim() === "") { 
 alert("Username cannot be empty."); 
 return; 
 } 
 if (!email.includes("@")) { 
 alert("Please enter a valid email."); 
 return; 
 } 
 
 console.log("Form is valid. Submitting:", username, email); 
 form.submit(); // proceed with actual submission 
 }); 
</script> 
• event.preventDefault() stops the browser's default action (a full-page reload/navigation on form submit), 
allowing custom JS validation logic to run first. 
• Client-side validation improves user experience with instant feedback, but is not a security measure — data 
must always be validated again on the server, since client-side JS can be bypassed or disabled. 
• FormData(form) is a convenient built-in object for gathering all form field values at once, especially useful 
when submitting via fetch()/AJAX instead of a traditional page reload. 
Module 2 summary: 
This module builds the presentation layer (CSS: syntax, selectors, box model, positioning, responsiveness) 
and the behaviour layer (JavaScript: fundamentals, control flow, arrays/objects, DOM manipulation, form 
processing) that sit on top of the HTML structure covered in Module 1 — together these three form the 
complete client-side web development stack.
