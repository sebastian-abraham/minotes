# MODULE 3 — Introduction to PHP · Exam kit
> 20CST461 Web Technologies · Part A = 3 marks, Part B = 14 marks · 2 Part-A questions and 1 of 2 Part-B questions come from this module.
> Line refs: `3:L113` = `module3.md` line 113 · `4:L65` = Module 4 deck.

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

**Six themes.** Data types & variables (68, 70, 76, 77, 85, 88, 203a, 205a, 216b, 221b) · operators & expressions (78, 79, 85, 86, 87, 204b, 205b) · functions (73, 86, 87, 90, 206, 210, 211, 212, 214a, 221a) · arrays (80, 81, 82, 89, 207b, 209, 210, 211, 213a, 213b, 218) · strings & regex (74, 75, 89, 208, 219, 220) · forms & business logic (83, 84, 208, 215, 216a, 220b). Every 14-mark program is themes 3+4+5+6 welded together with an `if` and a loop.

---

## 2. Deep dive

### 2.1 What PHP is (`3:L27–43`, `3:L72`)
**What:** a **server-side** scripting language: `.php` sits on the server, the **PHP engine** executes it, plain HTML goes out; the visitor never gets the source (`3:L30–31`).
- Re-executed on **every** request → same file, different HTML = "dynamic" (`3:L42–43`).
- Free, open-source, any host, big ecosystem (WordPress, Laravel) (`3:L35`).
- No engine → every `.php` becomes a text file the browser downloads.

**Request–response cycle** (`3:L55–72`, diagram `3:L57`):
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
**Small proof** (`3:L94–102`): view-source shows `Welcome to Saintgits`, no PHP.
```php
<?php
$college = "Saintgits";
echo "Welcome to $college";
?>
```

### 2.2 Syntax rules — five rules that govern every line (`3:L84–92`)
| Rule | Meaning |
|---|---|
| `<?php ... ?>` | **Tags** delimit PHP; anything outside is literal HTML. |
| `$name` | Every **variable** starts with `$`; no type keyword. |
| `;` | Every **statement** ends with a semicolon. |
| `//` `#` `/* */` | Three comment styles; `#` is PHP-only (standard). |
| case | Keywords **case-insensitive**; variables **case-sensitive** (standard). |

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
**Trap:** a dropped `;` → `syntax error, unexpected ...`; `$Name` for `$name` gives an undefined variable.

### 2.3 Output — `echo`, `print`, `<?=` (`3:L91`)
**What:** the only channel from the engine into the HTML.
- `echo` — construct: comma-separated list, returns nothing.
- `print` — expression: one value, returns `1`.
- `<?= $x ?>` = `<?php echo $x; ?>` (standard, not in your deck).
- No `document.write`, no template engine — `echo`/`print` is the only channel to the browser.

```php
<?php
echo "Hello", " ", "World";   // echo takes a list
print "Hello";                 // print takes one value, returns 1
?>
<p><?= $name ?></p>            <!-- short echo tag -->
```

### 2.4 Variables and naming rules (`3:L88–90`)
- `$` + letter/underscore + letters/digits/underscores, never a digit first (`3:L88–90`).
- **Dynamically typed**: no type keyword; the type belongs to the value, not the variable (`3:L90`).
- `$x = 5;` then `$x = "five";` is legal.

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
**Trap:** a wrong kind of value is caught at runtime, not compile time — hence `gettype()`/`var_dump()` (`3:L124`).

### 2.5 The data types — all eight (`3:L113–122`)
**What:** the deck's table names six; PHP has eight in three families.
| # | Type | Family | Example | Note |
|---|---|---|---|---|
| 1 | `int` | scalar | `$age = 21;` | whole numbers |
| 2 | `float` (double) | scalar | `$fee = 499.50;` | decimal numbers |
| 3 | `string` | scalar | `$name = "Anu";` | single or double quotes (`3:L119`) |
| 4 | `bool` | scalar | `$active = true;` | `true` / `false` |
| 5 | `array` | compound | `$m = [88, 92];` | ordered list **or** key→value map |
| 6 | `object` | compound | `$s = new Student("Rahul");` | instance of a class (`3:L471–495`) |
| 7 | `NULL` | special | `$x = null;` | explicitly "no value" |
| 8 | `resource` | special | `$f = fopen("a.txt","r");` | file or DB handle (standard, not in your deck) |

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
**Trap:** every operator depends on the operand type — `+` adds, `.` joins, `==` converts — so every output-prediction question is a type question.

### 2.6 Inspecting a value (`3:L124`)
- `gettype($v)` → type name as a **string**; `var_dump($v)` → **type and value**, recursive for arrays/objects.
- `print_r()` — array-friendly variant (standard).
```php
<?php
$x = "10";
echo gettype($x);    // string
var_dump($x);        // string(2) "10"
var_dump((int)$x);   // int(10)
?>
```
**Trap:** `echo` prints `10` for both `"10"` and `10`; only `var_dump` shows which.

### 2.7 Type juggling and casting (`3:L136–153`)
**What:** PHP converts types automatically, and you can force a conversion.
- Casts: `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` (`3:L140`); also `intval()`, `floatval()`, `strval()`, `boolval()` (`3:L141`).
- `settype($var, "integer")` converts **in place** (`3:L142`); `is_int()`, `is_string()`, `is_array()` test without converting (`3:L143`).
- Juggling: `"10" + 5` → 15; `"5" . 3` → `"53"`; `"5 apples" + 2` → 7, but `"apples" + 2` → `TypeError` in PHP 8; `"abc" == 0` true in PHP 7, false in PHP 8.
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
**Trap:** form data is **always a string** (`"25"`); `(int)$x` is not validation.

### 2.8 Operators I — arithmetic and assignment (`3:L170–171`)
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
**Trap:** `/` always returns a float (`10/4` → `2.5`), unlike C; `%` casts floats to int first.

### 2.9 Operator II — the dot (`3:L172`, recap `3:L770`)
**What:** `.` concatenates, `.=` appends. Java/JS use `+`; PHP uses `.` — the #1 syntax slip for a C/Java student.
```php
<?php
$first = "Web";
$last  = "Programming";
echo $first . " " . $last;   // Web Programming
$first .= " Tech";           // "Web Tech"
?>
```
**Trap:** `"a" + "b"` → PHP 8 `TypeError: Unsupported operand types: string + string`.

### 2.10 Operator III — `==` vs `===` (`3:L199–203`, recap `3:L760`)
**What:** `==` **loose** (converts, then compares); `===` **strict** (value **and** type); same for `!=` / `!==`. The deck calls it "one of PHP's most exam-relevant quirks" (`3:L199`).
```php
<?php
var_dump("5" == 5);    // true   — "5" converted to 5
var_dump("5" === 5);   // false  — string vs int
var_dump(0 == "abc");  // false  (PHP 8+)
var_dump(null == false); // true (standard, not in your deck)
var_dump(0 == "");     // true  in PHP 7, false in PHP 8 (standard)
?>
```
**Trap:** `"0" == false` is `true`, so an empty-looking PIN passes an emptiness check; before PHP 8 `0 == "abc"` was true.

### 2.11 Operator IV — relational, logical, increment, ternary (`3:L203–204`)
- Relational `< > <= >= != !==`; logical `&& || !`, plus low-precedence `and`, `or`, `xor` (standard).
- `++$i` add-then-use, `$i++` use-then-add, `--` likewise (standard; deck uses `$i++` at `3:L307` unnamed).
- Ternary `cond ? a : b`.
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
**Trap:** `&&` short-circuits, so `isset($a) && $a > 0` is safe; bitwise `&` evaluates both sides.

