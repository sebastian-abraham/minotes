# MODULE 4 — PHP + MySQL · Complete Study Kit

> 20CST461 Web Technologies · ESE Part A = 3 marks, Part B = 14 marks · 2 Part-A questions and 1 of 2 Part-B questions come from this module

---

## 0. How to use this kit

You have never written PHP. That is fine — this module is **one pattern repeated five times**, not 63 separate things.

Read in this order and stop when the clock says stop:

| When | Read | Time |
|---|---|---|
| First pass, learning | §2 concepts 2.1 → 2.21 in order, typing every snippet | 2 hrs |
| Second pass | §3.1 (all 26 master answers — these are your Part A marks) | 45 min |
| Third pass | §3.2 only the 8 Part-B answers marked ⭐ (highest probability) | 60 min |
| Hand practice | §4 drills D1–D16, on paper, closed book | 90 min |
| Night before | §5 memorize sheet + §7 defence lines | 25 min |

**Conventions used in this file**

- `4:L431–453` = lines 431–453 of `module4.md` (your lecture deck). Every one of these was checked against the file; if a claim has no ref, it is either my addition or flagged.
- **"(standard, not in your deck)"** = correct PHP that your slides never show. The question bank still asks it (regex, `$_PHP_SELF`, file upload, `SHOW DATABASES`). Learn it, but do not claim the slide said it.
- All code is inside fenced blocks, exactly as you would write it on the answer sheet. Copy it verbatim; nothing is escaped or mangled.
- Procedural `mysqli_*` functions are the default in this kit (that is what the deck teaches). Where the deck also shows the object-oriented style I say so, and §5 gives you both forms of every hot function.

**The one sentence that is the whole module:** *connect → build a SQL string → `mysqli_query()` → loop `mysqli_fetch_assoc()` → echo HTML.*

---

## 1. Module map + question coverage

63 questions: **38 Part A** (Q92–Q129, 3 marks each) and **25 Part B** (Q229–Q253, 14 marks each).

⚠️ The faculty bank's module headings are wrong: it prints "Module 4: PHP" above Q92–Q129, then "Module 5: PHP and MySQL Database Operations" above Q130 onwards — but Q130–Q153 are JSON/Laravel (real Module 5) while **Q229–Q253 sit under a second "Module 4: PHP" heading and are the descriptive (14-mark) block for this module**. Both blocks are covered here.

| Q# | What it asks (≤8 words) | Mark shape | Answered at |
|---|---|---|---|
| 92 | Steps to establish PHP–MySQL connection | 3 · Part A | §3.1 A1, §2.6 |
| 93 | `$_SESSION` vs `$_COOKIE`, when each | 3 · Part A | §3.1 A2, §2.4 |
| 94 | GET vs POST in form submission | 3 · Part A | §3.1 A3 |
| 95 | Session: store name, show other page | 3 · Part A | §3.1 A4, §4 D10 |
| 96 | Insert record, handle errors | 3 · Part A | §3.1 A6, §4 D4 |
| 97 | Regex email check returning boolean | 3 · Part A | §3.1 A7, §4 D16 |
| 98 | Update email, with error handling | 3 · Part A | §3.1 A8, §4 D8 |
| 99 | Prepared statements and why | 3 · Part A | §3.1 A9, §2.18 |
| 100 | Sessions keep state across pages | 3 · Part A | §3.1 A5 |
| 101 | Retrieve and display MySQL data | 3 · Part A | §3.1 A10, §4 D6 |
| 102 | PHP's role vs static HTML | 3 · Part A | §3.1 A11, §2.20 |
| 103 | Purpose of `$_PHP_SELF` | 3 · Part A | §3.1 A12 |
| 104 | Fetch data from DB to webpage | 3 · Part A | §3.1 A10, §4 D6 |
| 105 | Square root program | 3 · Part A | §3.1 A13, §4 D13 |
| 106 | `mysql_fetch_array` vs `_assoc` | 3 · Part A | §3.1 A14, §2.10 |
| 107 | List databases on MySQL server | 3 · Part A | §3.1 A15, §4 D3 |
| 108 | List data in a table | 3 · Part A | §3.1 A10 |
| 109 | CREATE operations from PHP | 3 · Part A | §3.1 A16, §4 D3 |
| 110 | Connection steps (duplicate of 92) | 3 · Part A | §3.1 A1 |
| 111 | Session importance across requests | 3 · Part A | §3.1 A5 |
| 112 | Insert + connection/query/errors | 3 · Part A | §3.1 A6, §4 D4 |
| 113 | What is a cookie + two uses | 3 · Part A | §3.1 A17, §2.2 |
| 114 | Session vs cookie | 3 · Part A | §3.1 A2 |
| 115 | Statement to start a session | 3 · Part A | §3.1 A18 |
| 116 | Basic MySQL connection statement | 3 · Part A | §3.1 A1, §2.6 |
| 117 | Purpose of CREATE TABLE | 3 · Part A | §3.1 A16, §2.13 |
| 118 | SQL to add a record + syntax | 3 · Part A | §3.1 A19, §2.14 |
| 119 | Purpose of DELETE | 3 · Part A | §3.1 A20, §2.15 |
| 120 | Purpose of SELECT | 3 · Part A | §3.1 A21, §2.16 |
| 121 | SQL to modify existing records | 3 · Part A | §3.1 A22, §2.15 |
| 122 | What is dynamic content | 3 · Part A | §3.1 A11 |
| 123 | Three advantages of sessions | 3 · Part A | §3.1 A5 |
| 124 | Cookie syntax with expiry | 3 · Part A | §3.1 A17, §5 |
| 125 | Purpose of `session_start()` | 3 · Part A | §3.1 A18 |
| 126 | Purpose of `mysqli_query()` | 3 · Part A | §3.1 A23, §2.9 |
| 127 | Why WHERE matters in UPDATE/DELETE | 3 · Part A | §3.1 A24 |
| 128 | What `mysqli_fetch_assoc()` is for | 3 · Part A | §3.1 A25, §2.10 |
| 129 | Two sources of dynamic content | 3 · Part A | §3.1 A26 |
| 229 | Form app: name + email validation ⭐ | 14 · Part B | §3.2 Q229, §4 D16 |
| 230 | PHP's importance + challenges (10m) | 14 · Part B | §3.2 Q230 |
| 231 | Dynamic page: date/time + greeting ⭐ | 14 · Part B | §3.2 Q231, §4 D12 |
| 232 | Username/password/email filled + format | 14 · Part B | §3.2 Q232 |
| 233 | File uploads + recursive factorial | 14 · Part B | §3.2 Q233, §4 D14–D15 |
| 234 | Connection step-by-step + patients DB ⭐ | 14 · Part B | §3.2 Q234 |
| 235 | Regex: extract emails + validate phone | 14 · Part B | §3.2 Q235 |
| 236 | Regex: replace substring + extract URLs | 14 · Part B | §3.2 Q236 |
| 237 | Password validation + phone validation | 14 · Part B | §3.2 Q237 |
| 238 | Cookies + associative array operations | 14 · Part B | §3.2 Q238 |
| 239 | Cookies create/access/delete + sessions | 14 · Part B | §3.2 Q239, §4 D10–D11 |
| 240 | MySQLi connection + error handling + program | 14 · Part B | §3.2 Q240, §4 D2 |
| 241 | CREATE/INSERT/DELETE + student table ⭐ | 14 · Part B | §3.2 Q241, §4 D3–D4 |
| 242 | Prepared INSERT/DELETE by register no. | 14 · Part B | §3.2 Q242, §4 D5 |
| 243 | SELECT multi-row → HTML table ⭐ | 14 · Part B | §3.2 Q243, §4 D6 |
| 244 | UPDATE syntax/precautions + update email ⭐ | 14 · Part B | §3.2 Q244, §4 D8 |
| 245 | App architecture + products into HTML list | 14 · Part B | §3.2 Q245 |
| 246 | Session lifecycle + session ID + login time | 14 · Part B | §3.2 Q246 |
| 247 | Cookies vs sessions + recommend for login | 14 · Part B | §3.2 Q247 |
| 248 | Full SQL workflow + INSERT success report | 14 · Part B | §3.2 Q248 |
| 249 | CREATE TABLE types/constraints + employee | 14 · Part B | §3.2 Q249 |
| 250 | Careful DELETE + prepared delete by dept | 14 · Part B | §3.2 Q250 |
| 251 | SELECT result processing + marks > 50 | 14 · Part B | §3.2 Q251 |
| 252 | UPDATE + affected_rows + 10% raise | 14 · Part B | §3.2 Q252 |
| 253 | Steps for dynamic HTML + students list | 14 · Part B | §3.2 Q253 |

### The six master themes (every question is one of these, wearing a hat)

1. **State management** — HTTP forgets you; cookies (client, 4 KB, editable) and sessions (server, ID cookie) remember you. → Q93, 94, 95, 100, 111, 113, 114, 115, 123, 124, 125, 238, 239, 246, 247.
2. **Connection** — `mysqli_connect()` / `new mysqli()` + failure check + `close()`. → Q92, 110, 116, 234, 240, 248.
3. **Fetch loop** — result handle → `while ($row = mysqli_fetch_assoc($result))` → `$row["col"]`. → Q101, 104, 106, 108, 128, 243, 251, 253.
4. **CRUD from PHP** — CREATE / INSERT / UPDATE / DELETE through `mysqli_query()`, with `affected_rows` and `insert_id`. → Q96, 98, 109, 117–121, 241, 242, 244, 248–252.
5. **Prepared statements** — `?` placeholders + `bind_param("ssi", …)`; structure and data never mix. → Q99, 242, 250.
6. **Dynamic pages** — static HTML vs HTML generated per request; PHP interleaved with markup, `<?= ?>`, alternative `while: endwhile`. → Q102, 122, 129, 229, 231, 245, 253.

---

## 2. PART 1 — Deep dive, from zero

### 2.1 Why HTTP is stateless — the problem everything else solves (4:L27–53)

**Story:** a shop assistant with amnesia. Every time you walk up to the counter he greets you as a brand-new customer, because he genuinely cannot remember the last 30 seconds.

**Definition.** HTTP is *stateless*: each request is a complete, independent message. The server opens nothing, remembers nothing, and by the time your second click arrives it has no idea the first one was also you (4:L31–33). That is a *feature* for serving 10,000 strangers cheaply, and a *bug* the moment you need "logged in".

**Why it bites, concretely.** Page 1 checks the password and shows the dashboard. Page 2 is a separate request — it has no idea a password was ever checked. Without a memory mechanism, every page would need the password again.

The deck names exactly two memory mechanisms (4:L37–51):

| Mechanism | Where the data lives | Who can read it |
|---|---|---|
| Cookie | Your browser's storage, sent back on every request to that domain | You — and any script on your machine (4:L73) |
| Session | The server's disk/temp storage | Only the server; your browser holds just an ID (4:L45) |

**Why it matters for marks:** "why state management?" is the opening move of Q93, 100, 111, 113, 247. The 2-mark skeleton is *stateless HTTP → need memory → two places to put it → client (cookie) or server (session)*.

> **Say this if grilled:** "HTTP has no memory between requests, so any continuity — login, cart, multi-step form — must be carried by something: a cookie on the client, or a session on the server referenced by a cookie."

### 2.2 Cookies — memory that lives in the browser (4:L63–88)

**Story:** a coffee-shop loyalty card the customer carries. The shop writes your stamp on *your* card; you show it next visit. Lose it, edit it, or forge it — the shop can't tell.

