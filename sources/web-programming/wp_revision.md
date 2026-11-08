# 📝 20CST461 Web Programming — Revision Notes (append-only)

> **What this file is:** the durable record of every teaching session — PART 1 Deep Dive (from scratch), PART 2 Exam Kit (skeletons + memorize lists), PART 3 worked code answers, and every correction from a graded drill. **Haze reads this; the agent never reads it back into context.** Newest session at the bottom.
>
> Facts marked ✅ *(3v4l)* were **executed on a real PHP interpreter** (8.2/8.3) — trust them over any memory or slide. Unmarked = directly from the deck.

---

# SESSION 1 — Module 3, hours 1–2: what PHP is, and the syntax layer under everything

Covers `module3.md` L27–246 (M3.1–M3.6 in the tracker).

---

## PART 1 — DEEP DIVE

### 1.1 What PHP actually is (3:L27–53)

**One-line story:** a web page that never changes is a *poster*; PHP is the *kitchen* — the visitor orders (a URL), and the kitchen cooks a fresh plate (HTML) per order. The visitor never sees the kitchen.

- **Static page:** the `.html` file on the server *is* the page. Every visitor gets byte-identical bytes. Written once, same forever.
- **Dynamic page:** the server holds a *program*, runs it fresh on every single request, and sends out whatever HTML that program printed *this* time. Same file, different output per request — different user, different time, different database rows.
- **Server-side scripting:** the program runs **on the web server, before anything reaches the browser**. This is the whole point: the user's browser receives *only plain HTML*. If the script queries the database, the password is never in the page. If the script chooses which rows to show, the user can't peek at the rows you didn't send.
  - Contrast (Module II): **JavaScript is client-side** — it ships to the browser as source and runs there. PHP is the mirror image: it stays home and only its *output* travels.
- **The name:** PHP = "PHP: Hypertext Preprocessor" (a recursive acronym — the first P stands for PHP itself). "Hypertext preprocessor" literally = *it processes text before it becomes hypertext/HTML*.
- **File extension `.php`**; PHP code is **mixed directly into HTML** inside `<?php ... ?>` blocks. The server processes those blocks; the plain HTML around them is passed through untouched.
- **Why it's popular (3:L33–35):** free and open-source; runs on virtually any hosting platform; huge ecosystem (WordPress, Laravel); purpose-built for dynamic pages and talking to databases. It's the **P in LAMP** (Linux, Apache, MySQL, PHP).

**The request–response cycle** (diagram 3:L57) — learn it as 5 boxes:

```
Browser  --requests page.php-->  Web Server  -->  PHP Engine runs the script
                                                      |
                                              MySQL Database (if the script queries it)
                                                      |
        <--plain HTML sent back to Browser<-----------+
```

The browser **never sees the `.php` source** — only whatever HTML the script decided to output for *this* request (3:L72).

> **Say this if grilled:** "PHP is a server-side scripting language: it executes on the web server, may talk to a database, and the client receives only the generated HTML — never the source."

### 1.2 The five syntax rules that govern every single line (3:L84–102)

Every PHP line you will ever write obeys these. Get these into your fingers and the rest is vocabulary.

**Rule 1 — the tags.** `<?php ... ?>` marks where PHP begins and ends. Anything outside them is HTML and is passed straight through.
```php
<?php
echo "inside PHP";      // the server interprets this
?>
<h1>plain HTML — the server leaves this alone</h1>
```
- A file may open and close `<?php ?>` **many times**, interleaving PHP and HTML. That is exactly how the Module 4 dynamic page works.
- **Short echo tag:** `<?= $row["name"] ?>` is a shorthand for `<?php echo $row["name"]; ?>`. Only for echoing one value.
- ⚠️ **No output may leave the server before `setcookie()` / `session_start()`** — headers must be sent first (Module 4).

**Rule 2 — variables start with `$` and need no type keyword.** `$college = "Saintgits"; $year = 2026;`

**Rule 3 — dynamically (loosely) typed.** "int" is not a thing you *declare*; it's a label describing whatever value currently sits in the box. `$x = "5";` then `$x = 5;` is legal — same variable, now a different type. Type is decided **at runtime**.

**Rule 4 — statements end with `;`** (same as C/Java). Missing `;` is the #1 beginner error. Blocks `{ }` and `if (...)` lines do **not** get a semicolon.

**Rule 5 — output goes out with `echo` / `print`,** and it becomes part of the HTML response. `echo` is not "printing to a console" — it is *appending to the page that is being built*.

