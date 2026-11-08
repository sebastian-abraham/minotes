# MODULE 3 — Introduction to PHP · Complete Study Kit
> 20CST461 Web Technologies · ESE Part A = 3 marks, Part B = 14 marks · 2 Part-A questions and 1 of 2 Part-B questions come from this module

## 0. How to use this kit

1. Read **Part 1 (Section 2)** once, slowly — it is the only read-through; every jargon word is decoded there.
2. **Part 2 (Section 3)** is what you actually write in the exam — memorise the *shape*, not the prose.
3. **Part 3 (Section 4)** is hand-writing drill practice — do these with the notes closed, on paper.
4. **Section 5** is the night-before list: syntax only, no explanation.
5. Line refs like `3:L113` point at `module3.md` line 113 — go read that slide if a claim looks thin.

---

## 1. Module map + question coverage

| Q# | what it asks (max 8 words) | mark shape | answered at § |
|---|---|---|---|
| 68 | data types + one example each | 3 | §3.1.A |
| 69 | sum of two numbers program | 3 | §3.1.F |
| 70 | variables: declare and initialise | 3 | §3.1.B |
| 71 | flow control functions + pos/neg/zero | 3 | §3.1.I |
| 72 | if-else vs switch | 3 | §3.1.J |
| 73 | functions + add() returning a value | 3 | §3.1.K |
| 74 | role of regex in string processing | 3 | §3.1.M |
| 75 | concatenate two strings, uppercase result | 3 | §3.1.N |
| 76 | short note on PHP variables | 3 | §3.1.B |
| 77 | short note on PHP data types | 3 | §3.1.A |
| 78 | types of operators with examples | 3 | §3.1.C |
| 79 | srand() vs rand() | 3 | §3.1.D |
| 80 | internal representation of PHP arrays | 3 | §3.1.O |
| 81 | actions of next, reset, prev | 3 | §3.1.P |
| 82 | sorting of arrays with examples | 3 | §3.1.Q |
| 83 | form handling in PHP | 3 | §3.1.R |
| 84 | cookies and session tracking | 3 | §3.1.S |
| 85 | type conversion in PHP | 3 | §3.1.E |
| 86 | building blocks script with addition function | 3 | §3.1.G |
| 87 | sum and difference via a function | 3 | §3.1.H |
| 88 | data types explained, simple example each | 3 | §3.1.A |
| 89 | explode() vs implode() | 3 | §3.1.T |
| 90 | functions + factorial script | 3 | §3.1.L |
| 91 | prime-check program | 3 | §3.1.U |
| 203 | building blocks + rectangle area script | 14 | §3.2.203 |
| 204 | switch day-of-week + expressions | 14 | §3.2.204 |
| 205 | type casting/juggling + operators | 14 | §3.2.205 |
| 206 | functions + default parameters | 14 | §3.2.206 |
| 207 | control statements + arrays | 14 | §3.2.207 |
| 208 | registration system with regex validation | 14 | §3.2.208 |
| 209 | arrays: creation, functions, access, sorting | 14 | §3.2.209 |
| 210 | unique strings; average and median | 14 | §3.2.210 |
| 211 | pass-by-value vs pass-by-reference partition | 14 | §3.2.211 |
| 212 | most frequent word from a file | 14 | §3.2.212 |
| 213 | array creation ways + explode/implode + Armstrong | 14 | §3.2.213 |
| 214 | functions + flow control functions | 14 | §3.2.214 |
| 215 | cookies + five MySQL CRUD operations | 14 | §3.2.215 |
| 216 | 5-field form into MySQL + dynamic typing | 14 | §3.2.216 |
| 217 | control statements + palindrome | 14 | §3.2.217 |
| 218 | associative arrays + sort student marks | 14 | §3.2.218 |
| 219 | string handling functions + count vowels | 14 | §3.2.219 |
| 220 | six string functions + GET sum/diff/product | 14 | §3.2.220 |
| 221 | functions + dynamic typing + explode/implode | 14 | §3.2.221 |

**The 43 questions collapse into six master themes.** (1) **Data types & variables** — Q68, 70, 76, 77, 85, 88, 203a, 205a, 216b, 221b: what a type is, how PHP decides it at runtime, how to convert it. (2) **Operators & expressions** — Q78, 79, 85, 86, 87, 204b, 205b: arithmetic, assignment, `.`, `==` vs `===`, and what an expression evaluates to. (3) **Functions** — Q73, 86, 87, 90, 206, 210, 211, 212, 214a, 221a: declare, call, return, defaults, scope, `&`, variadics. (4) **Arrays** — Q80, 81, 82, 89, 207b, 209, 210, 211, 213a, 213b, 218: creation, internal representation, traversal, sorting, explode/implode. (5) **Strings & regex** — Q74, 75, 89, 208, 219, 220: the string function table, PCRE, the five validation patterns. (6) **Form handling & business logic** — Q83, 84, 208, 215, 216a, 220b: `$_GET`/`$_POST`, `isset`/`empty`, sanitising, then the application rule. Every 14-mark program is just themes 3+4+5+6 welded together with an `if` and a loop.

---

## 2. PART 1 — Deep dive, from zero

### 2.1 What PHP is, and how one page actually reaches the browser
**Story:** a restaurant. You (the browser) order from a menu; you never walk into the kitchen, and you never see the recipe — only the plated dish.

**Definition.** PHP (recursive acronym: *PHP: Hypertext Preprocessor*) is a **server-side** scripting language. The `.php` file sits on the web server. When a request arrives, the **PHP engine** executes the code inside it and produces plain HTML, which is what gets sent. The visitor never receives the source (`3:L30–31`, `3:L72`). The deck's own slide says PHP "runs entirely on the web server, before anything reaches the browser" (`3:L27–31`). Because the script runs fresh on **every** request, the same file can output different HTML each time — that is what "dynamic" means here (`3:L42–43`).

**The request–response cycle, five boxes** (`3:L55–72`, diagram at `3:L57`):

```
Browser → "give me page.php"
   ↓
Web Server (Apache/Nginx)  — sees .php, hands it to the engine
   ↓
PHP Engine — runs the script top to bottom
   ↓  (only if the script asks)  →  MySQL database
   ↓
Plain HTML travels back → Browser renders it
```

**Code — the smallest possible proof** (`3:L94–102`):

```php
<?php
$college = "Saintgits";
echo "Welcome to $college";
?>
```

View-source in the browser shows `Welcome to Saintgits` and **no PHP at all**.

**Why it exists / what breaks without it.** HTML alone is a fixed document — the same bytes for every visitor. Without a server-side language there is no way to personalise, to read a form, or to query a database. PHP exists to generate HTML *per request*; remove the engine and every `.php` file becomes a text file the browser downloads.

---

### 2.2 The syntax rules — five rules that govern every line
**Story:** PHP is C wearing a dollar-sign costume. If you can write C, you already know 80% of the punctuation.

**Definition.** (`3:L84–92`)

| Rule | Meaning |
|---|---|
| `<?php ... ?>` | The **tags** delimit PHP code. Anything outside them is passed through as literal HTML. |
| `$name` | Every **variable** starts with `$`. No type keyword (`int`, `String`) is written at declaration. |
| `;` | Every **statement** ends with a semicolon — same as C/Java. |
| `//` `#` `/* */` | Three comment styles; `#` is the PHP-only one (standard, not in your deck). |
| case | Keywords (`if`, `echo`, `function`) are **case-insensitive**; variable names are **case-sensitive** (standard, not in your deck). |

```php
<?php
// this is a single-line comment
# also a comment (PHP only)
/* multi-line
   comment */
$name = "Anu";   // semicolon ends the statement
echo $name;
?>
```

**Why it exists / what breaks without it.** The tags are what let one file be *both* HTML and a program — the server only executes the enclosed islands. Drop a `;` and you get the single most common PHP parse error (`syntax error, unexpected ...`); mistype `$Name` for `$name` and you silently get an *undefined variable* instead of the value, because case matters.

---

### 2.3 Output: `echo`, `print`, `<?=`
**Story:** three doors out of the engine into the HTML, one wider than the others.

**Definition.** `echo` and `print` write text into the response (`3:L91`). `echo` is a *language construct* that accepts a comma-separated list and returns nothing; `print` is an expression that returns `1`, so it can be used inside a larger expression. `<?= $x ?>` is shorthand for `<?php echo $x; ?>` (standard, not in your deck — the deck itself uses only `echo`/`print`).

```php
<?php
echo "Hello", " ", "World";   // echo takes a list
print "Hello";                 // print takes one value, returns 1
?>
<p><?= $name ?></p>            <!-- short echo tag -->
```

**Why it exists / what breaks without it.** There is no `document.write`, no template engine — output *is* the program's only channel to the browser. `echo` exists in the list form because it is the hottest operation in a PHP page; the short tag exists so HTML templates are not littered with `<?php echo`.

---

### 2.4 Variables and their naming rules
**Story:** a labelled box. The label is the name, the contents are the value — and the box can be re-filled with a different *kind* of thing at any time.

**Definition.** A variable is a named slot in memory holding one value. In PHP the name always begins with `$`, then a letter or underscore, then letters/digits/underscores; it may **not** start with a digit (`3:L88–90`). No type is declared — `$x = 5;` then `$x = "five";` is legal, because PHP is **dynamically typed**: the type belongs to the *value*, not to the variable (`3:L90`).

```php
<?php
$name = "Anu";        // string
$age  = 21;           // int
$fee  = 49999.50;     // float
$ok   = true;         // bool
$age  = "twenty-one"; // legal: the box now holds a string
echo $age;
?>
```

**Why it exists / what breaks without it.** Dynamic typing removes boilerplate and lets a value come straight out of `$_POST` (always a string) and be used as a number. The cost: nothing stops you from storing the wrong kind, so bugs surface at *runtime*, not at compile time — which is exactly why `gettype()`/`var_dump()` exist (`3:L124`).

---

### 2.5 The data types — all eight
**Story:** eight kinds of luggage the box can hold; the label on the box never changes but the luggage does.

**Definition.** The deck's table names six (`3:L113–122`); PHP actually has **eight** primitive-ish types in three families:

| # | Type | Family | Example | Note |
|---|---|---|---|---|
| 1 | `int` | scalar | `$age = 21;` | whole numbers |
| 2 | `float` (a.k.a. double) | scalar | `$fee = 499.50;` | decimal numbers |
| 3 | `string` | scalar | `$name = "Anu";` | single or double quotes |
| 4 | `bool` | scalar | `$active = true;` | `true` / `false` |
| 5 | `array` | compound | `$m = [88, 92];` | ordered list **or** key→value map |
| 6 | `object` | compound | `$s = new Student("Rahul");` | instance of a class (`3:L471–495`) |
| 7 | `NULL` | special | `$x = null;` | explicitly "no value" |
| 8 | `resource` | special | `$f = fopen("a.txt","r");` | handle to an external thing — a file, a DB connection (standard, not in your deck) |

```php
<?php
$a = 21;            // int
$b = 499.50;        // float
$c = "Anu";         // string
$d = true;          // bool
$e = [88, 92];      // array
$f = null;          // NULL
echo gettype($a);   // "integer"
var_dump($b);       // float(499.5)
?>
```

**Why it exists / what breaks without it.** Every operator's behaviour depends on the operand's type: `+` adds numbers, `.` joins strings, `==` converts before comparing. Without a type system you cannot predict any output — which is why every output-prediction question in this module is really a type question.

---

### 2.6 Inspecting a value: `gettype()` and `var_dump()`
**Story:** an X-ray for a variable — `echo` shows you the shadow, `var_dump` shows you the bone.

**Definition.** `gettype($v)` returns the type name as a **string**; `var_dump($v)` prints the **type and the value** (and, for arrays/objects, the whole structure, recursively) (`3:L124`). `print_r()` is the friendlier array version (standard, not in your deck).

```php
<?php
$x = "10";
echo gettype($x);    // string
var_dump($x);        // string(2) "10"
var_dump((int)$x);   // int(10)
?>
```

**Why it exists / what breaks without it.** With loose typing, `echo` hides the difference between the string `"10"` and the int `10` — both print `10`. When a comparison misbehaves, `var_dump` is the only way to see which type you actually have.

---

### 2.7 Type juggling and explicit casting
**Story:** a bilingual shopkeeper who silently converts your rupees to dollars, unless you say "no, convert it *this* way".

**Definition.** **Type juggling** = PHP converts types automatically when a context demands it (`"10" + 5` → `15`). **Type casting** = you force the conversion with a cast operator `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` (`3:L140`), or with the functions `intval()`, `floatval()`, `strval()`, `boolval()` (`3:L141`), or `settype($var, "integer")` which converts **in place** (`3:L142`). Type-checking functions `is_int()`, `is_string()`, `is_array()` answer "is it this type?" (`3:L143`).

```php
<?php
$a = "10";
$b = (int)$a + 5;              // 15  — cast then add
$price = "499.99";
$total = floatval($price) * 2; // 999.98
settype($a, "integer");        // $a is now int(10)
echo is_string($a) ? "yes" : "no"; // no
?>
```

**Why it exists / what breaks without it.** Form data arrives as **strings, always** — `"25"` not `25`. Juggling makes `"25" * 2` work; casting makes it *predictable*. Without the explicit cast, `"5 apples" + 2` silently becomes `7` while `"apples" + 2` throws a `TypeError` in PHP 8 — the same source shape, two different outcomes.

---

### 2.8 Operators I — arithmetic and assignment
**Story:** the calculator keys, plus a shorthand that says "and put the answer back in the same box".

**Definition.** (`3:L170–171`)

| Arithmetic | Meaning | Assignment | Meaning |
|---|---|---|---|
| `+` `-` `*` `/` | as in C | `=` | assign |
| `%` | modulus (remainder) | `+=` `-=` `*=` `/=` | op then assign |
| `**` | exponent | `.=` | concatenate then assign |

```php
<?php
$a = 10; $b = 3;
echo $a % $b;   // 1
echo $a ** 2;   // 100
$msg = "Total: ";
$msg .= (5 + 3);
echo $msg;      // "Total: 8"
?>
```

**Why it exists / what breaks without it.** `/` always produces a float in PHP (`10/4` → `2.5`), unlike C's integer division — a classic output-prediction trap. `%` only works on integers; feed it a float and PHP casts it down first.

---

### 2.9 Operators II — the dot, and why it is not `+`
**Story:** `+` is glue for numbers only; strings are joined with a full stop because the plus sign was already taken.

**Definition.** `.` concatenates two strings; `.=` appends (`3:L172`, recap at `3:L770`). Java uses `+`, JavaScript uses `+`, PHP uses `.` — this is the single most common syntax slip for a C/Java student.

```php
<?php
$first = "Web";
$last  = "Programming";
echo $first . " " . $last;   // Web Programming
$first .= " Tech";           // "Web Tech"
?>
```

**Why it exists / what breaks without it.** If `+` concatenated, `"5" + 5` would be ambiguous — PHP resolves it as *addition* (`10`), so the designer needed a different glyph for joining. Write `"a" + "b"` and PHP 8 throws `TypeError: Unsupported operand types: string + string`.