**Definition.** A cookie is a small name/value pair that the server sends in an HTTP **response header** (`Set-Cookie`) and asks the browser to store and replay automatically on every later request to that domain (4:L39).

**The function** — `setcookie(name, value, expiry, path)`:

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

**Decoding the four arguments** (4:L67):

| Argument | What it is | Value to memorise |
|---|---|---|
| `name` | The key you will read back | `"username"` |
| `value` | The data (a string; keep it small) | `"Anu"` |
| `expiry` | Unix timestamp after which the browser discards it | `time() + 3600` = 1 hour |
| `path` | Which URLs on the site receive it | `"/"` = whole site |

**The three rules that earn marks**

1. **`setcookie()` must run before any HTML output** (4:L65). Cookies travel as HTTP *headers*, and headers are flushed before the body. One stray space, one `echo`, one blank line above `<?php` and you get *"headers already sent"*. Same rule for `session_start()` (4:L104).
2. **To delete, re-set with a past expiry** (4:L71) — set the value to `""` and the expiry to `time() - 3600`. There is no `deletecookie()`.
3. **Never store anything secret in a cookie** (4:L73). It sits in a text file the user can open and edit. A cookie saying `role=admin` is an invitation.

**Limits** — say these numbers: ~**4 KB per cookie** (4:L142), a few dozen cookies per domain, and the whole cookie jar travels with *every* matching request, so fat cookies slow every page.

**Where cookies are genuinely good** (4:L148): remembering a theme or language preference, a "remember me" token, a non-sensitive last-visited value.

**Why it matters:** Q113, Q124 ask straight for this, Q238/Q239 ask for create/access/delete, and every session answer starts "the browser holds a cookie containing the session ID".

> **Say this if grilled:** "A cookie is client-side storage written by `setcookie()` before any output, read back through `$_COOKIE`, deleted by re-setting it with a past expiry — and it is untrusted user-editable data, capped at about 4 KB."

### 2.3 Sessions — memory that lives on the server (4:L102–124)

**Story:** a cloakroom. You hand over your coat, you get a numbered token. The coat (your data) never leaves the building; you only carry the number.

**Definition.** A session is server-side storage for one visitor, identified by a **session ID** that PHP sends to the browser as a cookie (by default named `PHPSESSID`) (4:L45, 4:L106).

**The four calls** (4:L106–112):

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

**What each one actually does**

| Call | Effect | Exam-critical detail |
|---|---|---|
| `session_start()` | Reads the incoming `PHPSESSID` cookie; if none, mints a new ID and creates the session | Must precede **every** `$_SESSION` read/write, and must precede output (4:L104) |
| `$_SESSION["k"] = v` | Writes into the server's session store | Nothing is sent to the client except the ID |
| `unset($_SESSION["k"])` | Removes one key | `session_unset()` removes all — *this is not on your slide, it is standard* |
| `session_destroy()` | Deletes the session file on the server | It does **not** empty `$_SESSION` in the current request — call `session_unset()` first (standard) |

**Lifecycle in one line each** (this is Q246): browser requests page → `session_start()` → no ID cookie, so PHP mints an ID and sends `Set-Cookie: PHPSESSID=…` → the server creates a file keyed by that ID → every later request replays the cookie → `session_start()` loads that file into `$_SESSION` → on logout `session_unset()` + `session_destroy()`, and the ID becomes worthless.

**Session ID — the whole security model in one object.** It is a long random string. Anyone holding it *is* you, so: never put it in a URL if you can avoid it, and regenerate it on login with `session_regenerate_id(true)` so a pre-login ID can't be reused (standard).

**Why it matters:** sessions are the answer to Q95, Q100, Q111, Q123, Q125, Q246, Q247 — and the reason `$_SESSION["user_id"]` exists at all.

> **Say this if grilled:** "A session stores data on the server and gives the browser only a random session ID in a cookie; `session_start()` loads or creates it, `session_destroy()` deletes it — so the sensitive data never travels."

### 2.4 Cookies vs sessions — the comparison table you must be able to write cold (4:L136–160)

**Story:** a note pinned to your own fridge (cookie) versus a locked filing cabinet at the office with your name on the drawer (session).

| Point | Cookie | Session |
|---|---|---|
| Storage location | Browser/client (4:L140) | Server (4:L152) |
| What travels | The **data itself**, every request | Only the **session ID** |
| Size limit | ~4 KB per cookie (4:L142) | Practically unlimited (server disk) |
| Security | Visible and editable by the user — never sensitive (4:L144) | Data never leaves the server — safe for credentials/roles (4:L154) |
| Lifetime | Whatever expiry you set — days or months (4:L146) | Until browser closes by default, or a server timeout (4:L156) |
| Setup needed | `setcookie()` before output | `session_start()` on **every** page that uses it (4:L158) |
| Good for | Preferences, "remember me" (4:L148) | Login state, shopping cart, multi-step forms (4:L160) |

**Exam shortcut:** every row is one of four axes — *where it lives, how big, how safe, how long*. Q247 explicitly asks for storage/lifetime/security/application, i.e. exactly this table minus two rows.

**Why it matters:** Q93 and Q114 are this table in prose; Q247 is this table plus a recommendation ("sessions, because the credential must not be client-editable").

> **Say this if grilled:** "Cookies live in the browser and carry data; sessions live on the server and carry only an ID. Cookies are for preferences, sessions are for identity."

### 2.5 Why pair PHP with MySQL (4:L170–195)

**Story:** PHP is a brilliant talker with no memory; MySQL is a filing cabinet with no mouth. Together they can hold a conversation that lasts years.

**Four points, in the deck's order**

1. **Plain PHP forgets everything** (4:L176). Variables, sessions, form data all vanish when the script ends. Modules 1–3 gave you no permanent storage.
2. **A database is persistent and shared** (4:L182). MySQL is *relational*: data in tables of rows and columns, stored on disk, identical for every future request and every user.
3. **Why MySQL specifically** (4:L188): free and open-source, the default on almost all shared hosting, and the **M** in **LAMP** (Linux, Apache, MySQL, PHP).
4. **The bridge is an extension** (4:L194): PHP cannot speak MySQL's wire protocol itself. **MySQLi** (MySQL Improved) is the classic choice for this course; **PDO** is the modern, database-agnostic alternative.

**The one-line architecture** (also Q245, Q253): browser → Apache → PHP engine → MySQL → rows back to PHP → PHP prints HTML → browser. The browser never sees SQL, the schema, or the password.

**Why it matters:** Q230 (PHP's importance) and Q234/Q245 want this framing before any code; Q102/Q122 want "dynamic = generated from live data" which is only possible *because* of this pairing.

> **Say this if grilled:** "PHP alone has no persistence, so the database is the memory; MySQLi is the extension that lets PHP send SQL strings and receive rows."

### 2.6 Connecting: `mysqli_connect()` — the very first step (4:L206–230)

**Story:** dialling a phone number. Nothing can be said until the call connects, and if it doesn't connect you must *know* immediately instead of talking into silence.

**Signature (memorise exactly):**

```text
mysqli_connect(host, username, password, database)   ->  connection handle (object) | false
```

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

**Argument by argument** (4:L210–216)

| Argument | Meaning | Typical value |
|---|---|---|
| `host` | Machine running MySQL | `"localhost"` when PHP and MySQL share a server (4:L214) |
| `username` | MySQL account | `"root"` on XAMPP/local |
| `password` | That account's password | `""` on default XAMPP, never `""` in production |
| `database` | Which database to open | `"college_db"` — optional; if omitted you must `mysqli_select_db()` later |

**What comes back.** A **connection handle** — a `resource`/object representing the open link, stored in `$conn` and passed to *every* later call. On failure it returns `false` (procedural style) — which is why `if (!$conn)` works.

**`mysqli_close($conn)`** releases the link (4:L216). The deck notes PHP closes it automatically at script end, so it is *discipline*, not necessity — but write it in exams, it shows you know the lifecycle.

**Why it matters:** nothing else in this module compiles without a `$conn`. Q92, Q110, Q116, Q234, Q240, Q248 all start here.

> **Say this if grilled:** "`mysqli_connect()` takes host, user, password and database and returns a connection handle or `false`; every subsequent query passes that handle, and `mysqli_close()` releases it."

### 2.7 The same connection, object-oriented (4:L244–268)

**Story:** same phone call, different handset — buttons instead of a switchboard operator.

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

**Mapping table — know which side each name lives on** (4:L248–254)

| Job | Procedural | Object-oriented |
|---|---|---|
| Connect | `mysqli_connect(...)` | `new mysqli(...)` |
| Connection error | `mysqli_connect_error()` | `$conn->connect_error` |
| Run a query | `mysqli_query($conn, $sql)` | `$conn->query($sql)` |
| Fetch a row | `mysqli_fetch_assoc($result)` | `$result->fetch_assoc()` |
| Rows affected | `mysqli_affected_rows($conn)` | `$conn->affected_rows` |
| Last insert id | `mysqli_insert_id($conn)` | `$conn->insert_id` |
| Error text | `mysqli_error($conn)` | `$conn->error` |
| Close | `mysqli_close($conn)` | `$conn->close()` |

**Which to write in the exam?** The procedural form — it is what 90% of the deck's examples use, and mixing the two mid-script is the classic way to lose a mark. But *know* the OO column, because questions say "using MySQLi" and examiners like `$conn->affected_rows`.

> **Say this if grilled:** "MySQLi exposes two APIs over the same engine — functions taking `$conn` first, or methods on the connection object; they are interchangeable, but never mixed in one script."

### 2.8 Connection error handling + the four best practices (4:L280–305)

**Story:** a pilot's pre-flight check. Thirty seconds of checking prevents a crash nobody can diagnose later.

**The failure check is not optional.** A failed connection returns `false`; if you ignore it, every later call receives `false` where a handle should be and you get a chain of confusing warnings instead of one clear message (4:L290–292).

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
```

- `die("message")` prints the message and **stops the script** — correct here, because there is nothing sensible left to do without a database.
- `mysqli_connect_error()` returns the *reason* (e.g. `Access denied for user 'root'@'localhost'`). Printing it while learning is fine; in production you log it and show a generic page, because it leaks server details (standard).

**The four practices** (4:L284–304)

1. **Never hardcode credentials in shared code** — put them in a separate config file kept out of version control (4:L286).
2. **Always check for connection failure** (4:L290).
3. **Close the connection when done** — good discipline in long-running scripts (4:L296).
4. **Prepared statements are the production path** — the module builds SQL by string concatenation *for clarity*, but real code uses `mysqli_prepare()` (4:L302–304).

**One thing your deck does not say but PHP 8 does** (standard): since PHP 8.1, mysqli throws `mysqli_sql_exception` by default instead of returning `false`, so `if (!$conn)` never fires. The exam-safe pattern that works in both worlds is `try { … } catch (mysqli_sql_exception $e) { die($e->getMessage()); }`. Write the `if (!$conn)` form the deck teaches; mention exceptions only if asked "how would you harden this".

> **Say this if grilled:** "Check the return value immediately with `if (!$conn)` and `mysqli_connect_error()`, then `die()` — a silently failed connection produces misleading errors three function calls later."

### 2.9 Running a query: `mysqli_query()` and the result handle (4:L316–337)

**Story:** posting a letter. You hand it to the post office (MySQL). For a *question* ("SELECT") you get a parcel back; for an *instruction* ("INSERT") you get only a receipt saying it was accepted.

**Signature:** `mysqli_query($conn, $sql)` — the deck's own summary: *executes a query and returns a result handle (for SELECT) or true/false (for INSERT/UPDATE/DELETE)* (4:L320).

```php
<?php
$sql = "SELECT name, marks FROM students";
$result = mysqli_query($conn, $sql);

if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}
?>
```

**The two return types — this is the single most examined detail on the slide**

| Query kind | Returns on success | You then do |
|---|---|---|
| `SELECT`, `SHOW`, `DESCRIBE` | A **result handle** (a `mysqli_result` object) | `mysqli_fetch_assoc($result)` in a loop |
| `INSERT`, `UPDATE`, `DELETE`, `CREATE` | `true` | `mysqli_affected_rows($conn)` / `mysqli_insert_id($conn)` |

→ Trying to `fetch_assoc()` a `true` is the classic fatal error *"Call to a member function fetch_assoc() on bool"*.

**Error path.** `mysqli_error($conn)` returns MySQL's own message for the *last* failed query (4:L324). `$sql` is just a string — building it from user input is exactly how injection happens (4:L326), see 2.18.

**Why it matters:** Q126 asks its purpose in one line; every CRUD answer in Part B is this function with a different string.

> **Say this if grilled:** "`mysqli_query()` sends one SQL statement and returns a result handle for SELECT or a boolean for writes — so you branch on what kind of statement you sent."

### 2.10 Reading rows: `mysqli_fetch_assoc()` and its siblings (4:L351–370, 4:L383–393)

**Story:** a ticket roll. Each pull gives you the next ticket; when the roll is finished you get nothing — and "nothing" is exactly how you know to stop.

```php
<?php
while ($row = mysqli_fetch_assoc($result)) {
    echo $row["name"] . " " . $row["marks"] . "<br>";
}

