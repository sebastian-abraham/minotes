# MODULE 4 — PHP + MySQL · Exam Kit

> 20CST461 Web Technologies · ESE Part A = 3 marks, Part B = 14 marks · 2 Part-A questions and 1 of 2 Part-B questions come from this module

**The module in one line:** connect → build a SQL string → `mysqli_query()` → loop `mysqli_fetch_assoc()` → echo HTML.

**Refs:** `4:L431–453` = lines 431–453 of `module4.md` (lecture deck). **"(standard, not in your deck)"** = correct PHP your slides never show — the bank still asks it (regex, `$_PHP_SELF`, file upload, `SHOW DATABASES`). Learn it; don't claim the slide said it.

---

## 1. Module map + question coverage

63 questions: **38 Part A** (Q92–Q129, 3 marks) and **25 Part B** (Q229–Q253, 14 marks).

Bank headings are wrong: Q92–Q129 sit under "Module 4: PHP", Q130–Q153 are JSON/Laravel (Module 5), and **Q229–Q253 sit under a second "Module 4: PHP" heading** — the 14-mark set. Both covered.

| Q# | What it asks (≤8 words) | Answered at |
|---|---|---|
| 92 | Steps to establish PHP–MySQL connection | §3.1 A1, §2.6 |
| 93 | `$_SESSION` vs `$_COOKIE`, when each | §3.1 A2, §2.4 |
| 94 | GET vs POST in form submission | §3.1 A3 |
| 95 | Session: store name, show other page | §3.1 A4, §4 D10 |
| 96 | Insert record, handle errors | §3.1 A6, §4 D4 |
| 97 | Regex email check returning boolean | §3.1 A7, §4 D16 |
| 98 | Update email, with error handling | §3.1 A8, §4 D8 |
| 99 | Prepared statements and why | §3.1 A9, §2.18 |
| 100 | Sessions keep state across pages | §3.1 A5 |
| 101 | Retrieve and display MySQL data | §3.1 A10, §4 D6 |
| 102 | PHP's role vs static HTML | §3.1 A11, §2.20 |
| 103 | Purpose of `$_PHP_SELF` | §3.1 A12 |
| 104 | Fetch data from DB to webpage | §3.1 A10, §4 D6 |
| 105 | Square root program | §3.1 A13, §4 D13 |
| 106 | `mysql_fetch_array` vs `_assoc` | §3.1 A14, §2.10 |
| 107 | List databases on MySQL server | §3.1 A15, §4 D3 |
| 108 | List data in a table | §3.1 A10 |
| 109 | CREATE operations from PHP | §3.1 A16, §4 D3 |
| 110 | Connection steps (duplicate of 92) | §3.1 A1 |
| 111 | Session importance across requests | §3.1 A5 |
| 112 | Insert + connection/query/errors | §3.1 A6, §4 D4 |
| 113 | What is a cookie + two uses | §3.1 A17, §2.2 |
| 114 | Session vs cookie | §3.1 A2 |
| 115 | Statement to start a session | §3.1 A18 |
| 116 | Basic MySQL connection statement | §3.1 A1, §2.6 |
| 117 | Purpose of CREATE TABLE | §3.1 A16, §2.13 |
| 118 | SQL to add a record + syntax | §3.1 A19, §2.14 |
| 119 | Purpose of DELETE | §3.1 A20, §2.15 |
| 120 | Purpose of SELECT | §3.1 A21, §2.16 |
| 121 | SQL to modify existing records | §3.1 A22, §2.15 |
| 122 | What is dynamic content | §3.1 A11 |
| 123 | Three advantages of sessions | §3.1 A5 |
| 124 | Cookie syntax with expiry | §3.1 A17, §5 |
| 125 | Purpose of `session_start()` | §3.1 A18 |
| 126 | Purpose of `mysqli_query()` | §3.1 A23, §2.9 |
| 127 | Why WHERE matters in UPDATE/DELETE | §3.1 A24 |
| 128 | What `mysqli_fetch_assoc()` is for | §3.1 A25, §2.10 |
| 129 | Two sources of dynamic content | §3.1 A26 |
| 229 | Form app: name + email validation ⭐ | §3.2 Q229, §4 D16 |
| 230 | PHP's importance + challenges (10m) | §3.2 Q230 |
| 231 | Dynamic page: date/time + greeting ⭐ | §3.2 Q231, §4 D12 |
| 232 | Username/password/email filled + format | §3.2 Q232 |
| 233 | File uploads + recursive factorial | §3.2 Q233, §4 D14–D15 |
| 234 | Connection step-by-step + patients DB ⭐ | §3.2 Q234 |
| 235 | Regex: extract emails + validate phone | §3.2 Q235 |
| 236 | Regex: replace substring + extract URLs | §3.2 Q236 |
| 237 | Password validation + phone validation | §3.2 Q237 |
| 238 | Cookies + associative array operations | §3.2 Q238 |
| 239 | Cookies create/access/delete + sessions | §3.2 Q239, §4 D10–D11 |
| 240 | MySQLi connection + error handling + program | §3.2 Q240, §4 D2 |
| 241 | CREATE/INSERT/DELETE + student table ⭐ | §3.2 Q241, §4 D3–D4 |
| 242 | Prepared INSERT/DELETE by register no. | §3.2 Q242, §4 D5 |
| 243 | SELECT multi-row → HTML table ⭐ | §3.2 Q243, §4 D6 |
| 244 | UPDATE syntax/precautions + update email ⭐ | §3.2 Q244, §4 D8 |
| 245 | App architecture + products into HTML list | §3.2 Q245 |
| 246 | Session lifecycle + session ID + login time | §3.2 Q246 |
| 247 | Cookies vs sessions + recommend for login | §3.2 Q247 |
| 248 | Full SQL workflow + INSERT success report | §3.2 Q248 |
| 249 | CREATE TABLE types/constraints + employee | §3.2 Q249 |
| 250 | Careful DELETE + prepared delete by dept | §3.2 Q250 |
| 251 | SELECT result processing + marks > 50 | §3.2 Q251 |
| 252 | UPDATE + affected_rows + 10% raise | §3.2 Q252 |
| 253 | Steps for dynamic HTML + students list | §3.2 Q253 |

⭐ = highest probability.

### Six themes — every question is one of these

1. **State** — cookie (client, 4 KB, editable) or session (server, ID cookie)..
2. **Connection** — `mysqli_connect()` / `new mysqli()` + failure check + `close()`..
3. **Fetch loop** — handle → `while ($row = mysqli_fetch_assoc($result))` → `$row["col"]`..
4. **CRUD** — CREATE / INSERT / UPDATE / DELETE, `affected_rows`, `insert_id`..
5. **Prepared statements** — `?` + `bind_param("ssi", …)`; structure and data never mix..
6. **Dynamic pages** — HTML built per request; `<?= ?>`, `while: endwhile`..

---

## 2. Concepts

### 2.1 Why HTTP is stateless (`4:L27–53`)
**What:** each request is a complete, independent message; the server keeps nothing between them (4:L31–33).
- Cheap for 10,000 strangers, fatal the moment you need "logged in": page 1 checks the password, page 2 knows nothing about it.
- Only two memory mechanisms exist (4:L37–51):

| Mechanism | Data lives in | Who can read it |
|---|---|---|
| Cookie | browser storage, replayed per request | the user — and any script (4:L73) |
| Session | server disk/temp | only the server; browser holds an ID (4:L45) |

**Skeleton that opens Q93, 100, 111, 113, 247:** stateless → need memory → two places → client or server.

### 2.2 Cookies (`4:L63–88`)
**What:** a small name/value pair sent in a `Set-Cookie` response header, replayed automatically on every later request to that domain (4:L39).

```php
<?php
// 1. SET — expiry is a Unix timestamp, so "now + seconds"
setcookie("username", "Anu", time() + 3600);      // 1 hour from now

// 2. READ — on any later request, from the superglobal
if (isset($_COOKIE["username"])) {
    echo "Welcome back, " . $_COOKIE["username"];
}

// 3. DELETE — set the same name again with an expiry in the past
setcookie("username", "", time() - 3600);
?>
```

| Argument | What it is | Memorise |
|---|---|---|
| `name` | key you read back | `"username"` |
| `value` | the data, a string | `"Anu"` |
| `expiry` | Unix timestamp to discard at | `time() + 3600` |
| `path` | URLs that receive it | `"/"` = whole site |

**Three rules.** Before any output (4:L65) — headers flush first, one stray space gives *"headers already sent"*; same for `session_start()` (4:L104). Delete by re-setting a past expiry (4:L71) — no `deletecookie()`. Never store secrets (4:L73): the user can edit the file.
**Limits:** ~4 KB (4:L142), a few dozen per domain, sent with every matching request. Good for theme/language, "remember me", last-visited (4:L148).

### 2.3 Sessions (`4:L102–124`)
**What:** server-side storage for one visitor, keyed by a **session ID** sent as a cookie (`PHPSESSID`) (4:L45, 4:L106).

```php
<?php
session_start();                       // 1. begin or resume — very first line
$_SESSION["user_id"] = 101;            // 2. store (server-side)
$_SESSION["role"]    = "student";
echo $_SESSION["user_id"];             // 3. read

// 4. on logout
session_unset();                       //    clear the $_SESSION array
session_destroy();                     //    delete the server-side session file
?>
```

| Call | Effect | Exam detail |
|---|---|---|
| `session_start()` | reads the incoming `PHPSESSID`, else mints one | before every `$_SESSION` access **and** all output (4:L104) |
| `$_SESSION["k"] = v` | writes server-side | only the ID reaches the client |
| `unset($_SESSION["k"])` | removes one key | `session_unset()` removes all (standard) |
| `session_destroy()` | deletes the server file | does not empty `$_SESSION` now — `session_unset()` first (standard) |

**Lifecycle (Q246):** request → `session_start()` → no ID cookie, so PHP mints one and sends `Set-Cookie: PHPSESSID=…` → server makes a file keyed by it → later requests replay the cookie → `session_start()` loads it → logout: `session_unset()` + `session_destroy()`.
**ID = the whole security model:** whoever holds it *is* you — keep it out of URLs, regenerate at login with `session_regenerate_id(true)` (standard).

### 2.4 Cookie vs session (`4:L136–160`)

| Point | Cookie | Session |
|---|---|---|
| Storage | browser/client (4:L140) | server (4:L152) |
| Travels | the **data** | only the **ID** |
| Size | ~4 KB (4:L142) | server disk |
| Security | readable/editable — never sensitive (4:L144) | data stays server-side (4:L154) |
| Lifetime | your expiry (4:L146) | browser close / timeout (4:L156) |
| Setup | `setcookie()` before output | `session_start()` every page (4:L158) |
| Good for | preferences (4:L148) | login, cart (4:L160) |

**Four axes:** where it lives, how big, how safe, how long — Q247 asks exactly these; Q93/Q114 are the prose version.

### 2.5 Why pair PHP with MySQL (`4:L170–195`)
- **PHP forgets** everything at script end — variables, form data, sessions (4:L176).
- **MySQL persists and shares** — relational tables on disk, same for every request and user (4:L182).
- **Why MySQL** — free, default on shared hosting, the **M** in LAMP (4:L188).
- **The bridge is an extension** — MySQLi for this course, PDO the database-agnostic alternative (4:L194).

**Architecture, one line:** browser → Apache → PHP → MySQL → rows → PHP prints HTML → browser; the browser never sees SQL or the password..

### 2.6 Connecting: `mysqli_connect()` (`4:L206–230`)
**What:** open a connection to the MySQL server; every query needs one first.