---

### 2.10 Operators III — `==` vs `===` (the deck's own flagged quirk)
**Story:** `==` asks "do these *look* the same after translation?"; `===` asks "are these the *same thing*?".

**Definition.** `==` is **loose** equality: it converts types first, then compares values. `===` is **strict**: value **and** type must match, no conversion. Similarly `!=` vs `!==` (`3:L201–203`). The deck calls this "one of PHP's most exam-relevant quirks" (`3:L199`) and repeats it in the recap (`3:L760`).

```php
<?php
var_dump("5" == 5);    // true   — "5" converted to 5
var_dump("5" === 5);   // false  — string vs int
var_dump(0 == "abc");  // false  (PHP 8+)
var_dump(null == false); // true (standard, not in your deck)
var_dump(0 == "");     // true  in PHP 7, false in PHP 8 (standard)
?>
```

**Why it exists / what breaks without it.** Loose `==` is convenient with string-typed form input. It is also dangerous: before PHP 8, `0 == "abc"` was `true`, so `if ($role == 0)` could be satisfied by garbage. `===` exists to make "the user typed the string `0`" distinguishable from "the value is the integer 0" — including the case `"0" == false` → `true`, which lets an empty-looking PIN pass an emptiness check.

---

### 2.11 Operators IV — relational, logical, increment, ternary
**Story:** the bouncer at the door: several conditions, combined with AND/OR, deciding one outcome.

**Definition.** (`3:L203–204`) Relational: `<` `>` `<=` `>=` `!=` `!==`. Logical: `&&` (and), `||` (or), `!` (not) — plus the low-precedence word forms `and`, `or`, `xor` (standard, not in your deck). Increment/decrement: `++$i` (pre: increment then use), `$i++` (post: use then increment), `--` likewise (standard — the deck uses `$i++` at `3:L307` without naming it). Ternary: `cond ? a : b`.

```php
<?php
$age = 20; $hasID = true;
if ($age >= 18 && $hasID) { echo "Entry allowed"; }

$i = 5;
echo $i++;   // 5  (then $i becomes 6)
echo ++$i;   // 7  (increment, then print)

$grade = ($marks ?? 0) >= 50 ? "Pass" : "Fail";
?>
```

**Why it exists / what breaks without it.** `&&` short-circuits: if the left side is false, the right side is **never evaluated** — that is what makes `isset($a) && $a > 0` safe. Swap to `&` (bitwise) and both sides always run, so the guard stops guarding.

---

### 2.12 Expressions
**Story:** any phrase in the language that can be *answered* with a value — "2+2" is a phrase; "2+" is not.

**Definition.** An **expression** is anything that produces a value: a literal (`5`), a variable (`$x`), an operator applied to expressions (`$a + $b`), a function call (`calcTotal(499,3)`), an assignment (`$x = 5` — itself evaluates to 5), or a ternary. Statements are expressions plus a `;` plus an effect (`3:L173`). The deck's business-logic slide leans on this: `$marks = (int) ($_POST["marks"] ?? 0);` is a chain of expressions (`3:L695`).

```php
<?php
$x = 5;              // assignment expression, value 5
$y = ($x + 3) * 2;   // 16
$z = $x > 3;         // true  — a comparison IS an expression
echo $y + $z;        // 17  — true juggles to 1
?>
```

**Why it exists / what breaks without it.** Because comparisons are expressions, they can be nested inside other expressions — that is the whole basis of `if (...)`, of `?:`, and of `return $a > $b;`. Understand "everything has a value" and precedence questions become mechanical; miss it and `echo $y + $z;` printing `17` looks like magic.

**Precedence, the short version** (standard, not in your deck — the deck has no precedence table): `**` → `++/--` → `!` → `* / %` → `+ -` → `.` → `< <= > >=` → `== != === !==` → `&&` → `||` → `?:` → `=` → `and` → `or`. The only one that bites in exams: **`.` has the same precedence as `+ -`**, so `"Total: " . 5 + 3` evaluates as `("Total: " . 5) + 3` → a numeric-string plus int → `8`-ish nonsense. Always parenthesise: `"Total: " . (5 + 3)`.

---

### 2.13 Flow control functions — `exit()`, `die()`, `return`
**Story:** three ways to leave a room — `exit`/`die` burn the building down, `return` just closes the door behind you.

**Definition.** (`3:L227–243`)

1. **`exit()`** stops the script **immediately**; anything after it never runs. It can take a string (printed before dying) or an int status code.
2. **`die()`** is an exact **alias** of `exit()` — identical behaviour, shorter to type. Used after a fatal error: `die("Connection failed");` (`3:L235`).
3. **`return`** — inside a function it sends a value back **and** stops that function (`3:L239`); at file scope it ends the included file (standard).
4. The group matters together because all three decide *whether execution continues, branches, or stops* (`3:L243`).

```php
<?php
function checkAge($age) {
    if ($age < 0) { return "Invalid age"; }  // stops here, returns
    return "OK";
}
echo checkAge(-5);

if (!file_exists("data.txt")) {
    die("Data file missing");   // script ends, message printed
}
echo "never reached if file missing";
?>
```

**Why it exists / what breaks without it.** In a form script, once validation fails there is no point running the business logic or the INSERT. `exit`/`die` make "stop right now" a one-liner instead of wrapping the whole page in `else` blocks. Confusing `return` with `die` is a real bug: `return` inside a *function* only leaves the function, and a function that returns a string still lets the rest of the page run.

---

### 2.14 Control statements — `if`/`elseif`/`else`, `switch`, and the ternary
**Story:** a railway switchyard. `if` picks a track by *condition*; `switch` picks a track by *label*.

**Definition.** (`3:L255–278`) `if (cond) {...} elseif (cond) {...} else {...}` branches on any boolean expression. `switch ($var) { case v: ...; break; default: ...; }` compares one variable against a list of **fixed values** with loose `==`. `break` prevents **fall-through** (running the next case's code too); `default` catches everything unmatched (`3:L261–262`). `match` (PHP 8+) is a stricter, value-returning cousin — `$g = match(true) { $m>=90 => "A", default => "C" };` (standard, not in your deck).

```php
<?php
function grade($m) {
    if ($m >= 90) return "A";
    elseif ($m >= 75) return "B";
    else return "C";
}

switch (date("N")) {          // 1=Mon ... 7=Sun
    case 6:
    case 7: echo "Weekend"; break;   // deliberate fall-through
    default: echo "Weekday";
}
?>
```

**Why it exists / what breaks without it.** A chain of `elseif` re-evaluates a whole condition each time; `switch` evaluates the subject **once** and jumps to a label — that is its performance and readability argument, and it is the answer to Q72. Forget `break` and Monday's code runs inside Tuesday's case, the classic fall-through bug.

---

### 2.15 Loops — `for`, `while`, `do...while`, `foreach`
**Story:** four ways to walk a corridor: count the doors (`for`), walk until a sign says stop (`while`), open the first door before looking at the sign (`do...while`), or let a guide hand you each item (`foreach`).

**Definition.** (`3:L291–298`)

| Loop | Shape | When |
|---|---|---|
| `for (init; cond; step)` | known count | 1..n |
| `while (cond)` | test **before** | may run **zero** times |
| `do {...} while (cond)` | test **after** | always runs **at least once** |
| `foreach ($arr as $v)` / `as $k => $v` | array walker | the idiomatic array loop (`3:L298`, `3:L762`) |

```php
<?php
$marks = [88, 95, 60];
foreach ($marks as $m) { echo grade($m); }

for ($i = 1; $i <= 3; $i++) { echo $i; }

$n = 0;
while ($n < 3) { echo $n; $n++; }

$k = 10;
do { echo "once"; } while ($k < 5);   // prints once
?>
```

**Why it exists / what breaks without it.** `foreach` exists because a PHP array is an ordered map, not a C array — a `for ($i=0; $i<count(...); $i++)` loop *breaks* on associative arrays with string keys. `do...while` exists because some bodies must run before there is anything to test (read a line, then check for EOF).

---

### 2.16 Functions — declare, call, return
**Story:** a vending machine: you press a button, push in arguments, and a value comes out; you do not need to know the wiring inside.

**Definition.** `function name($param, ...) { ... return $value; }` (`3:L328`). Key facts for the exam:

- Declarations are **hoisted** — you may call a function defined *below* the call (`3:L329`).
- `return` sends a value back and exits the function (`3:L330`).
- A function with **no** `return` implicitly returns `NULL` (`3:L331`).
- A function may `echo` instead of returning — then its "value" is `NULL` and the output appears at the point of call (`3:L340–343`).

```php
<?php
function calcTotal($price, $qty) {
    return $price * $qty;
}
echo calcTotal(499, 3);   // 1497

function greet($name) {
    echo "Hello, $name!";
}
greet("Saintgits");       // prints, returns NULL
?>
```

**Why it exists / what breaks without it.** Without functions, the same validation block is copy-pasted into ten pages and a bug must be fixed ten times. Hoisting means file order never matters for definitions — but it also means a typo in the *definition* only explodes when the call runs.

---

### 2.17 Default parameter values, scope, `global`
**Story:** a form with pre-filled fields — if you leave a box empty, the printed default is used. And the function's room has one door: `global`.

**Definition.** (`3:L358–366`)

1. **Default parameter**: `function greet($name = "Guest")` — if the caller omits the argument, the default is used (`3:L362`). Defaults must come **after** required parameters (standard).
2. **Scope**: a variable created inside a function is **local** — it does not exist outside, and an outside variable does not exist inside (`3:L366`).
3. **`global $x;`** inside a function binds that name to the outer variable, so the function can read/write it (`3:L366`).
4. **`static $x = 0;`** keeps a local variable alive **between calls** — it is initialised once (standard, not in your deck).

```php
<?php
function greet($name = "Guest") { return "Hello, $name"; }
echo greet();          // Hello, Guest
echo greet("Anu");     // Hello, Anu

$count = 10;
function show() {
    global $count;     // without this line: undefined variable
    echo $count;
}
function counter() {
    static $n = 0;     // survives between calls
    $n++;
    return $n;
}
echo counter(); echo counter();   // 1 then 2
?>
```

**Why it exists / what breaks without it.** PHP has no "global by default" — that is deliberate: a function that can silently read any outside variable is untestable. `global` is the escape hatch, and `static` exists because a plain local is destroyed on every return, so an accumulator would reset to 0 each call.

---

### 2.18 Pass by value vs pass by reference (`&`), and variadics
**Story:** by value you hand over a **photocopy** of the document; by reference you hand over the **original**, so your scribbles land on it.

**Definition.** Arguments are passed **by value** — the function gets a copy, and modifying the copy leaves the caller's variable untouched. Prefixing the parameter with `&` passes **by reference**: the parameter is an alias for the caller's variable, so assignments inside the function change the original (`3:L370`). **Variadic** `function total(...$nums)` collects any number of arguments into an array named `$nums` (`3:L374`).

```php
<?php
function addTen($x)  { $x = $x + 10; }   // by value: copy
function addTenR(&$x) { $x = $x + 10; }  // by reference: original

$a = 5;  addTen($a);  echo $a;   // 5   — unchanged
$b = 5;  addTenR($b); echo $b;   // 15  — changed

function total(...$nums) {
    return array_sum($nums);
}
echo total(1, 2, 3, 4);   // 10
?>
```

**Why it exists / what breaks without it.** Value semantics make functions predictable and side-effect free — the default is the safe default. Reference semantics exist for exactly one exam-famous shape: a function that must return **more than one** result (Q211's "partition into positives and negatives" writes into two output arrays). Variadics exist because `total()` should not care whether it got 3 numbers or 300.

---

### 2.19 Indexed arrays
**Story:** a numbered row of lockers — 0, 1, 2 — and you open one by its number.

**Definition.** An indexed array is an **ordered list** whose keys are integers assigned automatically from 0 (`3:L388`). Two syntaxes: short `[10, 20, 30]` and long `array(10, 20, 30)` (`3:L390`). Access `$arr[0]`; append with `$arr[] = 40;` (empty brackets = "next free index"); `count($arr)` gives the length (`3:L391–393`).

```php
<?php
$marks = [88, 92, 79];
$marks[] = 95;            // append → index 3
echo $marks[0];           // 88
echo count($marks);       // 4

foreach ($marks as $i => $m) {
    echo "Index $i: $m\n";
}
?>
```

**Why it exists / what breaks without it.** C arrays are fixed-size and contiguous; PHP arrays are dynamic and can grow with `[]`. Without `$arr[] = ...` you would have to track the next index by hand — and `count()` is the only safe loop bound, since the array changes size as you append.

---

### 2.20 Associative and multidimensional arrays
**Story:** a labelled drawer set instead of numbered lockers — you ask for "marks", not "drawer 2". Stack the drawer sets and you have a filing cabinet.

**Definition.** An associative array uses **named keys**: `["name" => "Anu", "marks" => 88]`, read with `$stu["name"]` (`3:L423–424`). `=>` separates key from value (`=` alone is assignment and will not work). A **multidimensional** array is an array whose elements are arrays — e.g. a list of student records (`3:L425`). `foreach ... as $k => $v` exposes both (`3:L426`).

```php
<?php
$stu = ["name" => "Anu", "marks" => 88];
echo $stu["name"];        // Anu

$students = [
    ["name" => "Anu",   "marks" => 88],
    ["name" => "Rahul", "marks" => 72]
];
foreach ($students as $s) {
    echo $s["name"] . " " . $s["marks"] . "\n";
}
echo $students[1]["marks"];   // 72
?>
```

**Why it exists / what breaks without it.** A record has no natural numeric index — `$row[0]`/`$row[1]`/`$row[2]` is unreadable and breaks the moment a column is added. Named keys make code self-documenting, and they are exactly what `mysqli_fetch_assoc()` returns in Module 4, which is why the module insists on `=>`.

---

### 2.21 Array functions — the table, the sort family, and the internal pointer
**Story:** a Swiss-army knife for the locker row: count them, push one in, pop one out, sort them, or walk a cursor along them.

**Definition.** The deck's table (`3:L452–459`):

| Function | Purpose |
|---|---|
| `count($arr)` | number of elements |
| `array_push($arr, $val)` | add to the end — same as `$arr[] = $val` |
| `sort($arr)` / `rsort($arr)` | sort ascending / descending, **re-indexing keys** |
| `array_map($fn, $arr)` | apply a function to every element → new array |
| `array_filter($fn, $arr)` | keep only elements passing a test |
| `in_array($val, $arr)` | does the value exist? |

Beyond the table (standard, not in your deck — needed for Q82 and Q218): `asort()` sorts by **value** keeping keys, `arsort()` the reverse, `ksort()`/`krsort()` sort by **key**, `usort()` sorts by a **callback**. The **internal pointer** functions: `reset()` → first element, `end()` → last, `next()` → move forward and return, `prev()` → move back and return, `current()` → value at the pointer, `key()` → key at the pointer; they return `false` when they run off the end.

```php
<?php
$n = [3, 1, 2];
sort($n);                 // [1, 2, 3]  — keys renumbered 0,1,2
$m = ["Anu" => 88, "Rahul" => 72];
asort($m);                // by value, keys kept: Rahul=>72, Anu=>88
ksort($m);                // by key: Anu, Rahul

$p = [10, 20, 30];
echo current($p);         // 10
next($p);  echo current($p);  // 20
end($p);   echo current($p);  // 30
prev($p);  echo current($p);  // 20
reset($p); echo current($p);  // 10
?>
```

**Why it exists / what breaks without it.** `sort()` **destroys the key→value relationship** (it renumbers), which is why `asort()`/`ksort()` exist — sorting a marks array with `sort()` loses who got what. The pointer functions exist because arrays are ordered maps with an internal cursor; `foreach` hides the cursor, but `next`/`prev` let you walk manually.

---

### 2.22 Objects and classes
**Story:** a class is the cookie cutter; an object is a cookie. Each cookie can be decorated differently.

**Definition.** `class Name { ... }` defines a blueprint with **properties** (data) and **methods** (functions) (`3:L475`). `new ClassName()` creates an **instance** (`3:L476`). `->` accesses properties and methods — **not** `.` (`3:L477`, recap `3:L766`). `__construct()` runs automatically on creation (`3:L478`); `$this` is the current object inside a method (standard, implied by `3:L486`).

```php
<?php
class Student {
    public $name;
    public function __construct($n) {
        $this->name = $n;
    }
    public function greet() {
        return "Hi, " . $this->name;
    }
}

$s = new Student("Rahul");
echo $s->greet();     // Hi, Rahul
?>
```

**Why it exists / what breaks without it.** An array of student records has no behaviour — every operation becomes a loose function that must be told which array to touch. A class binds data and the operations that are valid on it, so `$s->greet()` cannot be called on the wrong data shape. `.` would be a string-concatenation operator here, so `->` is not cosmetic: `$s.name` is a syntax error.

---

### 2.23 Strings and the string-function table
**Story:** PHP ships a whole workshop for text — measure it, shout it, trim it, slice it.

**Definition.** A string is a sequence of characters in single or double quotes (`3:L119`). **Double quotes interpolate** `$variables` and interpret `\n`, `\t`; **single quotes are literal** (standard, not in your deck — but it changes the output of nearly every program). The deck's four (`3:L512–515`) plus the ones exam questions use (`3:L542–545`):

| Function | Does | Example → result |
|---|---|---|
| `strlen($s)` | length in bytes | `strlen("Saintgits")` → 9 |
| `strtoupper($s)` / `strtolower($s)` | change case | `"SAINTGITS"` / `"saintgits"` |
| `trim($s)` | strip whitespace both ends | `"  Anu  "` → `"Anu"` |
| `substr($s, start, len)` | slice | `substr("Saintgits",0,5)` → `"Saint"` |
| `str_replace($a,$b,$s)` | find & replace | `"World"`→`"PHP"` |
| `explode($delim,$s)` | string → array | `"HTML,CSS,JS"` → 3-element array |
| `implode($glue,$arr)` | array → string | `["HTML","CSS","JS"]` → `"HTML + CSS + JS"` |
| `strrev($s)` | reverse (standard) | `"madam"` → `"madam"` |
| `strpos($s,$needle)` | first position or `false` (standard) | `strpos("Saintgits","g")` → 5 |
| `ucfirst($s)` / `ucwords($s)` | capitalise (standard) | `"anu"` → `"Anu"` |
| `sprintf($fmt, ...)` | formatted build (standard) | `sprintf("%.2f", 499.5)` → `"499.50"` |
| `str_word_count($s)` | count words (standard) | `"a b c"` → 3 |

```php
<?php
$name = "  Saintgits  ";
$clean = trim($name);
echo strlen($clean);          // 9
echo strtoupper($clean);      // SAINTGITS
echo substr($clean, 0, 5);    // Saint

$parts  = explode(",", "HTML,CSS,JS");
$joined = implode(" + ", $parts);
echo $joined;                 // HTML + CSS + JS
?>
```

**Why it exists / what breaks without it.** Text is the only thing a web app ever receives from a user, and it always arrives dirty — padded with spaces, wrong case, comma-separated. Without `trim`/`explode`/`str_replace` every one of those normalisations would be a hand-written loop over characters.

---

### 2.24 Regular expressions — `preg_match`, `preg_replace`, `preg_split`
**Story:** a metal detector at the door. It does not care *what* you are carrying, only whether the shape matches the pattern.

**Definition.** PHP supports **PCRE** (Perl-Compatible Regular Expressions) (`3:L570`). `preg_match($pattern, $string)` returns `1` if the pattern is found, `0` if not, `false` on error (`3:L572`); it is a *test*, not an extractor. `preg_replace($pattern, $replacement, $string)` does regex find-and-replace (`3:L573`). `preg_split($pattern, $string)` splits on a regex delimiter (`3:L574`). Patterns are wrapped in **delimiters**, usually `/.../` (`3:L575`).

```php
<?php
$email = "user@saintgits.org";
if (preg_match("/^[\w.-]+@[\w.-]+\.[\w]+$/", $email)) {
    echo "Valid email";
}

$clean = preg_replace("/[0-9]/", "", "Room12A");
echo $clean;    // RoomA

$bits = preg_split("/[,;]/", "a,b;c");
print_r($bits); // [a, b, c]
?>
```

**Why it exists / what breaks without it.** `strpos`-style checks cannot express "exactly 10 digits, nothing else". Regex can, in one line, and it is the only practical way to validate an email/phone/PIN before it reaches a database. Without anchors (`^`, `$`) the check degrades into "contains", which is why `preg_match("/[0-9]{10}/", "1234567890123")` wrongly passes.

---

### 2.25 The five validation patterns (memorise verbatim)
**Story:** five pre-cut stencils — hold the stencil over the input; if it does not fit the hole, reject it.

**Definition.** (`3:L599–605`)

| Pattern | Matches | Used for |
|---|---|---|
| `/^[0-9]{10}$/` | exactly 10 digits | phone number |
| `/^[\w.-]+@[\w.-]+\.[\w]+$/` | basic email shape | email |
| `/^[A-Za-z]+$/` | letters only | name field |
| `/^\d{6}$/` | exactly 6 digits | PIN code |
| `/^[A-Za-z0-9]+$/` | letters and digits only | username |

Metacharacter glossary (`3:L607`): `\d` digit, `\w` word character (letter/digit/underscore), `{n}` exactly n times, `^` start anchor, `$` end anchor; plus `+` one-or-more, `*` zero-or-more, `?` optional, `[abc]` character class, `.` any character, `\.` a literal dot (standard).

```php
<?php
var_dump(preg_match("/^[0-9]{10}$/", "9876543210")); // 1
var_dump(preg_match("/^[0-9]{10}$/", "98765"));      // 0
var_dump(preg_match("/^\d{6}$/", "682001"));         // 1
var_dump(preg_match("/^[A-Za-z]+$/", "Anu K"));      // 0 — space not allowed
?>
```

**Why it exists / what breaks without it.** Without `^...$` the pattern matches a *substring*, so `"abc9876543210xyz"` would validate as a phone number. The anchors are the difference between "contains a valid-looking thing" and "is exactly a valid thing" — and that distinction is worth marks in Q208.

---

### 2.26 Form processing — `$_GET`, `$_POST`, `$_REQUEST`, `$_SERVER`
**Story:** two delivery methods for the same parcel. GET writes the contents on the outside of the envelope (in the URL); POST puts them inside (in the body).

**Definition.** PHP exposes submitted data through **superglobals** — arrays populated automatically for every request, available in every scope (`3:L621`).

| Superglobal | Carries | Notes |
|---|---|---|
| `$_GET["f"]` | query-string data (`method="GET"`) | visible in URL, bookmarkable, length-limited, never for passwords |
| `$_POST["f"]` | request-body data (`method="POST"`) | not in URL, no practical size limit |
| `$_REQUEST["f"]` | GET + POST + COOKIE merged | convenient but ambiguous — the deck says "less precise, usually avoid" (`3:L625`) |
| `$_SERVER["REQUEST_METHOD"]` | `"GET"` or `"POST"` | how a single script knows whether the form was submitted (`3:L630`) |
| `$_FILES`, `$_SESSION`, `$_COOKIE`, `$_ENV`, `$_SERVER` | the rest of the set | `$_SESSION`/`$_COOKIE` matter in M4 |

`isset($_POST["field"])` asks "was this key submitted at all?" (`3:L626`) — different from "is it empty?", which is `empty()`.

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["name"])) {
        $name = $_POST["name"];
        echo "Hello, $name!";
    }
}
?>
```

**Why it exists / what breaks without it.** HTTP is stateless: the server forgets you between requests. Superglobals are the mechanism that carries this request's data into the script. Without the `REQUEST_METHOD` guard, the same page would try to process fields on the *first*, empty visit and print warnings for every missing key.

---

### 2.27 Validating and sanitising input
**Story:** mailroom rules — check the parcel's shape at the counter (validate), then wipe the outside clean before handing it on (sanitise).

**Definition.** "Never trust data from a form" (`3:L652`). **Validation** asks *is this well-formed?* — `trim()`, `empty()`, `preg_match()`. **Sanitising** makes it *safe to use* — `htmlspecialchars()` converts `<`, `>`, `&`, `"` into entities so user text cannot inject HTML/JS when echoed back (`3:L655`).