echo "Total rows: " . mysqli_num_rows($result);
?>
```

**How the loop terminates — say this precisely.** `mysqli_fetch_assoc()` returns one row as an **associative array** (`["column" => value]`) and advances an internal pointer (4:L355–357). When no rows remain it returns **`NULL`**, `NULL` is falsy, so the `while` condition fails and the loop ends. That is why `while ($row = mysqli_fetch_assoc($result))` needs no counter (4:L357, 4:L393).

**The four fetch styles** (4:L385–391) — Q106 is this table:

| Function | Returns | Column access | Notes |
|---|---|---|---|
| `mysqli_fetch_assoc()` | Associative array | `$row["name"]` | Most common; readable (4:L387) |
| `mysqli_fetch_array()` | **Both** numeric and associative keys | `$row["name"]` **or** `$row[0]` | Flexible but heavier — each value stored twice (4:L388) |
| `mysqli_fetch_row()` | Indexed array only | `$row[0]` | Position-based; breaks if column order changes (4:L389) |
| `mysqli_fetch_object()` | Object | `$row->name` | Nice for OO code (4:L390) |

**Related counters**

- `mysqli_num_rows($result)` → integer count of returned rows, **without** consuming them (4:L361, 4:L391). Use it for "no records found" checks and paging.
- `mysqli_affected_rows($conn)` → rows *changed* by the last write query — a different thing entirely (2.17).
- `mysqli_free_result($result)` → frees the result memory (standard, optional).

**Why it matters:** Q101, Q104, Q108, Q128, Q243, Q251, Q253 all end in this loop. Half of Part B is "fetch rows and print an HTML table".

> **Say this if grilled:** "It pulls the next row as an associative array and moves the pointer; it returns `NULL` at the end, which is what terminates the `while` loop."

### 2.11 The five-step cycle + closing discipline (4:L399, 4:L405–419)

**Story:** a factory line with five stations. Every product — a student list, a product list, a marks report — goes through the same five stations.

The deck's own diagram (4:L399) and numbered list (4:L407–417):

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

**Close-out order** for a full page (the tidy version you should write in exams):

```php
<?php
mysqli_free_result($result);   // release the result set
mysqli_close($conn);           // release the connection
?>
```

**Why it matters:** it is the skeleton of Q243, Q245, Q248, Q251, Q253 and the "architecture" half of Q245. If you can draw five boxes and label them, you have 6–8 of those 14 marks before writing a line of code.

> **Say this if grilled:** "Build the SQL, run it, get a handle, loop the handle into rows, echo one HTML fragment per row — and the browser only ever sees step 5's output."

### 2.12 CREATE TABLE — defining structure before storing anything (4:L431–453)

**Story:** buying a filing cabinet and labelling the drawers *before* you have any paper. Once paper is in, changing the drawer labels is painful.

**SQL shape** (4:L435):

```sql
CREATE TABLE students (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    name   VARCHAR(50),
    marks  INT,
    joined DATE
);
```

**The pieces you must be able to name**

| Piece | Meaning | Why it's there |
|---|---|---|
| `CREATE TABLE name ( … )` | Defines columns and their types | A table must exist before any INSERT (4:L435) |
| `INT AUTO_INCREMENT PRIMARY KEY` | Unique, self-numbering id | Every row gets an identity you can target with `WHERE id = …` (4:L437) |
| `VARCHAR(50)` | Variable-length text up to 50 chars | Names, emails — the workhorse type |
| `TEXT` | Long text | Descriptions, feedback |
| `DATE` | Calendar date | `joined`, `admitted` |
| `DECIMAL(10,2)` | Exact decimal, 2 places | Money — never `FLOAT` for currency (standard) |
| `NOT NULL` | Column cannot be empty | Enforces data quality at the DB level (standard) |
| `UNIQUE` | No duplicate values | Email, register number (standard) |

**Run it from PHP** — the deck does this *once*, at setup (4:L441, 4:L445–452):

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

**Two traps**: (a) running it on every page load → *"table already exists"*; use `CREATE TABLE IF NOT EXISTS` or run it once from phpMyAdmin (standard). (b) Forgetting the `PRIMARY KEY` → duplicate rows you cannot address individually.

**Why it matters:** Q117 (purpose), Q109 (CREATE from PHP), Q241, Q249 all need this; Q249 additionally wants column types and constraints explained.

> **Say this if grilled:** "CREATE TABLE declares the schema — column names, types and constraints — and is run once at setup, because INSERT can only write into a structure that already exists."

### 2.13 INSERT — adding a new row (4:L468–490)

**Story:** filling in one new index card and dropping it in the drawer. The drawer's labels already tell you which field goes where.

**SQL shape** (4:L472): `INSERT INTO table (columns) VALUES (values)` — the deck insists the **explicit column list is safest**, because it survives later schema changes and cannot silently shift values into the wrong columns.

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

**Three rules**

1. **Strings get quotes, numbers don't** (4:L474). `'$name'` is quoted in the SQL text; `$marks` is cast to `(int)` so it needs none. Forget the quotes around a string and MySQL reads the word as a column name → `Unknown column 'Anu' in 'field list'`.
2. **`mysqli_insert_id($conn)`** returns the `AUTO_INCREMENT` id MySQL just assigned (4:L476) — the only way to know the new row's key without a second SELECT.
3. **Building `$sql` from raw form input is unsafe** (4:L478): that is injection. The deck's own fix is `(int)` casting for numbers and, properly, prepared statements (2.18).

**Omitting the column list** — `INSERT INTO students VALUES (…)` — works only if you supply *every* column in *table order*, and it breaks the moment a column is added (standard). Never do it in the exam.

**Why it matters:** Q96, Q112, Q118, Q241, Q242, Q248, Q253 — inserting a record *with* error handling is the single most repeated Part A/B demand in this module.

> **Say this if grilled:** "INSERT INTO table (columns) VALUES (values), strings quoted, numbers cast to int, checked with `if (!mysqli_query(...))` and confirmed with `mysqli_insert_id()`."

### 2.14 DELETE — removing rows (4:L505–525)

**Story:** a shredder, not a waste-paper basket. What goes in does not come back.

**SQL shape** (4:L509): `DELETE FROM table WHERE condition`

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

**The four points the slide makes**

1. `WHERE` limits deletion to matching rows (4:L509).
2. **Never omit `WHERE` unless you mean to empty the table** (4:L511) — `DELETE FROM students` with no clause wipes everything, and there is no undo.
3. `mysqli_affected_rows($conn)` tells you how many rows actually went (4:L513).
4. **Preview with the equivalent SELECT first** (4:L515) — a habit, not syntax.

**The zero-row trap.** A DELETE with a `WHERE` that matches nothing *succeeds* (no error) and affects 0 rows. Only `affected_rows` reveals that nothing happened (4:L687–689). Same for UPDATE.

**Why it matters:** Q119 (purpose), Q242b (delete by register number), Q250 (delete by department, prepared) — and the "safe DELETE" discussion is worth 7 of those 14 marks.

> **Say this if grilled:** "DELETE FROM table WHERE condition — the WHERE is the whole safety mechanism, affected_rows is the only proof it did what you meant, and a SELECT with the same WHERE is the dry run."

### 2.15 UPDATE — changing existing values (4:L630–652)

**Story:** correcting a typo on an existing card, not writing a new one. If you don't say *which* card, you rewrite the entire drawer.

**SQL shape** (4:L634): `UPDATE table SET col = value WHERE condition`

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

**Points to state** (4:L634–640)

- Multiple columns in one statement: `SET col1 = val1, col2 = val2` (comma-separated, one `SET`).
- **Without `WHERE`, every row is updated** — "almost always a mistake" (4:L638).
- `mysqli_affected_rows($conn)` confirms how many rows actually changed (4:L640).
- You can compute from the old value: `SET salary = salary * 1.10` (that is Q252).

**Subtlety worth a mark** (standard): MySQL's `affected_rows` counts rows whose values **actually changed**. Re-saving the same value returns 0 even though the row matched. `mysqli_info($conn)` or a `SELECT` confirms the match count if you need it.

**Why it matters:** Q98, Q121, Q244, Q252 — and Q127 wants exactly the "why WHERE matters" defence.

> **Say this if grilled:** "UPDATE table SET col = value WHERE condition; no WHERE means every row, and `affected_rows` is how you prove the right number of rows changed."

### 2.16 SELECT — the only statement that gives data back (4:L558–580, 4:L595–615)

**Story:** asking a librarian a question — the only interaction where something comes back over the counter.

**Definition.** SELECT *returns* rows; every other statement only succeeds or fails (4:L560). It is therefore the only statement whose result you loop over.

**The pieces**

| Clause | Purpose | Example |
|---|---|---|
| `SELECT *` | Every column | `SELECT * FROM students` (4:L562) |
| `SELECT col1, col2` | Only what you need — faster, clearer | `SELECT name, marks FROM students` (4:L564) |
| `WHERE` | Filters **rows** | `WHERE marks >= 75` (4:L566) |
| `ORDER BY col ASC/DESC` | Sorts rows | `ORDER BY marks DESC` (4:L599) |
| `LIMIT n` | Caps row count | `LIMIT 5` (4:L601) |
| `LIMIT offset, count` | Skips then takes — pagination | `LIMIT 10, 5` (4:L603) |
| `LIKE` | Pattern match | `WHERE name LIKE 'A%'` (4:L568) |

**Operators** (4:L568): `=`, `!=`, `>`, `<`, `>=`, `<=`, `LIKE`. `LIKE` uses `%` for "any characters": `'A%'` starts with A, `'%a'` ends with a, `'%an%'` contains "an".

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

**Clause order is fixed** — `SELECT … FROM … WHERE … ORDER BY … LIMIT …`. Swap two and MySQL errors out; this is a free mark in any "write the query" question.

**Why it matters:** Q101, Q104, Q108, Q120, Q243, Q251, Q253. The WHERE variant (`marks > 50`) is literally Q251.

> **Say this if grilled:** "SELECT is the read operation — column list, FROM, optional WHERE, ORDER BY, LIMIT — and it is the only query whose return value you fetch in a loop."

### 2.17 `affected_rows` — the number that proves a write happened (4:L513, 4:L640, 4:L687–689)

**Story:** a delivery receipt. "Delivered" without a count could mean one parcel or the whole warehouse.

```php
<?php
mysqli_query($conn, $sql);                 // some UPDATE or DELETE
echo mysqli_affected_rows($conn);          // rows actually touched
echo $conn->affected_rows;                 // OO form — same number
?>
```

**Three counts, do not confuse them**

| Function | Counts | Applies to |
|---|---|---|
| `mysqli_affected_rows($conn)` | Rows **changed** by the last write | INSERT / UPDATE / DELETE |
| `mysqli_num_rows($result)` | Rows **returned** by a SELECT | SELECT only |
| `mysqli_insert_id($conn)` | The id **generated** by the last INSERT | INSERT with AUTO_INCREMENT |

**Why the slide calls it a habit** (4:L687–689): a query can "succeed" with 0 affected rows — wrong `WHERE`, no matching id, duplicate value. No error is raised. The count is the only signal.

**Why it matters:** Q252a asks its role in one half; Q244, Q250 want it in code.

> **Say this if grilled:** "`affected_rows` is the count of rows the last UPDATE/DELETE/INSERT actually changed — success without a count can still mean zero rows matched."

### 2.18 SQL injection and prepared statements (4:L302–304, 4:L326, 4:L681–683)

**Story:** a form that asks for your name, and someone writes *"ignore the question, empty the safe"* — and the form obeys, because it pasted the answer into the instruction sheet.

**The vulnerability, concretely.** This code looks harmless:

```php
<?php
$email = $_POST["email"];
$sql = "SELECT * FROM users WHERE email = '$email'";
$result = mysqli_query($conn, $sql);
?>
```

If the user submits `' OR '1'='1`, the string becomes:

```sql
SELECT * FROM users WHERE email = '' OR '1'='1'
```

…which is true for every row: the whole table leaks. Submit `'; DROP TABLE users; --` and the table is gone. The cause is structural: **the data was concatenated into the SQL text, so the database cannot tell data from code** (4:L326).