The first program (3:L94–102), annotated:
```php
<?php
$college = "Saintgits";     // string
$year    = 2026;            // int
$fee     = 49999.50;        // float
echo "Welcome to $college <br>";   // double quotes → $college is substituted
echo "Year: " . $year;             // . joins string + number into "Year: 2026"
?>
```
Notice the two *different* ways of getting a variable into output: **inside double quotes it's interpolated**, **outside you glue it with `.`**. Both appear on every slide in this module.

### 1.3 Data types (3:L113–124)

| Type | Example | Notes |
|---|---|---|
| `int` | `$age = 21;` | Whole numbers |
| `float` (a.k.a. *double*) | `$fee = 499.50;` | Decimal numbers |
| `string` | `$name = "Anu";` | Text, single or double quotes |
| `bool` | `$active = true;` | `true` / `false` (case-insensitive: `TRUE` works too) |
| `array` | `$m = [88, 92];` | Ordered list **or** key-value map — the same type |
| `NULL` | `$x = null;` | Explicitly "no value" |

Plus, for completeness: `object` (an instance of a class, M3.14) and `resource` (a connection handle like `$conn` in Module 4).

**Inspecting types — the debugging pair (3:L124):**
```php
gettype($var)   // returns the type NAME as a string: "integer", "double", "string", "boolean", "array", "NULL"
var_dump($var)  // prints type AND value: string(6) "Anu"  → length in the string(bytes) form
```
✅ *(3v4l)* **Gotcha that trips people:** `gettype(1.0)` returns **`"double"`**, not `"float"` — the float type's old name shows through in `gettype`/`is_double`. In `var_dump` the float type shows as `float(1000)` in PHP 8. Know both names = same type.
✅ *(3v4l)* Type-checking functions: `is_int()`, `is_string()`, `is_array()`, `is_float()`, `is_bool()`, `is_null()` each return `true`/`false`.

### 1.4 Output: `echo` vs `print` vs `<?=` (3:L91)

| | `echo` | `print` |
|---|---|---|
| Arguments | one or more, comma-separated: `echo "a", "b";` | exactly one: `print "a";` |
| Returns a value | **nothing** (void) — so it can't be used inside an expression | ✅ returns **`1`** *(3v4l)* — so `$r = print "x";` sets `$r` to 1 |
| Speed | marginally faster (no return value, one construct fewer) | slower |
| Both | language constructs, not functions → **parentheses optional**: `echo("hi")` and `echo "hi"` both work | same |

```php
echo "A", "B", "C";          // ABC
$r = print("E: ");           // prints "E: " and returns 1  ✅ (3v4l: |1|)
echo "F:", 1, " ", 2;        // F:1 2
```
- `echo` can output **numbers, strings, booleans** — anything convertable to a string. `(string)true` → `"1"`, `(string)false` → `""` (empty!) ✅ *(3v4l)*. A classic: `echo false;` prints **nothing**.
- The short echo tag `<?= $x ?>` does exactly `echo $x;`.

### 1.5 String syntax — single vs double quotes (⭐ this is not spelled out on your slides, but it is a standard exam question and it changes the output of nearly every program)

| | Double quotes `"..."` | Single quotes `'...'` |
|---|---|---|
| Variable interpolation | ✅ **yes** — `"Hi $name"` substitutes | ❌ **no** — `'Hi $name'` prints the literal characters `$name` |
| Escape sequences | ✅ interprets `\n` newline, `\t` tab, `\\` backslash, `\"` quote, `\$` literal dollar | only `\\` and `\'` mean anything; `'\n'` prints `\n` literally |
| Speed | marginally slower (the string is parsed for variables) | marginally faster — "what you type is what you get" |
| Use when | you want interpolation/escapes | you want the string *verbatim* (HTML/JS with `$`, regex patterns, SQL) |

```php
$college = "Saintgits";
echo "A: Welcome to $college";   // A: Welcome to Saintgits   ✅ (3v4l)
echo 'B: Welcome to $college';   // B: Welcome to $college    ✅ (3v4l)  ← literal!
echo 'D: ' . $college . '\'s fee';  // D: Saintgits's fee      ✅ (3v4l) escaping \'
```