```php
<?php
$name  = trim($_POST["name"]  ?? "");
$email = trim($_POST["email"] ?? "");

if (empty($name) || empty($email)) {
    die("All fields are required.");
}

$safeName = htmlspecialchars($name);
echo "Welcome, $safeName";
?>
```

**Why it exists / what breaks without it.** `empty()` treats `""`, `"0"`, `0`, `null`, `false`, `[]` as empty — so `empty("0")` is `true`, a genuine trap for a marks field. `??` (null coalescing) suppresses the "undefined array key" warning on first load. Skip `htmlspecialchars` and a name of `<script>alert(1)</script>` executes in the next visitor's browser (XSS).

---

### 2.28 Business logic
**Story:** validation is the bouncer checking your ID; business logic is the manager deciding whether your ticket tier gets you a seat.

**Definition.** Business logic is the **application-specific rule applied to already-validated data**, kept separate from validation (`3:L686`): validation asks *is this data well-formed?*; business logic asks *given well-formed data, what should the app DO?* (`3:L688–689`). Examples: eligibility, fee calculation, grade computation (`3:L691`). Keeping the two steps distinct makes code readable and testable (`3:L690`).

```php
<?php
$marks      = (int) ($_POST["marks"] ?? 0);
$attendance = (int) ($_POST["attendance"] ?? 0);

// Business rule: pass needs marks >= 50 AND attendance >= 75
if ($marks >= 50 && $attendance >= 75) {
    echo "Eligible to pass";
} else {
    echo "Not eligible - check marks/attendance";
}
?>
```

**Why it exists / what breaks without it.** If the pass rule is buried inside the "is the field numeric" check, then changing the pass mark means editing validation code — and the rule cannot be tested without a form. Separating them means the rule is one `if` you can point at.

---

### 2.29 The whole pipeline: a complete form-processing script
**Story:** an assembly line with five stations; every PHP page that accepts input is this line.

