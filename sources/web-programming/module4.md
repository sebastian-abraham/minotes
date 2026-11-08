*\[Image Description: A dark circular icon containing a white three-tiered cylinder database symbol set against a dark navy blue background.\]*

# MODULE 4

### PHP  MySQL

### 6 Hours of Content Delivery

* Cookies & sessions - 1 Hr

* PHP-MySQL integration & connecting - 1 Hr

* Working with MySQL data - 1 Hr

* CREATE, INSERT & DELETE operations - 1 Hr

* SELECT & UPDATE operations - 1 Hr

* Building dynamic content - 1 Hr

**Web Programming Saintgits College of Engineering**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Why State Management? Cookies vs. Sessions

### 1

**HTTP is stateless**

Each request a browser makes to a server is independent the server has no memory of previous requests by default. Without help, a server can't tell if two requests came from the same visitor.

### 2

**Cookies - stored on the client**

Small pieces of data the server asks the browser to store, then sends back automatically on every subsequent request to that domain.

### 3

**Sessions - stored on the server**

Data is kept on the server itself; the browser only holds a small session ID (usually via a cookie) that links back to it.

### 4

**Why both exist**

Cookies are simple but limited in size and visible to the client; sessions can hold much more data securely, but need the server to manage that storage.

**Web Programming | Saintgits College of Engineering**

**2**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Working with Cookies

PHP's `setcookie()` must be called before any HTML output cookies are sent as HTTP headers.

* `setcookie("name", "value", time()+3600)` sets a cookie for 1 hour

* Read with `$_COOKIE["name"]`

* To delete a cookie, set it again with an expiry time in the past

* Cookies are visible to and editable by the user never store sensitive data in one

```php
<?php
// Set a cookie for 1 hour
setcookie("username", "Anu", time() + 3600);

// Read it on a later request
if (isset($_COOKIE["username"])) {
    echo "Welcome back, " . $_COOKIE["username"];
}

// Delete a cookie
setcookie("username", "", time() - 3600);
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**3**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Working with Sessions

`session_start()` must run before any session data is read or written typically the very first line of a script.

* `session_start()` - begins or resumes a session, linked via a session ID cookie

* `$_SESSION["key"] = value;` store data on the server for this visitor

* Data persists across multiple page loads until the session ends

* `session_destroy()` ends the session and clears its server-side data

```php
<?php
session_start();
$_SESSION["user_id"] = 101;
$_SESSION["role"] = "student";
echo $_SESSION["user_id"];

// On logout:
session_destroy();
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**4**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Cookies vs. Sessions Quick Reference

### Cookies

* Stored in the browser, sent with every matching request

* Limited to about 4KB per cookie

* Visible and editable by the user not for sensitive data

* Can persist for days/months (set by expiry time)

* Good for: remembering preferences, 'remember me' tokens

### Sessions

* Stored on the server; browser only holds a session ID

* Can hold much larger / more sensitive data safely

* Cleared when the browser closes, by default (unless configured otherwise)

* Requires `session_start()` on every page that uses it

* Good for: login state, shopping carts, multi-step forms

**Web Programming | Saintgits College of Engineering**

**5**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Why Pair PHP with MySQL?

### 1

**The problem with plain PHP**

Everything covered in Module III variables, sessions, form data disappears the moment the script finishes running. There's no permanent storage.

### 2

**What a database adds**

MySQL is a relational database: data is organised into tables (rows and columns), and it persists indefinitely on disk, available to every future request.

### 3

**Why MySQL specifically**

Free, open-source, the default pairing with PHP on most hosting platforms (including Hostinger-style shared hosting), and the 'M' in the classic LAMP stack (Linux, Apache, MySQL, PHP).

### 4

**The bridge: mysqli / PDO**

PHP doesn't talk to MySQL directly it uses an extension. MySQLi (MySQL Improved) is the classic choice for this course; PDO is a more modern, database-agnostic alternative.

**Web Programming | Saintgits College of Engineering**

**6**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Connecting to MySQL with PHP

`mysqli_connect()` opens the link between a PHP script and a MySQL server this is the very first step any database-driven page needs.

* `mysqli_connect(host, user, password, database)` returns a connection handle

* Always check the connection for failure before continuing

* "localhost" is the typical host value for same-server hosting

* `mysqli_close($conn)` releases the connection when done (optional PHP also closes it automatically at script end)