### 2.12 Expressions (`3:L173`)
**What:** anything producing a value — literal, variable, operator on expressions, function call, assignment (itself evaluates to 5), ternary. A statement = expression + `;` + an effect.
```php
<?php
$x = 5;              // assignment expression, value 5
$y = ($x + 3) * 2;   // 16
$z = $x > 3;         // true  — a comparison IS an expression
echo $y + $z;        // 17  — true juggles to 1
?>
```
**Precedence** (standard, not in your deck): `**` → `++/--` → `!` → `* / %` → `+ -` → `.` → `< <= > >=` → `== != === !==` → `&&` → `||` → `?:` → `=` → `and` → `or`.
**Trap:** `.` binds like `+ -`, so `"Total: " . 5 + 3` is `("Total: " . 5) + 3` → 8. Write `"Total: " . (5 + 3)`.

### 2.13 Flow control functions — `exit()`, `die()`, `return` (`3:L227–243`)
1. **`exit()`** — stops the script **immediately**; optional string (printed) or int status.
2. **`die()`** — exact **alias**, used after a fatal error: `die("Connection failed");` (`3:L235`).
3. **`return`** — value back **and** stops the function (`3:L239`); at file scope ends the include (standard).
4. Grouped: all three decide continue, branch, or stop (`3:L243`).
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
**Trap:** `return` inside a function leaves only the function; the rest of the page still runs.

### 2.14 Control statements (`3:L255–278`)
- `if (cond) {...} elseif (cond) {...} else {...}` — any boolean expression.
- `switch ($var) { case v: ...; break; default: ...; }` — one variable against **fixed values**, loose `==`; `break` prevents **fall-through**, `default` catches the rest (`3:L261–262`).
- `match` (PHP 8+) — stricter, returns a value: `$g = match(true) { $m>=90 => "A", default => "C" };` (standard).
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
**Trap:** no `break` → Monday's code runs inside Tuesday's case; `switch` has no ranges.

### 2.15 Loops (`3:L291–298`)
| Loop | Shape | When |
|---|---|---|
| `for (init; cond; step)` | known count | 1..n |
| `while (cond)` | test **before** | may run **zero** times |
| `do {...} while (cond)` | test **after** | always **at least once** |
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
**Trap:** `for ($i=0; $i<count($a); $i++)` breaks on associative arrays — a PHP array is an ordered map, not a C array.

### 2.16 Functions — declare, call, return (`3:L328`)
- `function name($param, ...) { ... return $value; }`; declarations **hoisted** (`3:L329`).
- `return` sends a value and exits (`3:L330`); no `return` → `NULL` (`3:L331`).
- `echo` instead of `return` → value is `NULL`, output at the call site (`3:L340–343`).
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
**Trap:** a typo in the *definition* only explodes when the call runs.

### 2.17 Defaults, scope, `global`, `static` (`3:L358–366`)
1. **Default parameter** — `function greet($name = "Guest")`: omitted → default (`3:L362`); defaults **after** required parameters (standard).
2. **Scope** — variables made inside a function are **local**; outside ones do not exist inside (`3:L366`).
3. **`global $x;`** binds the outer variable (`3:L366`).
4. **`static $x = 0;`** survives **between** calls, initialised once (standard).
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
**Trap:** `function f($a = 1, $b)` errors; explicit `null` does **not** trigger the default.

### 2.18 Pass by value vs reference, variadics (`3:L370`, `3:L374`)
- Default **by value**: a copy; the caller's variable is untouched.
- `&$param` **by reference**: an alias, assignments change the original (`3:L370`).
- `function total(...$nums)` — **variadic**, collects any number of arguments (`3:L374`).
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
**Trap:** omit `&` and Q211's two output arrays stay empty — the most common lost-mark error here.

### 2.19 Indexed arrays (`3:L388–393`)
- **Ordered list**, integer keys from 0; `[10, 20, 30]` or `array(10, 20, 30)` (`3:L390`).
- `$arr[0]` access; `$arr[] = 40;` appends at the next free index; `count($arr)` length (`3:L391–393`).
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

### 2.20 Associative and multidimensional arrays (`3:L423–426`)
- Named keys: `["name" => "Anu"]`, read `$stu["name"]`; `=>` maps key→value — `=` will not work.
- **Multidimensional** = array of arrays (`3:L425`); `foreach ... as $k => $v` exposes both (`3:L426`).
- Named keys are exactly what `mysqli_fetch_assoc()` returns in Module 4 — that is why the module insists on `=>`.
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
**Trap:** order is **insertion order**, never sorted order.

### 2.21 Array functions, sort family, internal pointer (`3:L452–459`)
| Function | Purpose |
|---|---|
| `count($arr)` | number of elements |
| `array_push($arr, $val)` | add to the end — same as `$arr[] = $val` |
| `sort($arr)` / `rsort($arr)` | ascending / descending, **re-indexing keys** |
| `array_map($fn, $arr)` | apply a function to every element |
| `array_filter($fn, $arr)` | keep elements passing a test |
| `in_array($val, $arr)` | does the value exist? |

- Key-preserving sorts (standard, needed for Q82/Q218): `asort()` by value, `arsort()` reverse, `ksort()`/`krsort()` by key, `usort()` by callback.
- Pointer: `reset()` first, `end()` last, `next()` forward, `prev()` back, `current()` value, `key()` key; `false` past the ends.
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
**Trap:** `sort()` **renumbers** keys — a sorted marks array loses who got what; `asort()` keeps the pairing.

### 2.22 Objects and classes (`3:L475–478`)
- `class Name { ... }` = blueprint of **properties** + **methods** (`3:L475`); `new ClassName()` = instance (`3:L476`).
- `->` for members, **never** `.` (`3:L477`, recap `3:L766`); `__construct()` runs on creation (`3:L478`); `$this` = current object (standard, implied `3:L486`).
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
**Trap:** `$s.name` is a syntax error, not concatenation.

