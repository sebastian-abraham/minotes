*[Image Description: A dark circular icon containing the white PHP logo set within an oval border against a dark blue background.]*

# MODULE 3

### php

# Introduction to PHP

### 6 Hours of Content Delivery

* Building blocks, variables & data types - 1 Hr
* Type conversion, operators & flow control - 1 Hr
* Control statements & functions - 1 Hr
* Arrays & objects - 1 Hr
* Strings, regex & pattern matching - 1 Hr
* Form processing & business logic - 1 Hr

**Web Programming | Saintgits College of Engineering**

---

*[Image Description: Small PHP oval logo graphic in the top header.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## What is PHP & How It Works

### 1
**Server-side scripting**  
PHP (PHP: Hypertext Preprocessor) runs entirely on the web server, before anything reaches the browser. The visitor only ever receives plain HTML they never see the PHP source code.

### 2
**Why PHP is popular**  
Free and open-source, runs on virtually any hosting platform, has a huge ecosystem (WordPress, Laravel), and is purpose-built for generating dynamic web pages and talking to databases.

### 3
**File extension & embedding**  
PHP files use the .php extension. PHP code can be mixed directly into an HTML file inside `<?php ... ?>` blocks the server processes those blocks and leaves the surrounding HTML untouched.

### 4
**What 'dynamic' means here**  
Because the script runs fresh on every request, the same .php file can output different content depending on the time, the logged-in user, or data pulled from a database.

**Web Programming | Saintgits College of Engineering**  
**2**

---

*[Image Description: Small PHP oval logo graphic in the top header.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## PHP in the Request-Response Cycle

*[Image Description: An architectural flow diagram depicting the PHP Request-Response Cycle. It shows three rounded rectangular process boxes along the top: the first teal-blue box is labeled "Browser Requests page.php", which connects to a dark navy-blue box labeled "Web Server", which in turn routes to another teal-blue box labeled "PHP Engine Runs the script". Below the server and engine boxes sits a green rectangular box representing the database, labeled "MySQL Database (if the script queries it)". Spanning across the lower section is a wide dark-blue rectangular container labeled "Plain HTML sent back to Browser", representing the final output delivered to the client.]*

Browser  
Requests page.php

Web Server

PHP Engine  
Runs the script

MySQL Database  
(if the script queries it)

Plain HTML sent back to Browser

The browser never sees the .php source only whatever HTML the script decided to output for this specific request.

**Web Programming | Saintgits College of Engineering**  
**3**

---

*[Image Description: A code tag icon labeled "</>" positioned in the top-left area alongside the PHP logo in the lower-right area.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## PHP Syntax & Variables

PHP code lives inside `<?php ... ?>`. Variables are loosely typed and always start with a dollar sign.

* `<?php ... ?>` marks where PHP code begins and ends
* Variables: `$name`, `$age` no type keyword needed
* PHP is dynamically typed type is decided by the value currently stored
* `echo` or `print` send output into the HTML response
* Statements end with a semicolon, same as C/Java

```php
<?php
$college = "Saintgits";
$year = 2026;
$fee = 49999.50;
echo "Welcome to $college <br>";
echo "Year: " . $year;
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**4**

---

**MODULE III 1 HR TOPIC**  
**20CST461**

## PHP Data Types

| Type | Example | Notes |
| :--- | :--- | :--- |
| int | `$age = 21;` | Whole numbers |
| float | `$fee = 499.50;` | Decimal numbers |
| string | `$name = "Anu";` | Text, single or double quotes |
| bool | `$active = true;` | true / false |
| array | `$m = [88, 92];` | Ordered or key-value collection |
| NULL | `$x = null;` | Explicitly 'no value' |

Note: `gettype($var)` returns a variable's current type as a string; `var_dump($var)` shows both type and value useful for debugging.

**Web Programming | Saintgits College of Engineering**  
**5**

---

*[Image Description: PHP logo located in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Converting Between Data Types

PHP converts types automatically in many contexts (loose typing), but explicit casting keeps behaviour predictable.

* `(int)`, `(float)`, `(string)`, `(bool)`, `(array)` - explicit casts
* `intval()`, `floatval()`, `strval()`, `boolval()` conversion functions
* `settype($var, "integer")` converts a variable in place
* `is_int()`, `is_string()`, `is_array()` - type-checking functions

```php
<?php
$a = "10";
$b = (int)$a + 5; // 15
$price = "499.99";
$total = floatval($price) * 2;
echo is_string($a) ? "yes" : "no";
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**6**

---

*[Image Description: A code tag icon labeled "</>" in the header and PHP logo in the lower right.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Operators & Expressions

PHP's arithmetic and assignment operators closely mirror C; string concatenation uses the dot (`.`) operator, not plus.

* Arithmetic: `+` `-` `*` `/` `%` `**` (exponent)
* Assignment: `=` `+=` `-=` `*=` `/=` `.=` (concatenate-and-assign)
* String concatenation: `.` joins two strings together
* An expression is anything that produces a value including a function call

```php
<?php
$a = 10; $b = 3;
echo $a % $b; // 1
echo $a ** 2; // 100
$msg = "Total: ";
$msg .= (5 + 3);
echo $msg; // "Total: 8"
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**7**

---

*[Image Description: A code tag icon labeled "</>" in the header and PHP logo in the lower right.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Comparison & Logical Operators

Loose vs. strict comparison is one of PHP's most exam-relevant quirks.

* `==` loose equality - converts types before comparing
* `===` strict equality checks value AND type
* `<`, `>`, `<=`, `>=`, `!=`, `!==` - standard relational comparisons
* `&&` (and), `||` (or), `!` (not) combine conditions

```php
<?php
var_dump(0 == "abc"); // false (PHP 8+)
var_dump("5" == 5); // true
var_dump("5" === 5); // false
$age = 20; $hasID = true;
if ($age >= 18 && $hasID) {
    echo "Entry allowed";
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**8**

---

**MODULE III 1 HR TOPIC**  
**20CST461**

## Flow Control Functions

### 1
**if / elseif / else**  
The core branching construct runs a block only when its condition evaluates to true, exactly as in C.

### 2
**exit() and die()**  
Immediately stop script execution die() is an alias of exit(). Commonly used after a fatal error: `die("Connection failed");`

### 3
**return**  
Inside a function, return both sends a value back to the caller AND immediately stops that function's execution nothing after it runs.

### 4
**Why these matter as a group**  
All of them control whether execution continues, branches, or stops the syllabus groups them as 'flow control functions' alongside the if/else statements covered next.

**Web Programming | Saintgits College of Engineering**  
**9**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Control Statements: if & switch

PHP control statements mirror C syntax closely a natural fit given the course's C pre-requisite.

* `if` / `elseif` / `else` for branching on arbitrary conditions
* `switch` for matching one variable against several fixed values
* `break` stops a case from falling through to the next one
* `default` catches anything not explicitly matched

```php
<?php
function grade($m) {
    if ($m >= 90) return "A";
    elseif ($m >= 75) return "B";
    else return "C";
}

switch (date("N")) {
    case 6:
    case 7: echo "Weekend"; break;
    default: echo "Weekday";
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**10**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Loops in PHP

for, while, and foreach cover virtually every repetition need in PHP foreach is the idiomatic way to walk through an array.

* `for (init; condition; step)` known number of repetitions
* `while (condition)` checks before each pass; may run zero times
* `do {...} while (condition)` checks after; always runs once
* `foreach ($array as $value)` the natural way to loop over PHP arrays

```php
<?php
$marks = [88, 95, 60];
foreach ($marks as $m) {
    echo grade($m);
}

for ($i = 1; $i <= 3; $i++) {
    echo $i;
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**11**

---

*[Image Description: A code tag icon labeled "</>" in the header and PHP logo in the lower right.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Working with Functions

Functions package reusable logic. PHP functions are defined with the function keyword and can return any type.

* `function name($params) { ... return value; }` defines a function
* Functions must be defined before OR after use PHP hoists function declarations
* `return` immediately exits the function with a value
* A function with no return statement implicitly returns `NULL`

```php
<?php
function calcTotal($price, $qty) {
    return $price * $qty;
}
echo calcTotal(499, 3); // 1497

function greet($name) {
    echo "Hello, $name!";
}
greet("Saintgits");
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**12**

---

*[Image Description: A code tag icon labeled "</>" in the header.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Function Parameters, Defaults & Scope

### 1
**Default parameter values**  
`function greet($name = "Guest") { ... }` if the caller omits the argument, `"Guest"` is used automatically.

### 2
**Variable scope**  
A variable declared inside a function is local to it by default - it does not exist outside. Use the `global` keyword inside a function to access a variable from the outer (global) scope.

### 3
**Passing by value vs. reference**  
Arguments are passed by value (a copy) by default. Prefixing a parameter with `&` (e.g. `function inc(&$x)`) passes by reference, letting the function modify the caller's original variable.

### 4
**Variadic functions**  
`function total(...$nums)` collects any number of arguments into an array called `$nums` inside the function useful when the argument count isn't fixed.

**Web Programming | Saintgits College of Engineering**  
**13**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Initialising & Manipulating Indexed Arrays

An indexed array is an ordered list, numbered automatically from 0 unless you say otherwise.

* `$arr = [10, 20, 30];` modern short syntax (`array(10, 20, 30)` also valid)
* Access by position: `$arr[0]` is 10
* `$arr[] = 40;` appends a new element to the end
* `count($arr)` gives the number of elements

```php
<?php
$marks = [88, 92, 79];
$marks[] = 95;
echo $marks[0]; // 88
echo count($marks); // 4

foreach ($marks as $i => $m) {
    echo "Index $i: $m\n";
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**14**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Associative & Multidimensional Arrays

Associative arrays use named keys instead of numeric indices; arrays can also nest inside each other.

* `$stu = ["name" => "Anu", "marks" => 88];` - key => value pairs
* Access via `$stu["name"]`
* A multidimensional array is an array of arrays - e.g. a list of student records
* `foreach` works on associative arrays too, exposing both key and value

```php
<?php
$students = [
    ["name" => "Anu", "marks" => 88],
    ["name" => "Rahul", "marks" => 72]
];

foreach ($students as $s) {
    echo $s["name"] . " " . $s["marks"] . "\n";
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**15**

---

**MODULE III 1 HR TOPIC**  
**20CST461**

## Common Array Functions

| Function | Purpose |
| :--- | :--- |
| count($arr) | Number of elements |
| array_push($arr, $val) | Add an element to the end (same as $arr[] = $val) |
| sort($arr) / rsort($arr) | Sort ascending / descending, re-indexing keys |
| array_map($fn, $arr) | Apply a function to every element, return a new array |
| array_filter($fn, $arr) | Keep only elements that pass a test function |
| in_array($val, $arr) | Check whether a value exists in the array |

**Web Programming | Saintgits College of Engineering**  
**16**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Objects & Classes in PHP

A class is a blueprint; an object is a specific instance built from that blueprint, with its own data.

* `class Name {...}` defines a blueprint with properties and methods
* `new ClassName()` creates an instance (an object)
* `->` accesses an object's properties and methods (not . like in some other languages)
* `__construct()` is a special method that runs automatically when an object is created

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
echo $s->greet();
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**17**

---

*[Image Description: A letter "A" / text typography icon in the upper-left header and a PHP logo in the bottom right.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Working with Strings

PHP has one of the largest built-in string-function libraries of any common server-side language.

* `strlen($s)` - length of a string
* `strtoupper($s)` / `strtolower($s)` - change case
* `trim($s)` removes whitespace from both ends
* `substr($s, start, length)` extracts part of a string

```php
<?php
$name = "  Saintgits  ";
$clean = trim($name);
echo strlen($clean); // 9
echo strtoupper($clean); // SAINTGITS
echo substr($clean, 0, 5); // Saint
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**18**

---

*[Image Description: A letter "A" / text typography icon in the upper-left header and a PHP logo in the bottom right.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## String Manipulation & Concatenation

Beyond reading strings, PHP makes it easy to build and transform them.

* Concatenation uses the `.` operator (and `.=` to append-and-assign)
* `str_replace($search, $replace, $s)` - find-and-replace
* `explode($delimiter, $s)` - splits a string into an array
* `implode($glue, $arr)` joins an array back into a string

```php
<?php
$msg = "Hello" . ", " . "World!";
$parts = explode(",", "HTML,CSS,JS");
$joined = implode(" + ", $parts);
$clean = str_replace("World", "PHP", $msg);
echo $joined; // HTML + CSS + JS
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**19**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Regular Expressions in PHP

PHP supports Perl-compatible regular expressions (PCRE) for flexible pattern matching beyond what simple string functions can do.

* `preg_match($pattern, $string)` tests whether a string matches a pattern
* `preg_replace($pattern, $replacement, $string)` find & replace via regex
* `preg_split($pattern, $string)` - split a string using a regex delimiter
* Patterns are wrapped in delimiters, usually `/pattern/`

```php
<?php
$email = "user@saintgits.org";
if (preg_match("/^[\w.-]+@[\w.-]+\.\w+$/", $email)) {
    echo "Valid email";
}
$clean = preg_replace("/[0-9]/", "", "Room12A");
echo $clean; // RoomA
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**20**

---

**MODULE III 1 HR TOPIC**  
**20CST461**

## Common Regex Patterns for Validation

| Pattern | Matches | Typical Use |
| :--- | :--- | :--- |
| `/^[0-9]{10}$/` | Exactly 10 digits | Phone number |
| `/^[\w.-]+@[\w.-]+\.\w+$/` | Basic email shape | Email validation |
| `/^[A-Za-z]+$/` | Letters only | Name field |
| `/^\d{6}$/` | Exactly 6 digits | PIN code |
| `/^[A-Za-z0-9]+$/` | Letters and digits only | Username field |

Note: `\d` means a digit, `\w` means a 'word character' (letter/digit/underscore), `{n}` means 'exactly n times', `^` and `$` anchor the start/end of the string.

**Web Programming | Saintgits College of Engineering**  
**21**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Reading Form Data: $_GET vs. $_POST

PHP exposes submitted form data through superglobal arrays - automatically populated for every request.

* `$_GET["field"]` - data sent via the URL query string (`method="GET"`)
* `$_POST["field"]` data sent in the request body (`method="POST"`)
* `$_REQUEST` combines GET, POST, and COOKIE data (less precise usually avoid)
* `isset($_POST["field"])` checks whether a field was actually submitted

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

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**22**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Validating & Sanitizing Input

Never trust data from a form directly always validate its shape and sanitize it before using or storing it.

* `trim()` removes accidental leading/trailing whitespace
* `htmlspecialchars()` prevents HTML/JS injection when echoing user input back
* `empty($_POST["field"])` checks for a missing or blank field
* Combine with `preg_match()` from the previous topic for shape validation (email, phone, etc.)

```php
<?php
$name = trim($_POST["name"] ?? "");
$email = trim($_POST["email"] ?? "");

if (empty($name) || empty($email)) {
    die("All fields are required.");
}

$safeName = htmlspecialchars($name);
echo "Welcome, $safeName";
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**23**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Business Logic Example

'Business logic' is the application-specific rule applied to validated data separate from the validation itself.

* Validation asks: is this data well-formed?
* Business logic asks: given well-formed data, what should the application DO?
* Keeping these as distinct steps makes code easier to read and to test
* Example: eligibility rules, fee calculation, grade computation

```php
<?php
$marks = (int) ($_POST["marks"] ?? 0);
$attendance = (int) ($_POST["attendance"] ?? 0);

// Business rule: pass needs marks >= 50 AND attendance >= 75
if ($marks >= 50 && $attendance >= 75) {
    echo "Eligible to pass";
} else {
    echo "Not eligible check marks/attendance";
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**24**

---

*[Image Description: PHP logo in the bottom-right corner.]*

**MODULE III 1 HR TOPIC**  
**20CST461**

## Putting It Together: A Form-Processing Script

A complete script combines: read input, validate, sanitize, apply business logic, and respond the full pipeline this module has built up to.

1. Check the request method
2. Read & trim the submitted fields
3. Validate (empty checks, regex where needed)
4. Apply business logic
5. Echo a response (Module IV will replace this with a database write)

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = trim($_POST["name"] ?? "");
    $marks = (int) ($_POST["marks"] ?? 0);

    if (empty($name)) { die("Name required"); }

    $grade = $marks >= 50 ? "Pass" : "Fail";
    echo htmlspecialchars($name) . ": $grade";
}
?>
```

**Web Programming | Saintgits College of Engineering**  
**PHP**  
**25**

---

*[Image Description: Small PHP logo in the upper header.]*

### php

# MODULE 3 RECAP

## Key Takeaways

PHP runs entirely server-side; the browser only ever sees the resulting HTML.

Variables are loosely typed and always start with $; types are decided at runtime.

=== checks both value and type; == checks value only a frequent exam trap.

foreach is the idiomatic way to iterate PHP arrays, indexed or associative.

Functions support default parameters, by-reference params, and variadics.

Objects use -> (not .) to access properties and methods.

preg_match()/preg_replace() bring regex pattern matching for validation.

Form data arrives via $_GET or $_POST - always validate and sanitize before use.

**20CST461**  
**Web Programming | Saintgits College of Engineering**  
**26**