```text
mysqli_connect(host, username, password, database)   ->  connection handle (object) | false
```

- Procedural: `mysqli_connect(host, username, password, database)` → handle, or `false`.
- Failure check: `if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }` (PHP 8.1+ throws `mysqli_sql_exception` instead of returning `false`).
- OO style: `new mysqli(...)`, then `$conn->connect_error`, `$conn->query()`, `$conn->close()`.

```php
<?php
$conn = mysqli_connect("localhost", "root", "password", "college_db");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully";

mysqli_close($conn);          // optional: PHP closes it at script end anyway
?>
```

| Argument | Meaning | Typical value |
|---|---|---|
| `host` | machine running MySQL | `"localhost"` (4:L214) |
| `username` | MySQL account | `"root"` on XAMPP |
| `password` | its password | `""` locally, never in production |
| `database` | database to open | `"college_db"`; optional — else `mysqli_select_db()` |

**Trap:** query before connect = fatal; credentials belong in a config file, never in the repo (4:L286).

### 2.7 The same connection, object-oriented (`4:L244–268`)

```php
<?php
$conn = new mysqli("localhost", "root", "password", "college_db");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";

$conn->close();
?>
```

| Job | Procedural | Object-oriented |
|---|---|---|
| Connect | `mysqli_connect(...)` | `new mysqli(...)` |
| Connect error | `mysqli_connect_error()` | `$conn->connect_error` |
| Query | `mysqli_query($conn, $sql)` | `$conn->query($sql)` |
| Fetch row | `mysqli_fetch_assoc($result)` | `$result->fetch_assoc()` |
| Rows affected | `mysqli_affected_rows($conn)` | `$conn->affected_rows` |
| Last insert id | `mysqli_insert_id($conn)` | `$conn->insert_id` |
| Error text | `mysqli_error($conn)` | `$conn->error` |
| Close | `mysqli_close($conn)` | `$conn->close()` |

**Write procedural in the exam** — 90% of the deck; know the OO column for "using MySQLi" questions.
**Trap:** mixing the two mid-script is the classic lost mark.

### 2.8 Connection error handling + four practices (`4:L280–305`)
**Why check:** failure returns `false`; later calls then get `false` where a handle belongs (4:L290–292).

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
```

- `die("message")` prints and **stops the script** — nothing sensible is left without a database.
- `mysqli_connect_error()` gives the reason (`Access denied for user 'root'@'localhost'`); in production log it, show a generic page (standard).

**Four practices** (4:L284–304): credentials in a config file out of version control (4:L286); always check failure (4:L290); close when done (4:L296); prepared statements are the production path (4:L302–304).
**PHP 8.1 nuance (standard):** mysqli now *throws* `mysqli_sql_exception`, so `if (!$conn)` never fires. Both-worlds form: `try { … } catch (mysqli_sql_exception $e) { die($e->getMessage()); }`. Write the deck's form; mention exceptions only when asked how to harden it.

### 2.9 Running a query: `mysqli_query()` (`4:L316–337`)
```php
<?php
$sql = "SELECT name, marks FROM students";
$result = mysqli_query($conn, $sql);

if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}
?>
```

| Query kind | Returns | You then |
|---|---|---|
| `SELECT`, `SHOW`, `DESCRIBE` | **result handle** (`mysqli_result`) | `mysqli_fetch_assoc()` in a loop |
| `INSERT`, `UPDATE`, `DELETE`, `CREATE` | `true` | `affected_rows()` / `insert_id()` |

**Traps:** `fetch_assoc()` on a `true` → *"Call to a member function fetch_assoc() on bool"*; `$sql` is just a string, so input concatenated into it is how injection happens (4:L326) → §2.18..

### 2.10 Reading rows: `mysqli_fetch_assoc()` (`4:L351–370`, `4:L383–393`)

```php
<?php
while ($row = mysqli_fetch_assoc($result)) {
    echo $row["name"] . " " . $row["marks"] . "<br>";
}

echo "Total rows: " . mysqli_num_rows($result);
?>
```

**Termination:** it returns one row as an associative array (`["column" => value]`) and advances a pointer (4:L355–357); with none left it returns **`NULL`**, which is falsy — that ends the `while`, no counter needed.

| Function | Returns | Access | Note |
|---|---|---|---|
| `mysqli_fetch_assoc()` | associative | `$row["name"]` | the default (4:L387) |
| `mysqli_fetch_array()` | both key sets | `$row["name"]` / `$row[0]` | values stored twice (4:L388) |
| `mysqli_fetch_row()` | indexed | `$row[0]` | breaks on column reorder (4:L389) |
| `mysqli_fetch_object()` | object | `$row->name` | for OO (4:L390) |

**Counters:** `mysqli_num_rows($result)` counts without consuming (4:L361, 4:L391); `mysqli_affected_rows($conn)` counts rows *changed* (§2.17); `mysqli_free_result()` frees memory (standard)..

### 2.11 The five-step cycle (`4:L399`, `4:L405–419`)

```text
1. Build SQL string
2. mysqli_query()
3. Result handle returned
4. while + fetch_assoc() loops through rows
5. echo HTML for each row
        |
        v
Browser displays the finished table
```

> "This five-step pattern — query, fetch, loop, echo — repeats throughout the rest of this module, regardless of what the query actually does." (4:L419)

```php
<?php
mysqli_free_result($result);   // release the result set
mysqli_close($conn);           // release the connection
?>
```

### 2.12 CREATE TABLE (`4:L431–453`)
**What:** declare the schema — columns, types, constraints — once; no INSERT works before it exists (4:L435).

```sql
CREATE TABLE students (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    name   VARCHAR(50),
    marks  INT,
    joined DATE
);
```

| Piece | Meaning |
|---|---|
| `INT AUTO_INCREMENT PRIMARY KEY` | unique, self-numbering id to target with `WHERE id = …` (4:L437) |
| `VARCHAR(50)` / `TEXT` | short text / long text |
| `DATE` | calendar date — `joined` |
| `DECIMAL(10,2)` | exact money, never `FLOAT` (standard) |
| `NOT NULL` / `UNIQUE` | no empty / no duplicate (standard) |

```php
<?php
$sql = "CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT,
    joined DATE
)";

if (!mysqli_query($conn, $sql)) {
    die("Create failed: " . mysqli_error($conn));
}
echo "Table created";
?>
```

**Traps:** running it every page load → *"table already exists"* (use `IF NOT EXISTS` or run once, standard); no `PRIMARY KEY` → duplicate rows you cannot address..

### 2.13 INSERT (`4:L468–490`)
**What:** `INSERT INTO table (columns) VALUES (values)` — the explicit column list is safest (4:L472).

```php
<?php
$name  = $_POST["name"];
$marks = (int)$_POST["marks"];

$sql = "INSERT INTO students (name, marks)
        VALUES ('$name', $marks)";

if (!mysqli_query($conn, $sql)) {
    die("Insert failed: " . mysqli_error($conn));
}

echo "New ID: " . mysqli_insert_id($conn);
?>
```

- **Strings quoted, numbers not** (4:L474) — unquote a string and MySQL reads it as a column: `Unknown column 'Anu' in 'field list'`.
- **`mysqli_insert_id($conn)`** gives the new `AUTO_INCREMENT` id (4:L476).
- **Raw input in `$sql` is injection** (4:L478); `(int)` covers numbers, prepared statements cover the rest (§2.18).
**Trap:** `INSERT INTO students VALUES (…)` without a column list needs every column in table order and breaks when one is added (standard)..

### 2.14 DELETE (`4:L505–525`)
```php
<?php
$id = (int)$_POST["id"];

$sql = "DELETE FROM students WHERE id = $id";

if (!mysqli_query($conn, $sql)) {
    die("Delete failed: " . mysqli_error($conn));
}

echo mysqli_affected_rows($conn) . " row(s) deleted";
?>
```

- `WHERE` limits deletion to matching rows (4:L509); **omit it and the table empties** (4:L511) — no undo.
- `mysqli_affected_rows($conn)` says how many went (4:L513).
- **Preview** with the same condition as a `SELECT` first (4:L515).
**Trap:** a `WHERE` matching nothing *succeeds* with 0 rows, no error — only the count reveals it (4:L687–689)..

### 2.15 UPDATE (`4:L630–652`)
```php
<?php
$id    = (int)$_POST["id"];
$marks = (int)$_POST["marks"];

$sql = "UPDATE students
        SET marks = $marks
        WHERE id = $id";

if (!mysqli_query($conn, $sql)) {
    die("Update failed: " . mysqli_error($conn));
}

echo mysqli_affected_rows($conn) . " row(s) updated";
?>
```

- Multiple columns: `SET col1 = val1, col2 = val2` — one `SET`, commas.
- **No `WHERE` = every row** — "almost always a mistake" (4:L638).
- Compute in SQL: `SET salary = salary * 1.10` (Q252).
**Subtlety (standard):** `affected_rows` counts rows whose values **actually changed** — re-saving the same value returns 0 though the row matched; `mysqli_info()` or a `SELECT` gives the match count..

### 2.16 SELECT (`4:L558–580`, `4:L595–615`)
**What:** the only statement that **returns** rows; the rest merely succeed or fail (4:L560) — so only this one is looped.

| Clause | Purpose | Example |
|---|---|---|
| `SELECT *` / `col1, col2` | all / chosen columns | `SELECT name, marks FROM students` (4:L564) |
| `WHERE` | filters rows | `WHERE marks >= 75` (4:L566) |
| `ORDER BY col ASC/DESC` | sorts | `ORDER BY marks DESC` (4:L599) |
| `LIMIT n` / `LIMIT offset, count` | cap / page | `LIMIT 5`, `LIMIT 10, 5` (4:L601–603) |
| `LIKE` | pattern | `WHERE name LIKE 'A%'` (4:L568) |

**Operators** (4:L568): `=`, `!=`, `>`, `<`, `>=`, `<=`, `LIKE` — `%` is "any characters": `'A%'`, `'%a'`, `'%an%'`.

```php
<?php
$sql = "SELECT name, marks FROM students
        WHERE marks >= 50
        ORDER BY marks DESC
        LIMIT 5";

$result = mysqli_query($conn, $sql);

if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}

while ($row = mysqli_fetch_assoc($result)) {
    echo $row["name"] . " — " . $row["marks"] . "<br>";
}
?>
```

**Clause order is fixed:** `SELECT … FROM … WHERE … ORDER BY … LIMIT …` — swap two and MySQL errors..

### 2.17 `affected_rows` (`4:L513`, `4:L640`, `4:L687–689`)
```php
<?php
mysqli_query($conn, $sql);                 // some UPDATE or DELETE
echo mysqli_affected_rows($conn);          // rows actually touched
echo $conn->affected_rows;                 // OO form — same number
?>
```

| Function | Counts | On |
|---|---|---|
| `mysqli_affected_rows($conn)` | rows **changed** | INSERT / UPDATE / DELETE |
| `mysqli_num_rows($result)` | rows **returned** | SELECT |
| `mysqli_insert_id($conn)` | id **generated** | INSERT + AUTO_INCREMENT |

**Why it is a habit** (4:L687–689): a query "succeeds" with 0 affected rows — wrong `WHERE`, no match, duplicate — and raises no error. The count is the only signal..

### 2.18 SQL injection and prepared statements (`4:L302–304`, `4:L326`, `4:L681–683`)
**The bug:** data concatenated into the SQL text, so the database cannot tell data from code (4:L326).

```php
<?php
$email = $_POST["email"];
$sql = "SELECT * FROM users WHERE email = '$email'";
$result = mysqli_query($conn, $sql);
?>
```

Submit `' OR '1'='1` and the statement becomes:

```sql
SELECT * FROM users WHERE email = '' OR '1'='1'
```

…true for every row, so the table leaks; `'; DROP TABLE users; --` destroys it.

