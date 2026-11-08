"""drills.py — a small set of COMBINED practice items.

Two per module: one mega fill-in-the-blank that touches most of the module's
syntax, and one write-it task that pulls the module together. The point is
coverage per drill, not drill count.
"""

DRILLS = [
    # ================================================================== M1
    dict(id="m1-page", m=1, type="fill", topic="one page, most of HTML",
         q="One page: skeleton, nav, image, table, form, entity, footer. Fill every blank.",
         scaffold='<!DOCTYPE html>\n<html lang="{{1}}">\n<head>\n  <meta {{2}}="UTF-8">\n  <meta name="viewport" content="{{3}}">\n  <title>{{4}}</title>\n</head>\n<body>\n  <header>\n    <h1>{{5}}</h1>\n    <nav><a href="{{6}}">Contact</a></nav>\n  </header>\n  <main>\n    <section {{7}}="contact">\n      <h2>Contact</h2>\n      <img {{8}}="logo.png" {{9}}="College logo" width="120">\n      <table>\n        <caption>{{10}}</caption>\n        <tr><th {{11}}="col">Course</th><th scope="col">Grade</th></tr>\n        <tr><td>Web Programming</td><td>{{12}}</td></tr>\n      </table>\n      <form action="save.php" method="{{13}}">\n        <{{14}} for="email">Email:</{{14}}>\n        <input {{15}}="email" id="email" name="email" {{16}}>\n        <button type="submit">Send</button>\n      </form>\n      <p>Use {{17}}lt;b{{18}}gt; to show a literal tag.</p>\n    </section>\n  </main>\n  <footer><p>{{19}}copy; 2026</p></footer>\n</body>\n</html>',
         answers=["en", "charset", "width=device-width, initial-scale=1.0", "Contacts",
                  "Saintgits CSE", "#contact", "id", "src", "alt", "Semester Result",
                  "scope", "A", "POST", "label", "type", "required", "&", "&", "&"],
         hint="attribute name vs value: id/src/alt/scope/type; entities are &lt; &gt; &amp; &copy;"),
    dict(id="m1-form", m=1, type="write", topic="registration form",
         q="Write a student registration form: name, roll number (6 digits), email, password, date of birth, gender radios, department select, address textarea, terms checkbox, submit. Use labels, required, and a pattern.",
         model='<form action="register.php" method="POST">\n  <label for="name">Name:</label>\n  <input type="text" id="name" name="name" required>\n\n  <label for="roll">Roll No:</label>\n  <input type="text" id="roll" name="roll" pattern="[0-9]{6}" required>\n\n  <label for="email">Email:</label>\n  <input type="email" id="email" name="email" required>\n\n  <label for="pwd">Password:</label>\n  <input type="password" id="pwd" name="pwd" required>\n\n  <label for="dob">Date of birth:</label>\n  <input type="date" id="dob" name="dob">\n\n  <label><input type="radio" name="gender" value="male"> Male</label>\n  <label><input type="radio" name="gender" value="female"> Female</label>\n\n  <label for="dept">Department:</label>\n  <select id="dept" name="dept">\n    <option value="CSE">CSE</option>\n    <option value="ECE">ECE</option>\n  </select>\n\n  <label for="addr">Address:</label>\n  <textarea id="addr" name="addr" rows="3"></textarea>\n\n  <label><input type="checkbox" name="terms" required> Accept terms</label>\n  <button type="submit">Register</button>\n</form>',
         points=["form action + method", "label for each field", "input types + required + pattern", "select/textarea/radio/checkbox", "submit button"]),

    # ================================================================== M2
    dict(id="m2-card", m=2, type="fill", topic="CSS + JS together",
         q="Style a card and wire one click handler. Fill the blanks (CSS then JS).",
         scaffold='/* 1. rule */\n{{1}} {\n  background: #fff;\n  {{2}}: 16px;\n  border: 1px {{3}} #ddd;\n  border-{{4}}: 12px;\n}\n\n/* 2. inline-block-ish layout */\n.cards { display: {{5}}; gap: 16px; }\n\n/* 3. hover state */\n.card:{{6}} { box-shadow: 0 4px 14px rgba(0,0,0,.12); }\n\n/* 4. responsive */\n@media ({{7}}: 768px) { .cards { grid-template-columns: 1fr 1fr; } }\n\n// 5. behaviour\nconst btn = document.{{8}}("btn");\nbtn.{{9}}("{{10}}", function () {\n  document.getElementById("msg").{{11}} = "Clicked";\n});',
         answers=[".card", "padding", "solid", "radius", "grid", "hover", "min-width",
                  "getElementById", "addEventListener", "click", "textContent"],
         hint="CSS: selector, padding, border shorthand, border-radius, display, pseudo-class, media query. JS: select, listen, event name, write text."),
    dict(id="m2-validate", m=2, type="write", topic="responsive box + validation",
         q="Write a page fragment: a .card styled with the box model and a hover state, full width on phones and 2 columns from 768px; plus a submit handler that blocks an empty name and writes an error into #err.",
         model='<style>\n.cards{display:grid;grid-template-columns:1fr;gap:16px}\n.card{padding:16px;border:1px solid #ddd;border-radius:12px}\n.card:hover{box-shadow:0 4px 14px rgba(0,0,0,.12)}\n@media (min-width:768px){.cards{grid-template-columns:1fr 1fr}}\n</style>\n\n<form id="f"><input id="name" required><span id="err"></span>\n  <button>Send</button></form>\n<script>\ndocument.getElementById("f").addEventListener("submit", function (e) {\n  e.preventDefault();\n  const v = document.getElementById("name").value.trim();\n  document.getElementById("err").textContent = v === "" ? "Name required" : "";\n  if (v !== "") this.submit();\n});\n</script>',
         points=["grid/flex layout", "box model properties", "hover pseudo-class", "media query min-width", "preventDefault + trim + error span"]),

    # ================================================================== M3
    dict(id="m3-form", m=3, type="fill", topic="one PHP script, most of the language",
         q="One script: read POST, trim, validate with regex, call a function, loop an array. Fill the blanks.",
         scaffold='<?php\nfunction clean({{1}}) {\n  return htmlspecialchars(trim({{1}}));\n}\n\nif ($_SERVER[{{2}}] == "POST") {\n  $name  = clean($_POST["name"] ?? "");\n  $email = clean($_POST["email"] ?? "");\n\n  if ($name == "" || !{{3}}("/^[^@]+@[^@]+\\.[a-z]{2,}$/i", $email)) {\n    {{4}}("Invalid input");\n  }\n\n  $marks = [{{5}} => 88, "Rahul" => 72];\n  $total = 0;\n  {{6}} ($marks as $k => $v) {\n    $total {{7}} $v;\n    echo $k . ": " . $v . "<br>";\n  }\n  echo "Total: " . {{8}};\n  echo "Average: " . round($total / {{9}}($marks), 2);\n}\n?>',
         answers=["$value", '"REQUEST_METHOD"', "preg_match", "die", '"Ali"', "foreach", "+=", "$total", "count"],
         hint="function param, superglobal key, regex function, stop-the-script function, array key, loop keyword, accumulate, count"),
    dict(id="m3-users", m=3, type="write", topic="registration with business logic",
         q="Write the PHP side of a registration form: read and trim name/email/password, reject empties, validate the email with a regex, enforce password length ≥ 8, then print a success message with the name escaped. Use a function for validation.",
         model='<?php\nfunction validate($name, $email, $pwd) {\n    if ($name === "" || $email === "" || $pwd === "") return "All fields are required.";\n    if (!preg_match("/^[^@\\s]+@[^@\\s]+\\.[a-z]{2,}$/i", $email)) return "Invalid email.";\n    if (strlen($pwd) < 8) return "Password needs 8+ characters.";\n    return "";\n}\n\nif ($_SERVER["REQUEST_METHOD"] == "POST") {\n    $name  = trim($_POST["name"] ?? "");\n    $email = trim($_POST["email"] ?? "");\n    $pwd   = $_POST["password"] ?? "";\n\n    $error = validate($name, $email, $pwd);\n    if ($error !== "") {\n        die($error);\n    }\n    echo "Registered " . htmlspecialchars($name) . " as " . htmlspecialchars($email);\n}\n?>',
         points=["function returning an error string", "method check", "trim + ?? default", "regex validation", "length rule", "escaping on output"]),

    # ================================================================== M4
    dict(id="m4-login", m=4, type="fill", topic="session + prepared select",
         q="A login: start the session, read POST, look the user up safely, store it, then read it on another page. Fill the blanks.",
         scaffold='<?php\n{{1}}();\n\n$conn = {{2}}("localhost", "root", "", "college");\nif (!$conn) {{3}}({{4}}());\n\n$stmt = mysqli_prepare($conn, "SELECT id, name FROM users WHERE email = ?");\nmysqli_stmt_bind_param($stmt, "{{5}}", $_POST["email"]);\nmysqli_stmt_execute($stmt);\n$result = mysqli_stmt_get_result($stmt);\n\nif ($row = {{6}}($result)) {\n  {{7}}["user"] = $row["name"];   // remember the user\n  header("Location: home.php");\n  {{8}};\n} else {\n  echo "Invalid login";\n}\n?>\n\n<?php /* home.php */\n{{1}}();\necho "Welcome " . {{9}}($_SESSION["user"]);\n?>',
         answers=["session_start", "mysqli_connect", "die", "mysqli_connect_error", "s",
                  "mysqli_fetch_assoc", "$_SESSION", "exit", "htmlspecialchars"],
         hint="session first, connect, kill on failure, bind type s for strings, fetch a row, superglobal to store in"),
    dict(id="m4-crud", m=4, type="write", topic="insert + list + update",
         q="One page: connect, insert a student with a prepared statement, list all students in an HTML table, and raise one student's marks by 5 with UPDATE. Show the affected_rows check.",
         model='<?php\n$conn = mysqli_connect("localhost", "root", "", "college");\nif (!$conn) die(mysqli_connect_error());\n\n// insert (safe)\n$stmt = mysqli_prepare($conn, "INSERT INTO students (regno, name, marks) VALUES (?, ?, ?)");\nmysqli_stmt_bind_param($stmt, "ssi", $regno, $name, $marks);\n$regno = "SJC22CS001"; $name = "Anu"; $marks = 72;\nif (!mysqli_stmt_execute($stmt)) die(mysqli_error($conn));\n\n// update + affected rows\nmysqli_query($conn, "UPDATE students SET marks = marks + 5 WHERE regno = \'SJC22CS001\'");\necho mysqli_affected_rows($conn) . " row(s) updated";\n\n// list\n$result = mysqli_query($conn, "SELECT regno, name, marks FROM students");\n?>\n<table border="1">\n  <tr><th>Reg No</th><th>Name</th><th>Marks</th></tr>\n  <?php while ($row = mysqli_fetch_assoc($result)): ?>\n    <tr><td><?= htmlspecialchars($row["regno"]) ?></td>\n        <td><?= htmlspecialchars($row["name"]) ?></td>\n        <td><?= $row["marks"] ?></td></tr>\n  <?php endwhile; ?>\n</table>\n<?php mysqli_close($conn); ?>',
         points=["connect + failure check", "prepared insert + bind_param types", "error handling", "UPDATE + affected_rows", "fetch loop into HTML", "close"]),

    # ================================================================== M5
    dict(id="m5-schema", m=5, type="fill", topic="JSON + schema + route + Blade",
         q="Four small pieces: a JSON document, its schema, a named route, and a Blade loop. Fill the blanks.",
         scaffold='// 1. JSON document\n{\n  "name": {{1}},\n  "mark": 88,\n  "active": {{2}},\n  "email": {{3}}\n}\n\n// 2. Schema\n{\n  "type": "object",\n  "{{4}}": ["name", "mark"],\n  "properties": {\n    "mark": { "type": "{{5}}", "{{6}}": 0, "maximum": 100 }\n  }\n}\n\n// 3. Route\nRoute::{{7}}("/students/{id}", [StudentController::class, "show"])->{{8}}("students.show");\n\n// 4. Blade (child view)\n@{{9}}("layouts.app")\n@{{10}}("content")\n  @{{11}}($students as $s)\n    <p>{{{{ $s->name }}}}</p>\n  @{{12}}\n@{{13}}',
         answers=['"Anu"', "true", "null", "required", "number", "minimum",
                  "get", "name", "extends", "section", "foreach", "endforeach", "endsection"],
         hint="JSON types; schema keywords required/minimum; route verb + name; Blade extends/section/foreach/endsection"),
    dict(id="m5-crud", m=5, type="write", topic="route → controller → view",
         q="Write the Laravel pieces for a student list: a resource route, the controller's index method, and a Blade view that loops students and prints Pass/Fail at 40 marks.",
         model='// routes/web.php\nRoute::resource("students", StudentController::class);\n\n// app/Http/Controllers/StudentController.php\npublic function index()\n{\n    $students = Student::all();\n    return view("students.index", compact("students"));\n}\n\n{{-- resources/views/students/index.blade.php --}}\n@extends("layouts.app")\n\n@section("content")\n  <h1>Students</h1>\n  @foreach ($students as $student)\n    <p>{{ $student->name }} —\n      @if ($student->mark >= 40) Pass @else Fail @endif\n    </p>\n  @endforeach\n@endsection',
         points=["resource route", "controller returns view with data", "compact or array", "@extends/@section", "@foreach + @if/@else"]),
]