**Interpolation rules you must know exactly** ✅ *(3v4l)*:
1. **Simple** syntax: `"$name"` or `"$name more text"` — a `$` plus a variable name. To glue a letter/digit straight on, use **complex syntax with braces**: `"{$college}2026"` → `Saintgits2026` (without braces `"$college2026"` looks for a variable literally named `$college2026`).
2. **Array elements need braces inside a string:**
   - `"$arr[0]"` → ✅ works for a plain numeric index.
   - `"$arr['key']"` (or any string key) → ❌ **error** — `Warning: Undefined array key` ✅ *(3v4l)*. You **must** write `"{$arr['key']}"`.
   - **Safe rule to memorize: always use `{$arr['key']}`.** It works in every case.
3. **Object properties** interpolate without braces if simple (`"$obj->name"`) but braces are always safe: `"{$obj->name}"`.
4. **Variable variables** (rare, but it's on slide 3:L86 as a `$` rule): `$college = "x"; echo ${"college"};` ✅ prints the value of `$college`.

### 1.6 Converting between data types (3:L136–153)

**Why it exists:** PHP converts types *automatically* (loose typing) — but automatic conversion follows rules you may not have meant, so *explicit* casting keeps behaviour predictable. The deck's words: "PHP converts types automatically in many contexts (loose typing), but explicit casting keeps behaviour predictable."

**Two mechanisms:**

1. **Casts** — put the target type in parentheses in front of the value. **Does not change the original variable**, it produces a converted value (for the expression at hand):
   ```php
   (int)  (float)  (string)  (bool)  (array)
   $b = (int)$a + 5;          // $a unchanged
   ```
2. **Conversion functions** — same job, function syntax:
   ```php
   intval($x)  floatval($x)  strval($x)  boolval($x)
   ```
3. **`settype($var, "integer")`** — different in kind: converts the variable **in place** (the real variable changes) ✅ *(3v4l: returns true and $x becomes int 5)*.

**Type-checking companions:** `is_int()`, `is_string()`, `is_array()`, `is_float()`, `is_bool()` — return a bool.

**The conversion rules (all verified ✅ 3v4l):**

| Expression | Result | Why |
|---|---|---|
| `(int)true` | `1` | bools → 1/0 |
| `(int)false` | `0` | |
| `(int)null` | `0` | NULL → 0 |
| `(int)[]` (empty array) | `0` | arrays → 1 if non-empty, else 0 |
| `(int)"12abc"` | `12` | leading numeric part is taken; trailing junk ignored |
| `(int)"499.99abc"` | `499` | truncates toward zero, no rounding |
| `(string)true` | `"1"` | ⭐ true becomes "1" |
| `(string)false` | `""` | ⭐ **false becomes the EMPTY string** |
| `(float)"1e3"` | `1000.0` | scientific notation parses |
| `(bool)"0"` | `false` | ⭐⭐ the string `"0"` is **falsy** |
| `(bool)"false"` | `true` | ⭐⭐ any non-empty string except `"0"` is **truthy** — `"false"` is TRUE |
| `(bool)""` | `false` | empty string falsy |
| `(bool)0.0`, `(bool)null`, `(bool)[]` | `false` | the falsy set |

**The complete FALSY list (memorize — it decides every `if` you write):**
`false` · `0` (int) · `0.0` (float) · `""` (empty string) · `"0"` (the string zero!) · `null` · `[]` (empty array) · `0`-valued variables. **Everything else is truthy**, including `"0.0"`, `"false"`, `-1`, and `[]`-containing elements. `(bool)"0.0"` is **true** ✅ (only the *string* `"0"` is falsy, not `"0.0"`).

**Automatic (implicit) conversion in arithmetic:** `"10" + 5` → `15` ✅; `"10abc" + 5` → `15` **plus a Warning** (`A non-numeric value encountered`) ✅ in PHP 8 — in PHP 7 that warning didn't exist and old code silently produced 15. So: numeric strings convert cleanly, partially-numeric strings convert + warn.

> **Say this if grilled:** "PHP is loosely typed, so it converts automatically at runtime; explicit casting — `(int)`, `intval()`, `settype()` — is used to make the conversion intentional and the behaviour predictable."

### 1.7 Operators & expressions (3:L166–184)

- **Arithmetic:** `+` `-` `*` `/` `%` (modulus, remainder) `**` (exponent). Division `/` always returns a **float** if not exact (`10/4` → `2.5`); `intdiv(7,3)` → `2` for integer division ✅. `%` takes the **sign of the dividend like C**: `7 % -3` → `1`, `-7 % 3` → `-1` ✅.
- **`**` is right-associative:** `2 ** 3 ** 2` = `2 ** (3 ** 2)` = `2**9` = **512** ✅ (not 64).
- **Assignment:** `=` `+=` `-=` `*=` `/=` `%=` and the string one `.=` ("append to the string").
- **String concatenation is `.` (dot), NOT `+`** (3:L168). This is the single most common syntax transfer error from C/Java. `+` on strings does *arithmetic* — `"5" + 5` → `10`; `"." ` glues — `"5" . 5` → `"55"` ✅. The deck's example: `$msg = "Total: "; $msg .= (5 + 3);` → `"Total: 8"`.
- **Expression** = "anything that produces a value" — a literal, a variable, `5+3`, a function call, even `$x = 7` (assignment is an expression returning 7).

**Precedence trap:** `.` and `+`/`-` sit at the **same precedence level and evaluate left-to-right** ✅ *(3v4l)*:
```php
"1" . "2" + 3      →  ("1"."2") = "12"  →  "12" + 3 = 15  →  string(2) "15"   ✅
```
Write parentheses when mixing `.` with arithmetic — the examiner doesn't either, and that is exactly why it shows up as an output-prediction question.

| Operator group (high → low) | Operators |
|---|---|
| Arithmetic / exponent | `**` then `* / %` then `+ -` |
| Concatenation | `.` — same level as `+ -`, left-to-right |
| Comparison | `< <= > >=` |
| Equality (non-associative) | `==` `!=` `===` `!==` `<=>` |
| Logical and | `&&` (then `\|\|`) |
| Assignment | `=` `.=` `+=` … (lowest, right-associative) |

Also on the list: `??` (null-coalescing, "use this if the left side is null/missing") — you'll use it constantly in form handling: `$_POST["name"] ?? ""`.

### 1.8 Comparison: `==` vs `===` — the deck's own "most exam-relevant quirk" (3:L197–215)

- `==` **loose equality** — converts types before comparing ("the values are equal after juggling")
- `===` **strict equality** — checks **value AND type**, no conversion ("identical")
- `!=` loose inequality, `!==` strict inequality, `< > <= >=` relational, `<=>` the three-way/spaceship operator (**returns `-1`, `0`, or `1`** ✅)
- `&&` and, `||` or, `!` not — combine conditions (`and`/`or` exist as low-precedence aliases; use `&&`/`||`).

```php
var_dump("5" == 5);      // true    (the string is converted to 5)        ✅
var_dump("5" === 5);     // false   (string vs int — different types)     ✅
var_dump(0 == "abc");    // false   ← in PHP 8!  (was true in PHP ≤7)    ✅
var_dump("abc" == 0);    // false   ← in PHP 8!  (was true in PHP ≤7)    ✅
var_dump(10 == "1e1");   // true    (both are numeric → 10 vs 10.0)      ✅
var_dump(0.1 + 0.2 == 0.3); // false (floating-point rounding!)          ✅
```

**How PHP 8 compares (the rules behind the table):**
1. **bool vs anything** → convert the other side to bool, compare.
2. **null vs anything** → convert both to bool (`null == false` → `true` ✅, `"" == null` → `true` ✅, `[] == false` → `true` ✅).
3. **number vs number** → compare numerically.
4. **number vs numeric string** (`"5"`, `"1e1"`, `" 5 "`) → compare numerically → so `"5" == 5` is `true`.
5. **number vs NON-numeric string** (PHP 8) → **convert the number to a string and compare as strings** → `0 == "abc"` is `false`. (PHP 7 did the reverse — converted the string to `0` — which is why `0 == "abc"` was famously `true` before PHP 8. Written in the deck as "false (PHP 8+)" — **write the PHP 8 answer and say why**.)
6. **string vs string** → if **both** are numeric strings, compare numerically (`"10" == "1e1"` → true ✅); otherwise compare as ordinary strings, **byte by byte, case-sensitively** (`"abc" < "abd"` → true ✅).
7. **array vs array** → same size + same key/value pairs (`==`), or same order too (`===`).

**Why this matters in real code:** `==` with user input is a bug factory — `if ($pin == 0)` is `true` for the input `"abc"` in PHP 7. **Rule to adopt: always use `===` unless you deliberately want type juggling.**

**The practical `if` from the slide (3:L211–214):**
```php
$age = 20; $hasID = true;
if ($age >= 18 && $hasID) {
    echo "Entry allowed";
}
```

### 1.9 Flow control functions (3:L227–243)

The deck groups four things under "flow control functions" — each controls whether execution branches or stops:

1. **`if / elseif / else`** — the core branching construct; runs a block only when the condition is true; "exactly as in C". Note the spelling: PHP's is **`elseif`** (one word) in the alternative syntax — `else if` also works as a plain nested `else`, but `elseif` is the PHP token.
2. **`exit()` / `die()`** — ✅ **immediately stop the script.** `die()` is an **alias of `exit()`** — identical function, friendlier name. Both optionally take a message/status: `die("Connection failed");` prints that and halts. Used constantly right after a failed connection or failed validation.
3. **`return`** — inside a function: sends a value back to the caller **and immediately stops that function** — nothing after the `return` runs. (At file scope, `return` ends the included file.)
4. **Why they're a group:** all four decide whether execution continues, branches, or stops — the syllabus treats them alongside if/else.

Careful: `exit("msg")` **prints the message and stops with status 0**; `exit()` with no argument is the plain stop. In a web script "stop" means the rest of the PHP never runs, so no further HTML is generated — the page is truncated there.

---

## PART 2 — EXAM KIT (all questions this chunk can produce)

### A. 3-mark skeletons

**Q. What is PHP? Why is it called a server-side scripting language? (3)**
1. PHP = **PHP: Hypertext Preprocessor**, a free, open-source, **server-side** scripting language used to generate dynamic web pages — the "P" in LAMP.
2. **Server-side** = the script executes **on the web server** before the response is sent; the client receives **only the generated HTML**, never the PHP source, and may receive different content on every request.
3. It can embed directly into HTML via `<?php ... ?>` blocks, is **loosely typed**, supports arrays/objects/functions, and connects to databases (MySQL) — hence its use for dynamic, data-driven pages. *(Files use the `.php` extension.)*

**Q. Explain the PHP request–response cycle. (3)**
1. The browser requests a `.php` page → the **web server** hands it to the **PHP engine**.
2. The engine **runs the script**; if it queries a database, **MySQL** is involved at this point; the script's `echo`/`print` output builds an HTML document.
3. The web server returns **plain HTML** to the browser — the browser never sees the PHP source (draw the 3-box flow: Browser → Web Server → PHP Engine, with MySQL below, `module3.md` L57).

**Q. List the data types in PHP with an example. (3)** — table of 6: `int $age = 21;` · `float $fee = 499.50;` · `string $name = "Anu";` · `bool $active = true;` · `array $m = [88, 92];` · `NULL $x = null;` — plus `object` and `resource`. Add the line: "PHP is **loosely typed** — the type is decided by the value stored at runtime, not declared; `gettype()`/`var_dump()` reveal it."

**Q. Differentiate `==` and `===` with examples. (3)**
1. `==` = **loose** equality: **converts types** before comparing. `"5" == 5` → **true**.
2. `===` = **strict** equality: compares **value AND type**, no conversion. `"5" === 5` → **false**.
3. Consequence/why it matters: loose comparison produces surprising results with mixed-type input (`0 == "abc"` was `true` before PHP 8; **in PHP 8 it is `false`** because PHP 8 converts the number to a string instead of the string to a number) → **prefer `===`** for safety. *(Also: `!=` vs `!==` differ the same way.)*

**Q. Differentiate `echo` and `print`. (3)**
1. Both output text into the HTML response; both are **language constructs**, not functions (parentheses optional).
2. `echo` accepts **one or more comma-separated arguments** and **returns nothing**; `print` accepts **exactly one argument** and **returns `1`**, so it can be used in an expression (`$x = print "hi";`). `echo` is marginally faster.
3. Shorthand: `<?= $var ?>` is equivalent to `<?php echo $var; ?>`.

**Q. Differentiate single-quoted and double-quoted strings in PHP. (3)**
1. **Double quotes** -> variables are **interpolated** (`"Hi $name"`) and escape sequences work (`\n`, `\t`, `\"`, `\$`); single quotes -> the text is **literal**, `'Hi $name'` prints `$name` itself.
2. Single quotes need escaping only for `\\` and `\'`; they are marginally faster because no interpolation pass is needed.
3. Use **single quotes** for verbatim strings (HTML/JS containing `$`, regex patterns, SQL); double quotes when you want interpolation. Complex interpolation needs braces: `"{$arr['key']}"`.

**Q. Explain type conversion in PHP. (3)**
1. **Implicit (automatic):** because PHP is loosely typed it converts operands as needed — `"10" + 5` → `15`, `"10" == 10` → `true`.
2. **Explicit (casting):** prefix with `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` — e.g. `$b = (int)$a + 5;` — or use the functions `intval()`, `floatval()`, `strval()`, `boolval()`; `settype($var,"integer")` changes the variable **in place**.
3. **Why:** explicit casting makes behaviour predictable and prevents bugs from unintended juggling; `is_int()`/`is_string()`/`is_array()` test the current type. *(Falsy values to quote: `0`, `"0"`, `""`, `null`, `[]`, `false`.)*

**Q. Explain flow control functions in PHP. (3)** — number it as the deck does: `if/elseif/else` (branch), `exit()`/`die()` (stop the script immediately; `die()` is an alias of `exit()`), `return` (send a value back and stop the current function), + one line on why they form a group (all decide continuation/branch/stop).

**Q. What is the difference between `gettype()` and `var_dump()`? (3)** — `gettype($x)` returns the **type name as a string** (`"integer"`, `"string"`, `"double"`, `"boolean"`, `"array"`, `"NULL"`); `var_dump($x)` prints the **type and the value, including string length** (`string(6) "Anu"`) and recurses into arrays/objects — the better debugging tool. Remember `gettype(1.0)` says **`"double"`** even though the type is also called `float`/`floatval`.

### B. 14-mark program skeleton — "write a simple PHP program that …" (the shape to reuse in every M3 program)

Build in these 5 steps, in this order, every time:
1. Open `<?php`.
2. **Declare variables** with `$` (a string, an int, a float — show you know types).
3. **Operate on them** (arithmetic with `+ - * / %`, strings with `.`).
4. **Decide** with `if / elseif / else` — spell `elseif` correctly.
5. **Output** with `echo`, using **double quotes for interpolation** and `.` to glue. Close `?>`.
Then add a comment line per step if the question says "with comments". If the question says "using a loop/array/function" → see Sessions 2–3.

### C. Predict-the-output method (this is the biggest code-question format — a method, not luck)

Run these 4 steps in order on every snippet:
1. **Mark the boundaries.** Which lines are inside `<?php ?>` and which are literal HTML? Everything inside is *executed*; everything outside is *printed as-is*. Count that first.
2. **Build a variable table.** One row per `$var`: value + type *at the point of use* (track reassignment; note that a value only changes when a statement assigns it — `(int)$a` does **not** change `$a`; `settype()` does).
3. **Resolve every `.` and every string.** Ask "is the variable in single or double quotes?" — single = literal, double = interpolated. Then apply precedence: `.` is left-to-right at the same level as `+`/`-`.
4. **Decide the type before the comparison.** For each `==`/`if`, apply the loose-comparison rules (§1.8); for each arithmetic op with a string operand, ask "numeric string (converts silently, ✅) or partially numeric (converts **and warns**)?"
Then write the answer as the **exact output text**, line by line, and note any warnings (`Undefined array key`, `non-numeric value`) because examiners award marks for spotting them.

### D. 🔴 Memorize verbatim (night-before list for this chunk)
- `<?php ... ?>` · `<?= $x ?>` · every statement ends `;` · variables `$name`, no type keyword, case-sensitive.
- The **6 data types** and one example each.
- **`.` concatenates, `+` adds** ("5" + 5 = 10; "5" . 5 = "55").
- `==` value only, `===` value **and** type → `"5" == 5` true, `"5" === 5` false.
- **Falsy list:** `0`, `"0"`, `""`, `null`, `[]`, `false`.
- `gettype()` → type name string (`float` shows as **"double"**); `var_dump()` → type + value.
- `(string)true` = `"1"`, `(string)false` = `""`.
- `die()` = alias of `exit()`; stops the script.
- Single quotes = literal, double quotes = interpolated; `"{$arr['key']}"` always works.

### E. 📐 Diagram pointers
- **PHP request–response cycle** — `module3.md` L57 (described) / L59–70 (labels). Reproduce as Browser → Web Server → PHP Engine, with MySQL below and "plain HTML back to browser" as the return path. This is the only figure in this chunk; it is also the answer diagram for "how PHP works".

### F. PHP-vs-C differences (C is the pre-requisite, so "compare with C" is a natural exam ask)
| | C | PHP |
|---|---|---|
| Variable declaration | `int age = 21;` type first | `$age = 21;` no type, `$` prefix |
| Types | static, fixed at compile time | dynamic, decided at runtime, juggled automatically |
| String join | `strcat`/`printf` | `.` operator |
| Output | `printf`, `puts` | `echo`, `print` (goes into the HTML response) |
| Booleans | `int` 0/1 (`stdbool.h` for `bool`) | real `bool` `true/false` |
| Array | fixed-size, same type, contiguous | dynamic, mixed types, ordered map |
| Errors | compile errors | runtime **warnings** that don't stop the script |