```php
<?php
$email = $_POST["email"];

$stmt = mysqli_prepare($conn, "SELECT id, name FROM users WHERE email = ?");
mysqli_stmt_bind_param($stmt, "s", $email);
mysqli_stmt_execute($stmt);

$result = mysqli_stmt_get_result($stmt);
while ($row = mysqli_fetch_assoc($result)) {
    echo htmlspecialchars($row["name"]);
}
mysqli_stmt_close($stmt);
?>
```

| Letter | Type | For |
|---|---|---|
| `s` | string | names, emails, dates |
| `i` | integer | ids, marks |
| `d` | double | prices |
| `b` | blob | binary |

`bind_param("ssi", $name, $email, $age)` = string, string, int — one letter per `?`, same order.

**Why it stops injection (the marked sentence):** the statement is compiled **before** the values arrive, so a value can never become syntax — `' OR '1'='1` is stored as a literal 13-character email. Bonus: one prepared statement re-executes with new values, faster for bulk work.
**Other defences** (4:L675–677): `(int)` cast for numbers, `SELECT` the `WHERE` first (4:L669). → Q99, 242, 250; precautions halves of Q244/Q250.

### 2.19 Mixing PHP into HTML (`4:L735–755`)

```php
<table border="1">
<?php while ($row = mysqli_fetch_assoc($result)): ?>
<tr>
    <td><?php echo htmlspecialchars($row["name"]); ?></td>
    <td><?php echo $row["marks"]; ?></td>
</tr>
<?php endwhile; ?>
</table>
```

- **`while (...):` + `endwhile;`** — the *alternative syntax*, because a lone `}` inside HTML is unreadable (4:L739); same for `if: endif;`, `foreach: endforeach;`.
- **`<?= $expr ?>` = `<?php echo $expr; ?>`** (4:L790, 3:L55).
- **A file may open and close `<?php ?>` many times** (4:L739).
- **`htmlspecialchars()` on every user value** (4:L743) turns `<` into `&lt;`, so `<script>alert(1)</script>` prints as text — XSS defence, a marked point.

```php
<?php while ($row = mysqli_fetch_assoc($result)) { ?>
<tr><td><?= htmlspecialchars($row["name"]) ?></td></tr>
<?php } ?>
```

→ Q229, 231, 245, 253. The colon/`endwhile` pair is the module's most commonly lost mark.

### 2.20 The complete dynamic page (`4:L770–792`)

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$result = mysqli_query($conn, "SELECT name, marks FROM students");

if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}
?>
<table border="1">
<tr><th>Name</th><th>Marks</th></tr>
<?php while ($row = mysqli_fetch_assoc($result)): ?>
<tr>
    <td><?= htmlspecialchars($row["name"]) ?></td>
    <td><?= $row["marks"] ?></td>
</tr>
<?php endwhile; ?>
</table>
<?php
mysqli_free_result($result);
mysqli_close($conn);
?>
```

**Three steps** (4:L774–778): connect, query, loop and echo each row. The deck's claim: *"This exact shape — connect, query, loop, render — is the backbone of almost every PHP page that shows database content"* (4:L780).
**What "dynamic" means** (4:L705): the `.php` file never changes; the HTML it emits is rebuilt per request. Add a row in phpMyAdmin, refresh, the page changes with no edit — answers Q102, Q122, Q129, half of Q253.
**Layering** (4:L717, Q245): data access, business logic, presentation visible as three concerns — the precursor to Module 5's MVC.

### 2.21 Five clusters your deck never covers (all "standard, not in your deck")

**(a) `$_SERVER['PHP_SELF']` (Q103).** The bank writes `$_PHP_SELF` — a typo, no such superglobal. The real one is the executing script's path, used as a form action so the form posts to itself:

```php
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
```

`htmlspecialchars()` matters: without it a crafted URL injects script into the `action` attribute.

**(b) Regex (Q97, 235, 236, 237)** — a Module 3 topic (3:L568–586, phone table 3:L597–607):

```php
<?php
if (preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
    echo "Valid email";
}
$clean = preg_replace("/[0-9]/", "", "Room12A");   // "RoomA"
?>
```

- `preg_match()` returns `1` / `0` / `false` on error → compare `== 1` or cast to bool.
- `preg_match_all()` fills an array with **every** match — how you extract all emails from text.
- Delimiters `/…/` required; `^` `$` anchor; `{n}` = exactly n times (3:L607).

**(c) File upload (Q233a)** — `$_FILES`, `enctype`, `move_uploaded_file()`; drill D15.
**(d) `sqrt()` / factorial / `date()` (Q105, 231, 233b)** — plain PHP functions; drills D12–D14.

**(e) `SHOW DATABASES` (Q107)** — SQL, not a PHP function:

```php
<?php
$result = mysqli_query($conn, "SHOW DATABASES");
while ($row = mysqli_fetch_row($result)) {   // index 0 = database name
    echo $row[0] . "<br>";
}
?>
```

`SHOW TABLES` is the same one level down; `DESCRIBE students` lists columns.

---

## 3. Answer bank

### 3.1 3-mark answers (Part A)

3 marks = three facts, or one short code block plus a line. Duplicates are merged into master answers; the numbers each covers are listed.

**A1 — Steps to establish a PHP–MySQL connection · also answers Q110, Q116, Q92**

1. **Connect** — `mysqli_connect(host, user, password, database)` → handle, or `false`.
2. **Check** — `if (!$conn) die(mysqli_connect_error());` stops the script immediately.
3. **Use, close** — `$conn` first in every `mysqli_query()`, then `mysqli_close($conn)`.

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }
echo "Connected successfully";
mysqli_close($conn);
?>
```

*OO variant if asked for object-oriented:* `$conn = new mysqli("localhost","root","","college_db"); if ($conn->connect_error) die($conn->connect_error);`

**A2 — `$_SESSION` vs `$_COOKIE` · also answers Q93, Q114**

1. **Storage** — session on the server, browser holds only the ID; cookie on the client, data itself.
2. **Limits** — session large and safe for secrets; cookie ~4 KB and user-editable.
3. **Setup, use** — `session_start()` first for login/cart; `setcookie()` before output for preferences.

Full table: §2.4.

**A3 — GET vs POST · Q94** *(Module 3: 3:L619–640)*

| | GET | POST |
|---|---|---|
| Data goes | in the URL query string | in the request body |
| Visible in address bar | yes | no |
| Length limit | ~2000 chars, browser-dependent | effectively none |
| Bookmark / cache / resend-safe | yes | no |
| Use for | searches, filters, ids | passwords, inserts, updates |
| PHP reads it with | `$_GET["f"]` | `$_POST["f"]` |

Forms default to GET — always write `method="post"` explicitly for anything that changes data or carries a password.

**A4 — Session: start, store name, display on another page · Q95**

1. **Store** — `session_start()` then `$_SESSION["username"] = "Anu";` on page 1.
2. **Separate request** — the browser replays the `PHPSESSID` cookie to page 2 automatically.
3. **Read** — `session_start()` again on page 2, then `echo $_SESSION["username"];`.

```php
<?php
session_start();
$_SESSION["username"] = "Anu";
echo "Stored. <a href='page2.php'>Next page</a>";
?>
```

```php
<?php
session_start();                                  // must repeat on every page
echo "Welcome, " . $_SESSION["username"];
?>
```

**A5 — Sessions keep state across pages; advantages · also answers Q100, Q111, Q123**

1. **Stateless HTTP** — page 1's login is invisible to page 2 (4:L31–33).
2. **Server-side data** — only an ID travels; credentials never cross the wire (4:L45).
3. **Three wins** — security (not client-visible), capacity (beyond 4 KB), continuity (4:L152–160).

**A6 — Insert a record with error handling · also answers Q96, Q112**

1. **Connect, check** — `mysqli_connect(...)` then `if (!$conn) die(mysqli_connect_error());`.
2. **Build** — cast the number `(int)`, quote the string, explicit column list.
3. **Branch** — on `true` echo `mysqli_insert_id($conn)`, on `false` echo `mysqli_error($conn)`.

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$name  = $_POST["name"];
$marks = (int)$_POST["marks"];

$sql = "INSERT INTO students (name, marks) VALUES ('$name', $marks)";

if (mysqli_query($conn, $sql)) {
    echo "Record inserted. New id = " . mysqli_insert_id($conn);
} else {
    echo "Insert failed: " . mysqli_error($conn);
}
mysqli_close($conn);
?>
```

**A7 — Function that validates an email with regex and returns a boolean · Q97** *(regex: 3:L568–586)*

1. **Function** — `function isValidEmail($email) { return (bool) preg_match($pattern, $email); }`.
2. **Pattern** — `/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/` anchors whole string, literal dot, 2+ letter TLD.
3. **Return** — `preg_match()` gives `1`/`0`, so cast to a real boolean.

```php
<?php
function isValidEmail($email) {
    return (bool) preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email);
}

if (isValidEmail("anu@saintgits.org")) { echo "Valid"; }
else { echo "Invalid"; }
?>
```

**A8 — Update a user's email with error handling · Q98**

1. **Shape** — `UPDATE users SET email = '$email' WHERE id = $id`, id cast to `(int)`.
2. **Check** — `if (!mysqli_query(...)) die("Update failed: " . mysqli_error($conn));`.
3. **Report** — `mysqli_affected_rows($conn)`; 0 means the id never matched.

```php
<?php
$id    = (int)$_POST["id"];
$email = $_POST["email"];

$sql = "UPDATE users SET email = '$email' WHERE id = $id";

if (!mysqli_query($conn, $sql)) {
    die("Update failed: " . mysqli_error($conn));
}
echo mysqli_affected_rows($conn) . " row(s) updated";
?>
```

**A9 — Prepared statements and why · Q99** *(4:L302–304, 4:L683)*

1. **Template first** — `mysqli_prepare()` sends SQL with `?` placeholders; MySQL compiles it before data arrives.
2. **Bind after** — `mysqli_stmt_bind_param($stmt, "ssi", $name, $email, $age)`, one letter per placeholder.
3. **Why safe** — input is only ever a value, never syntax; the compiled statement also re-executes cheaply.

```php
<?php
$stmt = mysqli_prepare($conn, "INSERT INTO students (name, marks) VALUES (?, ?)");
mysqli_stmt_bind_param($stmt, "si", $name, $marks);   // s = string, i = int
mysqli_stmt_execute($stmt);
mysqli_stmt_close($stmt);
?>
```

**A10 — Retrieve and display MySQL data on a page · also answers Q101, Q104, Q108**

1. **Connect, build** — open the connection, write the `SELECT`.
2. **Query** — `mysqli_query()` returns a **result handle**, not data.
3. **Loop** — `while ($row = mysqli_fetch_assoc($result))` pulls one row per pass, stops at `NULL`.

```php
<?php
$result = mysqli_query($conn, "SELECT name, marks FROM students");
if (!$result) { die("Query failed: " . mysqli_error($conn)); }