**Definition.** The deck's five steps (`3:L722–726`): (1) check the request method, (2) read & trim the fields, (3) validate (empty checks, regex), (4) apply business logic, (5) respond — with Module 4 replacing step 5 by a database write (`3:L726`).

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name  = trim($_POST["name"]  ?? "");
    $marks = (int) ($_POST["marks"] ?? 0);

    if (empty($name)) { die("Name required"); }

    $grade = $marks >= 50 ? "Pass" : "Fail";
    echo htmlspecialchars($name) . ": $grade";
}
?>
```

**Why it exists / what breaks without it.** Each station guards the next: without (1) the first load errors; without (2) `" 0"` bypasses checks; without (3) any string reaches the business rule; without (4) there is no decision at all; without (5) nothing appears. This shape is the skeleton for Q208, Q216 and half of Q220 — learn the five lines as a chant.

---

## 3. PART 2 — Answer bank (what to write in the exam)

> Mark arithmetic: a 3-mark answer = **3 or 4 numbered points, no preamble**. A 14-mark answer = **code + explanation + a labelled diagram/table if asked**. Do not write an introduction; the first line should already be a point.

### 3.1 3-mark answers (Part A)

#### A. Data types — **MASTER ANSWER** (answers Q68, Q77, Q88; also feeds Q203a)
1. **Definition.** A data type tells PHP what kind of value a variable holds and therefore which operations are legal on it. PHP is **dynamically typed** — the type belongs to the *value*, and is decided at runtime, not declared (`3:L90`).
2. **The types, each with its example.** `int` `$age = 21;` (whole numbers) · `float` `$fee = 499.50;` (decimals) · `string` `$name = "Anu";` (text in single or double quotes) · `bool` `$active = true;` (`true`/`false`) · `array` `$m = [88, 92];` (ordered list or key→value map) · `object` `$s = new Student("Rahul");` (instance of a class) · `NULL` `$x = null;` (explicitly "no value") · `resource` `$f = fopen("a.txt","r");` (handle to a file or DB connection — standard, not in the deck's six-row table at `3:L113–122`).
3. **Example program.**
```php
<?php
$age = 21; $fee = 499.50; $name = "Anu";
$ok = true; $m = [88, 92]; $x = null;
echo gettype($age);   // integer
var_dump($fee);       // float(499.5)
?>
```
4. **Inspection.** `gettype($v)` returns the type name as a string; `var_dump($v)` prints type **and** value — the two debugging tools the deck names (`3:L124`).

*Tweak for Q77 ("note on datatypes"): drop point 4, expand point 2 into the 8 bullet lines. Tweak for Q68 ("give an example for each"): keep the order exactly as above so the examiner ticks eight times.*

#### B. Variables — **MASTER ANSWER** (answers Q70, Q76)
1. **Definition.** A variable is a named memory slot holding a value. In PHP every variable name begins with `$`, followed by a letter or underscore, then letters/digits/underscores; it may not start with a digit (`3:L88–89`).
2. **No declaration, only assignment.** PHP has no `int x;` — a variable is created the moment you assign to it. `$name = "Anu";` both declares and initialises.
3. **Loosely/dynamically typed.** No type keyword is written; the type is whatever the current value is, and it may change on reassignment: `$x = 5; $x = "five";` is legal (`3:L90`, `3:L758`).
4. **Scope + case.** A variable created inside a function is local to it; `global $x;` reaches the outer one (`3:L366`). Names are case-sensitive: `$Name` and `$name` are two different variables.

```php
<?php
$college = "Saintgits";   // string
$year = 2026;             // int
$fee = 49999.50;          // float
echo "Welcome to $college, year $year";
?>
```

#### C. Types of operators (Q78)
1. **Arithmetic** — `+ - * / % **`; `**` is exponent, `/` always yields a float, `%` is integer remainder (`3:L170`).
2. **Assignment** — `=` plus the compound forms `+= -= *= /= .=`; `.=` concatenates and assigns (`3:L171`).
3. **String** — `.` joins two strings, `.=` appends; PHP does **not** use `+` for text (`3:L172`).
4. **Comparison and logical** — `== === != !== < > <= >=` (`==` converts types, `===` does not); `&& || !` combine conditions (`3:L201–204`). *(If a 4th slot is free, add increment `++/--` and the ternary `?:`.)*

```php
<?php
$a = 10; $b = 3;
echo $a % $b;              // 1
$s = "Total: "; $s .= 8;   // "Total: 8"
var_dump("5" === 5);       // false
?>
```

#### D. `srand()` vs `rand()` (Q79)
1. **`rand()`** returns a pseudo-random integer; `rand()` with no arguments gives a value between 0 and `getrandmax()`, and `rand($min, $max)` gives one inside an inclusive range (standard, not in your deck).
2. **`srand()`** *seeds* the generator — it does not return a random number at all; it sets the starting point of the sequence (`srand(seed)`).
3. **The relationship:** the same seed always reproduces the same sequence, so `srand()` is used for reproducible tests, and `srand(time())` (or `srand((int) microtime(true))`) is used to make each run different. Since PHP 4.2 `rand()` is seeded automatically, so `srand()` is only needed when you *want* a fixed sequence (standard).
4. **One-line example.**
```php
<?php
srand(42);              // fix the sequence
echo rand(1, 100);      // always the same number for seed 42
echo rand(1, 100);
?>
```

#### E. Type conversion (Q85; also answers Q205a)
1. **Implicit (juggling).** PHP converts automatically when the context demands it — `"10" + 5` is `15` because `+` needs numbers (`3:L138`).
2. **Explicit casts.** `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` — written in front of the value: `$b = (int)$a + 5;` (`3:L140`).
3. **Functions.** `intval()`, `floatval()`, `strval()`, `boolval()` return the converted value; `settype($var, "integer")` converts the variable **in place** (`3:L141–142`).
4. **Type checks.** `is_int()`, `is_string()`, `is_array()` test without converting (`3:L143`).
```php
<?php
$a = "10";
echo (int)$a + 5;            // 15
echo floatval("499.99") * 2; // 999.98
settype($a, "integer");      // $a is int(10) now
var_dump(is_string($a));     // false
?>
```

#### F. Sum of two numbers (Q69)
```php
<?php
$a = 15;
$b = 27;
$sum = $a + $b;
echo "Sum of $a and $b is $sum";   // Sum of 15 and 27 is 42
?>
```
Points to write beside it: (1) both values are stored in variables, (2) `+` performs arithmetic because both operands are numeric, (3) `echo` with double quotes interpolates the variables into the HTML output. If input must come from a form, read `(float)$_GET["num1"]` instead of hard-coding — see §3.2.220.

#### G. Building blocks with an addition function (Q86)
```php
<?php
function add($x, $y) {
    return $x + $y;
}
$a = 12; $b = 30;
$result = add($a, $b);
echo "Sum = " . $result;   // Sum = 42
?>
```
1. **Variables** `$a`, `$b` hold the operands; **operator** `+` does the arithmetic; **function** `add()` packages it; **`echo`** sends the result into the HTML; every statement ends with `;` inside `<?php ?>`.
2. Mention the three building blocks by name in the answer: *variables, data types/operators, functions* — that is the mark scheme's own vocabulary.
3. Demo of the return value: `add(12,30)` is an **expression** whose value is 42, so it can be echoed directly.

#### H. Sum and difference via a function (Q87)
```php
<?php
function sumDiff($a, $b, &$sum, &$diff) {
    $sum  = $a + $b;
    $diff = $a - $b;
}
$a = 20; $b = 8;
sumDiff($a, $b, $s, $d);
echo "Sum = $s <br>";
echo "Difference = $d";
?>
```
1. A function can return only **one** value with `return`, so two results are produced through **pass-by-reference** parameters (`&$sum`, `&$diff`) — the function writes into the caller's variables (`3:L370`).
2. Alternative accepted shape: return an array `return ["sum" => $a+$b, "diff" => $a-$b];` and read `$r["sum"]`.
3. Show the call and the two `echo` lines; that is where the marks for "displays the results" are.

#### I. Flow control functions + pos/neg/zero (Q71; also answers Q214b)
1. **`if/elseif/else`** — the branching construct: a block runs only when its condition is true, exactly as in C (`3:L231`).
2. **`exit()` / `die()`** — stop the script immediately; `die()` is an alias of `exit()`; used after a fatal error, e.g. `die("Connection failed");` (`3:L235`).
3. **`return`** — inside a function it sends a value back **and** stops that function; nothing after it runs (`3:L239`).
4. **Why grouped:** all three decide whether execution continues, branches, or stops (`3:L243`).
```php
<?php
$n = -7;
if ($n > 0)      { echo "Positive"; }
elseif ($n < 0)  { echo "Negative"; }
else             { echo "Zero"; }

if (!is_numeric($n)) { die("Input must be a number"); }
?>
```

#### J. if-else vs switch (Q72)
1. **`if-else`** evaluates an arbitrary **boolean expression** per branch (ranges, `&&`, function calls); `switch` compares one variable against a list of **fixed constant values** (`3:L259–260`).
2. **Evaluation count:** `if-elseif` re-evaluates each condition in order; `switch` evaluates the subject **once** and jumps to the matching label — cheaper and clearer for many-way equality.
3. **`break` and `default`:** without `break` control **falls through** into the next case; `default` catches everything unmatched (`3:L261–262`).
4. **Which to use:** ranges/compound tests → `if`; one variable, many discrete values (day number, menu choice, status code) → `switch`.
```php
<?php
$m = 82;
if ($m >= 90) echo "A"; elseif ($m >= 75) echo "B"; else echo "C";   // range → if

switch ($m) { case 100: echo "Perfect"; break; default: echo "Scored"; } // value → switch
?>
```

#### K. Functions + `add()` (Q73; overlaps §3.2.206 and Q214a)
1. **Definition.** A function is a named, reusable block of statements that may take parameters and may return a value: `function name($params) { ... return $value; }` (`3:L328`).
2. **Facts to quote:** declarations are **hoisted** (may be called before they appear); `return` exits immediately with a value; a function with no `return` implicitly returns `NULL` (`3:L329–331`).
3. **The required function.**
```php
<?php
function add($a, $b) {
    return $a + $b;
}
$result = add(25, 17);
echo "Sum = " . $result;    // Sum = 42
?>
```
4. **Point out** that the function itself produces no output — `echo` at the call site prints the returned value. That separation is what makes it reusable.

#### L. Functions + factorial (Q90)
1. **Function mechanics** as in K: definition, parameters, `return`, hoisting, `NULL` when no return (`3:L324–331`).
2. **The factorial rule:** `n! = n × (n-1) × ... × 1`, and `0! = 1` by definition.
3. **Iterative version (write this one — it is safer on paper).**
```php
<?php
function factorial($n) {
    $fact = 1;
    for ($i = 1; $i <= $n; $i++) {
        $fact = $fact * $i;
    }
    return $fact;
}
echo "Factorial of 5 = " . factorial(5);   // 120
?>
```
4. *(Add one line if space allows)* the recursive form `return ($n <= 1) ? 1 : $n * factorial($n - 1);` — same result, and it demonstrates that PHP functions may call themselves.

#### M. Role of regular expressions (Q74)
1. **Definition.** A regular expression is a **pattern** written in a mini-language that describes a set of strings; PHP implements PCRE — Perl-Compatible Regular Expressions (`3:L570`).
2. **The three functions.** `preg_match($pattern, $string)` tests for a match (returns 1/0/false); `preg_replace($pattern, $replacement, $string)` does pattern-based find-and-replace; `preg_split($pattern, $string)` splits a string on a pattern (`3:L572–575`).
3. **Why needed for string processing.** Plain string functions can only find or replace a *fixed* substring; regex expresses *shape* — "exactly 10 digits", "letters only", "something@something.something" — which is what validation requires (`3:L599–607`).
4. **Example.**
```php
<?php
$email = "user@saintgits.org";
if (preg_match("/^[\w.-]+@[\w.-]+\.[\w]+$/", $email)) {
    echo "Valid email";
}
?>
```
*Patterns are wrapped in delimiters `/.../`; `^` and `$` anchor the whole string, `\d` = digit, `\w` = word character, `{n}` = exactly n times (`3:L607`).*

#### N. Concatenate two strings, uppercase (Q75)
```php
<?php
$first = "web";
$second = "programming";
$joined = $first . " " . $second;      // concatenation with .
$upper  = strtoupper($joined);         // WEB PROGRAMMING
echo "Result: " . $upper;
?>
```
1. `.` is the concatenation operator; `+` cannot join strings in PHP (`3:L172`).
2. `strtoupper($s)` returns a new uppercase copy — it does not modify `$s` in place (that would be `strtoupper` on assignment: `$s = strtoupper($s);`).
3. `.=` is the append-and-assign shorthand: `$joined .= "!";` — worth one line for the extra mark.

#### O. Internal representation of PHP arrays (Q80)
1. **An array is an ordered hash table (map), not a C array.** Every PHP array — indexed or associative — is the same structure: a **hash table of buckets**, each bucket holding a *key* and a *value*, plus a pointer to the next bucket to preserve insertion order. That is why an "indexed" array and an "associative" array are the same type (standard, not in your deck — the deck asserts the *behaviour* at `3:L121`, `3:L423` but prints no diagram).
2. **Draw it.**
```
$stu = ["name" => "Anu", "marks" => 88];

  hash(key) ──► bucket ──────────────┐
                key   = "name"       │
                value = zval("Anu")  │
                next  ───────────────┼──► bucket
                                     │    key   = "marks"
                                     │    value = zval(88)
                                     │    next  = NULL
  internal pointer ──────────────────┘   (order preserved: name, marks)
```
3. **Consequences to state (this is where the marks are):** keys are integers **or** strings in one structure; integer keys are auto-assigned as (highest previous int + 1) so `$a[] = x` needs no counter (`3:L392`); insertion order is preserved, which is why `foreach` is deterministic (`3:L298`); a value is a `zval` (type + value), which is *why* the same array can mix `88`, `"Anu"` and `true`; and keys must be unique — assigning an existing key overwrites.
4. **Say the "because" sentence:** "because it is a hash table, lookup by key is O(1) and order is insertion order, not sorted order."

#### P. `next`, `reset`, `prev` (Q81)
1. Every PHP array carries an **internal pointer** (cursor) pointing at one element; these functions move it (standard, not in your deck — the deck's array slide `3:L450–459` lists no pointer functions).
2. **`reset($arr)`** moves the pointer to the **first** element and returns its value; **`end($arr)`** moves it to the **last** and returns it.
3. **`next($arr)`** advances one step **forward** and returns the new current value; **`prev($arr)`** steps **backward** and returns the new current value. Both return `false` when they move past the end/start.
4. **Related:** `current($arr)` reads the value at the pointer without moving, `key($arr)` reads its key. `foreach` uses this same pointer internally.
```php
<?php
$p = [10, 20, 30];
echo current($p);            // 10
next($p);  echo current($p); // 20
end($p);   echo current($p); // 30
prev($p);  echo current($p); // 20
reset($p); echo current($p); // 10
?>
```

#### Q. Sorting arrays (Q82)
1. **`sort($arr)`** sorts ascending by **value** and **re-numbers** the keys 0,1,2…; **`rsort($arr)`** does the same descending (`3:L456`).
2. **Key-preserving sorts:** `asort()` ascending by value keeping keys, `arsort()` descending by value keeping keys, `ksort()` by **key** ascending, `krsort()` descending; `usort($arr, $cmp)` sorts by a user function (standard, not in your deck).
3. **The exam point:** `sort()` must never be used on an associative array whose keys matter — the names are lost; use `asort()` instead.
4. **Example.**
```php
<?php
$n = [40, 10, 30];
sort($n);  print_r($n);        // 10,30,40  (keys 0,1,2)

$m = ["Anu" => 88, "Rahul" => 72, "Diya" => 95];
asort($m); print_r($m);        // Rahul 72, Anu 88, Diya 95 — names kept
arsort($m); print_r($m);       // Diya 95, Anu 88, Rahul 72
?>
```

#### R. Form handling (Q83)
1. **Mechanism.** An HTML `<form method="..." action="...">` submits its named fields; PHP receives them pre-parsed into **superglobal** arrays — `$_GET` for `method="GET"` (URL query string), `$_POST` for `method="POST"` (request body) (`3:L621–624`).
2. **Detecting submission.** `$_SERVER["REQUEST_METHOD"]` tells the script whether it was reached by GET or POST, so the same file can both render and process the form; `isset($_POST["field"])` checks a specific field arrived (`3:L626–630`).
3. **The five-step pipeline.** check method → read & `trim()` → validate (`empty`, `preg_match`) → apply business logic → respond (`3:L722–726`).
4. **Example.**
```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = trim($_POST["name"] ?? "");
    if (empty($name)) { die("Name required"); }
    echo "Hello, " . htmlspecialchars($name);
}
?>
<form method="POST" action=""><input type="text" name="name">
<input type="submit" value="Send"></form>
```

#### S. Cookies and session tracking (Q84 — cross-reference Module 4)
1. **The problem.** HTTP is **stateless** — the server keeps nothing between requests, so it cannot tell that two requests came from the same visitor.
2. **Cookies (client side).** `setcookie("name", "value", time()+3600)` stores a small text file in the browser; PHP reads it back on later requests via `$_COOKIE["name"]`; deleting = set it again with an expiry in the past (`4:L63–88`). Must be called **before any output**, because it is sent as an HTTP header (`4:L65`). Limit ~4 KB, fully visible/editable by the user — never store secrets (`4:L73`).
3. **Sessions (server side).** `session_start()` begins or resumes a session and issues a **session-ID cookie**; data lives on the server in `$_SESSION["key"] = value;` and persists across pages until `session_destroy()` (`4:L102–124`).
4. **Which to use.** Cookies: non-sensitive preferences that must survive a browser restart. Sessions: login state, user identity, cart — anything sensitive, since only an ID sits in the browser. Full comparison table at `4:L136–160`, answered in the M4 kit.

#### T. `explode()` vs `implode()` (Q89; also answers Q213b and Q221b)
1. **`explode($delimiter, $string)`** splits a string wherever the delimiter occurs and returns an **array** of the pieces: `explode(",", "HTML,CSS,JS")` → `["HTML","CSS","JS"]` (`3:L544`).
2. **`implode($glue, $array)`** joins array elements into one string, inserting the glue between them: `implode(" + ", $parts)` → `"HTML + CSS + JS"` (`3:L545`).
3. **They are inverses** — `implode(",", explode(",", $s))` returns the original `$s`; this round trip is the standard way to store a list in one database column.
4. **Example.**
```php
<?php
$parts  = explode(",", "HTML,CSS,JS");   // array of 3
$joined = implode(" + ", $parts);        // "HTML + CSS + JS"
echo count($parts) . " subjects: " . $joined;
?>
```

#### U. Prime check (Q91)
```php
<?php
$n = 29;
$isPrime = true;
if ($n < 2) {
    $isPrime = false;
} else {
    for ($i = 2; $i * $i <= $n; $i++) {
        if ($n % $i == 0) { $isPrime = false; break; }
    }
}
echo $isPrime ? "$n is prime" : "$n is not prime";
?>
```
1. **Logic.** 1 and everything below is not prime; otherwise test divisibility by every integer from 2 up to √n — if any divides exactly (`%` gives 0), it is composite.
2. **Why `$i * $i <= $n`** instead of `$i < $n`: a factor larger than √n must pair with one smaller than √n, so stopping at √n is enough — fewer iterations, same answer.
3. **Point out the `break`** — once a factor is found there is no need to continue; and `$isPrime` defaults to `true` so the loop only has to disprove it.

---

### 3.2 14-mark answers (Part B)

#### Q203 — Building blocks (6) + rectangle area script (8)
**Structure:** (a) 6 marks = tags, variables + naming, data types table, operators/expressions, echo/output, functions — six bullets, one mark each. (b) 8 marks = the program (5) + explanation of each line/`gettype()`/`var_dump()` (3).

**Full answer (a).** The **building blocks** of PHP are: (1) **tags** `<?php ... ?>` marking where PHP starts and stops, with HTML outside them passed through untouched (`3:L88`); (2) **variables** — names beginning with `$`, created by assignment, no type keyword (`3:L89`); (3) **data types** — `int`, `float`, `string`, `bool`, `array`, `object`, `NULL`, `resource`, decided at runtime because PHP is dynamically typed (`3:L90`, `3:L113–122`); (4) **operators and expressions** — arithmetic `+ - * / % **`, assignment `= += .=`, string `.`, comparison `== ===`, logical `&& || !`; an expression is anything producing a value (`3:L170–173`); (5) **output** — `echo`/`print` write into the HTML response (`3:L91`); (6) **functions** — `function name($p){ return $v; }`, hoisted, returning `NULL` when there is no `return` (`3:L328–331`). Every statement ends with `;`.

**Full answer (b).**
```php
<?php
// (b) Area of a rectangle + basic variable information
$length = 12.5;          // float
$breadth = 8;            // int
$area = $length * $breadth;

