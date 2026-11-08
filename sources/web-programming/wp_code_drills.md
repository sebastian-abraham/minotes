# ✍️ 20CST461 Web Programming — Code Drill Workbook (append-only)

> **How to use:** each drill is a *write-it-by-hand* task, exactly like the exam. Write your answer in the chat (or on paper), get it graded for **syntax**, then check yourself against the model answer at the bottom of this file. Answers are marked `✅` where they are straight from the deck and `⚠️` where a subtle syntax point is being tested.
>
> **Set 1 = Session 1** (Module 3, hours 1–2: tags, variables, types, casts, operators, `==` vs `===`, flow control functions).

---

## SET 1 — Syntax drills (Module 3, chunk 1)

**D1.** Write a complete PHP block that: opens the tag, declares a college name as a string, a year as an integer and a fee as a float, then prints `Welcome to Saintgits` followed by a `<br>` on one line, and `Fee: 49999.5` on the next line — **using `$college`, `$year`, `$fee`** (do not hardcode the values into the strings).

**D2.** Rewrite D1's two output lines **once** using only double-quote interpolation and **once** using only `.` concatenation. Both must print identical text.

**D3.** You have `$a = "10";`. Write **three different** statements that each produce the integer `15` from `$a` and `5` — one with a cast, one with a conversion function, one that relies on automatic conversion.

**D4.** You have `$price = "499.99";`. Write the statement(s) to compute double the price into `$total` using `floatval()`, and then print the type and value of `$total` for debugging.

**D5.** Write a statement that converts `$x = "5"` **in place** into an integer, then a statement that prints `yes` if `$x` is now an integer and `no` otherwise, using the ternary `?:` operator.

**D6.** Write the exact PHP line(s) that print, on one line: `Rate: 75%`. (`$r = 75;` is already set.) Get the `%` into the output without PHP treating it as anything special, and get the variable in.

**D7.** Write a statement that prints the string `It's a PHP file` using **single quotes**, and then the string `He said "PHP"` using **single quotes**. Use escaping where needed.

**D8.** Write the single line that prints `Welcome to Saintgits 2026` where `$college` and `$year` are variables, and both are inside one double-quoted string with **no string concatenation**. ⚠️ Careful: `$college2026` would be read as a different variable.

**D9.** Given `$stu = ["name" => "Anu", "marks" => 88];` write the exact interpolation you would use to echo `Anu scored 88` inside a double-quoted string. ⚠️ This is the array-in-string syntax rule.

**D10.** Write an `if / elseif / else` block that prints `A` if `$m >= 90`, `B` if `$m >= 75`, otherwise `C`. Then write the same logic as a single `?:`-style one-liner if you can.

**D11.** Write a `switch` statement on `$day` (an integer 1–7) that prints `Weekend` for 6 and 7 and `Weekday` for everything else. 💡 Note how two cases share one body.

**D12.** Write the statement that stops the script immediately with the message `All fields are required.` — using `die()`.

**D13.** For each line, write what it prints or `ERROR`, then justify it in ≤6 words:
```
$a) echo "Total: " . 5 + 3;
$b) echo "Total: " . (5 + 3);
$c) echo 5 + 3 . " total";
$d) echo "5" + 5;
$e) echo "5" . 5;
$f) var_dump("5" === 5);
```
**D14.** Write a complete PHP program (with an HTML form-free style, no database) that: declares marks and attendance as integers, applies the rule "pass needs `marks >= 50` AND `attendance >= 75`", and prints `Eligible` or `Not eligible`. Include comments naming the two steps (validation vs business logic).

**D15.** Fix the syntax of this snippet (there are **4** syntax errors):
```php
<?
$name = 'Anu'
$marks = 88;
if ($marks >= 50)
    echo "Passed $name;
else
    echo 'Failed'
>
```

---
---

# MODEL ANSWERS — SET 1

> Scroll only after writing your own attempt.

**D1. ✅ (deck 3:L94)**
```php
<?php
$college = "Saintgits";
$year = 2026;
$fee = 49999.50;
echo "Welcome to $college <br>";
echo "Fee: $fee";
?>
```
Marks come from: `<?php` tag, `$` on all three names, `;` on every statement, `1` int vs `49999.50` float (no quotes on numbers), `<br>` inside the string, closing `?>`.

**D2.**
```php
// interpolation-only
echo "Welcome to $college <br>";
echo "Fee: $fee";
// concatenation-only
echo "Welcome to " . $college . " <br>";
echo "Fee: " . $fee;
```
⚠️ Note the spaces: `"Welcome to "` needs the trailing space, `" <br>"` needs the leading space. Forgetting those spaces is the usual mark lost.