echo "<table border='1'><tr><th>Name</th><th>Marks</th></tr>";
while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr><td>" . htmlspecialchars($row["name"]) . "</td><td>" . $row["marks"] . "</td></tr>";
}
echo "</table>";
?>
```

**A11 — PHP's role in dynamic content vs static HTML · also answers Q102, Q122**

1. **Static** — the `.html` file *is* the response; identical bytes for every visitor.
2. **Dynamic** — a script runs per request and sends the HTML it produced *this* time (4:L705).
3. **Server-side** — PHP reads the DB, applies logic, loops; the browser sees only HTML, never SQL.

**A12 — Purpose of `$_PHP_SELF` · Q103**

1. **No such variable** — the real superglobal is `$_SERVER['PHP_SELF']`, the executing script's path.
2. **Self-post** — as a form `action` it lets one file both display and process the form.
3. **Escape it** — `htmlspecialchars()`, or a crafted URL injects script into the attribute.

```php
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
```

**A13 — Square root program · Q105**

1. **Function** — `sqrt($num)` returns the root; `sqrt(-1)` yields `NAN`.
2. **Output** — `echo "Square root of $num is " . sqrt($num);` gives `… 25 is 5`.
3. **Guard** — test `$num < 0` first, otherwise print that the root is not real.

```php
<?php
$num = 25;
if ($num < 0) {
    echo "Square root of a negative number is not real";
} else {
    echo "Square root of $num is " . sqrt($num);
}
?>
```

**A14 — `mysql_fetch_array()` vs `mysql_fetch_assoc()` · Q106**

1. **Keys** — `fetch_array()` gives numeric and associative; `fetch_assoc()` associative only.
2. **Cost** — array stores each value twice (bigger, magic indexes); assoc is smaller and readable.
3. **Both** — one row per call, `NULL` at the end; the bank's `mysql_` prefix is the dead API.

Modern names are `mysqli_fetch_*`; the full table is §2.10.

**A15 — List the databases on the MySQL server · Q107** *(standard — no slide)*

1. **Connect** — `mysqli_connect("localhost", "root", "")`, no database argument.
2. **Query** — `mysqli_query($conn, "SHOW DATABASES")` returns one column per database.
3. **Fetch** — `mysqli_fetch_row()` and echo `$row[0]`.

```php
<?php
$conn = mysqli_connect("localhost", "root", "");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$result = mysqli_query($conn, "SHOW DATABASES");
while ($row = mysqli_fetch_row($result)) {
    echo $row[0] . "<br>";
}
mysqli_close($conn);
?>
```

`SHOW TABLES` and `DESCRIBE tablename` are the same pattern one level down.

**A16 — CREATE operations from PHP; purpose of CREATE TABLE · also answers Q109, Q117**

1. **Defines structure** — column names, types, keys, constraints; no data goes in first (4:L433).
2. **Setup-time** — run once, not on every page load (4:L441); `IF NOT EXISTS` if unsure.
3. **From PHP** — a string through `mysqli_query()` returning only `true`/`false`, no rows.

```php
<?php
$sql = "CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT,
    joined DATE
)";
if (mysqli_query($conn, $sql)) { echo "Table created"; }
else { echo "Error: " . mysqli_error($conn); }
?>
```

**A17 — What is a cookie, two uses, syntax with expiry · also answers Q113, Q124**

1. **Definition** — a name/value pair the browser stores and replays on later requests (4:L39).
2. **Two uses** — preferences (theme, language) and "remember me" tracking (4:L148).
3. **Syntax** — `setcookie("username", "Anu", time() + 3600, "/");` — name, value, timestamp expiry, path.

Before any output; user-visible, so never store secrets (4:L65, 4:L73).

**A18 — Purpose of `session_start()` · also answers Q115, Q125**

1. **Starts or resumes** — reads the incoming `PHPSESSID`, or mints and sends one (4:L106).
2. **Loads data** — the session file fills `$_SESSION`, making it usable.
3. **Must be first** — before output and any `$_SESSION` access (4:L104); `session_start();` on every page using sessions.

**A19 — SQL command to add a record, with syntax · Q118**

1. **Form** — `INSERT INTO table_name (col1, col2, col3) VALUES (val1, val2, val3);`.
2. **Quoting** — strings in single quotes, numbers bare, column list always explicit (4:L472).
3. **From PHP** — pass the string to `mysqli_query()`, confirm with `mysqli_insert_id()` (4:L476).

```sql
INSERT INTO students (name, marks, joined) VALUES ('Anu', 88, '2026-11-08');
```

**A20 — Purpose of DELETE · Q119**

1. **Removes rows** — `DELETE FROM students WHERE id = 5;` permanently (4:L509).
2. **Irreversible** — no undo, hence the `WHERE` discipline (4:L511).
3. **No rows back** — only success/failure; `affected_rows()` reports the count (4:L513).

Safe practice: the same condition as a `SELECT` first (4:L515).

**A21 — Purpose of SELECT · Q120**

1. **Reads data** — the only statement returning rows, not a status (4:L560).
2. **Shape** — `SELECT cols FROM table WHERE cond ORDER BY col LIMIT n` (4:L562–603).
3. **In PHP** — returns a result handle you iterate with `mysqli_fetch_assoc()` (4:L355).

That is how dynamic pages get content: same query, fresh rows (4:L705).

**A22 — SQL command to modify existing records · Q121**

1. **Form** — `UPDATE table_name SET column = value WHERE condition;`.
2. **Multiple columns** — comma-separate assignments after one `SET`; no `WHERE` updates every row (4:L638).
3. **Confirm** — `mysqli_affected_rows()` says how many rows actually changed (4:L640).

```sql
UPDATE students SET marks = 92 WHERE id = 5;
```

**A23 — Purpose of `mysqli_query()` · Q126**

1. **Sends one statement** — SELECT, INSERT, UPDATE, DELETE or CREATE over an open connection (4:L320).
2. **Signature** — `mysqli_query($conn, $sql)`; `$conn` always first.
3. **Two returns** — a result handle for SELECT/SHOW, `true`/`false` for writes; check with `mysqli_error()`.

**A24 — Why WHERE matters in UPDATE/DELETE · Q127**

1. **Selects rows** — the only thing between one row and the whole table (4:L509, 4:L638).
2. **Without it** — `UPDATE` overwrites all rows, `DELETE` empties the table (4:L511).
3. **Verify first** — run it as `SELECT … WHERE …`; a plausible clause can still match 0.

**A25 — What `mysqli_fetch_assoc()` is for · Q128**

1. **Fetches next row** — as an associative array keyed by column name: `$row["name"]` (4:L355).
2. **Advances a pointer** — returns `NULL` when rows run out, which terminates the `while` (4:L357).
3. **Only on result handles** — never on the `true` from INSERT/UPDATE/DELETE (4:L359).

**A26 — Two sources of dynamic content · Q129**

1. **A database** — rows read with `SELECT` at request time, the module's main source (4:L705).
2. **Server-side/environment data** — `date()`, `$_POST`, session/cookie values, file contents (standard).
3. **Computation** — totals, filtered lists, formatted numbers, as in the Q231 time-of-day greeting.

### 3.2 14-mark answers (Part B)

#### Q229 — Form app: name + email validation

**Structure (marks):** 4 HTML form · 6 validation (empty + regex) · 3 personalised welcome · 1 request/response explanation.

**Answer:**

```php
<?php
$name = $email = "";
$errors = array();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name  = trim($_POST["name"]);
    $email = trim($_POST["email"]);

    if (empty($name)) {
        $errors[] = "Name is required";
    }
    if (empty($email)) {
        $errors[] = "Email is required";
    } elseif (!preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
        $errors[] = "Email format is invalid";
    }

    if (count($errors) == 0) {
        echo "<h2>Welcome, " . htmlspecialchars($name) . "!</h2>";
        echo "<p>Your email " . htmlspecialchars($email) . " has been accepted.</p>";
    } else {
        foreach ($errors as $e) { echo "<p style='color:red'>$e</p>"; }
    }
}
?>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
    Name:  <input type="text" name="name"><br>
    Email: <input type="text" name="email"><br>
    <input type="submit" value="Submit">
</form>
```

- **Self-post** — the form posts back to the same script via `$_SERVER['PHP_SELF']`.
- **Two requests** — `REQUEST_METHOD == "POST"` separates display from submission.
- **Clean, test** — `trim()`, `empty()`, then `preg_match()` for shape.
- **Accumulate** — errors pile in an array; success escapes with `htmlspecialchars()`.
- **Extension:** insert the record with a prepared statement (D5).

**Traps:**
- `action=""` self-posts too, but `$_PHP_SELF` is the expected answer.
- Echoing `$name` raw loses the XSS mark; `isset($_POST["name"])` alone is weaker than `REQUEST_METHOD`.

#### Q230 — Importance of PHP + challenges (10 of the 14 marks)

**Structure (marks):** 5 why PHP matters · 3 how it produces dynamic content · 2 challenges.

**Answer** (essay, no code):

- **Free, ubiquitous** — open-source, every shared host, the P in LAMP (4:L188); big ecosystem, cheap hosting and hiring.
- **Purpose-built** — mixes with HTML, talks to MySQL directly (4:L194); low learning curve.
- **Dynamic content** — server-side per request: read DB, apply rules, emit HTML from live data (4:L705).
- **Interactivity** — `$_GET`/`$_POST` → validate → query → respond; cookies/sessions add memory (4:L31–51).
- **Challenges + defence** — injection (prepared statements, 4:L326); XSS (escape output); reruns per request (cache); credentials in code (config file, 4:L286); SQL+logic+HTML in one file (MVC, 4:L717); `mysql_*` vs `mysqli`; PHP 5/7/8 drift.

**Traps:**
- 10 marks — do not spend it all on "it is free".
- Name every challenge **with** its defence.

#### Q231 — Dynamic page: date/time greeting

**Structure (marks):** 3 `date()` + timezone · 4 hour extraction + if/elseif · 3 formatted date · 2 per-request generation · 2 presentation.

**Answer:**

```php
<?php
date_default_timezone_set("Asia/Kolkata");

$hour = (int) date("H");          // 00–23

if ($hour < 12) {
    $greeting = "Good morning";
} elseif ($hour < 17) {
    $greeting = "Good afternoon";
} elseif ($hour < 21) {
    $greeting = "Good evening";
} else {
    $greeting = "Good night";
}
?>
<h1><?= $greeting ?>, visitor!</h1>
<p>Today is <?= date("l, d F Y") ?> and the time is <?= date("h:i:s A") ?>.</p>
```

- **Format letters** — `H` 24-hour, `h` 12-hour, `i` minutes, `s` seconds, `A` AM/PM, `l` weekday, `d` day, `F` month, `Y` year.
- **Cast** — `date("H")` is a string; `(int)` makes the comparisons numeric.
- **Dynamic proof** — the file never changes, yet the greeting does (4:L705).

**Traps:**
- No `date_default_timezone_set()` → UTC time that looks wrong.
- `date("h")` is 12-hour and breaks the ranges — use `H`.

#### Q232 — Username/password/email filled + format

**Structure (marks):** 4 form · 4 `empty()` on all three · 4 regex/`filter_var` email test · 2 error display or success message.

**Answer:**

```php
<?php
$errors = array();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user  = trim($_POST["username"]);
    $pass  = trim($_POST["password"]);
    $email = trim($_POST["email"]);

    if (empty($user))  { $errors[] = "Username cannot be empty"; }
    if (empty($pass))  { $errors[] = "Password cannot be empty"; }
    if (empty($email)) { $errors[] = "Email cannot be empty"; }
    elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Email is not in a valid format";
    }

    if (empty($errors)) {
        echo "All fields OK. Welcome " . htmlspecialchars($user);
    } else {
        foreach ($errors as $e) { echo "<p>$e</p>"; }
    }
}
?>
<form method="post" action="">
  Username: <input type="text" name="username"><br>
  Password: <input type="password" name="password"><br>
  Email:    <input type="text" name="email"><br>
  <input type="submit">