echo "Length = $length <br>";
echo "Breadth = $breadth <br>";
echo "Area of rectangle = " . $area . " sq units<br>";

echo "Type of length: " . gettype($length) . "<br>";
echo "Type of breadth: " . gettype($breadth) . "<br>";
echo "Type of area: " . gettype($area) . "<br>";

var_dump($area);
?>
```
**Explanation to write:** `$length` and `$breadth` are two variables of different types; `*` multiplies them and **juggling** promotes the int to float, so `$area` is `float(100)`; `gettype()` prints each type as a string and `var_dump()` prints type + value — the two inspection tools named at `3:L124`; `.` concatenates because `+` cannot join text (`3:L172`).

**Traps:** (1) writing `echo $length + $breadth;` — that *adds* (20.5), it does not print the two values. (2) Forgetting `;` on the assignment lines. (3) Calling `gettype()` without `echo` — it *returns* a string, so nothing prints.

#### Q204 — switch day-of-week (10) + expressions (4)
**Structure:** (a) 10 = definition/use of `switch` (3) + the 1–7 script (5) + explanation of `break`/`default` (2). (b) 4 = definition of an expression (1) + evaluation/precedence (1) + the types of expressions with examples (2).

**Full answer (a).** `switch` compares one variable against a list of fixed values. The subject is evaluated **once**, then control jumps to the matching `case`; `break` stops execution leaving the switch (without it, execution **falls through** into the next case); `default` is the catch-all when nothing matches (`3:L259–262`).
```php
<?php
$day = (int) ($_GET["day"] ?? 0);

switch ($day) {
    case 1: $name = "Monday";    break;
    case 2: $name = "Tuesday";   break;
    case 3: $name = "Wednesday"; break;
    case 4: $name = "Thursday";  break;
    case 5: $name = "Friday";    break;
    case 6: $name = "Saturday";  break;
    case 7: $name = "Sunday";    break;
    default:
        $name = "Invalid input - enter a number from 1 to 7";
}
echo "Day $day is $name";
?>
```
**Default explained:** it runs only when no case matched, i.e. when the input is outside 1–7 (or not numeric after the cast). It protects the program from producing an undefined `$name` and gives the user meaningful feedback. If `default` were omitted and the input were `9`, nothing would execute and `$name` would be undefined.

**Full answer (b).** An **expression** is any construct that produces a value — a literal, a variable, an operator applied to expressions, a function call, an assignment (`3:L173`). PHP evaluates it by **precedence then associativity**: `**` first, then `* / %`, then `+ -`, then comparison, then `&&`, then `||`, then `?:`, then `=` (standard — the deck has no precedence table). Types: **arithmetic** `$a + $b`, **string** `$first . $last`, **assignment** `$x = 10` (itself has the value 10), **comparison** `$a > $b` (value `true`/`false`), **logical** `$ok && $active`, **ternary** `$m >= 50 ? "Pass" : "Fail"`. Note that a comparison is an expression, which is exactly why it can sit inside `if (...)`.

**Traps:** (1) omitting `break` — Tuesday prints Monday's text too. (2) `switch` uses loose `==`, so `"1"` matches `case 1` — a place where that is convenient. (3) Claiming `switch` supports ranges — it does not; that is `if`'s job.

#### Q205 — Type juggling/casting (4) + operators (10)
**Structure:** (a) 4 = juggling definition + example (2), casting/cast list/`settype` (2). (b) 10 = three operator families, ~3 marks each + 1 for the summary.

**Full answer (a).** **Type juggling** is automatic conversion performed by PHP when an operator or construct needs a particular type: `"10" + 5` → `15`, `"5" == 5` → `true` (`3:L138`). **Type casting** is the programmer forcing it: `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` (`3:L140`), or `intval()`/`floatval()`/`strval()`/`boolval()` (`3:L141`), or `settype($var, "integer")` which changes the variable itself (`3:L142`). Casting is preferred because it makes behaviour predictable — `(int)"12abc"` is `12`, whereas relying on juggling in arithmetic hides errors.
```php
<?php
$a = "10";
$b = (int)$a + 5;            // 15
$price = "499.99";
$total = floatval($price) * 2;   // 999.98
settype($a, "integer");      // $a is now int(10)
var_dump(is_int($a));        // true
?>
```
**Full answer (b).** **Arithmetic:** `+ - * / % **` — `%` is remainder (`10 % 3` → 1), `**` is exponent (`10 ** 2` → 100), `/` always returns a float (`10 / 4` → 2.5). **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, `.=` — `$total .= 5;` appends. **String:** `.` and `.=`; `.` is not `+`. **Comparison:** `==` equal after conversion, `===` identical value **and** type, `!=`/`!==`, `< > <= >=`; `"5" == 5` is `true` but `"5" === 5` is `false` (`3:L201–203`). **Logical:** `&&`, `||`, `!` — short-circuiting, so `isset($x) && $x > 0` is safe (`3:L204`). **Increment/decrement:** `$i++` uses then increments, `++$i` increments then uses. **Ternary:** `cond ? a : b`. Every operator returns a value, which is what makes expressions composable.

**Traps:** (1) `$s = "Total: " . 5 + 3;` — `.` and `+` share precedence and evaluation is left to right, so parenthesise. (2) Saying `==` "is the same as" `===` — it is not, and this is the deck's flagged quirk (`3:L199`). (3) `%` on floats silently casts to int.

#### Q206 — Functions (7) + default parameters (7)
**Structure:** definition/mechanics 3, example function 4; then default-parameter rule 2, code 3, why useful 2.

**Full answer (a).** A **function** is a named, reusable block that may accept parameters and may return a value. Syntax: `function name($param1, $param2) { statements; return $value; }` (`3:L328`). Three facts to state: declarations are **hoisted**, so the call may appear above the definition (`3:L329`); `return` sends a value back and stops the function immediately (`3:L330`); a function with **no** `return` implicitly returns `NULL` (`3:L331`). Functions may also `echo` instead of returning, but then the output is a side effect and the caller gets `NULL`.
```php
<?php
function area($l, $b) {
    return $l * $b;
}
echo "Area = " . area(12, 8) . "<br>";   // 96

function greet($name) {
    echo "Hello, $name!";                // prints, returns NULL
}
greet("Saintgits");
?>
```
**Full answer (b).** A **default parameter value** is written in the signature as `$name = "Guest"`; if the caller omits that argument the default is used, and if the caller supplies it the supplied value wins (`3:L362`). Defaults must be placed **after** all required parameters (standard). Typical uses: optional greetings, optional formatting flags, optional limits.
```php
<?php
function greet($name = "Guest", $greeting = "Hello") {
    return "$greeting, $name!";
}
echo greet();                 // Hello, Guest!
echo greet("Anu");            // Hello, Anu!
echo greet("Rahul", "Hi");    // Hi, Rahul!
?>
```
**Why it matters:** the caller can skip arguments it does not care about, so one function replaces a family of overloads — PHP has no method overloading, and this is the idiom that replaces it (standard).

**Traps:** (1) a required parameter after a defaulted one — `function f($a = 1, $b)` — errors. (2) Passing `null` explicitly does **not** trigger the default; the default applies only when the argument is *omitted*. (3) Confusing "returns NULL" with "returns nothing" — a caller can still `var_dump()` the `NULL`.

#### Q207 — Control statements (8) + arrays (6)
**Structure:** 8 = if/elseif/else (2), switch (2), loops — for/while/do-while/foreach (3), break/continue (1). 6 = array definition + three kinds (3), functions table (2), example (1).

**Full answer (a).** **`if / elseif / else`** branches on any boolean expression, evaluated top-down, first true block wins, `else` is optional (`3:L259`). **`switch / case / break / default`** matches one variable against constant values, evaluated once; `break` prevents fall-through, `default` is the catch-all (`3:L260–262`). **Loops:** `for (init; cond; step)` for a known count; `while (cond)` tests before, may run zero times; `do {...} while (cond)` tests after, always runs at least once; `foreach ($arr as $v)` / `as $k => $v` iterates an array and is the idiomatic PHP loop (`3:L295–298`, `3:L762`). **`break`** leaves the loop, **`continue`** skips to the next iteration (standard).
```php
<?php
for ($i = 1; $i <= 3; $i++) { echo $i; }          // 123

$n = 3;
while ($n > 0) { echo $n; $n--; }                 // 321

$k = 9;
do { echo "runs once"; } while ($k < 5);          // runs once

foreach (["a" => 1, "b" => 2] as $key => $val) {
    echo "$key=$val ";                            // a=1 b=2
}
?>
```
**Full answer (b).** An **array** is an ordered map that associates **keys** with **values**; the keys may be integers (indexed array) or strings (associative array), and an array may contain arrays (multidimensional) (`3:L388`, `3:L423–425`). Creation: `[10, 20, 30]`, `array(10, 20, 30)`, `["name" => "Anu"]`, `$a[] = 5` to append. Core functions: `count`, `array_push`, `sort`/`rsort`, `asort`/`ksort`, `array_map`, `array_filter`, `in_array` (`3:L452–459`). Traversal: `foreach`, or `for` with integer keys; `count($arr)` is the only safe bound because arrays grow.
```php
<?php
$marks = ["Anu" => 88, "Rahul" => 72];
foreach ($marks as $name => $m) { echo "$name scored $m<br>"; }
echo "Students: " . count($marks);
?>
```
**Traps:** (1) `for` loops on associative arrays — `$arr[0]` does not exist. (2) `sort()` on a named array destroys the names (`3:L456`) — use `asort()`. (3) Writing `while ($i < 3)` without ever changing `$i` — infinite loop; the examiner looks for the increment.

#### Q208 — User registration system with regex validation (14)
**Structure:** form (2), reading + trimming input (2), regex validation of name/email/password (4), business logic + feedback messages (4), sanitised output/completeness (2).

**Full answer.** The script is the deck's five-step pipeline (`3:L722–726`) with three regex checks added (`3:L599–605`). Validation asks *is it well-formed*; business logic asks *what should the application do with well-formed data* (`3:L686–689`) — here, the password policy and the success/failure message.

```php
<?php
$errors = [];
$done = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name  = trim($_POST["fullname"] ?? "");
    $email = trim($_POST["email"] ?? "");
    $pass  = $_POST["password"] ?? "";

    // 1. presence
    if (empty($name))  { $errors[] = "Full name is required."; }
    if (empty($email)) { $errors[] = "Email is required."; }
    if (empty($pass))  { $errors[] = "Password is required."; }

    // 2. shape - regular expressions
    if (!empty($name) && !preg_match("/^[A-Za-z ]{3,40}$/", $name)) {
        $errors[] = "Name must be 3-40 letters or spaces only.";
    }
    if (!empty($email) && !preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
        $errors[] = "Email is not in a valid format.";
    }

    // 3. business logic - password policy
    $strong = strlen($pass) >= 8
           && preg_match("/[A-Z]/", $pass)
           && preg_match("/[0-9]/", $pass);

    if (!empty($pass) && !$strong) {
        $errors[] = "Password needs 8+ characters, one capital and one digit.";
    }

    if (empty($errors)) {
        $done = "Registration successful for " . htmlspecialchars($name)
              . " (" . htmlspecialchars($email) . ").";
    }
}
?>
<!DOCTYPE html>
<html><body>
<h2>User Registration</h2>

<?php if (!empty($errors)): ?>
  <ul style="color:red">
  <?php foreach ($errors as $e): ?>
    <li><?= htmlspecialchars($e) ?></li>
  <?php endforeach; ?>
  </ul>
<?php endif; ?>

<?php if ($done != ""): ?>
  <p style="color:green"><?= $done ?></p>
<?php endif; ?>

<form method="POST" action="">
  Full name: <input type="text" name="fullname"><br>
  Email:     <input type="text" name="email"><br>
  Password:  <input type="password" name="password"><br>
  <input type="submit" value="Register">