### 2.23 Strings and the function table (`3:L512–515`, `3:L542–545`)
- **Double quotes interpolate** `$variables`, `\n`, `\t`; **single quotes are literal** (standard — it changes nearly every program's output).
| Function | Does | Example → result |
|---|---|---|
| `strlen($s)` | length in bytes | `strlen("Saintgits")` → 9 |
| `strtoupper($s)` / `strtolower($s)` | change case | `"SAINTGITS"` / `"saintgits"` |
| `trim($s)` | strip whitespace both ends | `"  Anu  "` → `"Anu"` |
| `substr($s, start, len)` | slice | `substr("Saintgits",0,5)` → `"Saint"` |
| `str_replace($a,$b,$s)` | find & replace | `"World"`→`"PHP"` |
| `explode($delim,$s)` | string → array | `"HTML,CSS,JS"` → 3 elements |
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

### 2.24 Regular expressions (`3:L570–575`)
**What:** PHP supports **PCRE** (Perl-Compatible Regular Expressions) (`3:L570`).
- `preg_match($pattern, $string)` → `1` found, `0` not, `false` error — a *test*, not an extractor (`3:L572`).
- `preg_replace($pattern, $replacement, $string)` — regex find-and-replace (`3:L573`).
- `preg_split($pattern, $string)` — split on a regex delimiter (`3:L574`); patterns wrapped in `/.../` (`3:L575`).
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
**Trap:** without `^`/`$` the check degrades to "contains" — `preg_match("/[0-9]{10}/", "1234567890123")` wrongly passes.

### 2.25 The five validation patterns — memorise verbatim (`3:L599–605`)
| Pattern | Matches | Used for |
|---|---|---|
| `/^[0-9]{10}$/` | exactly 10 digits | phone number |
| `/^[\w.-]+@[\w.-]+\.[\w]+$/` | basic email shape | email |
| `/^[A-Za-z]+$/` | letters only | name field |
| `/^\d{6}$/` | exactly 6 digits | PIN code |
| `/^[A-Za-z0-9]+$/` | letters and digits only | username |

Glossary (`3:L607`): `\d` digit · `\w` word char · `{n}` exactly n · `^` start · `$` end · `+` one or more · `*` zero or more · `?` optional · `[abc]` class · `.` any char · `\.` literal dot (standard).
```php
<?php
var_dump(preg_match("/^[0-9]{10}$/", "9876543210")); // 1
var_dump(preg_match("/^[0-9]{10}$/", "98765"));      // 0
var_dump(preg_match("/^\d{6}$/", "682001"));         // 1
var_dump(preg_match("/^[A-Za-z]+$/", "Anu K"));      // 0 — space not allowed
?>
```
**Trap:** `/^[A-Za-z]+$/` rejects "Anu K" — the space must be in the class.

### 2.26 Superglobals (`3:L621–630`)
| Superglobal | Carries | Notes |
|---|---|---|
| `$_GET["f"]` | query string (`method="GET"`) | visible in URL, bookmarkable, length-limited, never passwords |
| `$_POST["f"]` | request body (`method="POST"`) | not in URL, no practical size limit |
| `$_REQUEST["f"]` | GET + POST + COOKIE merged | ambiguous — deck: "less precise, usually avoid" (`3:L625`) |
| `$_SERVER["REQUEST_METHOD"]` | `"GET"` or `"POST"` | how one script knows it was submitted (`3:L630`) |
| `$_FILES`, `$_SESSION`, `$_COOKIE`, `$_ENV` | the rest of the set | `$_SESSION`/`$_COOKIE` matter in M4 |

`isset($_POST["field"])` = "was this key submitted?" (`3:L626`); "is it empty?" is `empty()`.
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
**Trap:** no `REQUEST_METHOD` guard → the first empty GET warns on every field.

### 2.27 Validating vs sanitising (`3:L652–657`)
- **Validate** = well-formed? `trim()`, `empty()`, `preg_match()`.
- **Sanitise** = safe to emit? `htmlspecialchars()` turns `<`, `>`, `&`, `"` into entities (`3:L655`).
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
**Trap:** `empty("0")` is **true** — a real bug on a marks field.

### 2.28 Business logic (`3:L686–691`)
**What:** the **application rule applied to already-validated data**, kept separate from validation (`3:L686`).
- Validation: "well-formed?"; business logic: "what should the app DO?" (`3:L688–689`) — e.g. `$marks = (int) ($_POST["marks"] ?? 0);` (`3:L695`).
- Examples: eligibility, fee, grade (`3:L691`); separation keeps code readable and testable (`3:L690`).
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

### 2.29 The whole pipeline (`3:L722–726`)
Five steps: (1) check the method (2) read & trim (3) validate (4) business logic (5) respond — M4 replaces (5) with a DB write (`3:L726`).
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
**Trap:** each station guards the next. Skeleton of Q208, Q216, Q220b.

---

## 3. Answer bank

> 3 marks = 3 numbered points, no preamble. 14 marks = code + explanation + a labelled table/diagram where asked. First line is already a point.

### 3.1 3-mark answers (Part A)

#### A. Data types — MASTER ANSWER (answers Q68, Q77, Q88; also feeds Q203a)
1. **Definition** — the type is the kind of value, which decides the legal operations (`3:L90`).
2. **Eight types** — `int` `$age = 21;` · `float` `$fee = 499.50;` · `string` `$name = "Anu";` · `bool` `$active = true;` · `array` `$m = [88, 92];` · `object` `new Student("Rahul")` · `NULL` `$x = null;` · `resource` `fopen("a.txt","r")` (last one standard).
3. **Inspect** — `gettype($v)` returns the type name as a string; `var_dump($v)` prints type and value (`3:L124`).
```php
<?php
$age = 21; $fee = 499.50; $name = "Anu";
$ok = true; $m = [88, 92]; $x = null;
echo gettype($age);   // integer
var_dump($fee);       // float(499.5)
?>
```
*Q68 wants one example each — keep this order and the examiner ticks eight times. Q77 drops the inspection point.*

#### B. Variables — MASTER ANSWER (answers Q70, Q76)
1. **Definition** — a named memory slot; `$` + letter/underscore + letters/digits/underscores, never a digit first (`3:L88–89`).
2. **No declaration, only assignment** — `$name = "Anu";` both declares and initialises; there is no `int x;`.
3. **Dynamic, scoped, case-sensitive** — type follows the value (`3:L90`, `3:L758`); locals are function-scoped, `global $x;` reaches out (`3:L366`); `$Name` ≠ `$name`.
```php
<?php
$college = "Saintgits";   // string
$year = 2026;             // int
$fee = 49999.50;          // float
echo "Welcome to $college, year $year";
?>
```

#### C. Types of operators (Q78)
1. **Arithmetic** — `+ - * / % **`; `**` exponent, `/` always float, `%` integer remainder (`3:L170`).
2. **Assignment and string** — `= += -= *= /= .=`; `.` joins, `.=` appends, `+` never joins text (`3:L171–172`).
3. **Comparison and logical** — `== === != !== < > <= >=` (`==` converts, `===` does not); `&& || !` (`3:L201–204`). Add `++`/`--` and `?:` if a 4th slot is free.
```php
<?php
$a = 10; $b = 3;
echo $a % $b;              // 1
$s = "Total: "; $s .= 8;   // "Total: 8"
var_dump("5" === 5);       // false
?>
```

#### D. `srand()` vs `rand()` (Q79)
1. **`rand()`** — pseudo-random integer; `rand()` → 0 to `getrandmax()`, `rand($min, $max)` → inclusive range (standard, not in your deck).
2. **`srand()`** — **seeds** the generator, returns no random number; the same seed reproduces the same sequence.
3. **Use** — `srand(time())` or `srand((int) microtime(true))` for variety, `srand(42)` for reproducible tests; since PHP 4.2 `rand()` seeds itself, so `srand()` is only for fixed sequences (standard).
```php
<?php
srand(42);              // fix the sequence
echo rand(1, 100);      // always the same number for seed 42
echo rand(1, 100);
?>
```

#### E. Type conversion (Q85; also answers Q205a)
1. **Implicit (juggling)** — PHP converts when the context demands it: `"10" + 5` → 15 because `+` needs numbers (`3:L138`).
2. **Explicit casts** — `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` (`3:L140`), or `intval()`, `floatval()`, `strval()`, `boolval()` (`3:L141`).
3. **In place and test** — `settype($var, "integer")` converts the variable itself; `is_int()`, `is_string()`, `is_array()` test without converting (`3:L142–143`).
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
1. **Store** — the operands live in variables, `$a = 15;` and `$b = 27;`.
2. **Add** — `+` performs arithmetic because both operands are numeric.
3. **Print** — `echo` with double quotes interpolates the variables into the HTML.
```php
<?php
$a = 15;
$b = 27;
$sum = $a + $b;
echo "Sum of $a and $b is $sum";   // Sum of 15 and 27 is 42
?>
```
*From a form instead: `(float)$_GET["num1"]` — full script at §3.2.Q220.*

#### G. Building blocks with an addition function (Q86)
1. **Name the blocks** — variables, data types/operators, functions: the mark scheme's own vocabulary.
2. **`add()`** — packages `$x + $y` behind `return`, so `add(12,30)` is an expression worth 42.
3. **`echo`** — sends the result into the HTML; `<?php ?>` tags, `$` on every name, `;` on every statement.
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

#### H. Sum and difference via a function (Q87)
1. **Constraint** — `return` yields one value, so two results need **pass-by-reference** parameters (`3:L370`).
2. **Signature** — `function sumDiff($a, $b, &$sum, &$diff)` writes into the caller's variables.
3. **Alternative** — `return ["sum" => $a+$b, "diff" => $a-$b];` then read `$r["sum"]`.
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

#### I. Flow control functions + pos/neg/zero (Q71; also answers Q214b)
1. **`if/elseif/else`** — a block runs only when its condition is true, exactly as in C (`3:L231`).
2. **`exit()` / `die()`** — stop the script immediately; `die()` is an alias, used after a fatal error (`3:L235`).
3. **`return`** — sends a value back and stops that function (`3:L239`); all three decide continue/branch/stop (`3:L243`).
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
1. **`if-else`** — any boolean expression per branch: ranges, `&&`, function calls (`3:L259–260`).
2. **`switch`** — one variable against fixed constant values; the subject is evaluated **once**, then control jumps to the label.
3. **`break` and `default`** — without `break` control **falls through**; `default` catches everything unmatched (`3:L261–262`).
```php
<?php
$m = 82;
if ($m >= 90) echo "A"; elseif ($m >= 75) echo "B"; else echo "C";   // range → if

switch ($m) { case 100: echo "Perfect"; break; default: echo "Scored"; } // value → switch
?>
```

#### K. Functions + `add()` (Q73; overlaps Q206 and Q214a)
1. **Definition** — a named, reusable block that may take parameters and may return a value (`3:L328`).
2. **Facts to quote** — declarations are **hoisted**; `return` exits immediately with a value; no `return` → `NULL` (`3:L329–331`).
3. **Point out** — `add()` prints nothing; `echo` at the call site prints the value — that separation is the reusability.
```php
<?php
function add($a, $b) {
    return $a + $b;
}
$result = add(25, 17);
echo "Sum = " . $result;    // Sum = 42
?>
```

#### L. Functions + factorial (Q90)
1. **Mechanics** — definition, parameters, `return`, hoisting, `NULL` when there is no return (`3:L324–331`).
2. **The rule** — `n! = n × (n-1) × ... × 1`, and `0! = 1` by definition.
3. **Write the iterative one** — accumulator starts at 1, loop to `$n`, return; recursive form on one line if space allows.
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
*Recursive: `return ($n <= 1) ? 1 : $n * factorial($n - 1);` — same result, and proves functions may call themselves.*

#### M. Role of regular expressions (Q74)
1. **Definition** — a pattern in a mini-language describing a set of strings; PHP implements PCRE (`3:L570`).
2. **Three functions** — `preg_match` tests (1/0/false), `preg_replace` find-and-replace, `preg_split` splits (`3:L572–575`).
3. **Why string processing needs it** — plain functions match fixed substrings; regex expresses *shape* ("exactly 10 digits") (`3:L599–607`).
```php
<?php
$email = "user@saintgits.org";
if (preg_match("/^[\w.-]+@[\w.-]+\.[\w]+$/", $email)) {
    echo "Valid email";
}
?>
```
*Delimiters `/.../`; `^`/`$` anchor the whole string, `\d` digit, `\w` word character, `{n}` exactly n times (`3:L607`).*

#### N. Concatenate two strings, uppercase result (Q75)
1. **Join** — `.` is the concatenation operator; `+` cannot join strings in PHP (`3:L172`).
2. **Case** — `strtoupper($s)` returns a new uppercase copy; it does not modify `$s` in place.
3. **Shorthand** — `.=` appends and assigns: `$joined .= "!";` — worth one line for the extra mark.
```php
<?php
$first = "web";
$second = "programming";
$joined = $first . " " . $second;      // concatenation with .
$upper  = strtoupper($joined);         // WEB PROGRAMMING
echo "Result: " . $upper;
?>
```

#### O. Internal representation of PHP arrays (Q80)
1. **Structure** — every array, indexed or associative, is an **ordered hash table of buckets**: key, value (`zval`), next-bucket pointer preserving insertion order (standard, not in your deck; deck asserts behaviour at `3:L121`, `3:L423`).
2. **Consequences** — one type covers both kinds; integer keys auto-assign as highest+1, so `$a[] = x` needs no counter (`3:L392`); order preserved, `foreach` deterministic (`3:L298`); a value is `zval`, so one array mixes `88`, `"Anu"`, `true`; keys unique — assigning an existing key overwrites.
3. **Say it** — "because it is a hash table, key lookup is O(1) and the order is insertion order, not sorted order."
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

#### P. `next`, `reset`, `prev` (Q81)
1. **Pointer** — every array carries an internal cursor on one element (standard, not in your deck; `3:L450–459` lists no pointer functions).
2. **`reset()`** first, **`end()`** last (both return that value); **`next()`** forward, **`prev()`** back (both return the new current value).
3. **Edges** — `false` past either end; `current()` reads the value without moving, `key()` its key; `foreach` uses the same pointer.
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
1. **`sort()` / `rsort()`** — by **value**, ascending / descending, **re-numbering** keys 0,1,2 (`3:L456`).
2. **Key-preserving** — `asort()` by value, `arsort()` reverse, `ksort()`/`krsort()` by key, `usort($arr,$cmp)` by callback (standard).
3. **Exam point** — never `sort()` an associative array whose keys matter; the names are destroyed, so use `asort()`.
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
1. **Mechanism** — `<form method action>` fields arrive pre-parsed in `$_GET` (query string) or `$_POST` (body) (`3:L621–624`).
2. **Detection** — `$_SERVER["REQUEST_METHOD"]` lets one file render *and* process; `isset($_POST["field"])` checks a field (`3:L626–630`).
3. **Pipeline** — method → `trim()` → validate (`empty`, `preg_match`) → business logic → respond (`3:L722–726`).
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
1. **Problem** — HTTP is **stateless**; the server keeps nothing between requests, so it cannot tell two requests are one visitor.
2. **Cookies (client)** — `setcookie("name","value",time()+3600)`, read `$_COOKIE["name"]`, delete with a past expiry; **before any output** because it is a header (`4:L63–88`); ~4 KB, user-editable, never secrets (`4:L73`).
3. **Sessions (server)** — `session_start()` issues a session-ID cookie, data in `$_SESSION["key"]` until `session_destroy()` (`4:L102–124`); sessions for login state, cookies for non-sensitive prefs (`4:L136–160`).

#### T. `explode()` vs `implode()` (Q89; also answers Q213b and Q221b)
1. **`explode($delimiter, $string)`** — splits a string at every delimiter, returns an **array** (`3:L544`).
2. **`implode($glue, $array)`** — joins elements into one string with the glue between them (`3:L545`).
3. **Inverses** — `implode(",", explode(",", $s))` returns `$s`; the standard way to store a list in one DB column.
```php
<?php
$parts  = explode(",", "HTML,CSS,JS");   // array of 3
$joined = implode(" + ", $parts);        // "HTML + CSS + JS"
echo count($parts) . " subjects: " . $joined;
?>
```

#### U. Prime check (Q91)
1. **Logic** — below 2 is not prime; otherwise test divisibility by 2 … √n; `%` == 0 means composite.
2. **Why `$i * $i <= $n`** — a factor above √n must pair with one below it: fewer iterations, same answer.
3. **Flag and break** — `$isPrime` starts `true` so the loop only has to disprove it; `break` at the first factor; ternary prints the verdict.
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

---

### 3.2 14-mark answers (Part B)

#### Q203 — Building blocks (6) + rectangle area script (8)
**Structure (marks):** (a) 6 = tags, variables + naming, data types table, operators/expressions, `echo`/output, functions — one mark each. (b) 8 = program 5 + line explanation with `gettype()`/`var_dump()` 3.
**Answer:**
- (a) **Tags** `<?php ... ?>`, HTML outside untouched (`3:L88`) · **variables** `$`-names, created by assignment, no type keyword (`3:L89`) · **data types** eight, decided at runtime (`3:L90`, `3:L113–122`) · **operators/expressions** `+ - * / % **`, `= += .=`, `.`, `== ===`, `&& || !` (`3:L170–173`) · **output** `echo`/`print` (`3:L91`) · **functions** `function n($p){ return $v; }`, hoisted, `NULL` without `return` (`3:L328–331`). Every statement ends `;`.
- (b)
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
- Explanation: float × int → **juggling** promotes to float, so `$area` is `float(100)`; `gettype()` prints the type string, `var_dump()` type + value (`3:L124`); `.` concatenates, `+` adds (`3:L172`).
**Traps:**
- `echo $length + $breadth;` **adds** (20.5) instead of printing both; `gettype()` without `echo` prints nothing.
- A missing `;` on an assignment line.

#### Q204 — switch day-of-week (10) + expressions (4)
**Structure (marks):** (a) 10 = definition/use 3 + the 1–7 script 5 + `break`/`default` 2. (b) 4 = expression definition 1 + evaluation/precedence 1 + types with examples 2.
**Answer:**
- (a) `switch` evaluates the subject **once**, then jumps to the matching `case`; `break` leaves the switch, without it control **falls through**; `default` is the catch-all (`3:L259–262`).
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
- `default` runs only when nothing matched — input outside 1–7, or non-numeric after the cast; omit it and input `9` leaves `$name` undefined.
- (b) **Expression** = any construct producing a value: literal, variable, operator on expressions, call, assignment (`3:L173`). Order: `**` → `* / %` → `+ -` → comparison → `&&` → `||` → `?:` → `=` (standard; no deck table). Types: arithmetic `$a + $b`, string `$first . $last`, assignment `$x = 10` (value 10), comparison `$a > $b`, logical `$ok && $active`, ternary `$m >= 50 ? "Pass" : "Fail"`. A comparison *is* an expression — hence it fits in `if (...)`.
**Traps:**
- No `break` → Tuesday prints Monday's text too; claiming `switch` supports ranges (that is `if`'s job).
- `switch` compares with loose `==`, so `"1"` matches `case 1` — convenient here, dangerous elsewhere.