```php
<?php
$conn = mysqli_connect(
    "localhost", "root", "password", "college_db"
);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully";
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**7**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Object-Oriented Connection Style

mysqli also offers an object-oriented interface, doing the same job with a slightly different syntax common in real-world Laravel-adjacent code.

* `new mysqli(host, user, password, database)` creates a connection object

* `$conn->connect_error` checks for a failed connection

* `$conn->query("...")` runs a query (object method instead of a standalone function)

* `$conn->close()` closes the connection

```php
<?php
$conn = new mysqli(
    "localhost", "root", "password", "college_db"
);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**8**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Connection Best Practices

### 1

**Never hardcode credentials in shared/public code**

Database passwords belong in a separate config file (excluded from version control), not pasted directly into every script that needs a connection.

### 2

**Always check for connection failure**

A silently failed connection leads to confusing errors later checking immediately with `die()` or a proper error handler saves debugging time.

### 3

**Close connections when done**

Not strictly required (PHP cleans up at script end), but good discipline especially in scripts that open multiple connections or run for a long time.

### 4

**Looking ahead: prepared statements**

The queries in this module use direct string building for clarity. Production code should use prepared statements (`mysqli_prepare`) to prevent SQL injection worth knowing even if not the syllabus focus here.

**Web Programming | Saintgits College of Engineering**

**9**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Running a Query: mysqli_query()

Once connected, every SQL statement read or write is sent to MySQL the same way: as a string, through `mysqli_query()`.

* `mysqli_query($conn, $sql)` executes a query and returns a result handle (for SELECT) or true/false (for INSERT/UPDATE/DELETE)

* Always check the return value before assuming the query succeeded

* `mysqli_error($conn)` reports the database's error message if a query fails

* `$sql` is just a string - building it carelessly from user input risks SQL injection

```php
<?php
$sql = "SELECT name, marks FROM students";
$result = mysqli_query($conn, $sql);

if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**10**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Fetching Results: mysqli_fetch_assoc()

A result handle doesn't contain readable data by itself you must fetch each row, one at a time, usually inside a loop.

* `mysqli_fetch_assoc($result)` pulls one row as an associative array: `["col"=>value]`

* Calling it again moves to the next row; it returns NULL once rows run out

* `while` loop is the standard pattern to process every row in a result

* `mysqli_num_rows($result)` tells you how many rows were returned, without looping

```php
<?php
while ($row = mysqli_fetch_assoc($result)) {
    echo $row["name"] . " " . $row["marks"] . "<br>";
}

echo "Total rows: " . mysqli_num_rows($result);
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**11**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Other Ways to Fetch a Row

| Function | Returns | When to Use |
| --- | --- | --- |
| `mysqli_fetch_assoc()` | Associative array | Access columns by name most common |
| `mysqli_fetch_array()` | Both indexed + assoc | Flexible, but slightly heavier |
| `mysqli_fetch_row()` | Indexed array only | Access columns by position |
| `mysqli_fetch_object()` | An object | Access columns as `$row->name` |
| `mysqli_num_rows()` | Integer | Count rows without fetching them |

Note: All fetch functions advance an internal pointer once a row is fetched, the next call returns the next row, until none remain.

**Web Programming | Saintgits College of Engineering**

**12**