</form>
</body></html>
```
**Explanation to write beside it:** the `REQUEST_METHOD` guard means the same file renders the blank form on the first GET and processes it on POST; `trim()` + `??` remove whitespace and suppress the missing-key warning; `preg_match()` returns 1/0 so `!preg_match(...)` is the failure test; errors are collected in an **array** and rendered as a list rather than with `die()`, so the user sees *all* problems at once; `htmlspecialchars()` prevents injected HTML from executing when the name is echoed back.

**Traps:** (1) `die()` after the first error — you lose the other messages and the form. (2) Echoing `$name` without `htmlspecialchars()` — an XSS hole. (3) Using `/^[A-Za-z]+$/` for the name and then rejecting "Anu K" — the space must be in the character class.

#### Q209 — Arrays: creation, functions, sequential access, sorting
**Structure:** (a) creation 4 ways (3) · (b) function table + uses (4) · (c) sequential access `foreach`/`for`/pointer (4) · (d) sorting incl. key-preserving (3).

**Full answer (a).**
```php
<?php
$a = [10, 20, 30];              // short indexed syntax
$b = array(10, 20, 30);         // long syntax, same result
$c = ["name" => "Anu", "marks" => 88];   // associative
$d = [ ["name" => "Anu"], ["name" => "Rahul"] ];  // multidimensional
$e = [];                        // empty, then append
$e[] = 5;  $e[] = 9;            // keys 0 and 1 automatically
$f = [2 => "two", 5 => "five"]; // explicit integer keys
print_r($e);
?>
```
**(b) Functions** (`3:L452–459`): `count()` length · `array_push($a,$v)` append (same as `$a[]=$v`) · `array_pop($a)` remove last (standard) · `array_shift`/`array_unshift` remove/add at front (standard) · `sort`/`rsort` value sort, keys renumbered · `asort`/`arsort` value sort, keys kept · `ksort`/`krsort` key sort · `in_array($v,$a)` membership · `array_search($v,$a)` key of a value (standard) · `array_map($fn,$a)` transform all · `array_filter($fn,$a)` keep matching · `array_merge($a,$b)` concatenate (standard) · `array_keys`/`array_values` (standard) · `array_sum` total (standard) · `implode`/`explode` array↔string (`3:L544–545`).
**(c) Sequential access.** `foreach ($a as $v)` walks values in **insertion order**; `foreach ($a as $k => $v)` gives keys too; `for ($i=0; $i<count($a); $i++)` works only for integer-keyed arrays; the **internal pointer** (`reset`, `current`, `next`, `prev`, `end`, `key`) allows manual movement — `next()` returns the new current value and `false` past the end.
**(d) Sorting.**
```php
<?php
$n = [40, 10, 30];
sort($n);    // [10, 30, 40]  ascending, keys renumbered
rsort($n);   // [40, 30, 10]  descending

$m = ["Anu" => 88, "Rahul" => 72, "Diya" => 95];
asort($m);   // 72, 88, 95 — names preserved
ksort($m);   // Anu, Diya, Rahul — alphabetical by name
?>
```
**Traps:** (1) `count()` inside the `for` condition re-counts every iteration — harmless but worth noting. (2) `sort()` on `$m` would leave `[72, 88, 95]` with keys 0,1,2 and the names gone. (3) `$a[3] = x` on a 3-element array is *not* an append to index 3 if keys are non-sequential — `[]` is the safe append.

#### Q210 — Unique strings; average and median (14)
**Structure:** 7 + 7. Each half: algorithm in words (3), function (3), driver/demo output (1).

**Full answer (a) — algorithm.** Create an empty result array. Walk the input array once. For each string, test whether it is already in the result using `in_array()` (strict). If not, append it. Return the result — duplicates removed, original order preserved.

```php
<?php
function uniqueStrings($arr) {
    $out = [];
    foreach ($arr as $s) {
        if (!in_array($s, $out, true)) {   // strict: "1" != 1
            $out[] = $s;
        }
    }
    return $out;
}

$in = ["php", "html", "php", "css", "html"];
print_r(uniqueStrings($in));   // php, html, css
?>
```
**Alternative worth one line:** `array_unique($arr)` is the built-in (standard), but the question says *write algorithm and function*, so the loop is the answer.

**Full answer (b) — algorithm.** Average = sum ÷ count. Median = sort a copy, then if the count is odd take the middle element, else average the two middle elements.

```php
<?php
function stats($nums) {
    $n = count($nums);
    if ($n == 0) { return ["average" => 0, "median" => 0]; }

    $average = array_sum($nums) / $n;      // sum / count

    $sorted = $nums;                        // copy, keep caller's array intact
    sort($sorted);
    $mid = intdiv($n, 2);
    if ($n % 2 == 1) {
        $median = $sorted[$mid];            // odd: middle element
    } else {
        $median = ($sorted[$mid - 1] + $sorted[$mid]) / 2;  // even: mean of two
    }
    return ["average" => $average, "median" => $median];
}

$r = stats([10, 20, 30, 40, 50]);
echo "Average = " . $r["average"] . "<br>";   // 30
echo "Median = "  . $r["median"];             // 30

$r2 = stats([10, 20, 30, 40]);
echo "Average = " . $r2["average"] . "<br>";  // 25
echo "Median = "  . $r2["median"];            // 25
?>
```
**Traps:** (1) using `$n/2` as an index — for even counts that is a float index, hence `intdiv`. (2) Sorting `$nums` directly mutates the caller's array. (3) Dividing by zero on an empty array — guard it.

#### Q211 — Pass-by-value vs pass-by-reference partitioning (14)
**Structure:** concept of the two modes (4), algorithm (3), function with `&` (5), demo output (2).

**Full answer.** By default PHP passes arguments **by value**: the function receives a copy, so nothing it does is visible to the caller. Prefixing a parameter with `&` passes **by reference**: the parameter is an alias for the caller's variable, so assignments inside the function modify the original (`3:L369–370`). Since `return` can yield only one value, two result arrays must come back through two reference parameters — which is exactly the specification here.
```php
<?php
// array of numbers by value, two output arrays by reference
function partition($nums, &$positives, &$negatives) {
    $positives = [];
    $negatives = [];
    foreach ($nums as $n) {
        if ($n > 0) {
            $positives[] = $n;
        } elseif ($n < 0) {
            $negatives[] = $n;
        }
        // zero belongs to neither list
    }
    // no return value: the results are the two reference parameters
}

$data = [5, -3, 0, 8, -1, 12];
$pos = [];
$neg = [];

partition($data, $pos, $neg);

echo "Positives: " . implode(", ", $pos) . "<br>";   // 5, 8, 12
echo "Negatives: " . implode(", ", $neg) . "<br>";   // -3, -1
echo "Original array unchanged: " . implode(", ", $data);
?>
```
**Algorithm in words:** initialise both output arrays empty; traverse the input once; if the element is greater than zero append it to the first, if less than zero append it to the second; leave zeros out; return nothing.
**Proof that reference was necessary:** delete the `&` from the signature and both `echo` lines print empty arrays, because the function only filled its own copies.
**Traps:** (1) forgetting `&` — the single most common lost-marks error here. (2) Trying to `return` two arrays without `&` — you would have to return `[$pos, $neg]` and unpack it, which is not what the question asks. (3) Using `$n >= 0` and putting zeros in positives.

#### Q212 — Most frequent word from a file (14)
**Structure:** algorithm (4), reading + splitting (4), counting with an array (4), finding the max (2).

**Full answer.** **Algorithm:** open/read the file; replace the colon separators with spaces so both delimiters collapse into one; split on whitespace into an array of words; normalise case; count occurrences using a **frequency array keyed by the word** (this is the associative-array pattern); scan the counts for the maximum; return that word.
```php
<?php
function mostFrequentWord($filename) {
    if (!file_exists($filename)) { return null; }

    $text = file_get_contents($filename);          // whole file as one string
    if ($text === false) { return null; }

    $text  = str_replace(":", " ", $text);         // "a:b" -> "a b"
    $words = preg_split("/\s+/", trim($text));     // split on any whitespace

    $count = [];
    foreach ($words as $w) {
        if ($w === "") { continue; }               // skip empty pieces
        $w = strtolower($w);                       // "PHP" and "php" are one word
        if (isset($count[$w])) {
            $count[$w] = $count[$w] + 1;
        } else {
            $count[$w] = 1;
        }
    }

    $best = null;
    $max  = 0;
    foreach ($count as $word => $c) {
        if ($c > $max) { $max = $c; $best = $word; }
    }
    return $best;                                  // null if the file was empty
}

echo "Most frequent: " . mostFrequentWord("input.txt");
?>
```
**Why this shape:** the associative array `$count` *is* the algorithm — key = word, value = frequency, so "have I seen this word?" becomes an `isset` test, O(1). `preg_split("/\s+/", ...)` handles any run of spaces, newlines and tabs, which `explode(" ", ...)` cannot.
**Traps:** (1) `explode(" ", $text)` leaves `"word\n"` and `""` entries. (2) Not lower-casing — `PHP` and `php` are counted separately. (3) `file()` instead of `file_get_contents()` gives an array of *lines*, not words; if you use `file()`, you must `implode` or loop.

#### Q213 — Array creation (7) + implode/explode + Armstrong (7)
**Structure:** (a) four creation methods with code (7). (b) explode vs implode table/sentences (3) + Armstrong program (4).

**Full answer (a).** Four ways: (1) **short indexed** `$a = [10, 20, 30];`; (2) **long form** `$a = array(10, 20, 30);`; (3) **associative literal** `$s = ["name" => "Anu", "marks" => 88];`; (4) **incremental** `$a = []; $a[] = 10; $a[] = 20;` — the empty-bracket append assigns the next integer key automatically (`3:L390–392`). Add **multidimensional** `$m = [[1,2],[3,4]];` and **explicit keys** `$e = [5 => "five"];` for the extra marks. `print_r()` or `var_dump()` shows the structure.
**Full answer (b).** `explode($delimiter, $string)` → **string to array**: `explode(",", "HTML,CSS,JS")` gives three elements. `implode($glue, $array)` → **array to string**: `implode(" + ", $parts)` gives `"HTML + CSS + JS"` (`3:L544–545`). They are exact inverses; neither modifies its input.
```php
<?php
// Armstrong: an n-digit number equal to the sum of its digits each raised to n
$n = 153;
$temp = $n;
$digits = strlen((string)$n);   // 3
$sum = 0;

while ($temp > 0) {
    $d = $temp % 10;            // last digit
    $sum += $d ** $digits;      // digit^3
    $temp = intdiv($temp, 10);  // drop last digit
}

if ($sum == $n) {
    echo "$n is an Armstrong number";    // 1+125+27 = 153
} else {
    echo "$n is not an Armstrong number";
}
?>
```
**Traps:** (1) using `3` as the exponent instead of the digit count — 1634 is Armstrong with exponent 4. (2) `$temp / 10` instead of `intdiv` — leaves a float and loops forever. (3) Testing `$sum == $n` *after* modifying `$n` — keep `$temp` as the working copy.

#### Q214 — Functions sample script (8) + flow control functions (6)
**Structure:** (a) 8 = definition/syntax 2, parameter kinds 2, a working script with two functions 4. (b) 6 = `if/elseif/else` 2, `exit`/`die` 2, `return` 2.

**Full answer (a).**
```php
<?php
// 1. plain function with parameters and a return value
function area($l, $b) {
    return $l * $b;
}

// 2. default parameter
function greet($name = "Guest") {
    return "Hello, $name";
}

// 3. pass by reference - modifies the caller's variable
function addBonus(&$marks, $bonus = 5) {
    $marks = $marks + $bonus;
}

// 4. variadic - any number of arguments
function total(...$nums) {
    return array_sum($nums);
}

echo area(10, 4) . "<br>";        // 40
echo greet() . "<br>";            // Hello, Guest
echo greet("Anu") . "<br>";       // Hello, Anu

$m = 80;
addBonus($m);
echo "Marks after bonus: $m<br>";  // 85

echo "Total: " . total(1, 2, 3, 4); // 10
?>
```
Say: the `function` keyword names it; parameters are comma-separated with `$`; `return` ends it with a value; declarations are hoisted so order is irrelevant (`3:L329`); no `return` means `NULL` (`3:L331`); scope is local unless `global` is declared (`3:L366`); `&` gives reference semantics (`3:L370`); `...` collects into an array (`3:L374`).
**Full answer (b).** (1) **`if / elseif / else`** — branching; conditions evaluated in order, first true block runs, `else` covers the rest (`3:L231`). (2) **`exit()`** — terminates the script immediately, optionally printing a message or returning a status code; **`die()`** is its exact alias, used after a fatal error: `die("Connection failed");` (`3:L235`). (3) **`return`** — inside a function, sends a value to the caller **and** stops the function; nothing after it executes (`3:L239`). Together they control continuation, branching and termination (`3:L243`).
**Traps:** (1) `return` in the middle of a loop inside a function exits the *function*, not just the loop. (2) `die()` inside an `if` in a function kills the whole page, not just the function. (3) `exit` and `die` are language constructs, so `echo die("x")` is not meaningful.

#### Q215 — Cookies (6) + five MySQL operations (8)
**Structure:** (a) significance 2, create 2, read/delete 2. (b) connect 1 + one compact script demonstrating CREATE, INSERT, SELECT, UPDATE, DELETE 7.

**Full answer (a).** HTTP is **stateless**, so a cookie is the client-side mechanism that lets a site *remember* a visitor: a small name=value text record the server asks the browser to store and send back on every later request to that domain (`4:L65–73`). **Create:** `setcookie("username", "Anu", time() + 3600)` — name, value, expiry timestamp (here one hour); it must be called **before any HTML output**, because it travels as an HTTP header (`4:L65–67`). **Read:** `$_COOKIE["username"]` on subsequent requests. **Destroy:** call `setcookie` again with the same name and an expiry in the **past** — `setcookie("username", "", time() - 3600)` (`4:L71`, `4:L86`). Limits to state: ~4 KB, visible and editable by the user, so never store passwords or tokens (`4:L73`).
```php
<?php
setcookie("username", "Anu", time() + 3600);   // create
if (isset($_COOKIE["username"])) {             // read on a later request
    echo "Welcome back, " . $_COOKIE["username"];
}
setcookie("username", "", time() - 3600);      // destroy
?>
```
**Full answer (b).** Same five operations on one table; the SQL is Module 4's, the wrapper is `mysqli_query` (`4:L316–337`).
```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

/* CREATE - define the table (run once) */
mysqli_query($conn, "CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)");

/* INSERT - add a row */
mysqli_query($conn, "INSERT INTO students (name, marks) VALUES ('Anu', 88)");

/* SELECT - read rows back */
$res = mysqli_query($conn, "SELECT * FROM students");
while ($row = mysqli_fetch_assoc($res)) {
    echo $row["id"] . " " . $row["name"] . " " . $row["marks"] . "<br>";
}

/* UPDATE - modify an existing row (WHERE is mandatory) */
mysqli_query($conn, "UPDATE students SET marks = 92 WHERE name = 'Anu'");

/* DELETE - remove a row */
mysqli_query($conn, "DELETE FROM students WHERE id = 2");