**The fix — placeholders.** `mysqli_prepare()` sends the SQL *structure* first with `?` where values go; the values are sent separately afterwards (4:L683):

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

**The `bind_param` type string — one letter per `?`, in order** (standard, the deck only names the function):

| Letter | Type | Use for |
|---|---|---|
| `s` | string | names, emails, dates, decimals-as-text |
| `i` | integer | ids, marks, counts |
| `d` | double/float | prices, measurements |
| `b` | blob | binary data |

So `bind_param("ssi", $name, $email, $age)` means *string, string, int* — three placeholders, three variables, same order.

**Why prepared statements actually stop injection** (the sentence that earns the marks): the statement is **parsed and compiled before the values arrive**, so a value can never be reinterpreted as SQL syntax. `' OR '1'='1` is stored as a literal 13-character email, not as a condition. Bonus: the same prepared statement can be executed repeatedly with different values, which is faster for bulk inserts.

**Other defences the deck mentions** (4:L675–677): cast numeric input with `(int)`, and test the WHERE with a SELECT first (4:L669).

**Why it matters:** Q99 is a Part A certainty, Q242 and Q250 are Part B prepared-statement programs, and any "precautions" half of Q244/Q250 wants this.

> **Say this if grilled:** "Prepared statements compile the SQL before the data arrives, so user input is only ever a value — concatenation lets it become syntax, which is the entire injection bug."

### 2.19 Mixing PHP into HTML — the alternative syntax (4:L735–755)

**Story:** a stencil over a wall. The HTML is the wall; PHP lifts the stencil once per database row.

**The pattern** (the deck's own code, 4:L748–755):

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

**Four syntax facts to get right**

1. **`while (...):` with a colon, closed by `endwhile;`** — not `{ }`. This is PHP's *alternative syntax*, designed for templates because a `}` alone in the middle of HTML is unreadable (4:L739). The same exists for `if: endif;` and `foreach: endforeach;`.
2. **`<?= $expr ?>` is shorthand for `<?php echo $expr; ?>`** (4:L790, and 3:L55). Legal and expected in the dynamic-page answer.
3. **A `<?php ?>` block may open and close many times inside one file** (4:L739) — that is the whole technique.
4. **`htmlspecialchars()` around any user-supplied value** (4:L743) turns `<` into `&lt;`, so a stored name like `<script>alert(1)</script>` prints as text instead of executing. This is XSS defence, and it is a marked point.

**The same loop in non-alternative syntax** — safe to write if you forget the colon form:

```php
<?php while ($row = mysqli_fetch_assoc($result)) { ?>
<tr><td><?= htmlspecialchars($row["name"]) ?></td></tr>
<?php } ?>
```

**Why it matters:** Q229, Q231, Q245, Q253 all end in "display it as HTML"; the colon/endwhile pair is the most commonly lost mark in the module.

> **Say this if grilled:** "PHP can close and reopen mid-HTML; the alternative `while: … endwhile;` syntax keeps the markup readable, `<?=` echoes, and `htmlspecialchars()` stops stored HTML from executing."

### 2.20 The complete dynamic page — every piece in one file (4:L770–792)

**Story:** the whole kitchen, one service. Order in, plate out.

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

**Annotation, in the deck's own three steps** (4:L774–778): 1. connect, 2. run the query, 3. loop and echo each row as HTML. The deck's claim to quote: *"This exact shape — connect, query, loop, render — is the backbone of almost every PHP page that shows database content"* (4:L780).

**What "dynamic" means here, precisely** (4:L705): the `.php` file on disk never changes; the HTML it *emits* is rebuilt per request from whatever is in the table. Add a row in phpMyAdmin, refresh, and the page changes with no edit to the file. That sentence answers Q102, Q122, Q129 and half of Q253.

**Layering** (4:L717, and Q245): even in one file, keep three concerns visible — **data access** (the query), **business logic** (any PHP rules), **presentation** (the HTML). That separation is the informal precursor to Module V's MVC.

**Why it matters:** this is the highest-probability 14-mark answer in the module and the direct answer to Q253.

> **Say this if grilled:** "Connect, query, loop, render — the file is static, its output is not, because the row data is read at request time."

### 2.21 What the bank asks that your deck never covers (all "(standard, not in your deck)")

Five question clusters have no slide. Learn them here; do not claim the deck said them.

**(a) `$_SERVER['PHP_SELF']` (Q103).** The bank writes `$_PHP_SELF`, which is a typo — there is no such superglobal. The real value is `$_SERVER['PHP_SELF']`: the *path of the currently executing script*, used as a form's `action` so the form posts to itself:

```php
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
```

`htmlspecialchars()` matters here: without it a crafted URL can inject script into the action attribute (XSS).

**(b) Regex (Q97, Q235, Q236, Q237)** — the deck covers this in Module 3, not 4 (3:L568–586, telephone table 3:L597–607):

```php
<?php
if (preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)) {
    echo "Valid email";
}
$clean = preg_replace("/[0-9]/", "", "Room12A");   // "RoomA"
?>
```

- `preg_match()` returns `1` on match, `0` on no match, `false` on error → always compare with `== 1` or cast to bool.
- `preg_match_all()` fills an array with **every** match — that is how you extract all emails from a page of text.
- Delimiters `/…/` are required; `^` and `$` anchor start/end; `{n}` means exactly n times (3:L607).

**(c) File upload (Q233a)** — `$_FILES`, `enctype`, `move_uploaded_file()`; full drill at §4 D15.

**(d) `sqrt()` / factorial / `date()` (Q105, Q231, Q233b)** — plain PHP functions, drilled at §4 D12–D14.

**(e) `SHOW DATABASES` (Q107)** — a SQL statement, not a PHP function:

```php
<?php
$result = mysqli_query($conn, "SHOW DATABASES");
while ($row = mysqli_fetch_row($result)) {   // index 0 = database name
    echo $row[0] . "<br>";
}
?>
```

`SHOW TABLES` is the same idea one level down; `DESCRIBE students` lists a table's columns.

---

## 3. PART 2 — Answer bank

### 3.1 3-mark answers (Part A)

Write **3 or 4 numbered/bulleted points**, or one short code block plus two lines. That is the whole shape of a 3-mark answer: three facts, or code + one explanation. Duplicates are merged into **MASTER ANSWERS**; the numbers each one covers are listed.

**A1 — Steps to establish a PHP–MySQL connection · also answers Q110, Q116, Q92**

1. **Connect** — `mysqli_connect(host, user, password, database)` returns a connection handle or `false`.
2. **Check** — `if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }` so a failure stops the script with a readable reason.
3. **Use** — pass `$conn` as the first argument to `mysqli_query()` for every statement.
4. **Close** — `mysqli_close($conn)` (optional; PHP closes at script end).

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "college_db");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }
echo "Connected successfully";
mysqli_close($conn);
?>
```

*OO one-liner variant if the question says "using object-oriented MySQLi":* `$conn = new mysqli("localhost","root","","college_db"); if ($conn->connect_error) die($conn->connect_error);`

**A2 — `$_SESSION` vs `$_COOKIE` · also answers Q93, Q114**

| | `$_SESSION` | `$_COOKIE` |
|---|---|---|
| Stored on | Server | Client browser |
| Browser holds | Only the session ID | The data itself |
| Size | Large | ~4 KB |
| Security | Safe for sensitive data | User-editable — never trust it |
| Lifetime | Until browser closes / timeout | Until its expiry timestamp |
| Needs | `session_start()` first | `setcookie()` before output |

**Use a session** for login state, a cart, anything secret. **Use a cookie** for a theme preference or "remember me" token.

**A3 — GET vs POST · Q94** *(Module 3 material: 3:L619–640)*

| | GET | POST |
|---|---|---|
| Data goes | In the URL query string | In the request body |
| Visible in address bar | Yes | No |
| Length limit | ~2000 chars, browser-dependent | Effectively none |
| Bookmark / cache / resend-safe | Yes | No |
| Should be used for | Searches, filters, ids | Passwords, inserts, updates |
| PHP reads it with | `$_GET["f"]` | `$_POST["f"]` |

One extra mark: forms default to GET, so always write `method="post"` explicitly for anything that changes data or carries a password.

**A4 — Session: start, store name, display on another page · Q95**

*page1.php* stores it:

```php
<?php
session_start();
$_SESSION["username"] = "Anu";
echo "Stored. <a href='page2.php'>Next page</a>";
?>
```
*page2.php* reads it — a completely separate request:

```php
<?php
session_start();                                  // must repeat on every page
echo "Welcome, " . $_SESSION["username"];
?>
```
The link works because the browser replays the `PHPSESSID` cookie; `session_start()` on page 2 loads the same server-side data.

**A5 — Sessions keep state across pages; why they matter; advantages · also answers Q100, Q111, Q123**

1. HTTP is stateless — each request is independent, so a login on page 1 is invisible to page 2 unless something carries it (4:L31–33).
2. A session stores that state **on the server** and gives the browser only an ID, so credentials and roles never travel over the wire (4:L45).
3. Data persists across page loads until the session ends, which is what makes multi-page workflows (login → dashboard → checkout) possible (4:L110).
4. **Three advantages to name:** security (data not client-visible), capacity (far more than 4 KB), and continuity (survives navigation across the whole site) (4:L152–160).

**A6 — Insert a record with error handling · also answers Q96, Q112**

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
Points: connection check → `(int)` cast for the number → quoted string → branch on the boolean return of `mysqli_query()` → `mysqli_error()` on failure, `mysqli_insert_id()` on success.

**A7 — Function that validates an email with regex and returns a boolean · Q97** *(regex: 3:L568–586)*

```php
<?php
function isValidEmail($email) {
    return (bool) preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email);
}