</form>
```

- Three `empty()` tests = "filled?"; the email gets a second, shape-level test.
- `filter_var($email, FILTER_VALIDATE_EMAIL)` (returns the email or `false`) or the `preg_match` pattern — name the one you use.

**Traps:**
- `empty("0")` is `true` in PHP, so a password of `"0"` is rejected — a known quirk worth a footnote.
- Password *format* is not asked here, only presence.

#### Q233 — File uploads (6) + recursive factorial (8)

**Structure (marks):** 6 upload (form attrs, `$_FILES` keys, validation, `move_uploaded_file`) · 8 factorial (function, base case, recursion, output).

**Answer (a) — upload:**

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["myfile"])) {
    $f = $_FILES["myfile"];

    if ($f["error"] != 0) {
        echo "Upload error code: " . $f["error"];
    } elseif ($f["size"] > 2 * 1024 * 1024) {
        echo "File too large (max 2 MB)";
    } else {
        $target = "uploads/" . basename($f["name"]);
        if (move_uploaded_file($f["tmp_name"], $target)) {
            echo "Uploaded to " . htmlspecialchars($target);
        } else {
            echo "Could not move the file";
        }
    }
}
?>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="myfile">
  <input type="submit" value="Upload">
</form>
```

- `enctype="multipart/form-data"` is **mandatory** or `$_FILES` stays empty.
- `$_FILES["myfile"]` holds `name`, `type`, `tmp_name`, `size`, `error`.
- Temp file must be moved with `move_uploaded_file()` or it dies at script end.
- Error codes: `0` OK, `1` over `upload_max_filesize`, `2` over `MAX_FILE_SIZE`, `3` partial, `4` none chosen.
- `basename()` blocks `../../etc/passwd`; validate size/extension first (standard).

**Answer (b) — recursive factorial:**

```php
<?php
function factorial($n) {
    if ($n <= 1) {
        return 1;                 // base case
    }
    return $n * factorial($n - 1); // recursive case
}
echo "Factorial of 5 is " . factorial(5);   // 120
?>
```

- Trace: `factorial(5)` → `5 * factorial(4)` → … → `5*4*3*2*1 = 120`.
- Base case `$n <= 1` stops it; without it, infinite recursion.
- Iterative: `for ($i = 2, $f = 1; $i <= $n; $i++) $f *= $i;`

**Traps:**
- Missing `enctype` is the most common lost mark; the destination dir must be writable.
- Factorial must `return`, not `echo`.

#### Q234 — Connection steps (10) + patients DB (4)

**Structure (marks):** 10 five steps with code and reason · 4 `CREATE DATABASE` + `CREATE TABLE patients` with sensible columns.

**Answer (a) — five steps:**

1. **Locate** — host `localhost`, MySQL user, password (4:L210).
2. **Connect** — `mysqli_connect(host, user, pass, db)` → handle or `false`.
3. **Verify** — `if (!$conn) die(mysqli_connect_error());` (4:L224–226).
4. **Run statements** — `mysqli_query($conn, $sql)`, checking each and reporting `mysqli_error()` (4:L320–324).
5. **Close** — `mysqli_close($conn)` (4:L216).

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "hospital");
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($conn);
?>
```

Add: credentials in a config file, not inline (4:L286); OO form `new mysqli(...)` + `$conn->connect_error` (4:L258–263).

**Answer (b) — patients schema:**

```sql
CREATE DATABASE hospital;

USE hospital;

CREATE TABLE patients (
    pid       INT AUTO_INCREMENT PRIMARY KEY,
    pname     VARCHAR(50) NOT NULL,
    age       INT,
    gender    VARCHAR(10),
    disease   VARCHAR(100),
    phone     VARCHAR(15),
    admitted  DATE
);
```

From PHP: `mysqli_query($conn, "CREATE DATABASE hospital")` **without** a database argument, then `mysqli_select_db($conn, "hospital")` before creating the table (standard).

**Traps:**
- Creating the table before the database is created or selected.
- `INT` for money instead of `DECIMAL`; forgetting `PRIMARY KEY`.

#### Q235 — Regex: extract emails + validate phone

**Structure (marks):** 7 email extraction with `preg_match_all()` + pattern explanation · 7 phone validation with `preg_match()` + pattern table.

**Answer:**

```php
<?php
// (a) Extract EVERY email address from a block of text
$text = "Contact anu@saintgits.org or hod@college.edu.in, not 123@invalid";

$pattern = "/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/";

if (preg_match_all($pattern, $text, $matches)) {
    echo "Found " . count($matches[0]) . " email(s):<br>";
    foreach ($matches[0] as $email) {
        echo htmlspecialchars($email) . "<br>";
    }
} else {
    echo "No email addresses found";
}
?>
```

```php
<?php
// (b) Validate a 10-digit phone number
function isValidPhone($phone) {
    return (bool) preg_match("/^[0-9]{10}$/", $phone);
}

echo isValidPhone("9876543210") ? "Valid" : "Invalid";   // Valid
echo isValidPhone("98765abcde") ? "Valid" : "Invalid";   // Invalid
?>
```

- **Anatomy** (3:L607): `[A-Za-z0-9._%+-]+` local part · `@` · `[A-Za-z0-9.-]+` domain · `\.` literal dot · `[A-Za-z]{2,}` TLD.
- **Unescaped `.`** means "any character" — it would match `a@b,com`.
- **Phone**: `^…$` stops a match inside longer strings (`"98765432109"`); `{10}` = exactly ten digits; Indian mobiles `^[6-9][0-9]{9}$` (standard).
- `preg_match_all()` returns the **count** and fills `$matches[0]`; `preg_match()` stops at the first.

**Traps:**
- `preg_match` returns `1`/`0`, not booleans — a strict `=== true` fails.
- No delimiters `/…/` is a fatal pattern error; `$matches[1]` is the first group, `$matches[0]` the whole match.

#### Q236 — Regex: replace substring + extract URLs

**Structure (marks):** 7 `preg_replace()` literal + pattern · 7 URL extraction with `preg_match_all()`.

**Answer:**

```php
<?php
// (a) Replace a substring — plain and case-insensitive
$text = "Welcome to the world of PHP. The world is big.";

$new = preg_replace("/world/i", "universe", $text);
echo $new;
// Welcome to the universe of PHP. The universe is big.

// Replace with a back-reference: swap "Anu Thomas" -> "Thomas, Anu"
$name = "Anu Thomas";
echo preg_replace("/(\w+)\s(\w+)/", "$2, $1", $name);   // Thomas, Anu
?>
```

```php
<?php
// (b) Extract all URLs from a string
$html = 'See https://saintgits.org and http://example.com/page?id=5 for details';

$pattern = "#https?://[^\s\"'<>]+#i";