**D3.** `$a = "10";`
```php
$b = (int)$a + 5;          // cast
$c = intval($a) + 5;       // conversion function
$d = $a + 5;               // automatic/loose conversion
```

**D4.**
```php
$price = "499.99";
$total = floatval($price) * 2;
var_dump($total);            // float(999.98)
// also valid: var_dump(gettype($total), $total);
```

**D5.**
```php
$x = "5";
settype($x, "integer");       // converts in place; the value is now int 5
echo is_int($x) ? "yes" : "no";
```
⚠️ `(int)$x;` alone would **not** work — a cast produces a value, it doesn't convert the variable. `settype()` is the in-place one.

**D6.**
```php
$r = 75;
echo "Rate: $r%";     // % is not special in PHP strings — no escaping needed
// equally fine: echo "Rate: " . $r . "%";   or  echo "Rate: {$r}%";
```

**D7.**
```php
echo 'It\'s a PHP file';      // \' escapes a single quote inside single quotes
echo 'He said "PHP"';         // double quotes need NO escaping inside single quotes
```

**D8.**
```php
echo "Welcome to {$college} {$year}";
```
⚠️ `"{$college} {$year}"` — braces make the variable name unambiguous. `"$college $year"` also works because the space terminates the name; `"$college$year"` would **not**.

**D9.**
```php
$stu = ["name" => "Anu", "marks" => 88];
echo "{$stu['name']} scored {$stu['marks']}";
```
⚠️ `"$stu['name'] scored"` is **wrong** — a quoted key inside a double-quoted string needs `{ }`. `$stu[name]` (no quotes) happens to work in simple syntax but is not safe to rely on. Braces always work.

**D10.**
```php
if ($m >= 90) {
    echo "A";
} elseif ($m >= 75) {
    echo "B";
} else {
    echo "C";
}
// one-liner form (nested ternary — parenthesise it, PHP requires it in PHP 8)
echo $m >= 90 ? "A" : ($m >= 75 ? "B" : "C");
```
⚠️ Spelling: **`elseif`**, one word, no space. `$m >= 90 ? "A" : $m >= 75 ? "B" : "C"` without parentheses is a **fatal error in PHP 8** (nested ternaries without parentheses are deprecated/removed) — parentheses are the safe form.

**D11. ✅ (deck 3:L272)**
```php
switch ($day) {
    case 6:
    case 7:
        echo "Weekend";
        break;
    default:
        echo "Weekday";
}
```
⚠️ Two `case` labels may share one body by stacking (fall-through on purpose). `break;` stops the fall-through; `default:` catches everything else and **does not need** a `break` at the end.

**D12.**
```php
die("All fields are required.");     // or: die("All fields are required");
```
Also correct: `exit("All fields are required.");` — same function.

**D13.**
| | Output | Why |
|---|---|---|
| a | `Total: 8` | `.` and `+` are the same precedence, **left to right** → `("Total: " . 5)` = `"Total: 5"`, then `+ 3` → `8` → `"Total: 8"`. ⚠️ PHP 8 warns "non-numeric value" here; the printed text is still `Total: 8` |
| b | `Total: 8` | parentheses force `5 + 3` = `8`, then concatenate → identical here, but **not** always — this is why you always parenthesise |
| c | `8 total` | `5 + 3` = `8` first, then `8 . " total"` → `8 total` |
| d | `10` | `+` forces arithmetic: `"5"` becomes `5` |
| e | `55` | `.` forces string glue: `5` becomes `"5"` |
| f | `bool(false)` | `===` compares value **and** type; `"5"` is a string, `5` is an int |

**D14. ✅ (deck 3:L694)**
```php
<?php
$marks = 60;          // integer
$attendance = 80;     // integer

// Business rule: pass needs marks >= 50 AND attendance >= 75
if ($marks >= 50 && $attendance >= 75) {
    echo "Eligible";
} else {
    echo "Not eligible";
}
?>
```
⚠️ The combined condition needs `&&` (not `and`, not a comma) and **both** comparisons written out: `if ($marks >= 50 && $attendance >= 75)` — a frequent slip is `$marks >= 50 && 75`.

**D15.** Four errors fixed:
```php
<?php
$name = 'Anu';              // 1. missing semicolon
$marks = 88;
if ($marks >= 50)
    echo "Passed $name";    // 2. missing closing double quote  &  3. missing semicolon
else
    echo 'Failed';          // 4. missing semicolon
?>
```
5th (bonus) point: `<?` short-open tags are **off by default** in modern PHP — always write `<?php`, and the closing tag must be `?>` not `>`.

---

## Drill log

| Drill set | Date | Score | Corrections to remember |
|---|---|---|---|
| Set 1 | 2026-09-24 | pending | |