#### Q205 — Type juggling/casting (4) + operators (10)
**Structure (marks):** (a) 4 = juggling + example 2, casting / cast list / `settype` 2. (b) 10 = three operator families ~3 marks each + 1 summary.
**Answer:**
- (a) **Juggling** = automatic conversion when a context needs a type: `"10" + 5` → 15, `"5" == 5` → `true` (`3:L138`). **Casting** = forced: `(int) (float) (string) (bool) (array)` (`3:L140`), `intval()`/`floatval()`/`strval()`/`boolval()` (`3:L141`), `settype($var,"integer")` in place (`3:L142`). Casting wins: `(int)"12abc"` is 12, predictable; juggling hides errors.
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
- (b) **Arithmetic** `+ - * / % **` (`10 % 3`→1, `10 ** 2`→100, `10 / 4`→2.5) · **assignment** `= += -= *= /= .=` · **string** `.` `.=`, never `+` · **comparison** `==` (converts) vs `===` (value + type), `!= !== < > <= >=` (`3:L201–203`) · **logical** `&& || !`, short-circuit (`3:L204`) · **increment** `$i++` use-then-add, `++$i` add-then-use · **ternary** `cond ? a : b`. Every operator returns a value — that is what makes expressions composable.
**Traps:**
- `$s = "Total: " . 5 + 3;` — `.` and `+` share precedence, left to right, so parenthesise.
- Saying `==` "is the same as" `===` (it is not — the deck's flagged quirk, `3:L199`); `%` on floats casts to int.

#### Q206 — Functions (7) + default parameters (7)
**Structure (marks):** definition/mechanics 3 + example function 4; then default rule 2 + code 3 + why useful 2.
**Answer:**
- (a) **Function** = named reusable block: `function name($p1, $p2) { statements; return $value; }` (`3:L328`); hoisted (`3:L329`); `return` exits with a value (`3:L330`); no `return` → `NULL` (`3:L331`); `echo`-only → `NULL` plus output at the call site.
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
- (b) **Default parameter** `$name = "Guest"`: omitted → default, supplied → wins (`3:L362`); defaults **after** required parameters (standard). Uses: optional greetings, formatting flags, limits.
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
- One function replaces a family of overloads — PHP has no overloading (standard).
**Traps:**
- `function f($a = 1, $b)` errors; explicit `null` does **not** trigger the default (only omission does).
- "Returns `NULL`" is not "returns nothing" — the caller can still `var_dump()` the `NULL`.

#### Q207 — Control statements (8) + arrays (6)
**Structure (marks):** 8 = if/elseif/else 2, switch 2, loops 3, break/continue 1. 6 = array definition + three kinds 3, functions 2, example 1.
**Answer:**
- (a) `if/elseif/else` — first true wins (`3:L259`). `switch/case/break/default` — one variable against constants, evaluated once; `break` stops fall-through, `default` catches the rest (`3:L260–262`). Loops: `for` known count, `while` pre-test, `do...while` post-test, `foreach`/`as $k => $v` arrays (`3:L295–298`, `3:L762`). `break` exits, `continue` skips (standard).
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
- (b) **Array** = ordered map key→value: int keys indexed, string keys associative, arrays of arrays multidimensional (`3:L388`, `3:L423–425`). Create `[10,20,30]`, `array(10,20,30)`, `["name"=>"Anu"]`, `$a[] = 5`. Functions `count`, `array_push`, `sort`/`rsort`, `asort`/`ksort`, `array_map`, `array_filter`, `in_array` (`3:L452–459`). Walk with `foreach`; `count()` is the only safe bound.
```php
<?php
$marks = ["Anu" => 88, "Rahul" => 72];
foreach ($marks as $name => $m) { echo "$name scored $m<br>"; }
echo "Students: " . count($marks);
?>
```
**Traps:**
- `for` over an associative array (`$arr[0]` does not exist); `sort()` on a named array destroys the names (`3:L456`).
- `while ($i < 3)` with no increment is an infinite loop — the examiner looks for the increment.

#### Q208 — User registration system with regex validation (14)
**Structure (marks):** form 2, reading + trimming 2, regex validation 4, business logic + messages 4, sanitised output + completeness 2.
**Answer:**
- The five-step pipeline (`3:L722–726`) with three regex checks (`3:L599–605`). Validation = well-formed; business logic = what the app does with it (`3:L686–689`) — here the password policy and the message.
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
- Beside the code: the `REQUEST_METHOD` guard makes one file render on GET and process on POST; `trim()` + `??` strip whitespace and suppress the warning; `!preg_match()` is the failure test; errors collect in an **array** and render as a list instead of `die()`, so all problems show at once; `htmlspecialchars()` stops injected HTML executing.
**Traps:**
- `die()` after the first error — you lose the other messages and the form.
- Echoing `$name` unescaped (XSS); `/^[A-Za-z]+$/` then rejecting "Anu K" — the space must be in the class.

#### Q209 — Arrays: creation, functions, sequential access, sorting
**Structure (marks):** (a) creation 4 ways 3 · (b) function table + uses 4 · (c) access `foreach`/`for`/pointer 4 · (d) sorting incl. key-preserving 3.
**Answer:**
- (a)
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
- (b) `3:L452–459`: `count()` length · `array_push($a,$v)` append (= `$a[]=$v`) · `array_pop` last (standard) · `array_shift`/`array_unshift` front (standard) · `sort`/`rsort` keys renumbered · `asort`/`arsort` keys kept · `ksort`/`krsort` by key · `in_array($v,$a)` membership · `array_search($v,$a)` key of a value (standard) · `array_map($fn,$a)` transform · `array_filter($fn,$a)` filter · `array_merge($a,$b)` (standard) · `array_keys`/`array_values` (standard) · `array_sum` (standard) · `implode`/`explode` array↔string (`3:L544–545`).
- (c) `foreach ($a as $v)` walks values in **insertion order**; `as $k => $v` gives keys; `for ($i=0; $i<count($a); $i++)` only for integer keys; the **pointer** (`reset`, `current`, `next`, `prev`, `end`, `key`) allows manual movement — `next()` returns the new value, `false` past the end.
- (d)
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
**Traps:**
- `sort($m)` leaves `[72, 88, 95]` with keys 0,1,2 and the names gone.
- `$a[3] = x` is not an append when keys are non-sequential — use `[]`; `count()` in a `for` condition re-counts each iteration.

#### Q210 — Unique strings; average and median (14)
**Structure (marks):** 7 + 7. Each half: algorithm in words 3, function 3, driver/output 1.
**Answer:**
- (a) Algorithm: empty result array; walk the input once; test each string with strict `in_array()`; append if absent; return — duplicates gone, original order kept.
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
- Built-in worth one line: `array_unique($arr)` (standard) — but the question says *write algorithm and function*, so the loop is the answer.
- (b) Algorithm: average = sum ÷ count; median = sort a **copy**, odd → middle element, even → mean of the two middles.
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
**Traps:**
- `$n/2` as an index is a float for even counts — hence `intdiv`; sorting `$nums` directly mutates the caller's array.
- An empty array divides by zero — guard it.

#### Q211 — Pass-by-value vs pass-by-reference partitioning (14)
**Structure (marks):** the two modes 4, algorithm 3, function with `&` 5, demo output 2.
**Answer:**
- By default **by value**: a copy, nothing visible to the caller. `&` = **by reference**: an alias, assignments modify the original (`3:L369–370`). `return` yields one value → two result arrays need two reference parameters.
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
- Algorithm: init both output arrays empty; one pass; `> 0` → positives, `< 0` → negatives; zeros to neither; return nothing.
- Proof `&` was needed: delete it and both `echo` lines print empty arrays — the function filled only its own copies.
**Traps:**
- Forgetting `&` — the single most common lost-marks error here.
- `$n >= 0` puts zeros in positives; `return`-ing two arrays instead of using the partition signature.

#### Q212 — Most frequent word from a file (14)
**Structure (marks):** algorithm 4, reading + splitting 4, counting with an array 4, finding the max 2.
**Answer:**
- Algorithm: read the file; `:` → space; split on whitespace; normalise case; count with a **frequency array keyed by word**; scan counts for the maximum; return that word.
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
- Why: `$count` **is** the algorithm — key = word, value = frequency, so "seen this word?" is an `isset` test, O(1). `preg_split("/\s+/")` handles runs of spaces, newlines, tabs; `explode(" ")` cannot.
**Traps:**
- `explode(" ", $text)` leaves `"word\n"` and `""` entries; no `strtolower` counts `PHP` and `php` separately.
- `file()` gives *lines*, not words — use `file_get_contents()` (or `implode`/loop).

#### Q213 — Array creation (7) + implode/explode + Armstrong (7)
**Structure (marks):** (a) four creation methods with code 7. (b) explode vs implode 3 + Armstrong 4.
**Answer:**
- (a) **short indexed** `[10, 20, 30]` · **long form** `array(10, 20, 30)` · **associative** `["name" => "Anu", "marks" => 88]` · **incremental** `$a = []; $a[] = 10;` — the empty bracket takes the next integer key (`3:L390–392`). Add **multidimensional** `[[1,2],[3,4]]` and **explicit keys** `[5 => "five"]` for the extra marks; `print_r()`/`var_dump()` shows structure.
- (b) `explode($delimiter,$string)` → **string to array**; `implode($glue,$array)` → **array to string** (`3:L544–545`); exact inverses, neither modifies input.
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
**Traps:**
- Hard-coded exponent 3 — 1634 is Armstrong with exponent 4; use the digit count.
- `$temp / 10` leaves a float and loops forever — `intdiv`; comparing after modifying `$n` loses the original — keep `$temp`.

#### Q214 — Functions sample script (8) + flow control functions (6)
**Structure (marks):** (a) 8 = definition/syntax 2, parameter kinds 2, working script 4. (b) 6 = `if/elseif/else` 2, `exit`/`die` 2, `return` 2.
**Answer:**
- (a)
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
- Say: `function` names it; parameters comma-separated with `$`; `return` ends it with a value; hoisted (`3:L329`); no `return` → `NULL` (`3:L331`); scope local unless `global` (`3:L366`); `&` = reference (`3:L370`); `...` collects into an array (`3:L374`).
- (b) `if/elseif/else` — branching, first true block runs (`3:L231`) · `exit()` terminates at once, optional message/status, `die()` its exact alias (`3:L235`) · `return` sends a value and stops the function (`3:L239`). All three decide continue / branch / stop (`3:L243`).
**Traps:**
- `return` inside a loop exits the *function*, not just the loop.
- `die()` inside a function kills the whole page, not just the function; `echo die("x")` is meaningless (language constructs).

#### Q215 — Cookies (6) + five MySQL operations (8)
**Structure (marks):** (a) significance 2, create 2, read/delete 2. (b) connect 1 + one compact script with CREATE, INSERT, SELECT, UPDATE, DELETE 7.
**Answer:**
- (a) HTTP is **stateless**, so a cookie lets a site remember a visitor: a small `name=value` record the browser stores and resends to that domain (`4:L65–73`). **Create** `setcookie("username","Anu",time()+3600)` — name, value, expiry — **before any HTML**, because it is a header (`4:L65–67`). **Read** `$_COOKIE["username"]`; **destroy** with a **past** expiry (`4:L71`, `4:L86`). ~4 KB, user-editable, never secrets (`4:L73`).
```php
<?php
setcookie("username", "Anu", time() + 3600);   // create
if (isset($_COOKIE["username"])) {             // read on a later request
    echo "Welcome back, " . $_COOKIE["username"];
}
setcookie("username", "", time() - 3600);      // destroy
?>
```
- (b) The same five operations on one table; the SQL is Module 4's, the wrapper is `mysqli_query` (`4:L316–337`).
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
- Full CRUD treatment, `mysqli_insert_id`, `affected_rows`, prepared statements → **Module 4 kit**; here you need the five statements and the connect/close frame.
**Traps:**
- `setcookie` after `echo` → "headers already sent".
- `UPDATE`/`DELETE` without `WHERE` hits the whole table; reading `$_COOKIE` in the request that set it (it arrives on the next).

#### Q216 — 5-field registration into MySQL (10) + dynamic typing (4)
**Structure (marks):** form 2, connect 2, read/validate 2, INSERT 2, feedback + close 2; then dynamic typing 4.
**Answer:**
- (a)
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
- Explanation: five named inputs → five `$_POST` keys → trimmed and validated → one `INSERT` with the column list → `mysqli_query` returns `true`/`false`, which drives the message → `mysqli_close`. Hardening worth a line: quote strings, cast numbers `(int)`, prefer `mysqli_prepare` + `?` against injection (`4:L665–689`).
- (b) **Dynamically typed** = no declared type; the type belongs to the current value, resolved at **runtime**: `$x = 5;` int, `$x = "five";` string, no cast, no error (`3:L90`). Consequences: (1) no compile-time checking, errors at execution; (2) auto-**juggling** — `"10" + 5` is 15 (`3:L138`); (3) form input (always a string) usable numerically after `(int)`/`(float)`; (4) `==` must convert, hence `===` (`3:L199–210`); (5) `gettype()`, `var_dump()`, `is_int()` inspect the runtime type (`3:L124`, `3:L143`). PHP 7+ allows optional type declarations; default stays dynamic (standard).
**Traps:**
- `$sql` interpolated without escaping — SQL injection; no column list in `INSERT`.
- Closing the connection before the query.

#### Q217 — Control statements (7) + palindrome (7)
**Structure (marks):** (a) if/else 2, switch 2, loops 2, break/continue 1. (b) logic 2, code 4, test cases 1.
**Answer:**
- (a) As Q207a: `if/elseif/else` first true branch (`3:L259`) · `switch/case/break/default` evaluated once, `break` stops fall-through (`3:L260–262`) · `for`/`while`/`do...while`/`foreach` with `as $k => $v` (`3:L295–298`) · `break` exits, `continue` skips (standard) · ternary `?:` as an expression-level branch.
- (b) A **palindrome** reads the same both ways: reverse and compare, or compare from both ends inward.
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
- The loop: `$temp % 10` peels the last digit, `$rev * 10` shifts left, `intdiv($temp,10)` drops it — 12321 builds 1 → 12 → 123 → 1232 → 12321.
**Traps:**
- Comparing `$rev` with `$temp` after the loop (`$temp` is 0) — keep `$n`.
- `strrev` on a number needs `(string)$n`; use `===` for the string compare.

#### Q218 — Associative arrays (7) + sort student marks (7)
**Structure (marks):** (a) definition 2, syntax/`=>` 2, traversal + functions 3. (b) build 2, sort 2, print 3.
**Answer:**
- (a) **Named keys** instead of positions, so each value has a meaningful label (`3:L421–424`): `$stu = ["name" => "Anu", "marks" => 88];` — `=>` maps key to value, `=` is a syntax error here. Access `$stu["name"]`; traverse `foreach ($stu as $key => $value)` (`3:L426`); functions `array_keys`, `array_values`, `in_array`, `array_key_exists`, `asort`/`arsort`, `ksort`/`krsort` (`3:L452–459` + standard).
```php
<?php
$student = ["name" => "Anu", "roll" => 21, "marks" => 88];
foreach ($student as $k => $v) {
    echo "$k: $v<br>";
}
echo $student["marks"];
?>
```
- (b)
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
- Why `asort`: `sort()` renumbers keys 0..n and destroys the names (`3:L456`) — the marks print but nobody's; `asort()` keeps the pairing, the whole point of an associative array.
**Traps:**
- `sort($marks)` — the classic lost-marks answer; `=>` written as `=`.
- Assuming `foreach` sorts — it returns **insertion order**.

#### Q219 — String handling functions (8) + count vowels (6)
**Structure (marks):** (a) six to eight functions, name + purpose + one-line example 8. (b) logic 2, code 3, output 1.
**Answer:**
- (a) `strlen($s)` length — 9 for "Saintgits" · `strtoupper`/`strtolower` — "SAINTGITS" · `trim` — `"  Anu  "` → `"Anu"` · `substr($s, start, length)` — "Saint" · `str_replace($search,$replace,$s)` — "World"→"PHP" · `explode`/`implode` string↔array · `strrev` reverse · `strpos` first position (`false` if absent) · `ucfirst`/`ucwords` capitalise · `str_repeat($s,$n)` · `sprintf` format · `str_word_count` · `htmlspecialchars` escape (`3:L512–515`, `3:L542–545`, `3:L655`). All **return** a new string; none modifies the original unless you assign back.
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
- Why `!== false`: `strpos` returns `0` for a match at position zero — the `'a'` case — and `0` is falsy, so a loose test undercounts. That is the trap the examiner looks for.
**Traps:**
- `$str[$i]` breaks on multibyte characters (irrelevant for ASCII exam text); forgetting both cases in `$vowels`.
- `strlen` in the loop condition on a huge string — cache it if efficiency is asked.

#### Q220 — Six string functions (6) + GET sum/difference/product (8)
**Structure (marks):** (a) six functions with examples 6. (b) purpose of `$_GET`/`$_POST` 2, the HTML form 2, the processing script 4.
**Answer:**
- (a) `strlen` → 9 for "Saintgits" · `strtoupper` → "SAINTGITS" · `trim` → strips leading/trailing whitespace, essential on form input · `substr($s,0,5)` → "Saint" · `str_replace("World","PHP","Hello World")` → "Hello PHP" · `explode(",", "HTML,CSS,JS")` → 3 elements. Extras: `implode`, `strrev`, `strpos`, `ucfirst` (`3:L512–515`, `3:L542–545`).
- (b) `$_GET`/`$_POST` are **superglobal arrays**, populated per request, keyed by each field's `name` (`3:L621`). `$_GET` = query string (`method="GET"`): visible, bookmarkable, size-limited, not for passwords. `$_POST` = body: not in the URL, no practical limit. Both **always strings**, so numeric use needs a cast.
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
**Traps:**
- `$_POST` in a script whose form says `method="GET"` — the arrays are empty.
- No `isset` guard → undefined-key warnings on first load; `(float)` is what earns the type-conversion mark.

#### Q221 — Functions (6) + dynamic typing & explode/implode (8)
**Structure (marks):** (a) definition + syntax 2, parameter kinds 2, sample script 2. (b) dynamic typing 4, explode vs implode 4.
**Answer:**
- (a) As Q214a: `function name($params) { ... return $v; }`, hoisted (`3:L329`), `return` exits with a value (`3:L330`), no `return` → `NULL` (`3:L331`), locals function-scoped (`3:L366`), `&` by reference (`3:L370`), `...$args` variadic (`3:L374`). Compact sample:
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
- (b) **Dynamic typing:** no declared type (historically not even allowed); the value carries the type, resolved at **runtime** (`3:L90`). Proof: `gettype($x)` → `integer`, then `string` after `$x = "ten";`, no error. Consequences: (1) juggling — `"10" + 5` = 15, `"5" == 5` true (`3:L138`, `3:L209`); (2) errors at execution, not compilation; (3) `===` demands type equality (`3:L202`); (4) `is_int`/`is_string`/`gettype`/`var_dump` inspect the type (`3:L124`, `3:L143`). **explode vs implode:** string→array at each delimiter / array→string with the glue; inverses (`3:L544–545`).
```php
<?php
$csv    = "Anu,88,Rahul,72";
$parts  = explode(",", $csv);        // 4-element array
$joined = implode(" | ", $parts);    // "Anu | 88 | Rahul | 72"
echo count($parts) . " pieces: " . $joined;
?>
```
**Traps:**
- Saying "PHP has no types" — it has eight, just no *declared* types.
- `implode($arr, $glue)` — glue **first** in modern PHP; `explode` with an empty delimiter is fatal.

---

## 4. Code you must be able to write by hand

> Handwriting rules: `<?php` first, `?>` last, `$` on every variable, `;` on every statement, `.` to join strings, `=>` inside arrays, `->` on objects.

### D1 — Sum of two numbers
```php
<?php
$a = 15;
$b = 27;
echo "Sum = " . ($a + $b);
?>
```
**Memorise:** `$` on variables; `+` adds; `.` joins the label to the result, never `+`.

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
**Memorise:** `$i * $i <= $n` (√n bound), `%` for divisibility, `break` at the first factor.

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
**Memorise:** `$rev * 10 + digit` builds the reverse; `intdiv` drops a digit; keep the original in a second variable.

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
**Memorise:** `asort`/`arsort` keep keys, plain `sort` destroys them; `reset` + `key` + `current` read the first pair.

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
**Memorise:** `array_sum`/`count`; odd → middle, even → mean of the two middles; `intdiv` for the index.

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
**Memorise:** `&` on the parameter, not on the call; the function returns nothing — outputs are the references.

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
**Memorise:** `str_replace(":", " ")` normalises the second delimiter; `$count[$word]++` is the frequency map; scan for the max after.

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
**Memorise:** `explode(delimiter, string)`, `implode(glue, array)` — the delimiter/glue is always **first**; they are inverses.

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
**Memorise:** the five stations (method → trim → validate → business rule → respond); `$errors[]` + `count($errors) == 0`; `htmlspecialchars` on output.

---

## 5. Night-before memorize sheet

| Item | Exact syntax / value to recall | Asked at |
|---|---|---|
| PHP tags | `<?php ... ?>` ; short echo `<?= $x ?>` | every program (`3:L88`) |
| Variable | `$name = "Anu";` — `$` required, no type keyword | Q70, Q76 |
| Statement end | `;` after every statement | parse error otherwise |
| Concatenation | `.` and `.=` — **never** `+` | Q75, the #1 trap |
| Strict equality | `"5" === 5` → `false`; `"5" == 5` → `true` | Q205 (`3:L199`) |
| Exponent / remainder | `**`, `%`; `10 ** 2` = 100, `10 % 3` = 1 | Q78, Q91 |
| Casts | `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` | Q85, Q205 |
| Type inspectors | `gettype($v)`, `var_dump($v)`, `is_int()`, `is_string()` | Q68, Q88 |
| Array literal | `[10, 20, 30]` or `array(10, 20, 30)` | Q209a, Q213a |
| Associative key | `"name" => "Anu"` — `=>`, **not** `=` | Q218 |
| Append | `$arr[] = 40;` | Q209 |
| Object access | `$obj->method()` / `$obj->prop` — arrow, not dot | Q207, `3:L766` |
| Length / count | `strlen($s)` strings, `count($arr)` arrays | Q219, Q209 |
| Sort family | `sort`/`rsort` renumber · `asort`/`arsort` keep keys · `ksort` by key | Q82, Q218 |
| Pointer set | `reset` first · `end` last · `next` forward · `prev` back · `current` value · `key` key | Q81 |
| String slice | `substr($s, 0, 5)` → `"Saint"` | Q219, Q220 |
| Split / join | `explode(",", $s)` → array · `implode(" + ", $arr)` → string | Q89, Q213b |
| Regex test | `preg_match("/^\d{6}$/", $pin)` → 1 or 0 | Q74, Q208 |
| Five patterns | `/^[0-9]{10}$/` · `/^[\w.-]+@[\w.-]+\.[\w]+$/` · `/^[A-Za-z]+$/` · `/^\d{6}$/` · `/^[A-Za-z0-9]+$/` | verbatim `3:L599–605` |
| GET / POST | `$_GET["f"]` URL · `$_POST["f"]` body · `$_REQUEST` merges | Q83, Q220b |
| Method check | `$_SERVER["REQUEST_METHOD"] == "POST"` | every form script (`3:L630`) |
| Presence / blank | `isset($_POST["f"])` vs `empty($_POST["f"])` — `empty("0")` is **true** | Q83, Q216a |
| Escape output | `htmlspecialchars($name)` | XSS, `3:L655` |
| Null coalescing | `$_POST["x"] ?? ""` | kills undefined-key warnings |
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

## 6. Diagram + figure index

`grep -n "Image Description" module3.md` → 23 hits, but **only one is real content**; the rest are slide furniture (PHP logo, `</>` icon, "A" typography icon).

| md line | What the figure shows | Reproduce? |
|---|---|---|
| `3:L57` | **PHP request–response cycle**: three boxes across the top (Browser requests page.php → Web Server → PHP Engine runs the script), a green MySQL box under the server/engine, a wide bar underneath labelled "Plain HTML sent back to Browser" | **Yes — draw this for any "how does PHP work" question** |
| `3:L59–70` | the same diagram's plain-text labels: "Browser Requests page.php", "Web Server", "PHP Engine Runs the script", "MySQL Database (if the script queries it)", "Plain HTML sent back to Browser" | use these five labels verbatim |
| `3:L1`, `22`, `50`, `79`, `96`\*, `131`, `161`, `192`, `250`, `286`, `319`, `353`, `381`, `414`, `466`, `503`, `533`, `563`, `614`, `645`, `679`, `713`, `748` | slide furniture only — PHP oval logo, `</>` code-tag icon, "A" typography icon | no |

\*L96 is a plain-text label line inside the same slide, not a separate image.

**Deck tables worth reproducing verbatim in an answer.**

| Deck table | md range | For |
|---|---|---|
| Data types (type / example / notes) | `3:L115–122` | Q68, Q77, Q88, Q203a |
| Common array functions (6 rows) | `3:L452–459` | Q82, Q207b, Q209b |
| Common regex patterns for validation (5 rows) | `3:L599–605` | Q74, Q208, Q216a |
| Cookies vs sessions quick reference | `4:L138–160` | Q84, Q215a (M4 deck) |
| Fetch styles (`fetch_assoc`/`array`/`row`/`object`) | `4:L385` | Q215b only if asked |

**Diagrams the deck does NOT contain** — draw them yourself, labelled "(standard)": **operator precedence ladder** (no table anywhere; only safe claim: `.` binds like `+`/`-`, so parenthesise — §2.12) · **array internal representation**, hash table of buckets (§3.1.O) · **form → `$_POST` → validate → business logic → response** flow (only five numbered steps exist, `3:L722–726`) · **cookie vs session** split (M4, `4:L27–53`).

---

## 7. Say-this-if-grilled defence lines

1. **Why does `===` exist if `==` works?** — `==` converts first, so `"0" == false` and `"1" == "01"` are true; `===` refuses to convert, the only safe test when the type carries meaning (a PIN arriving as a string).
2. **Why is PHP dynamically typed?** — No type is written on the variable; the type travels with the value and is resolved at runtime, so `$x = 5;` then `$x = "five";` is legal (`3:L90`).
3. **Why `=>` and `->`, not `=` and `.`?** — `=` is assignment and would parse as an expression, `.` is concatenation, so key-mapping and member access needed their own tokens; both are syntax errors otherwise (`3:L477`).
4. **Why does `sort()` lose my names?** — It sorts values and **re-indexes** keys 0..n, discarding the key→value pairing; `asort()` is the key-preserving version (`3:L456`).
5. **Why can the browser never see my PHP (and why call it slow)?** — The engine executes the file server-side and writes only the resulting HTML into the response (`3:L31`, `3:L72`); it re-executes per request instead of staying resident like a servlet, which OPcache mitigates (`3:L34–35`).
6. **Why `setcookie` before any HTML?** — Cookies travel as HTTP **headers**, and headers go before the body; any `echo` first triggers "headers already sent" (`4:L65`).
7. **Why check `REQUEST_METHOD` instead of reading `$_POST`?** — On the first GET the fields do not exist, so an unguarded read warns and may process empty data; the guard makes one file serve both roles (`3:L630`).
8. **Why `!== false` after `strpos`?** — `strpos` returns `0` for a match at position zero and `0` is falsy, so a loose test rejects exactly the valid first-character case.
9. **Why pass by reference at all?** — `return` yields one value; when a function must produce two results (positives/negatives) the clean way is `&` parameters (`3:L370`).
10. **Why validate *and* sanitise?** — Different questions: validation decides whether to accept the data, sanitising makes accepted data safe to emit; a well-formed name can still contain `<script>` (`3:L652–657`).