mysqli_close($conn);
?>
```
**Cross-reference:** the full CREATE/INSERT/DELETE/SELECT/UPDATE treatment, `mysqli_insert_id`, `affected_rows` and prepared statements are in the **Module 4 kit** — here you only need the five statements and the connect/close frame.
**Traps:** (1) `setcookie` after `echo` — "headers already sent". (2) `UPDATE`/`DELETE` without `WHERE` — whole table. (3) Reading the cookie in the *same* request that set it — `$_COOKIE` is populated on the **next** request.

#### Q216 — 5-field registration into MySQL (10) + dynamic typing (4)
**Structure:** form with 5 fields (2), connect (2), read/validate (2), INSERT (2), feedback + close (2); then a 4-mark paragraph on dynamic typing.

**Full answer (a).**
```php
<?php
$msg = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name  = trim($_POST["name"] ?? "");
    $email = trim($_POST["email"] ?? "");
    $phone = trim($_POST["phone"] ?? "");
    $city  = trim($_POST["city"] ?? "");
    $pass  = $_POST["password"] ?? "";

    if (empty($name) || empty($email) || empty($phone)
        || empty($city) || empty($pass)) {
        $msg = "All five fields are required.";
    } elseif (!preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
        $msg = "Invalid email format.";
    } elseif (!preg_match("/^[0-9]{10}$/", $phone)) {
        $msg = "Phone must be exactly 10 digits.";
    } else {
        $conn = mysqli_connect("localhost", "root", "", "college");
        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }
        $hash = password_hash($pass, PASSWORD_DEFAULT);   // never store plain text
        $sql = "INSERT INTO users (name, email, phone, city, password)
                VALUES ('$name', '$email', '$phone', '$city', '$hash')";
        if (mysqli_query($conn, $sql)) {
            $msg = "Registered successfully.";
        } else {
            $msg = "Insert failed: " . mysqli_error($conn);
        }
        mysqli_close($conn);
    }
}
?>
<!DOCTYPE html>
<html><body>
<h2>Register</h2>
<p><?= htmlspecialchars($msg) ?></p>
<form method="POST" action="">
  Name:     <input type="text" name="name"><br>
  Email:    <input type="text" name="email"><br>
  Phone:    <input type="text" name="phone"><br>
  City:     <input type="text" name="city"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Register">
</form>
</body></html>
```
**Explanation:** five named inputs → five `$_POST` keys → trimmed and validated → one `INSERT` with the column list written out → `mysqli_query` returns `true`/`false`, which drives the feedback message → `mysqli_close`. *(Standard hardening, worth a line: quote string values, cast numbers with `(int)`, and prefer `mysqli_prepare` + `?` to block SQL injection — `4:L665–689`.)*
**Full answer (b).** PHP is **dynamically typed** because a variable carries **no declared type** — the type belongs to the value it currently holds and is resolved at **runtime**. `$x = 5;` makes it an int, `$x = "five";` makes the same variable a string, with no cast and no error (`3:L90`). Consequences: (1) no type declarations or compiler type-checking, so type errors appear only when the line executes; (2) PHP **juggles** types automatically in context — `"10" + 5` is `15` (`3:L138`); (3) this is why form input (always a string) can be used arithmetically after `(int)`/`(float)`; (4) it also means `==` must convert before comparing, which is why strict `===` exists (`3:L199–210`); (5) `gettype()`, `var_dump()` and `is_int()` exist precisely to inspect and defend against the missing static type (`3:L124`, `3:L143`). *(PHP 7+ allows optional type declarations, but the default behaviour remains dynamic — standard.)*
**Traps:** (1) `$sql` interpolated without escaping — injection. (2) Forgetting the column list in `INSERT`. (3) Closing the connection before the query.

#### Q217 — Control statements (7) + palindrome (7)
**Structure:** (a) if/else 2, switch 2, loops 2, break/continue 1. (b) logic 2, code 4, test cases 1.

**Full answer (a).** **`if / elseif / else`** — conditional branching on any boolean expression; only the first true branch executes (`3:L259`). **`switch / case / break / default`** — one subject compared against constant labels, evaluated once; `break` prevents fall-through, `default` is unmatched input (`3:L260–262`). **Loops** — `for` (known count), `while` (pre-test, zero or more), `do...while` (post-test, at least once), `foreach` (array traversal, `as $k => $v` for keys) (`3:L295–298`). **`break`** exits the loop, **`continue`** skips to the next iteration (standard). Also mention the **ternary** `?:` as an expression-level branch.
**Full answer (b).** A **palindrome** reads the same forwards and backwards. Two methods: reverse the digits/characters and compare, or compare characters from both ends moving inward.
```php
<?php
// (i) numeric palindrome by reversing the digits arithmetically
$n = 12321;
$temp = $n;
$rev = 0;

while ($temp > 0) {
    $rev = $rev * 10 + ($temp % 10);
    $temp = intdiv($temp, 10);
}

if ($rev == $n) { echo "$n is a palindrome"; }
else            { echo "$n is not a palindrome"; }

// (ii) string palindrome with strrev
$s = "madam";
if ($s === strrev($s)) { echo "$s is a palindrome"; }
?>
```
**Explain the loop:** `$temp % 10` peels off the last digit; multiplying `$rev` by 10 shifts what we have one place left; `intdiv($temp,10)` drops the digit just used. For 12321 the reversal builds 1 → 12 → 123 → 1232 → 12321.
**Traps:** (1) comparing `$rev` with `$temp` after the loop — `$temp` is 0; keep `$n`. (2) Using `$s == strrev($s)` on strings — prefer `===`. (3) `strrev` on a number needs a cast: `strrev((string)$n)`.

#### Q218 — Associative arrays (7) + sort student marks (7)
**Structure:** (a) definition 2, syntax/`=>` 2, traversal + functions 3. (b) build the array 2, sort 2, print 3.

**Full answer (a).** An **associative array** is an array whose keys are **named** (strings) instead of positional integers, so each value is addressed by a meaningful label (`3:L421–424`). Syntax: `$stu = ["name" => "Anu", "marks" => 88];` — `=>` separates key from value (a plain `=` is an assignment and is a syntax error here). Access: `$stu["name"]`. Traverse with `foreach ($stu as $key => $value)` (`3:L426`). Useful functions: `array_keys`, `array_values`, `in_array`, `array_key_exists`, `asort`/`arsort` (sort by value, keys kept), `ksort`/`krsort` (sort by key) — `3:L452–459` plus standard.
```php
<?php
$student = ["name" => "Anu", "roll" => 21, "marks" => 88];
foreach ($student as $k => $v) {
    echo "$k: $v<br>";
}
echo $student["marks"];
?>
```
**Full answer (b).**
```php
<?php
// name => marks
$marks = [
    "Anu"   => 88,
    "Rahul" => 72,
    "Diya"  => 95,
    "Kiran" => 61
];

echo "<h3>Original</h3>";
foreach ($marks as $name => $m) { echo "$name: $m<br>"; }

asort($marks);            // ascending by marks, names preserved
echo "<h3>Ascending</h3>";
foreach ($marks as $name => $m) { echo "$name: $m<br>"; }

arsort($marks);           // descending by marks
echo "<h3>Descending</h3>";
foreach ($marks as $name => $m) { echo "$name: $m<br>"; }

echo "<h3>Topper</h3>";
reset($marks);                          // pointer to first = highest after arsort
echo key($marks) . " with " . current($marks);
?>
```
**Why `asort` and not `sort`:** `sort()` renumbers the keys 0..n, so the names would be destroyed (`3:L456`) — the marks would be printed but nobody's. `asort()` keeps the key→value pairing, which is the whole point of an associative array.
**Traps:** (1) `sort($marks)` — the classic lost-marks answer. (2) `=>` written as `=`. (3) Assuming `foreach` returns elements sorted — it returns **insertion order**.

#### Q219 — String handling functions (8) + count vowels (6)
**Structure:** (a) six to eight functions, each name + purpose + one-line example (8). (b) logic 2, code 3, output 1.

**Full answer (a).** `strlen($s)` length in characters — `strlen("Saintgits")` = 9. `strtoupper($s)`/`strtolower($s)` case conversion — `"SAINTGITS"`. `trim($s)` strips whitespace (and optionally other characters) from both ends — `"  Anu  "` → `"Anu"`. `substr($s, start, length)` extracts a slice — `substr("Saintgits",0,5)` = `"Saint"`. `str_replace($search,$replace,$s)` replaces all occurrences — `"World"`→`"PHP"`. `explode($delim,$s)` splits to an array; `implode($glue,$arr)` joins to a string. `strrev($s)` reverses; `strpos($s,$needle)` finds the first position (returns `false` if absent); `ucfirst`/`ucwords` capitalise; `str_repeat($s,$n)` repeats; `sprintf` formats; `str_word_count` counts words; `htmlspecialchars` escapes for output (`3:L512–515`, `3:L542–545`, `3:L655`). All of them **return** a new string — they do not modify the original unless you assign back.
**Full answer (b).**
```php
<?php
function countVowels($str) {
    $vowels = "aeiouAEIOU";
    $count = 0;
    for ($i = 0; $i < strlen($str); $i++) {
        if (strpos($vowels, $str[$i]) !== false) {   // !== false, NOT != 0
            $count++;
        }
    }
    return $count;
}

$text = "Saintgits College of Engineering";
echo "Vowels in \"$text\" = " . countVowels($text);
?>
```
**Why `!== false`:** `strpos` returns `0` when the character is the **first** in the haystack — i.e. for `'a'`. A loose `!= 0` (or a truthiness test) rejects exactly the `a` case and undercounts. This is the trap the examiner is looking for.
**Traps:** (1) `$str[$i]` on a multibyte character breaks — irrelevant for ASCII exam text. (2) Forgetting both cases in `$vowels`. (3) `strlen` inside the loop condition on a huge string — cache it if asked about efficiency.

#### Q220 — Six string functions (6) + GET sum/difference/product (8)
**Structure:** (a) six functions with examples (6). (b) purpose of `$_GET`/`$_POST` (2), the HTML form (2), the processing script (4).

**Full answer (a).** `strlen` → 9 for `"Saintgits"`. `strtoupper` → `"SAINTGITS"`. `trim` → removes leading/trailing whitespace, essential on form input. `substr($s,0,5)` → `"Saint"`. `str_replace("World","PHP","Hello World")` → `"Hello PHP"`. `explode(",", "HTML,CSS,JS")` → a 3-element array. *(Extras if a seventh slot exists: `implode`, `strrev`, `strpos`, `ucfirst`.)* (`3:L512–515`, `3:L542–545`.)
**Full answer (b).** `$_GET` and `$_POST` are **superglobal arrays** — automatically populated for every request, holding the submitted form fields keyed by their `name` attribute (`3:L621`). `$_GET` carries data appended to the URL as a query string (`method="GET"`): visible, bookmarkable, size-limited, unsuitable for passwords. `$_POST` carries data in the request body: not visible in the URL, no practical size limit. Both are **always strings**, so numeric use requires a cast.
```html
<!-- form.html -->
<form method="GET" action="calc.php">
  Number 1: <input type="text" name="num1"><br>
  Number 2: <input type="text" name="num2"><br>
  <input type="submit" value="Calculate">
</form>
```
```php
<?php
// calc.php - collects the GET data and computes the three results
if (isset($_GET["num1"]) && isset($_GET["num2"])
    && $_GET["num1"] !== "" && $_GET["num2"] !== "") {

    $a = (float) $_GET["num1"];
    $b = (float) $_GET["num2"];

    echo "First number: $a <br>";
    echo "Second number: $b <br>";
    echo "Sum = " . ($a + $b) . "<br>";
    echo "Difference = " . ($a - $b) . "<br>";
    echo "Product = " . ($a * $b) . "<br>";
} else {
    echo "Please fill both numbers in the form.";
}
?>
```
**Traps:** (1) Using `$_POST` in the script while the form says `method="GET"` — the arrays are empty. (2) `$a + $b` without the cast still works by juggling, but `(float)` is what earns the "type conversion" mark. (3) Not guarding `isset` — undefined-key warnings on the first load.

#### Q221 — Functions (6) + dynamic typing & explode/implode (8)
**Structure:** (a) definition + syntax 2, parameter kinds 2, sample script 2. (b) dynamic typing 4, explode vs implode 4.

**Full answer (a).** As §3.2.214a — `function name($params) { ... return $v; }`, hoisted declarations (`3:L329`), `return` exits with a value (`3:L330`), no `return` → `NULL` (`3:L331`), locals are function-scoped (`3:L366`), `&` = by reference (`3:L370`), `...$args` = variadic (`3:L374`). A compact sample:
```php
<?php
function add($a, $b)       { return $a + $b; }
function greet($n = "Guest"){ return "Hello, $n"; }
function bump(&$x)          { $x++; }

echo add(4, 6);          // 10
echo greet();            // Hello, Guest
$c = 5; bump($c); echo $c;   // 6
?>
```
**Full answer (b) — dynamic typing.** PHP does not require (and historically did not allow) a type in a variable declaration; the *value* carries the type and the variable simply points at it, so the type is resolved at **runtime** (`3:L90`). Proof: `$x = 10; echo gettype($x); $x = "ten"; echo gettype($x);` prints `integer` then `string` with no error. Consequences: (1) automatic **juggling** in context — `"10" + 5` = 15, `"5" == 5` is `true` (`3:L138`, `3:L209`); (2) type errors surface at execution, not compilation; (3) strict `===` was introduced so you can demand type equality (`3:L202`); (4) `is_int`/`is_string`/`gettype`/`var_dump` exist to inspect the runtime type (`3:L124`, `3:L143`). **explode vs implode:** `explode($delimiter,$string)` breaks a string into an array at each delimiter; `implode($glue,$array)` joins array elements into one string with the glue between them; they are inverses (`3:L544–545`).
```php
<?php
$csv    = "Anu,88,Rahul,72";
$parts  = explode(",", $csv);        // 4-element array
$joined = implode(" | ", $parts);    // "Anu | 88 | Rahul | 72"
echo count($parts) . " pieces: " . $joined;
?>
```
**Traps:** (1) Saying "PHP has no types" — it has eight; it has no *declared* types. (2) `implode($arr, $glue)` — argument order is glue **first** in modern PHP. (3) `explode` on an empty delimiter — fatal error.

---

## 4. PART 3 — Code you must be able to write by hand

> Rules for all drills: `<?php` first, `?>` last, `$` on every variable, `;` on every statement, `.` to join strings, `=>` inside arrays, `->` on objects. Write them on paper, then check against the model.

### D1 — Sum of two numbers
```php
<?php
$a = 15;
$b = 27;
echo "Sum = " . ($a + $b);
?>
```
**Memorise:** variables start with `$`; `+` adds; `.` joins the label to the result — never `+`.

### D2 — Factorial, loop and recursion
```php
<?php
function factLoop($n) {
    $f = 1;
    for ($i = 1; $i <= $n; $i++) { $f = $f * $i; }
    return $f;
}
function factRec($n) {
    if ($n <= 1) { return 1; }        // base case
    return $n * factRec($n - 1);      // recursive case
}
echo factLoop(5) . " " . factRec(5);   // 120 120
?>
```
**Memorise:** the accumulator starts at **1**, not 0; recursion needs a base case or it never terminates.

### D3 — Prime check
```php
<?php
$n = 29;
$prime = ($n >= 2);
for ($i = 2; $i * $i <= $n; $i++) {
    if ($n % $i == 0) { $prime = false; break; }
}
echo $prime ? "$n is prime" : "$n is not prime";
?>
```
**Memorise:** `$i * $i <= $n` (√n bound), `%` for divisibility, `break` on the first factor.

### D4 — Palindrome, number and string
```php
<?php
$n = 12321; $t = $n; $rev = 0;
while ($t > 0) {
    $rev = $rev * 10 + ($t % 10);
    $t = intdiv($t, 10);
}
echo ($rev == $n) ? "palindrome" : "not palindrome";