if (preg_match_all($pattern, $html, $m)) {
    foreach ($m[0] as $url) {
        echo "<a href='" . htmlspecialchars($url) . "'>" . htmlspecialchars($url) . "</a><br>";
    }
}
?>
```

- `preg_replace($pattern, $replacement, $subject)` returns a **new string** — assign it back.
- `/i` = case-insensitive (`WORLD` matches).
- `(\w+)` captures a group, referenced as `$1`, `$2` in the replacement.
- URLs: `https?` = http/https, `[^\s"'<>]+` = not whitespace/quotes/brackets, `#…#` avoids escaping `/`.

**Traps:**
- `preg_replace(...)` alone does nothing visible — assign the result.
- `$1` inside a double-quoted PHP string is interpolated by PHP; safest is `"\${1}"` or single quotes with concatenation.

#### Q237 — Password + phone validation

**Structure (marks):** 8 password policy with a lookahead regex + hashing points · 6 phone validation.

**Answer:**

```php
<?php
function isValidPassword($pass) {
    // min 8 chars, at least one upper, one lower, one digit, one special
    $pattern = "/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W_]).{8,}$/";
    return (bool) preg_match($pattern, $pass);
}

function isValidPhone($phone) {
    return (bool) preg_match("/^[6-9][0-9]{9}$/", $phone);
}

$pass  = "Anu@2026";
$phone = "9876543210";

echo isValidPassword($pass)  ? "Password OK"  : "Password too weak";
echo "<br>";
echo isValidPhone($phone)    ? "Phone OK"     : "Invalid phone";
?>
```

- **Decode aloud:** `(?=.*[a-z])` is a **lookahead** — "somewhere ahead a lowercase letter" — consuming nothing, so four lookaheads check four classes in one pass; `.{8,}` then demands eight characters.
- **Discussion marks:** a regex validates *shape*, never *safety* — store with `password_hash()`, check with `password_verify()` (standard).
- **Phone:** `^[6-9][0-9]{9}$` = Indian mobile prefix; `^\+91[0-9]{10}$` with country code.

**Traps:**
- `[\W_]` (non-word or underscore) is the usual "special character" class; `(?=.*\W)` misses `_`.
- Without `^…$` the pattern accepts `"aaaaA1!x"` embedded in junk.

#### Q238 — Cookies (6) + array operations (8)

**Structure (marks):** 3 significance of cookies · 3 create and destroy · 8 four array statements (2 each).

**Answer (a) — cookies:** HTTP is stateless, so cookies give the client memory — preferences, "remember me", tracking, and the session ID itself (4:L39, 4:L841).

```php
<?php
// create — before any output, 1 hour, whole site
setcookie("user", "Anu", time() + 3600, "/");

// read
if (isset($_COOKIE["user"])) {
    echo "Hello " . htmlspecialchars($_COOKIE["user"]);
}

// destroy — same name, past expiry
setcookie("user", "", time() - 3600, "/");
?>
```

**Answer (b) — four array statements:**

```php
<?php
// i) declare
$marks = array("Ram" => 40, "Alice" => 20, "Raj" => 45, "Mary" => 35);

// ii) modify
$marks["Ram"] = 50;

// iii) sort and print
asort($marks);                       // by VALUE, keeps keys
foreach ($marks as $k => $v) {
    echo "$k => $v <br>";
}
// Alice => 20, Mary => 35, Raj => 45, Ram => 50

// iv) delete the entry "Raj"
unset($marks["Raj"]);
?>
```

| Sort | Orders by | Keeps names |
|---|---|---|
| `asort()` | value | yes — what a marks table wants |
| `ksort()` | key | yes |
| `arsort()` / `krsort()` | value / key, descending | yes |
| `sort()` | value | **no** — renumbers, destroys names |

**Traps:**
- `sort()` on an associative array loses the names — a classic 2-mark loss.
- `asort` sorts in place (no assignment); the `foreach` form is what "print the sorted pairs" wants.

#### Q239 — Cookies create/access/delete + session calls

**Structure (marks):** 7 cookies (three snippets + header rule) · 7 sessions (four calls + ID explanation).

**Answer (a) — cookies:**

```php
<?php
setcookie("theme", "dark", time() + 86400, "/");     // create: 1 day
echo $_COOKIE["theme"];                              // access (next request)
setcookie("theme", "", time() - 3600, "/");          // delete
?>
```

Facts: `setcookie()` before output (4:L65); `$_COOKIE` fills only on the **next** request; delete = same name + past expiry (4:L71).

**Answer (b) — sessions:**

```php
<?php
session_start();                       // 1. start / resume  (4:L106)

$_SESSION["user"]  = "Anu";            // 2. store           (4:L108)
$_SESSION["role"]  = "student";

echo $_SESSION["user"];                // 3. access

unset($_SESSION["role"]);              // 4a. remove one key
session_unset();                       // 4b. remove all
session_destroy();                     // 4c. destroy the session (4:L112)
?>
```

Browser holds only `PHPSESSID`; `session_start()` repeats every page; `session_destroy()` alone leaves `$_SESSION` populated this request — `session_unset()` first.

**Traps:**
- Writing `$_SESSION` before `session_start()` silently does nothing; calling it twice raises a notice.
- `unset($_SESSION)` is wrong — `unset()` takes a variable; use `session_unset()`.

#### Q240 — MySQLi connection procedure + program

**Structure (marks):** 10 procedure with error handling, step by step · 4 complete program with a success message.

**Answer (a) — procedure:**

1. **Credentials** — host, user, password, database (4:L210).
2. **Connect** — `mysqli_connect(...)` or `new mysqli(...)` (4:L258).
3. **Test** — `if (!$conn)` + `mysqli_connect_error()`, or `$conn->connect_error` (4:L224, 4:L262).
4. **Fail loudly** — `die()` with the reason (4:L292); guard the body with `try/catch (mysqli_sql_exception $e)` under PHP 8 (standard).
5. **Close** — `mysqli_close($conn)` / `$conn->close()` (4:L216).

**Answer (b) — both styles:**

```php
<?php
// procedural
$conn = mysqli_connect("localhost", "root", "", "college_db");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully to college_db";
mysqli_close($conn);
?>
```

```php
<?php
// object-oriented — same job
$conn = new mysqli("localhost", "root", "", "college_db");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully to college_db";
$conn->close();
?>
```

Failure messages: *Access denied for user* (bad credentials), *Unknown database* (typo / not created), *Connection refused* (MySQL down / wrong host).

**Traps:**
- `@` suppression loses marks; both APIs drive one engine.

#### Q241 — CREATE/INSERT/DELETE + student program

**Structure (marks):** 9 three operations with SQL and PHP each · 5 program that creates the table and inserts a row.

**Answer (a) — three operations:**

```text
CREATE  CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY,
                               name VARCHAR(50), marks INT);
        -> writes structure, returns true/false, run once        (4:L435)

INSERT  INSERT INTO students (name, marks) VALUES ('Anu', 88);
        -> adds one row, true/false, mysqli_insert_id() gives id (4:L472)

DELETE  DELETE FROM students WHERE id = 5;
        -> removes matching rows, affected_rows reports count    (4:L509)
```

All three are **write** operations: no readable data, only success/failure and a row count (4:L546).

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$sql = "CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)";
if (!mysqli_query($conn, $sql)) {
    die("Create failed: " . mysqli_error($conn));
}
echo "Table ready.<br>";

$sql = "INSERT INTO students (name, marks) VALUES ('Anu', 88)";
if (mysqli_query($conn, $sql)) {
    echo "Inserted with id " . mysqli_insert_id($conn);
} else {
    echo "Insert failed: " . mysqli_error($conn);
}
mysqli_close($conn);
?>
```

**Traps:**
- Second run without `IF NOT EXISTS` errors; missing quotes around `'Anu'`.
- `mysqli_num_rows()` on an INSERT gives nothing useful — it is `affected_rows`.

#### Q242 — Prepared INSERT/DELETE by register no.

**Structure (marks):** 8 why and how prepared statements work (`prepare`/`bind_param`/`execute`, type string) · 6 delete-by-regno program.

**Answer (a) — how it works:**

```php
<?php
// step 1: prepare the template once
$stmt = mysqli_prepare($conn, "INSERT INTO students (name, marks) VALUES (?, ?)");
// step 2: bind values — "si" = string, integer, in placeholder order
mysqli_stmt_bind_param($stmt, "si", $name, $marks);
// step 3: execute
mysqli_stmt_execute($stmt);
echo "Inserted id: " . mysqli_insert_id($conn);
mysqli_stmt_close($stmt);
?>
```

The SQL is parsed and compiled **before** the values arrive (4:L683), so a value can never become syntax. `bind_param` takes variables **by reference** (pass `$name`, not `'Anu'`); the first argument has one letter per `?` — `s`, `i`, `d`, `b`.

**Answer (b) — delete by register number:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$regno = $_POST["regno"];

$stmt = mysqli_prepare($conn, "DELETE FROM students WHERE regno = ?");
mysqli_stmt_bind_param($stmt, "s", $regno);
mysqli_stmt_execute($stmt);

if (mysqli_stmt_affected_rows($stmt) > 0) {
    echo mysqli_stmt_affected_rows($stmt) . " record deleted";
} else {
    echo "No student with register number " . htmlspecialchars($regno);
}
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
```

**Traps:**
- `mysqli_stmt_affected_rows($stmt)` takes the **statement**, `mysqli_affected_rows($conn)` takes the **connection** — mixing them is the most common error.
- Skipping the `affected_rows` check loses the "no such student" mark.

#### Q243 — SELECT many rows → HTML table

**Structure (marks):** 6 what SELECT returns + fetch-loop steps · 8 the program with table markup.

**Answer (a) — steps:**

1. **Build** — `SELECT regno, name, marks FROM students`.
2. **Query** — `mysqli_query()` returns a **result handle**, not data (4:L320).
3. **Check** — on `false`, `mysqli_error()`.
4. **Loop** — `while (...fetch_assoc...)`, one row per pass, `NULL` ends it (4:L365).
5. **Render** — one `<tr>` per iteration; `num_rows()` for the count (4:L361).

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$result = mysqli_query($conn, "SELECT regno, name, marks FROM students");
if (!$result) { die("Query failed: " . mysqli_error($conn)); }

echo "<table border='1' cellpadding='6'>";
echo "<tr><th>Reg No</th><th>Name</th><th>Marks</th></tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>" . htmlspecialchars($row["regno"]) . "</td>";
    echo "<td>" . htmlspecialchars($row["name"])  . "</td>";
    echo "<td>" . $row["marks"] . "</td>";
    echo "</tr>";
}
echo "</table>";

echo "<p>Total students: " . mysqli_num_rows($result) . "</p>";
mysqli_free_result($result);
mysqli_close($conn);
?>
```

The alternative-syntax version (`while (...):` … `endwhile;`, `<?= ?>`) earns full marks too — §2.19.

**Traps:**
- `mysqli_num_rows()` after the loop still works — the pointer moved, the count did not.
- Fetching before printing `<tr><th>` gives a headerless table; forgetting `</table>`.

#### Q244 — UPDATE syntax/precautions + update email

**Structure (marks):** 7 syntax, multi-column SET, WHERE rule, `affected_rows`, precautions · 7 the program.

**Answer (a) — syntax and precautions:**

```sql
UPDATE students SET email = 'new@saintgits.org' WHERE regno = '20CST461';
```

1. **Never without `WHERE`** — every row changes (4:L638).
2. **Preview** the rows with the same `WHERE` as a `SELECT` (4:L669).
3. **Bind or cast** — `(int)` numbers, prepared statements for strings (4:L675–683).
4. **Check** `affected_rows()` — 0 means nothing matched (4:L687).
5. **Validate** the new value first; back up or use a transaction for bulk updates (standard).

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$regno = $_POST["regno"];
$email = $_POST["email"];

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    die("Invalid email format");
}

$stmt = mysqli_prepare($conn, "UPDATE students SET email = ? WHERE regno = ?");
mysqli_stmt_bind_param($stmt, "ss", $email, $regno);
mysqli_stmt_execute($stmt);

$n = mysqli_stmt_affected_rows($stmt);
if ($n > 0) {
    echo "$n record updated for " . htmlspecialchars($regno);
} else {
    echo "No change — check the register number";
}
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
```

**Traps:**
- Two `"s"` letters — both are strings.
- Binding order must match placeholder order; swap them and the email lands in the regno column.

#### Q245 — App architecture + products list

**Structure (marks):** 7 the layers and request flow · 7 product-listing program.

**Answer (a) — architecture:**

```text
Browser  --HTTP request-->  Apache/IIS  -->  PHP engine
                                             |  (1) connect  mysqli_connect
                                             |  (2) query    mysqli_query
                                             |  (3) fetch    fetch_assoc loop
                                             |  (4) render   echo HTML
                                        MySQL  <-- SQL -->  tables on disk
Browser  <--plain HTML------  PHP output
```

- **Presentation** — HTML produced by `echo`; **business logic** — validation, calculations; **data access** — connection + SQL. Separating them is 4:L717, the precursor of MVC.
- **State** — cookies/sessions between stateless requests (4:L31–51).

**Answer (b) — products as an HTML list:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "shop_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$result = mysqli_query($conn, "SELECT pname, price FROM products ORDER BY price ASC");
if (!$result) { die("Query failed: " . mysqli_error($conn)); }

echo "<h2>Product Catalogue</h2><ul>";
while ($row = mysqli_fetch_assoc($result)) {
    echo "<li>" . htmlspecialchars($row["pname"])
       . " — Rs. " . number_format($row["price"], 2) . "</li>";
}
echo "</ul>";
mysqli_close($conn);
?>
```

`<ul>` vs `<table>` is irrelevant — *one HTML fragment per row inside the loop* is the idea (4:L737); `number_format()` is presentation logic in the render step.

**Traps:**
- The architecture half is where marks are lost — draw the boxes and label the four PHP steps.
- Omitting MySQL-on-disk or the state layer leaves the diagram half-answered.

#### Q246 — Session lifecycle + ID + login time

**Structure (marks):** 6 lifecycle stages · 4 role of the session ID · 4 two-page program.

**Answer (a) — lifecycle:**

1. **Create** — `session_start()`; no ID cookie exists, so PHP mints one and sends `Set-Cookie: PHPSESSID=…` (4:L106).
2. **Store** — `$_SESSION["name"] = "Anu"` writes a server file named after that ID (4:L108).
3. **Resume** — the cookie replays; `session_start()` reloads the file (4:L110).
4. **Expire** — browser close, server timeout, or `session_unset()` + `session_destroy()` (4:L112, 4:L156).

The ID is the only link between browser and data — a lookup key, no username or role. Steal it and you inherit the session: random, over HTTPS, regenerated at login (`session_regenerate_id(true)`, standard).

**Answer (b) — two pages:**

```php
<?php
session_start();
$_SESSION["username"]  = "Anu";
$_SESSION["login_time"] = date("d-m-Y h:i:s A");
echo "Stored. <a href='welcome.php'>Go to welcome page</a>";
?>
```

```php
<?php
session_start();
if (!isset($_SESSION["username"])) {
    die("Please log in first");
}
echo "Welcome " . htmlspecialchars($_SESSION["username"]) . "<br>";
echo "You logged in at " . $_SESSION["login_time"];
?>
```

**Traps:**
- Missing `session_start()` on page 2 — the classic zero.
- No `isset` guard gives an undefined-index warning; `date()` must run **when storing**, not when displaying.

#### Q247 — Cookie vs session + recommendation

**Structure (marks):** 8 four-axis comparison table · 6 recommendation with justification.

**Answer (a) — comparison** (4:L136–160):

| Axis | Cookie | Session |
|---|---|---|
| **Storage** | client cookie store, sent with every request (4:L140) | server file/DB keyed by the ID (4:L152) |
| **Lifetime** | your expiry — survives restarts (4:L146) | browser close, or server idle timeout (4:L156) |
| **Security** | readable, editable, forgeable; ~4 KB (4:L144, L142) | data stays server-side; only a random ID travels; needs HTTPS (4:L154) |
| **Applications** | preferences, "remember me", tracking (4:L148) | login state, cart, multi-step forms (4:L160) |

**Answer (b) — recommendation:**

- **Sessions, for the logged-in state** — login is a security decision, so it must not be client-editable: `loggedin=1` is forged in seconds, a session ID cannot be invented, and the data stays server-side.
- **Capacity and lifetime** — a session holds the whole user record, not a 4 KB string, and dies at browser close — what users expect from a login.
- **Cookie only for the non-sensitive half** — a long random "remember me" token checked against the DB, never the identity.

**Traps:**
- "Sessions are more secure" is half a sentence — add *because the data is not client-side*.
- Sessions still rely on a cookie (the ID), so the mechanisms are layered, not alternatives.

#### Q248 — SQL workflow + INSERT success report

**Structure (marks):** 7 the workflow step by step · 7 INSERT program with success/failure report.

**Answer (a) — workflow** (the deck's five-step cycle, 4:L405–419):

1. `mysqli_connect(...)` → handle, else `die()`.
2. Build the SQL **string** (`INSERT INTO …`, strings quoted).
3. `mysqli_query($conn, $sql)` → for writes, `true`/`false`.
4. Branch: `true` → success + `mysqli_insert_id()`; `false` → `mysqli_error($conn)`.
5. `mysqli_close($conn)`.

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$name  = trim($_POST["name"]);
$marks = (int)$_POST["marks"];

if ($name == "") {
    die("Name is required");
}

$stmt = mysqli_prepare($conn, "INSERT INTO students (name, marks) VALUES (?, ?)");
mysqli_stmt_bind_param($stmt, "si", $name, $marks);

if (mysqli_stmt_execute($stmt)) {
    echo "Success: record inserted with id " . mysqli_insert_id($conn);
} else {
    echo "Failure: " . mysqli_error($conn);
}
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
```