if (isValidEmail("anu@saintgits.org")) { echo "Valid"; }
else { echo "Invalid"; }
?>
```
Explain: `preg_match()` returns `1`/`0`, so it is cast to a real boolean; `^`/`$` anchor the whole string; `[\w.-]+` allows letters, digits, underscore, dot, hyphen; `\.` is a literal dot; `{2,}` requires at least two letters in the TLD.

**A8 — Update a user's email with error handling · Q98**

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
Key marks: `SET col = value WHERE key = value`, the id cast to `(int)`, the error branch, and `affected_rows` reported — because a successful query that changed 0 rows means the id did not match.

**A9 — Prepared statements and why · Q99** *(4:L302–304, 4:L683)*

1. A prepared statement sends the SQL **template** with `?` placeholders to MySQL, which parses and compiles it *before* any data arrives.
2. The values are then bound separately: `mysqli_stmt_bind_param($stmt, "ssi", $name, $email, $age)` — one type letter per placeholder.
3. Injection is impossible because user input is only ever a **value**; it cannot become SQL syntax.
4. Bonus: the compiled statement can be executed repeatedly with new values — faster for bulk work.

```php
<?php
$stmt = mysqli_prepare($conn, "INSERT INTO students (name, marks) VALUES (?, ?)");
mysqli_stmt_bind_param($stmt, "si", $name, $marks);   // s = string, i = int
mysqli_stmt_execute($stmt);
mysqli_stmt_close($stmt);
?>
```

**A10 — Retrieve and display MySQL data on a page · also answers Q101, Q104, Q108**

1. Connect, then build a `SELECT`.
2. `mysqli_query()` returns a **result handle** (not data).
3. `while ($row = mysqli_fetch_assoc($result))` pulls one row per iteration and stops at `NULL`.
4. `echo` inside the loop emits the HTML.

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

1. **Static:** the `.html` file *is* the response; every visitor gets identical bytes.
2. **Dynamic:** the server runs a script per request and sends whatever HTML it produced *this* time — different user, different time, different rows (4:L705).
3. PHP is **server-side**: it can read a database, apply logic, and loop; the browser only ever receives the generated HTML, never the source or the SQL.
4. Consequence: the same `students.php` shows 3 rows or 3000 without a single edit to the file (4:L745).

**A12 — Purpose of `$_PHP_SELF` · Q103**

1. There is no `$_PHP_SELF` variable — the real superglobal is **`$_SERVER['PHP_SELF']`**, the path of the currently running script.
2. Used as a form's `action` so the form submits **to itself**, letting the same file both display and process the form.
3. Must be escaped with `htmlspecialchars()` when echoed into HTML, or a crafted URL can inject script into the `action` attribute.

```php
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
```

**A13 — Square root program · Q105**

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
Output: `Square root of 25 is 5`. Two marks for `sqrt()` + `echo`, one for the negative-input guard (`sqrt(-1)` yields `NAN`).

**A14 — `mysql_fetch_array()` vs `mysql_fetch_assoc()` · Q106**

| | `mysql_fetch_array()` | `mysql_fetch_assoc()` |
|---|---|---|
| Keys | Numeric **and** associative | Associative only |
| Access | `$row[0]` **or** `$row["name"]` | `$row["name"]` |
| Memory | Larger — each value stored twice | Smaller |
| Readability | Poor (magic numbers) | Good (column names) |
| Default in modern code | Rare | `mysqli_fetch_assoc()` — the standard |

Both return one row at a time and `NULL` when the rows run out; the bank's `mysql_` prefix is the deprecated PHP 5 API, the current names are `mysqli_fetch_*`. `mysqli_fetch_row()` is the indexed-only sibling.

**A15 — List the databases on the MySQL server · Q107** *(standard — no slide)*

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
`SHOW DATABASES` returns one column per database, so `mysqli_fetch_row()` with `$row[0]` is the natural fetch. `SHOW TABLES` and `DESCRIBE tablename` are the same pattern one level down.

**A16 — CREATE operations on a MySQL table from PHP; purpose of CREATE TABLE · also answers Q109, Q117**

1. `CREATE TABLE` defines a table's **structure** — column names, data types, keys, constraints. No data can be inserted until the structure exists (4:L433).
2. It is a **setup-time** statement: run once, not on every page load (4:L441).
3. From PHP it is executed like any other statement — a string through `mysqli_query()` — and returns only `true`/`false`, no rows.

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

**A17 — What is a cookie, its uses, and syntax with expiry · also answers Q113, Q124**

1. A cookie is a small name/value pair the server asks the browser to store; the browser replays it on every later request to that domain (4:L39).
2. **Two uses:** remembering user preferences (theme, language) and "remember me" / non-sensitive tracking between visits (4:L148).
3. Syntax: `setcookie("username", "Anu", time() + 3600, "/");` — name, value, **expiry as a Unix timestamp**, path. `time()+3600` = one hour (4:L67).
4. It must be called **before any output** (headers), and it is user-visible, so never store secrets (4:L65, 4:L73).

**A18 — Purpose of `session_start()` · also answers Q115, Q125**

1. It **starts or resumes** a session: it reads the incoming `PHPSESSID` cookie, and if there is none, generates a new session ID and sends it to the browser (4:L106).
2. It loads the server-side session data into the `$_SESSION` array, so `$_SESSION[...]` is usable.
3. It must be the **first thing** in the script — before any HTML output and before any `$_SESSION` access (4:L104).
4. Statement: `session_start();` — that exact line, on every page that touches session data.

**A19 — SQL command to add a record, with syntax · Q118**

`INSERT INTO table_name (col1, col2, col3) VALUES (val1, val2, val3);`

```sql
INSERT INTO students (name, marks, joined) VALUES ('Anu', 88, '2026-11-08');
```
Points: strings in single quotes, numbers bare; the column list should always be explicit (4:L472); from PHP the string is passed to `mysqli_query()` and confirmed with `mysqli_insert_id()` (4:L476, 4:L489).

**A20 — Purpose of DELETE · Q119**

1. Permanently **removes rows** matching a `WHERE` condition: `DELETE FROM students WHERE id = 5;` (4:L509).
2. It is irreversible — there is no undo, hence the `WHERE` discipline (4:L511).
3. It returns no rows, only success/failure; `mysqli_affected_rows()` reports how many were deleted (4:L513).
4. Safe practice: run the same condition as a `SELECT` first to preview the victims (4:L515).

**A21 — Purpose of SELECT · Q120**

1. **Reads** data — the only statement that returns rows rather than a status (4:L560).
2. Shape: `SELECT columns FROM table WHERE condition ORDER BY col LIMIT n` (4:L562–603).
3. In PHP the return value is a **result handle** you iterate with `mysqli_fetch_assoc()` (4:L355).
4. It is how dynamic pages get their content: same query, fresh rows per request (4:L705).

**A22 — SQL command to modify existing records · Q121**

`UPDATE table_name SET column = value WHERE condition;`

```sql
UPDATE students SET marks = 92 WHERE id = 5;
```
Points: comma-separate multiple assignments (`SET marks = 92, name = 'Anu'`); without `WHERE` **every row** is updated (4:L638); confirm with `mysqli_affected_rows()` (4:L640).

**A23 — Purpose of `mysqli_query()` · Q126**

1. It sends one SQL statement — SELECT, INSERT, UPDATE, DELETE, CREATE alike — to MySQL over an open connection (4:L320, 4:L847).
2. Signature: `mysqli_query($conn, $sql)`.
3. Return value differs by statement: a **result handle** for SELECT/SHOW, `true`/`false` for writes (4:L320).
4. Always check it; on `false`, `mysqli_error($conn)` gives the reason (4:L322–324).

**A24 — Why the WHERE clause is important in UPDATE/DELETE · Q127**

1. `WHERE` selects **which rows** the statement acts on; it is the only thing standing between one row and the whole table (4:L509, 4:L638).
2. Without it, `UPDATE` overwrites every row and `DELETE` empties the table — both irreversible in effect (4:L511, 4:L638).
3. Test the clause first as `SELECT … WHERE …`; if it returns the wrong rows, the destructive query would have hit them too (4:L669).
4. Even a correct-looking `WHERE` can match nothing — `mysqli_affected_rows()` (0) is the proof (4:L687–689).

**A25 — What `mysqli_fetch_assoc()` is for · Q128**

1. It fetches the **next row** of a result set as an **associative array** keyed by column name — `$row["name"]` (4:L355).
2. Each call advances an internal pointer; it returns **`NULL`** when no rows remain, which terminates `while (...)` (4:L357).
3. Used as `while ($row = mysqli_fetch_assoc($result)) { … }` to walk every row of a SELECT (4:L359, 4:L365).
4. It works only on a result handle from SELECT-type queries — never on the `true` returned by INSERT/UPDATE/DELETE.

**A26 — Two sources of dynamic content · Q129**

1. **A database** — rows read with `SELECT` at request time (the module's main source) (4:L705).
2. **Server-side/environment data** — the current date and time (`date()`), form input (`$_POST`), session/cookie values, or file contents (standard; the "time of day greeting" of Q231 is exactly this).
3. *(Third, for safety)* results of computation — totals, filtered lists, formatted numbers.

### 3.2 14-mark answers (Part B)

Each answer has **Structure** (how to split the marks), **Full answer** (code + the prose you write around it) and **Traps**. ⭐ = highest probability.

---

#### Q229 — Form app with name + email validation ⭐

**Structure:** 4 — the HTML form; 6 — validation logic (empty check + regex); 3 — personalised welcome on success; 1 — explanation of the request/response steps.

**Full answer**

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

**Explanation you write (2–3 sentences each):** the form posts back to the same script (`$_SERVER['PHP_SELF']`); `$_SERVER["REQUEST_METHOD"]` distinguishes the first display from the submitted request; `trim()` removes stray spaces; `empty()` catches missing fields; `preg_match()` checks the shape; errors accumulate in an array so all are shown at once; on success `htmlspecialchars()` neutralises anything HTML-like before echoing. *Optional 2-mark extension: insert the record with a prepared statement (§4 D5) instead of only echoing.*

**Traps:** `action=""` self-post works but `$_PHP_SELF` is the "expected" answer; echoing `$name` raw loses the XSS mark; `if (isset($_POST["name"]))` alone is weaker than checking `REQUEST_METHOD`.

---

#### Q230 — Importance of PHP in modern web development + challenges (10 marks)

**Structure:** 5 — why PHP matters; 3 — how it produces dynamic/interactive content; 2 — challenges.

**Full answer — point form (this is a 10-mark essay, not code)**

*Importance:* free and open-source; runs on virtually every shared host and on the LAMP stack (4:L188); huge ecosystem (WordPress, Laravel, Wikipedia); purpose-built for mixing with HTML and talking to MySQL (4:L194); low learning curve for a server-side language; enormous deployment base means cheap hosting and easy hiring.

*How it enables dynamic content:* the script runs on the **server** per request, so it can read a database (`SELECT`), apply business rules, and emit HTML built from live data — the same `.php` file shows different content per user and per moment (4:L705). Interactivity comes from the form pipeline: `$_GET`/`$_POST` in → validate → query → respond. Sessions/cookies add memory across requests (4:L31–51).

*Challenges:* **SQL injection** if input is concatenated instead of bound (4:L326); **XSS** if output is echoed unescaped; performance — PHP re-runs the whole script per request, so heavy queries need caching; security misconfiguration (credentials in code, 4:L286); maintainability — mixing SQL, logic and HTML in one file, which is why frameworks impose MVC (4:L717); the old `mysql_*` API confusion vs `mysqli`/PDO; deployment/version drift between PHP 5/7/8.

**Traps:** the question says 10 marks — do not spend it all on "it is free". Challenges must be named with the defence (`prepared statements`, `htmlspecialchars`).

---

#### Q231 — Dynamic page: date/time + greeting by time of day ⭐

**Structure:** 3 — `date()` and timezone; 4 — hour extraction + if/elseif/else; 3 — formatted date display; 2 — how the page is generated per request; 2 — presentation.

**Full answer**

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

**Explanation:** `date("H")` returns the 24-hour hour as a two-digit string, cast to `int` for numeric comparison; the `if/elseif` chain maps ranges to greetings. Format characters to name: `H` 24-hour, `h` 12-hour, `i` minutes, `s` seconds, `A` AM/PM, `l` weekday name, `d` day, `F` month name, `Y` four-digit year. Because the script runs on each request, the page shows a different greeting in the morning and the evening without the file changing — that *is* the definition of dynamic content (4:L705).

**Traps:** forgetting `date_default_timezone_set()` gives a UTC time that looks wrong; comparing the string `"09"` with `< 12` works but `(int)` is cleaner and examiners like it; `date("h")` is 12-hour and breaks the logic — use `H`.

---

#### Q232 — Username/password/email filled check + email format

**Structure:** 4 — form; 4 — `empty()` checks on all three; 4 — regex email test; 2 — error display / success message.

**Full answer**

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

**Explanation:** three `empty()` tests answer "has the user filled the textboxes"; the email gets a *second*, shape-level test. Either `filter_var($email, FILTER_VALIDATE_EMAIL)` (built-in, returns the email or `false`) or `preg_match("/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/", $email)` is acceptable — name whichever you use.

**Traps:** `empty("0")` is `true` in PHP — a password of `"0"` would be rejected, which is a known quirk worth a footnote; validating the password *format* is not asked here, only presence.

---

#### Q233 — File uploads (6) + recursive factorial (8)

**Structure:** 6 — upload: form attributes, `$_FILES` keys, validation, `move_uploaded_file()`; 8 — factorial: function, base case, recursive call, output.

**Full answer (a) — upload**

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

Points to write: `enctype="multipart/form-data"` is **mandatory** or `$_FILES` stays empty; `$_FILES["myfile"]` is an array with `name`, `type`, `tmp_name`, `size`, `error`; the file lands in a temp directory (`tmp_name`) and must be moved with `move_uploaded_file()` or it is deleted at script end; `error` codes — `0` OK, `1` exceeds `upload_max_filesize`, `2` exceeds `MAX_FILE_SIZE`, `3` partial, `4` no file chosen; `basename()` blocks path tricks like `../../etc/passwd`; validate size and extension before moving (standard).

**Full answer (b) — recursive factorial**

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

Trace to write out: `factorial(5)` → `5 * factorial(4)` → `5*4*factorial(3)` → … → `5*4*3*2*1 = 120`. The **base case** `$n <= 1` stops the recursion; without it you get infinite recursion and a stack/memory error. Iterative alternative: `for ($i = 2, $f = 1; $i <= $n; $i++) $f *= $i;`.

**Traps:** forgetting `enctype` is the single most common lost mark; `move_uploaded_file` needs the destination directory to exist and be writable; factorial must return (not echo) inside the function.

---

#### Q234 — Connection step by step (10) + patients database (4) ⭐

**Structure:** 10 — five steps with code and the reason for each; 4 — `CREATE DATABASE` + `CREATE TABLE patients` with sensible columns.

**Full answer (a) — the five steps**

1. **Locate the server** — host `localhost`, MySQL user, password (4:L210).
2. **Connect** — `mysqli_connect(host, user, pass, db)` returns a handle or `false`.
3. **Verify** — `if (!$conn) die("Connection failed: " . mysqli_connect_error());` (4:L224–226).
4. **Run statements** — `mysqli_query($conn, $sql)` for every query; check each return value and report `mysqli_error($conn)` on failure (4:L320–324).
5. **Close** — `mysqli_close($conn)` when finished (4:L216).

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
Say also: credentials belong in a config file, not inline (4:L286); the OO form is `new mysqli(...)` with `$conn->connect_error` (4:L258–263).

**Full answer (b) — patients database**

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

From PHP: `mysqli_query($conn, "CREATE DATABASE hospital")` **without** a database argument in the connect call, then `mysqli_select_db($conn, "hospital")` before creating the table (standard).

**Traps:** creating the table before selecting/creating the database; `DECIMAL` vs `INT` for anything monetary; forgetting `PRIMARY KEY`.

#### Q235 — Regex: extract email addresses + validate a phone number

**Structure:** 7 — email extraction with `preg_match_all()` and explanation of the pattern; 7 — phone validation with `preg_match()` and the pattern table.

**Full answer**

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

**Pattern anatomy to write out** (3:L607): `[A-Za-z0-9._%+-]+` = local part (one or more allowed characters); `@` literal; `[A-Za-z0-9.-]+` = domain labels; `\.` = the literal dot before the TLD — unescaped `.` means "any character", so it would match `a@b,com`; `[A-Za-z]{2,}` = at least two letters. For the phone: `^…$` anchors prevent matching inside a longer string, `[0-9]{10}` (or `\d{10}`) means exactly ten digits — without the anchors `"98765432109"` would pass. Indian mobiles often use `^[6-9][0-9]{9}$` (standard). `preg_match_all()` returns the **count** and puts all matches in `$matches[0]`; `preg_match()` stops at the first.

**Traps:** `preg_match` returns `1`/`0`, not `true`/`false` — a strict `=== true` fails; forgetting delimiters `/…/` is a fatal pattern error; `$matches[1]` would be the first *group*, `$matches[0]` is the whole match.

---

#### Q236 — Regex: replace a substring + extract URLs

**Structure:** 7 — `preg_replace()` with a literal and a pattern; 7 — URL extraction with `preg_match_all()`.

**Full answer**

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

**Explanation:** `preg_replace($pattern, $replacement, $subject)` returns a **new string** — it does not modify the original unless you assign it back. The `/i` modifier makes matching case-insensitive (`WORLD` also matches). `(\w+)` captures a group, referenced in the replacement as `$1`, `$2`. For URLs, `https?` matches http/https, `[^\s"'<>]+` means "one or more characters that are not whitespace or quotes or angle brackets", and `#…#` is an alternative delimiter so the `/` inside URLs needs no escaping.

**Traps:** forgetting to assign the result (`preg_replace(...)` alone does nothing visible); `$1` inside a double-quoted PHP string is interpolated by PHP too — safest form is `"\${1}"` or use single quotes and concatenate; the URL pattern deliberately stops at quotes so it does not swallow HTML attributes.

---

#### Q237 — Password validation + phone validation

**Structure:** 8 — password policy with a lookahead regex, plus points on hashing; 6 — phone validation.

**Full answer**

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

**How the password pattern works — decode it aloud in the exam:** `^…$` anchors the whole string; `(?=.*[a-z])` is a **lookahead** — "somewhere ahead there is a lowercase letter", and it consumes nothing; four lookaheads enforce four classes; `.{8,}` finally requires at least eight characters of any kind. Because lookaheads do not consume, the `.` keeps scanning from the same point, which is why all conditions can be checked in one pass.

**What to add for the discussion marks:** a regex validates *shape*, never *safety*; the password must be stored with `password_hash($pass, PASSWORD_DEFAULT)` and checked with `password_verify()`, never in plain text (standard). Phone: `^[6-9][0-9]{9}$` enforces a valid Indian mobile prefix; `^\+91[0-9]{10}$` if the country code is required.

**Traps:** `[\W_]` (non-word or underscore) is the usual way to express "special character" inside a character class; `(?=.*\W)` misses `_`; a pattern without `^…$` accepts `"aaaaA1!x"` embedded in a longer junk string.

---

#### Q238 — Cookies (6) + associative array operations (8)

**Structure:** 3 — significance of cookies; 3 — create and destroy; 8 — four array statements (2 marks each).

**Full answer (a) — cookies**

Significance: HTTP is stateless, so cookies give the client a memory — preferences, "remember me", tracking, and the session ID itself (4:L39, 4:L841).

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

**Full answer (b) — the four array statements**

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

**Say which sort and why:** `asort()` sorts by **value** preserving keys (what a marks table wants); `ksort()` sorts by **key**; `arsort()`/`krsort()` are the descending versions; `sort()` renumbers and destroys the names, so it is wrong here. `unset($marks["Raj"])` removes the key *and* its value.

**Traps:** `sort()` on an associative array loses the names — a classic 2-mark loss; `asort` must be assigned? No — it sorts in place (unlike `array_sort` in some languages); printing with `print_r()` is acceptable but the `foreach` form is what "print the sorted key-value pairs" asks for.

---

#### Q239 — Cookies created/accessed/deleted + sessions start/store/access/destroy

**Structure:** 7 — cookies with three snippets and the header rule; 7 — sessions with four calls and the ID explanation.

**Full answer (a) — cookies**

```php
<?php
setcookie("theme", "dark", time() + 86400, "/");     // create: 1 day
echo $_COOKIE["theme"];                              // access (next request)
setcookie("theme", "", time() - 3600, "/");          // delete
?>
```
Three facts: `setcookie()` before any output (4:L65); `$_COOKIE` is only populated on the **next** request, not the same one; deletion = same name + past expiry (4:L71).

**Full answer (b) — sessions**

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
Explain that the browser holds only `PHPSESSID`, that `session_start()` must be repeated on every page, and that `session_destroy()` alone leaves `$_SESSION` populated until the request ends — hence `session_unset()` first.

**Traps:** writing `$_SESSION` before `session_start()` silently does nothing; calling `session_start()` twice raises a notice; `unset($_SESSION)` is wrong — `unset()` takes a variable, not the whole superglobal (use `session_unset()`).

---

#### Q240 — MySQLi connection procedure + working connection program

**Structure:** 10 — procedure with error handling explained step by step; 4 — complete program with a success message.

**Full answer (a) — procedure**

1. **Have the four credentials** — host, MySQL user, password, database name (4:L210).
2. **Call the connector** — procedural `mysqli_connect(...)` or OO `new mysqli(...)` (4:L258).
3. **Test the result** — procedural: `if (!$conn)` + `mysqli_connect_error()`; OO: `if ($conn->connect_error)` (4:L224, 4:L262).
4. **Fail loudly** — `die()`/`exit()` with the reason, because every later call needs a valid handle (4:L292).
5. **Guard the body** — wrap queries in `try/catch (mysqli_sql_exception $e)` in PHP 8, where mysqli throws instead of returning `false` (standard).
6. **Close** — `mysqli_close($conn)` / `$conn->close()` (4:L216).

**Full answer (b) — both styles, complete**

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

Common failure messages worth quoting: *Access denied for user* (wrong user/password), *Unknown database* (name typo or not created), *Connection refused* (MySQL not running / wrong host).

**Traps:** mixing styles (`$conn->query()` on a procedural handle is fine, but `mysqli_query($conn,…)` after `new mysqli` also works — do not *claim* they are different objects); suppressing errors with `@` loses marks.

---

#### Q241 — CREATE/INSERT/DELETE from PHP + student table program ⭐

**Structure:** 9 — three operations with SQL and PHP each; 5 — program that creates the table and inserts one row.

**Full answer (a) — the three operations**

```text
CREATE  CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY,
                               name VARCHAR(50), marks INT);
        -> writes structure, returns true/false, run once        (4:L435)

INSERT  INSERT INTO students (name, marks) VALUES ('Anu', 88);
        -> adds one row, true/false, mysqli_insert_id() gives id (4:L472)

DELETE  DELETE FROM students WHERE id = 5;
        -> removes matching rows, affected_rows reports count    (4:L509)
```
The deck's one-line summary worth quoting: all three are **write** operations — they return no readable data, only success/failure and an affected-row count (4:L546).

**Full answer (b) — program**

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

**Traps:** running `CREATE TABLE` twice without `IF NOT EXISTS` errors on the second run; forgetting quotes around `'Anu'`; using `mysqli_num_rows()` on an INSERT (returns nothing useful — it is `affected_rows`).

---

#### Q242 — Prepared INSERT/DELETE + delete by register number

**Structure:** 8 — why and how prepared statements work (`prepare`/`bind_param`/`execute`, type string); 6 — the delete-by-regno program.

**Full answer (a) — how it works**

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
Why it is safe: the SQL is parsed and compiled **before** the values arrive (4:L683), so a value can never become syntax. `bind_param` passes variables **by reference**, which is why you pass `$name`, not `'Anu'`; the first argument has one letter per `?` (`s` string, `i` int, `d` double, `b` blob).

**Full answer (b) — delete by register number, prepared**

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

**Traps:** `mysqli_stmt_affected_rows($stmt)` takes the **statement**, `mysqli_affected_rows($conn)` takes the **connection** — mixing them is the most common error; forgetting to check `affected_rows` loses the "no such student" mark.

#### Q243 — SELECT multi-row retrieval → all students in an HTML table ⭐

**Structure:** 6 — what SELECT returns and the fetch-loop steps; 8 — the program with table markup.

**Full answer (a) — the steps**

1. Build the query string (`SELECT regno, name, marks FROM students`).
2. `mysqli_query()` → returns a **result handle**, not data (4:L320).
3. Check it — on `false`, `mysqli_error()`.
4. Loop `while ($row = mysqli_fetch_assoc($result))` — one row per iteration, `NULL` ends it (4:L365).
5. Echo one `<tr>` per iteration; `mysqli_num_rows()` for the count (4:L361).

**Full answer (b) — program**

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

*(Alternative-syntax version with `while (...):` … `endwhile;` and `<?= ?>` — see §2.19; either earns full marks.)*

**Traps:** calling `mysqli_num_rows()` *after* the loop still works (the pointer moved, the count did not); fetching inside the `<table>` before printing `<tr><th>` gives a headerless table; forgetting to close the `</table>`.

---

#### Q244 — UPDATE syntax/precautions + update email by register number ⭐

**Structure:** 7 — syntax, multi-column SET, the WHERE rule, `affected_rows`, precautions; 7 — the program.

**Full answer (a) — syntax and precautions**

```sql
UPDATE students SET email = 'new@saintgits.org' WHERE regno = '20CST461';
```
Precautions to list: (1) **never run UPDATE without WHERE** — every row changes (4:L638); (2) run the same `WHERE` as a `SELECT` first to see the target rows (4:L669); (3) cast numeric input `(int)` and prefer prepared statements for strings (4:L675–683); (4) check `mysqli_affected_rows()` — 0 means nothing matched, not that it worked (4:L687); (5) validate the new value (email format) before writing; (6) back up / use a transaction for bulk updates (standard).

**Full answer (b) — program**

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

**Traps:** two `"s"` letters because both are strings; binding order must match placeholder order (email first, regno second) — swap them and the email lands in the regno column.

---

#### Q245 — Architecture of a dynamic PHP app + products into an HTML list

**Structure:** 7 — the layers and the request flow; 7 — the product-listing program.

**Full answer (a) — architecture**

```text
Browser  --HTTP request-->  Apache/IIS  -->  PHP engine
                                             |  (1) connect  mysqli_connect
                                             |  (2) query    mysqli_query
                                             |  (3) fetch    fetch_assoc loop
                                             |  (4) render   echo HTML
                                        MySQL  <-- SQL -->  tables on disk
Browser  <--plain HTML------  PHP output
```
Layers to name: **presentation** (HTML/CSS produced by echo), **business logic** (validation, calculations), **data access** (connection + SQL) — the deck's "separating concerns" (4:L717), the informal precursor of MVC. State is carried by cookies/sessions between the stateless requests (4:L31–51).

**Full answer (b) — products as an HTML list**

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

**Why `<ul>` and not a table:** the container is irrelevant to the pattern — *one HTML fragment per row inside the loop* is the whole idea (4:L737). `number_format()` is presentational logic, correctly kept in the render step.

**Traps:** the "architecture" half is where marks are lost — draw the boxes, label the four PHP steps, mention MySQL on disk.

---

#### Q246 — Session lifecycle + session ID + store name & login time

**Structure:** 6 — lifecycle stages; 4 — role of the session ID; 4 — the two-page program.

**Full answer (a) — lifecycle**

1. **Create** — `session_start()` on the first page; no ID cookie exists, so PHP generates a random ID (e.g. `7f3c…`) and sends `Set-Cookie: PHPSESSID=7f3c…` (4:L106).
2. **Store** — `$_SESSION["name"] = "Anu"` writes into a server-side file named after that ID (4:L108).
3. **Resume** — every later request replays the cookie; `session_start()` reads it and reloads the file into `$_SESSION` (4:L110).
4. **Expire/end** — browser close (default), a server timeout, or explicit `session_unset()` + `session_destroy()` (4:L112, 4:L156).

**The ID's role:** it is the *only* link between the browser and the server-side data. It carries no information itself — no username, no role — just a lookup key. Anyone who steals it inherits the session, which is why it must be random, sent over HTTPS, and regenerated at login (`session_regenerate_id(true)`, standard).

**Full answer (b) — two pages**

*login.php*

```php
<?php
session_start();
$_SESSION["username"]  = "Anu";
$_SESSION["login_time"] = date("d-m-Y h:i:s A");
echo "Stored. <a href='welcome.php'>Go to welcome page</a>";
?>
```

*welcome.php*

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

**Traps:** missing `session_start()` on page 2 (the classic zero); no `isset` guard (an undefined-index warning); forgetting that `date()` must be evaluated **when storing**, not when displaying.

---

#### Q247 — Cookies vs sessions on storage/lifetime/security/applications + recommendation

**Structure:** 8 — the four-axis comparison table; 6 — the recommendation with justification.

**Full answer (a) — comparison** (4:L136–160)

| Axis | Cookie | Session |
|---|---|---|
| **Storage location** | Client — browser's cookie store, sent with every matching request (4:L140) | Server — file/DB keyed by session ID; browser holds only the ID (4:L152) |
| **Lifetime** | Set explicitly by expiry — survives browser restarts (4:L146) | Until browser closes, or a server-side timeout/idle limit (4:L156) |
| **Security** | Plain text on the user's machine: readable, editable, forgeable; ~4 KB cap; must never hold secrets (4:L144, L142) | Data never leaves the server; only a random ID travels; still needs HTTPS to stop ID theft (4:L154) |
| **Typical applications** | Preferences (theme, language), "remember me" token, non-sensitive tracking (4:L148) | Login state, shopping cart, multi-step forms, flash messages (4:L160) |

**Full answer (b) — recommendation**

**Sessions, for the logged-in state.** Justification: the login state is a security decision, so it must not be client-editable — a cookie saying `loggedin=1` can be forged in seconds, while a session ID cannot be invented and the data it points to stays on the server. Sessions also hold the whole user record (id, role, name) rather than a 4 KB-limited string, and they die when the browser closes, which is the behaviour users expect from a login. **Use a cookie only for the non-sensitive half** — a "remember me" token that is a long random value checked against the database, never the identity itself.

**Traps:** "sessions are more secure" is only half a sentence — add *because the data is not client-side*; a good answer notes that sessions still rely on a cookie (the ID), so the mechanisms are layered, not alternatives.

#### Q248 — Complete SQL workflow from PHP + INSERT reporting success

**Structure:** 7 — the workflow, step by step; 7 — the INSERT program with a success/failure report.

**Full answer (a) — the workflow** (this is the deck's five-step cycle, 4:L405–419)

1. `mysqli_connect(...)` → handle, else `die()`.
2. Build the SQL **string** (`INSERT INTO …`, quotes around strings).
3. `mysqli_query($conn, $sql)` → for writes, `true`/`false`.
4. Branch: on `true` report success (+ `mysqli_insert_id()`), on `false` report `mysqli_error($conn)`.
5. `mysqli_close($conn)`.

**Full answer (b) — program**

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

**Say out loud:** `mysqli_query()`/`execute()` returning true proves the *statement ran*, not that the data was sensible — validation happens before the query, and `insert_id`/`affected_rows` after it.

**Traps:** reporting success without checking the return value (the "always prints Success" bug); using `mysqli_error($conn)` after a *prepared* statement also works, but `mysqli_stmt_error($stmt)` is the precise form.

---

#### Q249 — CREATE TABLE, column types & constraints + employee table

**Structure:** 7 — types and constraints explained; 7 — the employee table SQL executed from PHP.

**Full answer (a) — types and constraints**

| Category | Choice | Why |
|---|---|---|
| Whole numbers | `INT` | ids, age, counts |
| Short text | `VARCHAR(n)` | name, department — n is the max length |
| Long text | `TEXT` | remarks, descriptions |
| Dates | `DATE` / `DATETIME` | admission, joined |
| Money | `DECIMAL(10,2)` | exact — `FLOAT` rounds and loses paise |
| Constraint `PRIMARY KEY` | unique row identity | needed for `WHERE id = …` (4:L437) |
| `AUTO_INCREMENT` | MySQL assigns 1,2,3… | no manual id collisions |
| `NOT NULL` | column must have a value | blocks empty critical fields |
| `UNIQUE` | no duplicates | email, register number |
| `DEFAULT` | fallback value | `DEFAULT 'General'` |

**Full answer (b) — employee table from PHP**

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

**Traps:** `VARCHAR` with no length is a syntax error; storing salary as `INT` loses the decimal part; `PRIMARY KEY` and `AUTO_INCREMENT` on the same column is the normal pattern, not two separate keys.

---

#### Q250 — Careful DELETE + prepared delete by department

**Structure:** 6 — why DELETE is dangerous and the precautions; 8 — the prepared-statement program.

**Full answer (a) — precautions**

1. `WHERE` is mandatory in intent — without it the table is emptied (4:L511).
2. **Preview**: run `SELECT * FROM employees WHERE department = ?` with the same condition first (4:L515, L669).
3. Prefer a **prepared statement** so the department value cannot inject (4:L683).
4. Check `affected_rows` — delete count must match what the preview showed (4:L687).
5. Prefer a **soft delete** (`UPDATE … SET deleted = 1`) where recovery matters, and take a backup before bulk deletes (standard).
6. Use a transaction (`START TRANSACTION` / `ROLLBACK`) when deleting across tables (standard).

**Full answer (b) — program**

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

**Traps:** the question wants the *prepared* form, not a concatenated `WHERE department = '$dept'`; `mysqli_stmt_get_result()` is needed before `fetch_assoc()` on a prepared SELECT.

---

#### Q251 — SELECT result processing + students with marks > 50

**Structure:** 6 — how a result set is processed (handle → pointer → loop → free); 8 — the filtered program.

**Full answer (a) — processing steps**

`mysqli_query()` returns a `mysqli_result` handle holding the whole set server-side with an internal pointer (4:L353). `mysqli_fetch_assoc()` returns the current row and advances the pointer; at the end it returns `NULL`, ending the `while` (4:L357). `mysqli_num_rows()` reports the count without fetching (4:L361). `mysqli_free_result()` releases memory when done.

**Full answer (b) — program**

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

**Traps:** `>` vs `>=` — the question says *greater than* 50; the empty-result branch is worth a mark and is usually forgotten.

---

#### Q252 — UPDATE + role of affected_rows + 10% raise by department

**Structure:** 6 — UPDATE mechanics and `affected_rows`; 8 — the raise program.

**Full answer (a) — explanation**

`UPDATE table SET col = value WHERE condition` rewrites matching rows (4:L634). `mysqli_affected_rows($conn)` returns how many rows the last write **actually changed** (4:L640, L513) — the difference between "the query ran" and "the data changed". It is `0` when the WHERE matched nothing, and also `0` when the new value equals the old one, because MySQL counts changed rows, not matched rows (standard). That is why you compare it against a `SELECT COUNT(*)` when the distinction matters.

**Full answer (b) — program**

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

SQL-only form for the first half: `UPDATE employees SET salary = salary * 1.10 WHERE department = 'Sales';` — note the arithmetic happens *inside* SQL, so no PHP loop is required.

**Traps:** computing the raise in PHP row by row (works, but wastes marks — one statement does it); `salary * 1.1` on a `DECIMAL` is exact, on `FLOAT` it drifts.

---

#### Q253 — Steps for dynamic HTML from MySQL + students list ⭐

**Structure:** 6 — the steps/architecture; 8 — the listing program with names and marks.

**Full answer (a) — the steps** (4:L774–780)

1. **Connect** to MySQL.
2. **Query** — `SELECT name, marks FROM students`.
3. **Fetch** — loop `mysqli_fetch_assoc($result)`.
4. **Render** — echo one HTML row per record, escaping user data.
5. **Close** — free result, close connection.
Say why it is *dynamic*: the same file emits different HTML per request because the rows are read at request time (4:L705, L780).

**Full answer (b) — program** (alternative syntax — the deck's own shape, 4:L782–792)

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

**Traps:** `while (...)` with braces instead of `while (...):` … `endwhile;` is a syntax error when the body is HTML — pick one style and stay in it; `<?=` needs no semicolon but does need the closing `?>`.

---

## 4. PART 3 — Code you must write by hand

Write these on paper, closed book, until they come out without thinking. Line counts are what a 14-mark answer can afford. **Every drill from D3 onward assumes `$conn` is already open (D1/D2) and that `college_db` with a `students` table exists.**

**D1 — Connect and close (the 6-line skeleton)**

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

**D10 — Session login/logout pair**
*login.php*

```php
<?php
session_start();
$_SESSION["user"] = "Anu";
$_SESSION["time"] = date("d-m-Y h:i A");
header("Location: home.php");     // redirect
exit;
?>
```
*home.php*

```php
<?php
session_start();
if (!isset($_SESSION["user"])) { die("Not logged in"); }
echo "Welcome " . htmlspecialchars($_SESSION["user"]);
echo " | <a href='logout.php'>Logout</a>";
?>
```
*logout.php*

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
*Memorise:* `time()+3600` to set, `time()-3600` to delete, nothing echoed before `setcookie()`.

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

## 5. 🔴 Night-before memorize sheet

| Item | Exact syntax / signature | Why it is asked |
|---|---|---|
| Connect | `mysqli_connect('localhost','user','pass','db')` | Q92, 110, 116, 234, 240 — the first line of every answer |
| Connect error | `mysqli_connect_error()` · OO `$conn->connect_error` | The "error handling" mark in every connection question |
| Close | `mysqli_close($conn);` · OO `$conn->close();` | Completes the lifecycle; cheap mark |
| Query | `mysqli_query($conn, $sql)` | Q126; result handle vs bool is the examined detail |
| Query error | `mysqli_error($conn)` | Any "with error handling" question |
| Fetch loop | `while ($row = mysqli_fetch_assoc($result))` | Q128, 243, 251, 253 — the canonical pattern |
| Row access | `$row["column_name"]` | Every display answer |
| Count rows | `mysqli_num_rows($result)` | "No records found" branch, paging |
| Rows changed | `mysqli_affected_rows($conn)` · OO `$conn->affected_rows` | Q127, 244, 250, 252 |
| Last id | `mysqli_insert_id($conn)` | Any INSERT answer |
| Prepared INSERT | `mysqli_prepare($conn, "INSERT … VALUES (?, ?)")` | Q99, 242, 250 |
| Bind | `mysqli_stmt_bind_param($stmt, "ssi", $a, $b, $c)` | The type string `s`/`i`/`d`/`b` is the mark |
| Execute | `mysqli_stmt_execute($stmt)` | — |
| Prepared rows | `mysqli_stmt_affected_rows($stmt)` · `mysqli_stmt_error($stmt)` | Different from the `$conn` versions |
| Start session | `session_start();` | Q115, 125 — must be the first statement |
| Session write/read | `$_SESSION["key"] = value;` · `echo $_SESSION["key"];` | Q95, 100, 111 |
| End session | `session_unset(); session_destroy();` | Q239, 246 |
| Set cookie | `setcookie('name','value',time()+3600,'/');` | Q113, 124, 238, 239 |
| Read cookie | `$_COOKIE["name"]` | — |
| Delete cookie | `setcookie('name','',time()-3600,'/');` | Past expiry, same path |
| Create table | `CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));` | Q109, 117, 241, 249 |
| Insert | `INSERT INTO t (col1, col2) VALUES ('str', 123);` | Q118 |
| Update | `UPDATE t SET col = value WHERE key = value;` | Q121, 244, 252 |
| Delete | `DELETE FROM t WHERE key = value;` | Q119, 242, 250 |
| Select | `SELECT cols FROM t WHERE cond ORDER BY col DESC LIMIT 5;` | Q120, 251 |
| List databases | `SHOW DATABASES` (+ `SHOW TABLES`, `DESCRIBE t`) | Q107 |
| Alternative loop | `<?php while (...): ?> … <?php endwhile; ?>` | Q243, 253 — syntax mark |
| Short echo | `<?= $row["name"] ?>` | Same as `<?php echo …; ?>` |
| Escape output | `htmlspecialchars($str)` | XSS mark, every display question |
| Self action | `$_SERVER['PHP_SELF']` (not `$_PHP_SELF`) | Q103 |
| Email regex | `/^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$/` with `preg_match()` | Q97, 229, 232, 235 |
| Phone regex | `/^[0-9]{10}$/` or `/^[6-9][0-9]{9}$/` | Q235, 237 |
| Greeting hour | `(int) date("H")` + `if/elseif` | Q231 |
| Root | `sqrt($n)` | Q105 |
| Factorial | `return $n * fact($n-1);` with base case `$n <= 1` | Q233 |
| Upload | `$_FILES["f"]["tmp_name"]` + `move_uploaded_file()` + `enctype="multipart/form-data"` | Q233 |
| Sort assoc | `asort()` by value, `ksort()` by key, `unset($a["k"])` | Q238 |

---

## 6. 📐 Diagram + figure index

`grep 'Image Description' module4.md` returns **16** hits. Fifteen are decorative slide furniture; exactly **one** is a real diagram — know that one cold.

| Line | What the figure shows | Exam value |
|---|---|---|
| 4:L1 | Dark circular database-cylinder icon — title slide furniture | none |
| 4:L57 | Small DB cylinder + PHP logo — furniture | none |
| 4:L96 | DB cylinder + PHP logo — furniture | none |
| 4:L200 | DB cylinder + PHP logo — furniture | none |
| 4:L238 | DB cylinder + PHP logo — furniture | none |
| 4:L310 | DB cylinder + PHP logo — furniture | none |
| 4:L345 | DB cylinder + PHP logo — furniture | none |
| 4:L399 | **The five-step query cycle** — five boxes: (1) Build SQL string, (2) `mysqli_query()`, (3) Result handle returned, (4) `while` + `fetch_assoc()` loops through rows, (5) echo HTML for each row, all sitting above a bar labelled "Browser displays the finished table" | **High** — draw this for Q243/Q245/Q248/Q253, and the prose list is at 4:L407–417 |
| 4:L425 | DB cylinder + "PHP + SQL" tag — furniture | none |
| 4:L462 | DB cylinder + "PHP + SQL" tag | none |
| 4:L499 | DB cylinder + "PHP + SQL" tag | none |
| 4:L552 | DB cylinder + "PHP + SQL" tag | none |
| 4:L589 | DB cylinder + "PHP + SQL" tag | none |
| 4:L624 | DB cylinder + "PHP + SQL" tag | none |
| 4:L729 | DB cylinder + PHP logo | none |
| 4:L764 | DB cylinder + PHP logo | none |

**Flows you may be asked to sketch that are NOT drawn in this deck**

- **Request/response flow** (browser → Apache → PHP → MySQL → HTML back): described in words in Module 3, diagram at `module3.md` L57. Reuse it for Q245/Q253 — but say "the request–response cycle from Module 3", do not claim Module 4 draws it.
- **Session flow** (browser ⇄ `PHPSESSID` cookie ⇄ server session file): not drawn; the prose is 4:L106–112, reconstructed in §2.3.
- **Cookie round trip** (`Set-Cookie` response header → cookie jar → `Cookie` request header → `$_COOKIE`): not drawn; prose 4:L39.

---

## 7. Say-this-if-grilled defence lines

1. **Why sessions beat cookies for login:** the identity is a server-side record and the browser holds only an unguessable ID, so nothing the user can edit decides who they are.
2. **Why `WHERE` is non-negotiable:** without it `UPDATE` writes every row and `DELETE` empties the table — and neither has an undo.
3. **Why prepared statements stop injection:** the statement is compiled before the values arrive, so input is data forever and can never be parsed as SQL syntax.
4. **Why `mysqli_fetch_assoc()` returns `NULL` at the end:** the result set has an internal pointer; once it passes the last row there is nothing to return, and `NULL` is falsy — which is exactly what ends the `while`.
5. **Why the connection must precede the query:** `mysqli_query()` needs a live handle as its first argument; without one you are passing `false` into a function that expects a connection.
6. **Why `setcookie()`/`session_start()` must be first:** both emit HTTP headers, and headers are already on the wire once any body output starts.
7. **Why `affected_rows` matters even when there was no error:** MySQL happily reports success for a statement that matched zero rows; the count is the only evidence the right rows changed.
8. **Why `mysqli_query()` returns two different things:** SELECT-type statements produce a result set to iterate; write statements produce only a status, so there is nothing to fetch.
9. **Why you escape with `htmlspecialchars()` on output, not input:** the danger is a value being *interpreted as HTML* when it is displayed, so the escaping belongs at the point of rendering.
10. **Why the page is dynamic even though the file never changes:** the file is a program; the HTML is rebuilt per request from whatever the database holds at that moment.
11. **Why `(int)` casting is not a substitute for prepared statements:** it closes injection through numeric fields only; strings still need binding.
12. **Why `session_destroy()` alone looks broken:** it deletes the server file but leaves `$_SESSION` populated for the rest of that request — `session_unset()` first, then destroy.
13. **Why the deck's string-built SQL is still shown:** it is clearer for teaching the query/fetch cycle; the deck itself flags `mysqli_prepare()` as the production path (4:L302–304).
14. **Why cookies still matter if you use sessions:** every session *is* a cookie — the mechanism is layered, not alternative.