$s = "madam";
echo ($s === strrev($s)) ? "palindrome" : "not palindrome";
?>
```
**Memorise:** `$rev * 10 + digit` to build the reverse; `intdiv` to drop a digit; keep the original in a second variable.

### D5 — Armstrong number
```php
<?php
$n = 153; $t = $n; $sum = 0;
$p = strlen((string)$n);          // number of digits
while ($t > 0) {
    $d = $t % 10;
    $sum += $d ** $p;
    $t = intdiv($t, 10);
}
echo ($sum == $n) ? "Armstrong" : "not Armstrong";
?>
```
**Memorise:** the exponent is the **digit count**, not always 3; `**` for the power.

### D6 — Count vowels
```php
<?php
$s = "Saintgits College";
$v = "aeiouAEIOU";
$c = 0;
for ($i = 0; $i < strlen($s); $i++) {
    if (strpos($v, $s[$i]) !== false) { $c++; }
}
echo "Vowels = $c";
?>
```
**Memorise:** `!== false`, not `!= 0` — `strpos` returns `0` for `'a'`, which is falsy.

### D7 — Sort an associative array (student marks)
```php
<?php
$marks = ["Anu" => 88, "Rahul" => 72, "Diya" => 95];
asort($marks);                      // ascending by value, keys kept
foreach ($marks as $name => $m) { echo "$name: $m<br>"; }
arsort($marks);                     // descending
reset($marks);
echo "Topper: " . key($marks) . " (" . current($marks) . ")";
?>
```
**Memorise:** `asort`/`arsort` keep keys; plain `sort` destroys them; `reset` + `key` + `current` read the first pair.

### D8 — Unique strings
```php
<?php
function unique($arr) {
    $out = [];
    foreach ($arr as $s) {
        if (!in_array($s, $out, true)) { $out[] = $s; }
    }
    return $out;
}
print_r(unique(["php", "css", "php", "html"]));
?>
```
**Memorise:** `!in_array(...)` + `$out[] =` — the accumulate-if-absent pattern.

### D9 — Average and median
```php
<?php
function stats($a) {
    $n = count($a);
    if ($n == 0) { return [0, 0]; }
    $avg = array_sum($a) / $n;
    sort($a);
    $mid = intdiv($n, 2);
    $med = ($n % 2 == 1) ? $a[$mid] : ($a[$mid - 1] + $a[$mid]) / 2;
    return [$avg, $med];
}
list($avg, $med) = stats([10, 20, 30, 40]);
echo "Average $avg, Median $med";
?>
```
**Memorise:** `array_sum/count`; odd → middle, even → mean of the two middles; `intdiv` for the index.

### D10 — Partition by sign, pass-by-reference
```php
<?php
function partition($nums, &$pos, &$neg) {
    $pos = []; $neg = [];
    foreach ($nums as $n) {
        if ($n > 0)      { $pos[] = $n; }
        elseif ($n < 0)  { $neg[] = $n; }
    }
}
$p = []; $q = [];
partition([5, -3, 0, 8, -1], $p, $q);
echo implode(",", $p) . " | " . implode(",", $q);   // 5,8 | -3,-1
?>
```
**Memorise:** `&` on the parameter, not on the call; the function returns nothing — the outputs are the references.

### D11 — Most frequent word from a file
```php
<?php
$text = file_get_contents("input.txt");
$text = str_replace(":", " ", $text);
$words = preg_split("/\s+/", trim($text));

$count = [];
foreach ($words as $w) {
    if ($w === "") { continue; }
    $w = strtolower($w);
    $count[$w] = isset($count[$w]) ? $count[$w] + 1 : 1;
}

$best = ""; $max = 0;
foreach ($count as $w => $c) {
    if ($c > $max) { $max = $c; $best = $w; }
}
echo "$best appears $max times";
?>
```
**Memorise:** `str_replace(":", " ")` normalises the second delimiter; `$count[$word]++` is the frequency map; scan for the max afterwards.

### D12 — explode / implode round trip
```php
<?php
$csv = "Anu,88,Rahul,72";
$arr = explode(",", $csv);          // string -> array (4 elements)
$str = implode(" | ", $arr);        // array -> string
echo count($arr) . " pieces: " . $str;
echo (implode(",", $arr) === $csv) ? "round trip OK" : "broken";
?>
```
**Memorise:** `explode(delimiter, string)`; `implode(glue, array)` — delimiter/glue always **first**; they are inverses.

### D13 — Regex email + phone validation
```php
<?php
$email = "user@saintgits.org";
$phone = "9876543210";

if (preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
    echo "Email OK<br>";
} else { echo "Email invalid<br>"; }

if (preg_match("/^[0-9]{10}$/", $phone)) {
    echo "Phone OK";
} else { echo "Phone invalid"; }
?>
```
**Memorise:** anchors `^...$`, `\w` word char, `{10}` exactly ten, `\.` a literal dot; `preg_match` returns 1/0.

### D14 — Full registration form: validation + business logic
```php
<?php
$errors = [];
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name  = trim($_POST["name"] ?? "");
    $email = trim($_POST["email"] ?? "");
    $pass  = $_POST["password"] ?? "";

    if (empty($name))  { $errors[] = "Name required"; }
    if (empty($email)) { $errors[] = "Email required"; }
    if (empty($pass))  { $errors[] = "Password required"; }

    if ($name != "" && !preg_match("/^[A-Za-z ]+$/", $name)) {
        $errors[] = "Name: letters and spaces only";
    }
    if ($email != "" && !preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
        $errors[] = "Email format invalid";
    }

    // business logic: password policy
    if ($pass != "" && !(strlen($pass) >= 8
        && preg_match("/[A-Z]/", $pass) && preg_match("/[0-9]/", $pass))) {
        $errors[] = "Password: 8+ chars, 1 capital, 1 digit";
    }

    if (count($errors) == 0) {
        echo "Welcome, " . htmlspecialchars($name);
    }
}
?>
<form method="POST" action="">
  Name: <input type="text" name="name">
  Email: <input type="text" name="email">
  Password: <input type="password" name="password">
  <input type="submit" value="Register">
</form>
```
**Memorise:** the five stations (method → trim → validate → business rule → respond); `$errors[]` array + `count($errors) == 0`; `htmlspecialchars` on output.

---

## 5. 🔴 Night-before memorize sheet

| Item | Exact syntax / value to recall | Why it is asked |
|---|---|---|
| PHP tags | `<?php ... ?>` ; short echo `<?= $x ?>` | every program's first and last line (`3:L88`) |
| Variable | `$name = "Anu";` — `$` required, no type keyword | Q70, Q76 |
| Statement end | `;` after every statement | parse error otherwise |
| Concatenation | `.` and `.=` — **never** `+` | Q75, the #1 syntax trap |
| Strict equality | `"5" === 5` → `false`; `"5" == 5` → `true` | Q205, flagged by the deck (`3:L199`) |
| Exponent / remainder | `**` and `%`; `10 ** 2` = 100, `10 % 3` = 1 | Q78, Q91 |
| Casts | `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` | Q85, Q205 |
| Type inspectors | `gettype($v)`, `var_dump($v)`, `is_int()`, `is_string()` | Q68, Q88 |
| Array literal | `[10, 20, 30]` or `array(10, 20, 30)` | Q209a, Q213a |
| Associative key | `"name" => "Anu"` — `=>`, **not** `=` | Q218, `=>` is a syntax must |
| Append | `$arr[] = 40;` | Q209 |
| Object access | `$obj->method()` / `$obj->prop` — arrow, not dot | Q207, recap `3:L766` |
| Length / count | `strlen($s)` for strings, `count($arr)` for arrays | Q219, Q209 |
| Sort family | `sort`/`rsort` (renumber keys) · `asort`/`arsort` (keep keys) · `ksort` (by key) | Q82, Q218 |
| Pointer set | `reset` first · `end` last · `next` forward · `prev` back · `current` value · `key` key | Q81 |
| String slice | `substr($s, 0, 5)` → `"Saint"` | Q219, Q220 |
| Split / join | `explode(",", $s)` → array · `implode(" + ", $arr)` → string | Q89, Q213b |
| Regex test | `preg_match("/^\d{6}$/", $pin)` → 1 or 0 | Q74, Q208 |
| Five patterns | `/^[0-9]{10}$/` · `/^[\w.-]+@[\w.-]+\.[\w]+$/` · `/^[A-Za-z]+$/` · `/^\d{6}$/` · `/^[A-Za-z0-9]+$/` | verbatim table `3:L599–605` |
| GET / POST | `$_GET["f"]` URL · `$_POST["f"]` body · `$_REQUEST` merges | Q83, Q220b |
| Method check | `$_SERVER["REQUEST_METHOD"] == "POST"` | the guard in every form script (`3:L630`) |
| Presence / blank | `isset($_POST["f"])` vs `empty($_POST["f"])` — `empty("0")` is **true** | Q83, Q216a |
| Escape output | `htmlspecialchars($name)` | XSS, `3:L655` |
| Null coalescing | `$_POST["x"] ?? ""` | suppresses undefined-key warnings |
| Stop script | `exit()` / `die("msg")` — identical | Q71, Q214b |
| Function | `function add($a, $b) { return $a + $b; }` | Q73, Q206 |
| Default param | `function greet($name = "Guest")` | Q206b |
| By reference | `function inc(&$x) { $x++; }` | Q211, Q87 |
| Variadic | `function total(...$nums)` | Q206a |
| Class | `class S { public $n; function __construct($n){ $this->n = $n; } }` | Q207b, `3:L482` |
| Cookie | `setcookie("u","Anu",time()+3600)`; read `$_COOKIE["u"]`; delete `time()-3600` | Q84, Q215a (`4:L67–86`) |
| Session | `session_start(); $_SESSION["k"] = $v;` … `session_destroy();` | Q84 (`4:L102–124`) |
| Connect | `mysqli_connect("localhost","root","","db")` + `mysqli_connect_error()` | Q215b, Q216a |
| CRUD verbs | `CREATE TABLE` · `INSERT INTO t (cols) VALUES (...)` · `SELECT * FROM t` · `UPDATE t SET c=v WHERE ...` · `DELETE FROM t WHERE ...` | Q215b |
| Integer divide | `intdiv($a, $b)` | Q213b, Q217b |
| Sum of array | `array_sum($arr)` | Q210b, Q214a |

---

## 6. 📐 Diagram + figure index

`grep -n "Image Description" module3.md` returns 23 hits. **Only one is real content** — the rest are repeated slide furniture (PHP logo, `</>` code icon, "A" typography icon) that carries no information.

| md line | What the figure actually shows | Worth reproducing? |
|---|---|---|
| `3:L57` | **PHP request–response cycle**: three boxes across the top (Browser requests page.php → Web Server → PHP Engine runs the script), a green MySQL box under the server/engine, and a wide bar underneath labelled "Plain HTML sent back to Browser" | **Yes — draw this for any "how does PHP work" question** |
| `3:L59–70` | the same diagram's plain-text labels: "Browser Requests page.php", "Web Server", "PHP Engine Runs the script", "MySQL Database (if the script queries it)", "Plain HTML sent back to Browser" | use these exact five labels |
| `3:L1`, `22`, `50`, `79`, `96`*, `131`, `161`, `192`, `250`, `286`, `319`, `353`, `381`, `414`, `466`, `503`, `533`, `563`, `614`, `645`, `679`, `713`, `748` | slide furniture only — PHP oval logo, `</>` code-tag icon, "A" typography icon | no |

\*L96 is a plain-text label line inside the same slide, not a separate image.

**Tables in the deck worth reproducing verbatim in an answer.**

| Deck table | md range | Reproduce for |
|---|---|---|
| Data types (type / example / notes) | `3:L115–122` | Q68, Q77, Q88, Q203a |
| Common array functions (6 rows) | `3:L452–459` | Q82, Q207b, Q209b |
| Common regex patterns for validation (5 rows) | `3:L599–605` | Q74, Q208, Q216a |
| Cookies vs sessions quick reference | `4:L138–160` | Q84, Q215a (M4 deck) |
| Fetch styles (`fetch_assoc`/`array`/`row`/`object`) | `4:L385` | Q215b only if asked |

**Diagrams the deck does NOT contain** — draw these yourself, labelled "(standard)": the **operator precedence ladder** (no precedence table exists anywhere in `module3.md`; the only safe claim is `.` binds like `+`/`-`, so parenthesise); the **PHP array internal representation** (hash table of buckets — see §3.1.O); the **form → `$_POST` → validate → business logic → response** data flow (the deck gives it as five numbered steps at `3:L722–726`, no picture); the **client-side cookie vs server-side session** split (M4, `4:L27–53`).

---

## 7. Say-this-if-grilled defence lines

1. **"Why does `===` exist if `==` works?"** — Because `==` converts before comparing, so `"0" == false` and `"1" == "01"` are both true; `===` refuses to convert, so it is the only safe test when the *type* is part of the meaning, e.g. a PIN that arrives as a string.
2. **"Why is PHP called dynamically typed?"** — No type is written on the variable; the type travels with the value and is resolved at runtime, which is why `$x = 5;` then `$x = "five";` is legal (`3:L90`).
3. **"Why `=>` and not `=` in an array?"** — `=` is the assignment operator and would be parsed as an expression; `=>` is a distinct token that means "this key maps to this value". Writing `=` is a syntax error, not a silent bug.
4. **"Why `->` for objects but `.` for strings?"** — `.` is already taken by concatenation, so member access needed its own token; `->` does not overload by context, which keeps the parser unambiguous (`3:L477`).
5. **"Why does `sort()` lose my names?"** — Because `sort()` sorts values and **re-indexes** keys 0..n; the key→value pairing is deliberately discarded. `asort()` is the key-preserving version (`3:L456`).
6. **"Why is the browser never able to see my PHP?"** — The engine executes the file on the server and only the resulting HTML is written to the response; the source never enters the HTTP body (`3:L31`, `3:L72`).
7. **"Why `setcookie` before any HTML?"** — Cookies travel as HTTP **headers**, and headers must be sent before the body; any `echo` first triggers "headers already sent" (`4:L65`).
8. **"Why check `REQUEST_METHOD` instead of just reading `$_POST`?"** — On the first GET the fields do not exist, so an unguarded read produces undefined-key warnings and sometimes processes empty data; the guard makes one file serve both roles (`3:L630`).
9. **"Why `!== false` after `strpos`?"** — `strpos` returns `0` for a match at position zero, and `0` is falsy; a loose test rejects exactly the valid first-character case.
10. **"Why pass by reference at all?"** — `return` yields one value; when a function must produce two results (partition into positives/negatives) the only clean way is `&` parameters (`3:L370`).
11. **"Why is PHP considered slow?"** — It recompiles/re-executes per request rather than staying resident like a Java servlet; opcode caches (OPcache) mitigate it, and the trade is deployment simplicity — every shared host runs it (`3:L34–35`).
12. **"Why validate *and* sanitise? Isn't one enough?"** — They answer different questions: validation decides whether to accept the data at all, sanitising makes accepted data safe to *emit*; a well-formed name can still contain `<script>` (`3:L652–657`).