`execute()` returning true proves the *statement ran*, not that the data was sensible — validate before the query, and read `insert_id`/`affected_rows` after it.

**Traps:**
- Reporting success without checking the return value — the "always prints Success" bug.
- After a prepared statement `mysqli_stmt_error($stmt)` is the precise form (the `$conn` version also works).

#### Q249 — CREATE TABLE types/constraints + employees

**Structure (marks):** 7 types and constraints explained · 7 employee table SQL executed from PHP.

**Answer (a) — types and constraints:**

| Category | Choice | Why |
|---|---|---|
| Whole numbers | `INT` | ids, age, counts |
| Short/long text | `VARCHAR(n)` / `TEXT` | name, department / remarks |
| Dates | `DATE` / `DATETIME` | admission, joined |
| Money | `DECIMAL(10,2)` | exact — `FLOAT` loses paise |
| `PRIMARY KEY` + `AUTO_INCREMENT` | unique identity, MySQL numbers 1,2,3… | needed for `WHERE id = …` (4:L437) |
| `NOT NULL` / `UNIQUE` | value required / no duplicates | email, register number |
| `DEFAULT` | fallback value | `DEFAULT 'General'` |

**Answer (b) — employee table from PHP:**

```php
<?php
$sql = "CREATE TABLE employees (
    emp_id     INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50) NOT NULL,
    department VARCHAR(30) DEFAULT 'General',
    salary     DECIMAL(10,2) NOT NULL
)";

if (mysqli_query($conn, $sql)) {
    echo "employees table created";
} else {
    echo "Error: " . mysqli_error($conn);
}
?>
```

**Traps:**
- `VARCHAR` with no length is a syntax error.
- `salary INT` loses the decimal part.

#### Q250 — Careful DELETE + prepared delete by dept

**Structure (marks):** 6 why DELETE is dangerous + precautions · 8 the prepared-statement program.

**Answer (a) — precautions:**

1. **`WHERE` in intent** — without it the table empties (4:L511).
2. **Preview** — `SELECT … WHERE department = ?` first (4:L515, L669).
3. **Prepared** — so the value cannot inject (4:L683).
4. **Verify** — `affected_rows` must match the preview (4:L687).
5. **Soft delete** (`SET deleted = 1`) or a transaction (`START TRANSACTION` / `ROLLBACK`) where recovery matters (standard).

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "company_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$dept = $_POST["department"];

// 1. preview
$stmt = mysqli_prepare($conn, "SELECT COUNT(*) AS c FROM employees WHERE department = ?");
mysqli_stmt_bind_param($stmt, "s", $dept);
mysqli_stmt_execute($stmt);
$row = mysqli_fetch_assoc(mysqli_stmt_get_result($stmt));
echo "About to delete " . $row["c"] . " record(s) from " . htmlspecialchars($dept) . "<br>";
mysqli_stmt_close($stmt);

// 2. delete
$stmt = mysqli_prepare($conn, "DELETE FROM employees WHERE department = ?");
mysqli_stmt_bind_param($stmt, "s", $dept);
mysqli_stmt_execute($stmt);

echo mysqli_stmt_affected_rows($stmt) . " record(s) deleted";
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
```

**Traps:**
- The question wants the *prepared* form, not concatenated `WHERE department = '$dept'`.
- `mysqli_stmt_get_result()` is required before `fetch_assoc()` on a prepared SELECT.

#### Q251 — SELECT result processing + marks > 50

**Structure (marks):** 6 result processing (handle → pointer → loop → free) · 8 filtered program.

**Answer (a) — processing:** `mysqli_query()` returns a `mysqli_result` holding the set with an internal pointer (4:L353); `fetch_assoc()` returns the current row and advances it, `NULL` ends the `while` (4:L357); `num_rows()` counts without fetching (4:L361); `free_result()` releases memory.

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$sql = "SELECT regno, name, marks FROM students WHERE marks > 50 ORDER BY marks DESC";
$result = mysqli_query($conn, $sql);
if (!$result) { die("Query failed: " . mysqli_error($conn)); }

if (mysqli_num_rows($result) == 0) {
    echo "No student scored above 50";
} else {
    echo "<table border='1'><tr><th>Reg No</th><th>Name</th><th>Marks</th></tr>";
    while ($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td>" . htmlspecialchars($row["regno"]) . "</td>";
        echo "<td>" . htmlspecialchars($row["name"]) . "</td>";
        echo "<td>" . $row["marks"] . "</td></tr>";
    }
    echo "</table>";
}
mysqli_free_result($result);
mysqli_close($conn);
?>
```

**Traps:**
- `>` vs `>=` — the question says *greater than* 50.
- The empty-result branch is worth a mark and is usually forgotten.

#### Q252 — UPDATE + affected_rows + 10% raise

**Structure (marks):** 6 UPDATE mechanics and `affected_rows` · 8 the raise program.

**Answer (a) — explanation:**

- `UPDATE t SET col = value WHERE condition` rewrites matching rows (4:L634).
- `affected_rows()` reports how many **actually changed** (4:L640, L513) — "query ran" vs "data changed".
- It is `0` when the WHERE matched nothing **and** when the new value equals the old, since MySQL counts changed rows (standard); compare with `SELECT COUNT(*)`.

**Answer (b) — program:**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "company_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$dept = $_POST["department"];

$stmt = mysqli_prepare($conn,
    "UPDATE employees SET salary = salary * 1.10 WHERE department = ?");
mysqli_stmt_bind_param($stmt, "s", $dept);
mysqli_stmt_execute($stmt);

$n = mysqli_stmt_affected_rows($stmt);
if ($n > 0) {
    echo "$n employee(s) in " . htmlspecialchars($dept) . " received a 10% raise";
} else {
    echo "No employee found in that department";
}
mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
```

SQL-only form for the first half: `UPDATE employees SET salary = salary * 1.10 WHERE department = 'Sales';` — the arithmetic happens *inside* SQL, so no PHP loop is needed.

**Traps:**
- Computing the raise row by row in PHP works but wastes marks — one statement does it.
- `salary * 1.1` is exact on `DECIMAL`, drifts on `FLOAT`.

#### Q253 — Steps for dynamic HTML + students list

**Structure (marks):** 6 the steps/architecture · 8 listing program with names and marks.

**Answer (a) — the steps** (4:L774–780):

1. **Connect** to MySQL.
2. **Query** — `SELECT name, marks FROM students`.
3. **Fetch** — loop `fetch_assoc($result)`.
4. **Render** — one HTML row per record, escaped.
5. **Close** — free result, close connection.

*Dynamic* because the same file emits different HTML per request (4:L705, L780).

**Answer (b) — program** (alternative syntax, the deck's own shape, 4:L782–792):

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

$result = mysqli_query($conn, "SELECT name, marks FROM students");
if (!$result) { die("Query failed: " . mysqli_error($conn)); }
?>
<table border="1">
<tr><th>Name</th><th>Marks</th></tr>
<?php while ($row = mysqli_fetch_assoc($result)): ?>
<tr>
    <td><?= htmlspecialchars($row["name"]) ?></td>
    <td><?= $row["marks"] ?></td>
</tr>
<?php endwhile; ?>
</table>
<?php
mysqli_free_result($result);
mysqli_close($conn);
?>
```

**Traps:**
- `while (...)` with braces holding HTML is a syntax error — pick `while (...):` … `endwhile;` and stay in it.
- `<?=` needs no semicolon but does need the closing `?>`.

---

## 4. Code you must write by hand

On paper, closed book. Every drill from D3 onward assumes `$conn` is open (D1/D2) and that `college_db.students` exists.

**D1 — Connect and close (6-line skeleton)**

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
mysqli_close($conn);
?>
```
*Memorise:* four arguments in order — host, user, password, database.

**D2 — Connect with an error check (both styles)**

```php
<?php
// procedural
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";

// OO equivalent
$conn2 = new mysqli("localhost", "root", "", "college_db");
if ($conn2->connect_error) {
    die("Connection failed: " . $conn2->connect_error);
}
?>
```
*Memorise:* `if (!$conn)` + `mysqli_connect_error()`; OO is `$conn->connect_error`.

**D3 — Create a table + list databases**

```php
<?php
$sql = "CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    marks INT
)";
if (!mysqli_query($conn, $sql)) {
    die("Create failed: " . mysqli_error($conn));
}

$db = mysqli_query($conn, "SHOW DATABASES");
while ($row = mysqli_fetch_row($db)) {
    echo $row[0] . "<br>";
}
?>
```
*Memorise:* `CREATE TABLE name (col type, …)`; `SHOW DATABASES` + `fetch_row()[0]`.

**D4 — Insert with error handling**

```php
<?php
$name  = $_POST["name"];
$marks = (int)$_POST["marks"];
$sql   = "INSERT INTO students (name, marks) VALUES ('$name', $marks)";

if (mysqli_query($conn, $sql)) {
    echo "Inserted. id = " . mysqli_insert_id($conn);
} else {
    echo "Insert failed: " . mysqli_error($conn);
}
?>
```
*Memorise:* strings quoted, numbers cast, `mysqli_insert_id()` on success.

**D5 — Insert with a prepared statement**

```php
<?php
$stmt = mysqli_prepare($conn, "INSERT INTO students (name, marks) VALUES (?, ?)");
mysqli_stmt_bind_param($stmt, "si", $name, $marks);
if (mysqli_stmt_execute($stmt)) {
    echo "Inserted. id = " . mysqli_insert_id($conn);
} else {
    echo "Error: " . mysqli_stmt_error($stmt);
}
mysqli_stmt_close($stmt);
?>
```
*Memorise:* prepare → bind_param("si", …) → execute → close. One letter per `?`.

**D6 — Select all into an HTML table**

```php
<?php
$result = mysqli_query($conn, "SELECT regno, name, marks FROM students");
if (!$result) { die(mysqli_error($conn)); }
?>
<table border="1">
<tr><th>Reg No</th><th>Name</th><th>Marks</th></tr>
<?php while ($row = mysqli_fetch_assoc($result)): ?>
<tr>
    <td><?= htmlspecialchars($row["regno"]) ?></td>
    <td><?= htmlspecialchars($row["name"]) ?></td>
    <td><?= $row["marks"] ?></td>