*\[Image Description: A multi-step process diagram illustrating the full cycle from query to browser display. Along the top row are three horizontal boxes: Box 1 (teal blue) labeled "1. Build SQL string", Box 2 (dark navy) labeled "2. mysqli_query()", and Box 3 (teal blue) labeled "3. Result handle returned". Below them on the left sits Box 4 (a wide green rectangle) labeled "4. while + fetch_assoc() loops through rows", positioned beside Box 5 (teal blue) labeled "5. echo HTML for each row". Spanning beneath them across the bottom is a wide dark navy container labeled "Browser displays the finished table".\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## From Query to Output: The Full Cycle

1. Build SQL string

2. mysqli_query()

3. Result handle returned

4. while + fetch_assoc() loops through rows

5. echo HTML for each row

Browser displays the finished table

This five-step pattern - query, fetch, loop, echo - repeats throughout the rest of this module, regardless of what the query actually does.

**Web Programming | Saintgits College of Engineering**

**13**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP + SQL tag in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## CREATE TABLE - Defining Structure

Before any data can be stored, a table's structure its columns and their types must be defined.

* `CREATE TABLE name (column type, ...)` defines a new table

* `AUTO_INCREMENT PRIMARY KEY` gives each row a unique, self-numbering id

* Column types: `INT`, `VARCHAR(n)`, `TEXT`, `DATE`, `DECIMAL`, etc.

* Run once during setup not on every page load

```php
<?php
$sql = "CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT,
    joined DATE
)";

mysqli_query($conn, $sql);
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP + SQL**

**14**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP + SQL tag in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## INSERT - Adding New Rows

INSERT writes a new row of data into an existing table.

* `INSERT INTO table (cols) VALUES (vals)` - explicit column list is safest

* String values must be quoted in the SQL; numbers don't need quotes

* `mysqli_insert_id($conn)` returns the auto-increment id of the row just inserted

* Building `$sql` with raw form input directly is unsafe sanitize/escape first (or use prepared statements)

```php
<?php
$name = $_POST["name"];
$marks = (int)$_POST["marks"];

$sql = "INSERT INTO students (name, marks)
        VALUES ('$name', $marks)";

mysqli_query($conn, $sql);
echo "New ID: " . mysqli_insert_id($conn);
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP + SQL**

**15**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP + SQL tag in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## DELETE - Removing Rows

DELETE permanently removes rows matching a condition there's no 'undo' once it runs.

* `DELETE FROM table WHERE condition` removes only matching rows

* Never omit the `WHERE` clause unless you intend to clear the entire table

* `mysqli_affected_rows($conn)` tells you how many rows were actually deleted

* Good habit: run the equivalent `SELECT` first to preview what would be deleted

```php
<?php
$id = (int)$_POST["id"];

$sql = "DELETE FROM students WHERE id = $id";
mysqli_query($conn, $sql);

echo mysqli_affected_rows($conn) . " row(s) deleted";
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP + SQL**

**16**

**MODULE IV 1 HR TOPIC**

**20CST461**

## CREATE / INSERT / DELETE - Quick Reference

| Operation | Core Syntax | Risk if Misused |
| --- | --- | --- |
| CREATE | `CREATE TABLE t (col type, ...)` | Run more than once without `DROP` first |
| INSERT | `INSERT INTO t (cols) VALUES (...)` | Unescaped input → SQL injection |
| DELETE | `DELETE FROM t WHERE condition` | Missing `WHERE` → entire table wiped |

Note: All three are 'write' operations none of them return readable data, only success/failure and an affected-row count.

**Web Programming | Saintgits College of Engineering**

**17**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP + SQL tag in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## SELECT - Basic & Filtered Queries

SELECT is the only operation that returns readable data every other query just succeeds or fails.

* `SELECT * FROM table` every column, every row

* `SELECT col1, col2 FROM table` only the columns you need (faster, clearer)

* `WHERE condition` filters which rows come back

* Comparison operators in SQL: `=`, `!=`, `>`, `<`, `>=`, `<=`, `LIKE` (pattern match)

```php
<?php
$sql = "SELECT name, marks FROM students
        WHERE marks >= 75";

$result = mysqli_query($conn, $sql);

while ($row = mysqli_fetch_assoc($result)) {
    echo $row["name"] . "<br>";
}
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP + SQL**

**18**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP + SQL tag in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## SELECT - Sorting & Limiting Results

ORDER BY and LIMIT refine which rows come back and in what order common in any listing page.

* `ORDER BY column ASC/DESC` sorts results (`DESC` = highest/most recent first)

* `LIMIT n` caps the number of rows returned

* `LIMIT offset, count` used for pagination (skip, then take)

* These clauses can be combined with `WHERE` in the same query

```php
<?php
$sql = "SELECT name, marks FROM students
        WHERE marks >= 50
        ORDER BY marks DESC
        LIMIT 5";

$result = mysqli_query($conn, $sql);
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP + SQL**

**19**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP + SQL tag in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## UPDATE - Modifying Existing Rows

UPDATE changes values in rows that already exist like DELETE, it relies entirely on WHERE to target the right rows.

* `UPDATE table SET col = value WHERE condition`

* Multiple columns: `SET col1 = val1, col2 = val2`

* Without `WHERE`, every row in the table gets updated almost always a mistake

* `mysqli_affected_rows($conn)` confirms how many rows actually changed

```php
<?php
$id = (int)$_POST["id"];
$marks = (int)$_POST["marks"];

$sql = "UPDATE students
        SET marks = $marks
        WHERE id = $id";

mysqli_query($conn, $sql);
?>
```

**Web Programming | Saintgits College of Engineering**

**PHP + SQL**

**20**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Safe SELECT / UPDATE / DELETE Practices

### 1

**Test the WHERE clause with SELECT first**

Before running an UPDATE or DELETE, run the equivalent `SELECT ... WHERE ...` and check the rows it returns if it's the wrong set, the destructive query would have been too.

### 2

**Cast numeric input explicitly**

`(int)$_POST["id"]` before dropping it into SQL closes off a whole class of injection via that field, even without full prepared statements.

### 3

**Prefer prepared statements in real applications**

`mysqli_prepare()` with `?` placeholders separates SQL structure from data entirely the gold-standard defence against SQL injection, even though this module's examples use direct string-building for simplicity.

### 4

**Always check mysqli_affected_rows()**

A query can 'succeed' (no error) while affecting zero rows e.g. a WHERE clause that matched nothing. Checking the affected-row count catches that silently wrong outcome.

**Web Programming | Saintgits College of Engineering**

**21**

**MODULE IV 1 HR TOPIC**

**20CST461**

## What Makes Content 'Dynamic'?

### 1

**Static vs. dynamic**

A static page's HTML is fixed and identical for every visitor. A dynamic page's HTML is generated fresh on each request, often by querying a database so the same .php file can show completely different content each time.

### 2

**Mixing PHP with HTML**

PHP can be embedded directly inside HTML using `<?php ... ?>` blocks most commonly inside a loop that echoes one row of HTML per database record.

### 3

**Separating concerns**

Even in a simple script, it helps to mentally separate: data access (the query), business logic (any PHP rules applied), and presentation (the HTML being echoed) a precursor to the MVC pattern Module V's Laravel section formalizes.

### 4

**Tying it back to Module III**

This is the same form-processing pipeline from Module III, with one new final step: instead of just echoing a response, the validated data is now written to or read from a real, permanent database.

**Web Programming | Saintgits College of Engineering**

**22**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## Looping Database Rows into HTML

The most common dynamic-content pattern: query once, then echo one chunk of HTML per row inside the fetch loop.

* The `<?php ?>` block can open mid-HTML and close again, letting PHP and markup interleave naturally

* Each loop iteration outputs one row of the visible table

* `htmlspecialchars()` around any user-supplied data prevents it from being interpreted as HTML/JS

* This pattern works the same whether there are 3 rows or 3,000

```html
<table>
<?php while ($row = mysqli_fetch_assoc($result)): ?>
<tr>
<td><?php echo htmlspecialchars($row["name"]); ?></td>
<td><?php echo $row["marks"]; ?></td>
</tr>
<?php endwhile; ?>
</table>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**23**

*\[Image Description: Small database cylinder logo graphic in the top-left area and PHP logo in the lower-right area.\]*

**MODULE IV 1 HR TOPIC**

**20CST461**

## A Complete Dynamic Page

Putting every piece of this module together: connect, query, loop, and render a full, working dynamic page.

* 1. Connect to the database

* 2. Run the query

* 3. Loop through and echo each row as HTML

* This exact shape connect, query, loop, render - is the backbone of almost every PHP page that shows database content

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
$result = mysqli_query($conn, "SELECT name, marks FROM students");
?>
<table border="1">
<tr><th>Name</th><th>Marks</th></tr>
<?php while ($row = mysqli_fetch_assoc($result)): ?>
<tr><td><?= $row["name"] ?></td><td><?= $row["marks"] ?></td></tr>
<?php endwhile; ?>
</table>
```

**Web Programming | Saintgits College of Engineering**

**PHP**

**24**

**MODULE IV 1 HR TOPIC**

**20CST461**

## Looking Ahead to Module V

### 1

**What this module built**

Every page so far hand-writes the connect → query → loop → render pattern from scratch, every single time functional, but repetitive across a real application with dozens of pages.

### 2

**JSON a lighter way to exchange this data**

Module V introduces JSON as a standard format for exchanging the same kind of structured data (e.g. that `$row` array) between a server and other applications, not just rendering it as HTML.

### 3

**Laravel - structuring this pattern at scale**

Laravel's Eloquent ORM replaces raw `mysqli_query()` strings with PHP objects and methods; its MVC structure formally separates the data, logic, and presentation concerns this module only handled informally.

### 4

**The core idea doesn't change**

Whether it's raw mysqli or Laravel's Eloquent, every dynamic page is still fundamentally: get some data, decide what to do with it, then render it exactly the cycle practiced throughout this module.

**Web Programming | Saintgits College of Engineering**

**25**

**MODULE 4 RECAP**

**20CST461**

## Key Takeaways

* Cookies live in the browser; sessions live on the server, linked by a session ID cookie.

* `session_start()` must run before any `$_SESSION` read or write.

* `mysqli_connect()` (or `new mysqli()`) opens the link between PHP and MySQL.

* `mysqli_query()` runs any SQL string - SELECT, INSERT, UPDATE, DELETE, CREATE alike.

* `mysqli_fetch_assoc()` + a while loop is the standard pattern to read result rows.

* DELETE and UPDATE need a careful WHERE clause test with SELECT first.

* Dynamic content = HTML generated at request-time from live database data.

* This connect-query-loop-render pattern is the direct precursor to Laravel's MVC model.

**Web Programming | Saintgits College of Engineering**

**26**