</tr>
<?php endwhile; ?>
</table>
```
*Memorise:* `while (...):` … `endwhile;` and `<?= ?>`.

**D7 — Select with WHERE, ORDER BY, LIMIT**

```php
<?php
$sql = "SELECT name, marks FROM students
        WHERE marks >= 50
        ORDER BY marks DESC
        LIMIT 5";
$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_assoc($result)) {
    echo $row["name"] . " — " . $row["marks"] . "<br>";
}
?>
```
*Memorise:* clause order `WHERE → ORDER BY → LIMIT`.

**D8 — Update with affected_rows**

```php
<?php
$id    = (int)$_POST["id"];
$email = $_POST["email"];
$sql   = "UPDATE students SET email = '$email' WHERE id = $id";

if (!mysqli_query($conn, $sql)) {
    die("Update failed: " . mysqli_error($conn));
}
echo mysqli_affected_rows($conn) . " row(s) updated";
?>
```
*Memorise:* `UPDATE t SET col = val WHERE key = val` and the affected-rows count.

**D9 — Delete with WHERE**

```php
<?php
$id  = (int)$_POST["id"];
$sql = "DELETE FROM students WHERE id = $id";

if (!mysqli_query($conn, $sql)) {
    die("Delete failed: " . mysqli_error($conn));
}
echo mysqli_affected_rows($conn) . " row(s) deleted";
?>
```
*Memorise:* `DELETE FROM t WHERE …` — never without WHERE.

**D10 — Session login/home/logout trio**

```php
<?php
session_start();
$_SESSION["user"] = "Anu";
$_SESSION["time"] = date("d-m-Y h:i A");
header("Location: home.php");     // redirect
exit;
?>
```

```php
<?php
session_start();
if (!isset($_SESSION["user"])) { die("Not logged in"); }
echo "Welcome " . htmlspecialchars($_SESSION["user"]);
echo " | <a href='logout.php'>Logout</a>";
?>
```

```php
<?php
session_start();
session_unset();
session_destroy();
header("Location: login.php");
exit;
?>
```
*Memorise:* `session_start()` on **every** page; `session_unset()` before `session_destroy()`.

**D11 — Cookie set / read / delete**

```php
<?php
setcookie("username", "Anu", time() + 3600, "/");   // set, 1 hour
if (isset($_COOKIE["username"])) {                  // read (next request)
    echo "Welcome " . htmlspecialchars($_COOKIE["username"]);
}
setcookie("username", "", time() - 3600, "/");      // delete
?>
```
*Memorise:* `time()+3600` sets, `time()-3600` deletes, nothing echoed before `setcookie()`.

**D12 — Dynamic date/time greeting page**

```php
<?php
date_default_timezone_set("Asia/Kolkata");
$h = (int) date("H");
if ($h < 12)      { $g = "Good morning"; }
elseif ($h < 17)  { $g = "Good afternoon"; }
elseif ($h < 21)  { $g = "Good evening"; }
else              { $g = "Good night"; }
?>
<h1><?= $g ?>, visitor!</h1>
<p><?= date("l, d F Y — h:i:s A") ?></p>
```
*Memorise:* `date("H")` for the 24-hour hour; `H i s A l d F Y` format letters.

**D13 — Square root**

```php
<?php
$n = 25;
echo "Square root of $n = " . sqrt($n);        // 5
?>
```
*Memorise:* `sqrt($n)`; guard negatives if the question says "any number".

**D14 — Factorial (recursive)**

```php
<?php
function fact($n) {
    if ($n <= 1) return 1;
    return $n * fact($n - 1);
}
echo fact(5);        // 120
?>
```
*Memorise:* base case first, then `$n * fact($n-1)`.

**D15 — File upload**

```php
<?php
if (isset($_FILES["f"]) && $_FILES["f"]["error"] == 0) {
    $target = "uploads/" . basename($_FILES["f"]["name"]);
    if (move_uploaded_file($_FILES["f"]["tmp_name"], $target)) {
        echo "Uploaded: " . htmlspecialchars($target);
    } else {
        echo "Move failed";
    }
} else {
    echo "No file / upload error";
}
?>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="f"><input type="submit">
</form>
```
*Memorise:* `enctype="multipart/form-data"`, `$_FILES["f"]["tmp_name"]`, `move_uploaded_file()`, `basename()`.

**D16 — Registration form → MySQL insert, with validation**

```php
<?php
$msg = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name  = trim($_POST["name"]);
    $email = trim($_POST["email"]);
    $pass  = $_POST["password"];

    if ($name == "" || $email == "" || $pass == "") {
        $msg = "All fields are required";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $msg = "Invalid email format";
    } elseif (strlen($pass) < 8) {
        $msg = "Password must be at least 8 characters";
    } else {
        $conn = mysqli_connect("localhost", "root", "", "college_db");
        if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }

        $hash = password_hash($pass, PASSWORD_DEFAULT);
        $stmt = mysqli_prepare($conn,
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
        mysqli_stmt_bind_param($stmt, "sss", $name, $email, $hash);
        if (mysqli_stmt_execute($stmt)) {
            $msg = "Registered successfully as " . htmlspecialchars($name);
        } else {
            $msg = "Insert failed: " . mysqli_stmt_error($stmt);
        }
        mysqli_stmt_close($stmt);
        mysqli_close($conn);
    }
}
?>
<form method="post" action="<?= htmlspecialchars($_SERVER['PHP_SELF']) ?>">
  Name: <input type="text" name="name"><br>
  Email: <input type="text" name="email"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Register">
</form>
<p><?= $msg ?></p>
```
*Memorise:* validate → connect → hash → prepare/bind/execute → report. `password_hash()` is standard, not in the deck.

---

## 5. Night-before memorize sheet

| Item | Exact syntax / signature | Asked at |
|---|---|---|
| Connect | `mysqli_connect('localhost','user','pass','db')` | Q92 |
| Connect error | `mysqli_connect_error()` · OO `$conn->connect_error` | every connection question |
| Close | `mysqli_close($conn);` · OO `$conn->close();` | lifecycle mark |
| Query | `mysqli_query($conn, $sql)` | Q126 |
| Query error | `mysqli_error($conn)` | any "error handling" |
| Fetch loop | `while ($row = mysqli_fetch_assoc($result))` | Q128 |
| Row access | `$row["column_name"]` | every display answer |
| Count rows | `mysqli_num_rows($result)` | "no records found", paging |
| Rows changed | `mysqli_affected_rows($conn)` · OO `$conn->affected_rows` | Q127 |
| Last id | `mysqli_insert_id($conn)` | any INSERT |
| Prepared | `mysqli_prepare($conn, "INSERT … VALUES (?, ?)")` | Q99 |
| Bind | `mysqli_stmt_bind_param($stmt, "ssi", $a, $b, $c)` | the type string is the mark |
| Execute | `mysqli_stmt_execute($stmt)` | — |
| Prepared rows | `mysqli_stmt_affected_rows($stmt)` · `mysqli_stmt_error($stmt)` | not the `$conn` versions |
| Start session | `session_start();` | Q115 |
| Session write/read | `$_SESSION["key"] = value;` · `echo $_SESSION["key"];` | Q95 |
| End session | `session_unset(); session_destroy();` | Q239 |
| Set cookie | `setcookie('name','value',time()+3600,'/');` | Q113 |
| Read cookie | `$_COOKIE["name"]` | — |
| Delete cookie | `setcookie('name','',time()-3600,'/');` | past expiry, same path |
| Create table | `CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));` | Q109 |
| Insert | `INSERT INTO t (col1, col2) VALUES ('str', 123);` | Q118 |
| Update | `UPDATE t SET col = value WHERE key = value;` | Q121 |
| Delete | `DELETE FROM t WHERE key = value;` | Q119 |
| Select | `SELECT cols FROM t WHERE cond ORDER BY col DESC LIMIT 5;` | Q120 |
| List databases | `SHOW DATABASES` (+ `SHOW TABLES`, `DESCRIBE t`) | Q107 |
| Alternative loop | `<?php while (...): ?> … <?php endwhile; ?>` | Q243 |
| Short echo | `<?= $row["name"] ?>` | = `<?php echo …; ?>` |
| Escape output | `htmlspecialchars($str)` | XSS mark, every display |
| Self action | `$_SERVER['PHP_SELF']` (not `$_PHP_SELF`) | Q103 |
| Email regex | `/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/` + `preg_match()` | Q97 |
| Phone regex | `/^[0-9]{10}$/` or `/^[6-9][0-9]{9}$/` | Q235 |
| Greeting hour | `(int) date("H")` + `if/elseif` | Q231 |
| Root | `sqrt($n)` | Q105 |
| Factorial | `return $n * fact($n-1);` base case `$n <= 1` | Q233 |
| Upload | `$_FILES["f"]["tmp_name"]` + `move_uploaded_file()` + `enctype="multipart/form-data"` | Q233 |
| Sort assoc | `asort()` value, `ksort()` key, `unset($a["k"])` | Q238 |

---

## 6. Figure index

`grep 'Image Description' module4.md` → **16** hits. Fifteen are slide furniture (DB cylinder + PHP logo at 4:L1, 57, 96, 200, 238, 310, 345, 425, 462, 499, 552, 589, 624, 729, 764) — no exam value.

| Line | Figure | Exam value |
|---|---|---|
| 4:L399 | **Five-step query cycle** — five boxes: build SQL → `mysqli_query()` → result handle → `while` + `fetch_assoc()` → echo HTML per row, over the bar "Browser displays the finished table" | **High** — draw for Q243/245/248/253; prose 4:L407–417 |

**Not drawn in this deck**
- **Request/response** (browser → Apache → PHP → MySQL → HTML): `module3.md` L57 — cite the Module 3 cycle.
- **Session flow** (`PHPSESSID` ⇄ server file): prose 4:L106–112, §2.3.
- **Cookie round trip** (`Set-Cookie` → jar → `Cookie` → `$_COOKIE`): prose 4:L39.

---

## 7. Defence lines

1. **Sessions over cookies for login:** identity is a server-side record; the browser holds only an unguessable ID, so nothing the user can edit decides who they are.
2. **`WHERE` is non-negotiable:** without it `UPDATE` writes every row, `DELETE` empties the table, and neither has an undo.
3. **Prepared statements stop injection:** the statement is compiled before the values arrive, so input stays data and can never be parsed as syntax.
4. **`fetch_assoc()` returns `NULL` at the end:** the result set has an internal pointer; past the last row there is nothing to return, and `NULL` is falsy, which ends the `while`.
5. **Connection before query:** `mysqli_query()` needs a live handle; otherwise `false` goes where a connection belongs.
6. **`setcookie()`/`session_start()` first:** both emit HTTP headers, and headers are already on the wire once body output starts.
7. **`affected_rows` matters even with no error:** MySQL reports success for a statement that matched zero rows; the count is the only evidence.
8. **`mysqli_query()` returns two things:** SELECT gives a result set to iterate, writes only a status — nothing to fetch.
9. **Escape on output, not input:** the danger is a value being interpreted as HTML when displayed, so escaping belongs at rendering.
10. **The page is dynamic though the file is not:** the file is a program; the HTML is rebuilt per request from whatever the database holds then.
11. **`(int)` is not a substitute for prepared statements:** it closes injection through numeric fields only; strings still need binding.
12. **`session_destroy()` alone looks broken:** it deletes the server file but leaves `$_SESSION` populated this request — `session_unset()` first. Every session *is* a cookie, so the mechanisms are layered.
