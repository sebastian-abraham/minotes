# MODULE 5 — JSON and Laravel · Complete Study Kit
> 20CST461 Web Technologies · ESE Part A = 3 marks, Part B = 14 marks · 2 Part-A questions and 1 of 2 Part-B questions come from this module

---

## 0. How to use this kit

You are learning JSON **and** Laravel from zero in one module. That is why this kit is ordered the way it is: JSON first (a data format — small, closed, memorisable), then Laravel (a framework — big, but only ~9 ideas are examinable).

**The 6-hour plan**

| Time | Do this | Output |
|---|---|---|
| 60 min | Read §2.1–§2.13 (JSON half) slowly, typing every snippet yourself | You can produce a valid JSON document from memory |
| 45 min | §4 drills D1–D6 on paper, no looking | JSON + PHP round-trip is automatic |
| 75 min | Read §2.14–§2.37 (Laravel half) | You can draw the request lifecycle on a blank page |
| 90 min | §4 drills D7–D14, then §3.2 read B4, B5, B8, B10 only | The four high-frequency 14-markers are covered |
| 45 min | §3.1 all 20 master answers, aloud | Part A is 6/6 |
| 30 min | §5 memorize sheet + §7 defence lines | Recall under pressure |

**Three rules for this module**

1. **Never write Laravel code without `$`.** Every Laravel variable is `$request`, `$student`, `$students`. In the exam, half the marks in a code question are for getting `$` and `->` right.
2. **JSON is strict, PHP is loose.** Almost every JSON trap in the question bank is a strictness trap: single quotes, trailing comma, a comment, an unquoted key. §2.2 is the highest-value page in this kit.
3. **Name the layer.** Any Laravel answer scoring 14 will say *which* layer does what: route → middleware → controller → model → view/redirect. Answers that blur layers lose marks.

**Marking reality (from the question shapes):** Part B is never one essay. It is `a)` + `b)` with splits like 8+6, 7+7, 10+4, 6+8, 5+9. **Write the split in the margin before you start**, and give each part roughly its proportional space. A 6-mark half answered in 3 lines and an 8-mark half answered in 25 lines is how people lose 4 marks they knew.

**Honesty note on sources.** Every `5:pN` reference in this kit was checked against `module5.md` (28 pages). Where the deck does **not** contain something the question bank asks for (JSON Schema keywords, resource controllers, sub-domains, service providers, migrations, explicit binding, `JSON.parse`), it is marked **(standard, not in your deck)**. Those are still fully answerable — they are standard Laravel/JSON — but do not claim the slide said them.

---

## 1. Module map + question coverage

The bank's heading for this block is mislabelled *"Module 5: PHP and MySQL Database Operations"*. The content is JSON + Laravel. 31 Part-A questions (130–160), 33 Part-B questions (254–286).

| Q# | what it asks (max 8 words) | mark shape | answered at § |
|---|---|---|---|
| 130 | JSON as a data interchange format | 3 | §3.1 A1 |
| 131 | PHP decode, modify, re-encode JSON | 3 | §3.1 A2 · §4 D5 |
| 132 | Short note on the Laravel framework | 3 | §3.1 A3 |
| 133 | Design patterns used in Laravel | 3 | §3.1 A4 |
| 134 | Note on routing in Laravel | 3 | §3.1 A5 |
| 135 | Explain middleware in Laravel | 3 | §3.1 A6 |
| 136 | Purpose of `@extends` + example | 3 | §3.1 A7 |
| 137 | Route model binding, implicit example | 3 | §3.1 A8 |
| 138 | Resource controllers and CRUD | 3 | §3.1 A9 |
| 139 | Schema of a JSON document + example | 3 | §3.1 A10 |
| 140 | JSON types representing structured data | 3 | §3.1 A11 |
| 141 | Role of `$schema` and `$id` | 3 | §3.1 A12 |
| 142 | List three Laravel features | 3 | §3.1 A13 |
| 143 | Define JSON + two advantages over XML | 3 | §3.1 A1 |
| 144 | Three JSON data types with examples | 3 | §3.1 A11 |
| 145 | JSON Schema and its purpose | 3 | §3.1 A14 |
| 146 | Middleware + an example use case | 3 | §3.1 A6 |
| 147 | GET vs POST vs route model binding | 3 | §3.1 A15 |
| 148 | Basic data types supported by JSON | 3 | §3.1 A11 |
| 149 | JSON object vs JSON array | 3 | §3.1 A16 |
| 150 | What JSON Schema is used for | 3 | §3.1 A14 |
| 151 | PHP functions JSON ↔ PHP value | 3 | §3.1 A2 |
| 152 | Which design pattern Laravel follows | 3 | §3.1 A4 |
| 153 | State three Laravel features | 3 | §3.1 A13 |
| 154 | Purpose of the application structure | 3 | §3.1 A17 |
| 155 | What routing is in Laravel | 3 | §3.1 A5 |
| 156 | What middleware is in Laravel | 3 | §3.1 A6 |
| 157 | Role of a controller in Laravel | 3 | §3.1 A18 |
| 158 | What route model binding is | 3 | §3.1 A8 |
| 159 | What Blade is | 3 | §3.1 A19 |
| 160 | Purpose of `@foreach` in Blade | 3 | §3.1 A20 |
| 254 | JSON Schema role + error handling | 8 | §3.2 B2 |
| 255 | MVC in Laravel with an example | 14 | §3.2 B4 |
| 256 | Service providers + migrations | 10+4 | §3.2 B13 |
| 257 | Resource controllers + third-party packages | 8+6 | §3.2 B7 |
| 258 | Routing in detail + custom middleware | 10+4 | §3.2 B5, B6 |
| 259 | Views, closures vs controllers, redirections | 10+4 | §3.2 B9 |
| 260 | Sub-domain routing + Blade inheritance | 7+7 | §3.2 B11, B10 |
| 261 | MVC diagram + routing mechanisms | 6+8 | §3.2 B4, B5 |
| 262 | JSON types + parse/stringify + binding types | 8+6 | §3.2 B1, B8 |
| 263 | JSON types + student schema + views | 8+6 | §3.2 B1, B2, B9 |
| 264 | Middleware types + redirections | 8+6 | §3.2 B6, B9 |
| 265 | Request lifecycle + Blade features | 5+9 | §3.2 B12, B10 |
| 266 | JSON syntax rules + student JSON | 7+7 | §3.2 B1 |
| 267 | JSON vs PHP types + decode and display | 7+7 | §3.2 B3 |
| 268 | Serializing/deserializing + employees | 8+6 | §3.2 B3 |
| 269 | MVC + Laravel directory structure | 7+7 | §3.2 B4 |
| 270 | Routing + GET/POST/binding difference | 7+7 | §3.2 B5, B8 |
| 271 | JSON syntax + types + student document | 14 | §3.2 B1 |
| 272 | Schema + type/required/properties + student | 14 | §3.2 B2 |
| 273 | encode/decode + decode-modify-re-encode | 14 | §3.2 B3 |
| 274 | Laravel, MVC, features, structure, setup | 14 | §3.2 B4 |
| 275 | Routing/middleware/controller + protected route | 14 | §3.2 B5, B6, B7 |
| 276 | Binding + views + redirects + example | 14 | §3.2 B8, B9 |
| 277 | Blade echoing + control structures + pass/fail | 14 | §3.2 B10 |
| 278 | JSON syntax + nested college document | 14 | §3.2 B1 |
| 279 | Identify six JSON types + array to JSON | 14 | §3.2 B1, B3 |
| 280 | Schema validation + course credits 1–6 | 14 | §3.2 B2 |
| 281 | MVC responsibilities + student mapping | 14 | §3.2 B4 |
| 282 | Important Laravel directories | 14 | §3.2 B4 |
| 283 | Middleware auth/filtering + request flow | 14 | §3.2 B6 |
| 284 | GET/POST routes + named + form routes | 14 | §3.2 B5 |
| 285 | Binding implicit vs explicit + view | 14 | §3.2 B8 |
| 286 | Blade echoing/conditionals/loops + pass/fail | 14 | §3.2 B10 |

### The five master themes (everything above is one of these)

1. **JSON as a format** — syntax rules, six data types, nesting. *17 of 64 questions.* The single most-asked object in the module.
2. **JSON Schema** — validation rules expressed *as JSON*. *7 questions.* Always paired with "type/required/properties".
3. **PHP ↔ JSON** — `json_encode` / `json_decode` / round trip. *6 questions.* The only place PHP and JSON meet.
4. **Laravel architecture** — framework, MVC, features, directory structure, setup, request lifecycle. *13 questions.*
5. **Laravel request machinery** — routing, middleware, controllers, route model binding, views, redirections, Blade. *21 questions.* Highest density; this is where the 14-markers live.

**Prediction for your paper:** Part A will almost certainly be (a) a JSON types / syntax / Schema keyword question and (b) a Laravel one-term definition (middleware / routing / binding / Blade / `@extends`). Part B will almost certainly be a **7+7 hybrid** — one JSON half and one Laravel half — because 21 of the 33 Part-B questions are exactly that shape.

---

## 2. PART 1 — Deep dive, from zero

### 2.1 What JSON is, and why it beat XML
**Story:** XML is a shipping crate — every item needs a lid and a label saying "lid". JSON is a padded envelope: you see the contents immediately.
**Definition:** JSON (JavaScript Object Notation) is a lightweight, text-based format for structured data, readable by humans and parseable by machines. It is used by virtually every language, not just JavaScript `5:p2`.
**Snippet:**
```json
{ "name": "Anu", "age": 20, "isActive": true, "marks": [88, 92, 79] }
```
**Why it exists / why it won `5:p2`:** (i) far less verbose than XML — no closing tags; (ii) maps directly onto structures every language already has (objects/maps and arrays/lists), so no translation layer; (iii) parses faster. **What it is not:** a programming language — no functions, no comments, no logic. Data only `5:p2`.
**Exam hook:** "Define JSON + two advantages over XML" is Q143, a pure recall 3-marker. Two advantages, one line each, plus a 1-line example.

### 2.2 JSON syntax rules (the strictness page)
**Story:** JSON is a passport form. One box filled wrongly and the whole form is rejected — there is no "close enough".
**Definition:** JSON has exactly two container structures — object `{ }` (unordered key–value pairs) and array `[ ]` (ordered list) — and everything else nests inside them `5:p3`.
**The five rules `5:p3`:**

| # | Rule | Legal | Illegal |
|---|---|---|---|
| 1 | Keys are **always double-quoted strings** | `{"name": "Anu"}` | `{name: "Anu"}`, `{'name': 'Anu'}` |
| 2 | **No comments** of any kind | — | `{"a":1} // note`, `/* note */` |
| 3 | **No trailing comma** | `{"a":1,"b":2}` | `{"a":1,"b":2,}` |
| 4 | **Exactly one top-level value** | `{...}` or `[...]` | `{...} {...}` |
| 5 | Strings use **double quotes only**; only `\"  \\  \/  \b  \f  \n  \r  \t  \uXXXX` are legal escapes | `"say \"hi\""` | `'hi'`, `"line\n"` written raw across lines |

**Snippet:**
```json
{
  "name": "Anu",
  "age": 20,
  "isActive": true,
  "marks": [88, 92, 79]
}
```
**Why the strictness exists:** a parser must be unambiguous and streaming-safe. Allowing comments or trailing commas means every parser invents its own dialect, and two systems stop interoperating — the whole point of JSON disappears. Note the deck's phrasing: "strict syntax, unlike JavaScript object literals" `5:p3`. That is the sentence to quote: **a JS object literal is not JSON** (`{a:1,}` is valid JS, invalid JSON).
**Trap:** numbers may not have leading `+`, leading zeros, `.5`, or hex. `NaN` and `Infinity` are not JSON. Dates are not a type — they travel as strings.

### 2.3 The six JSON data types
**Story:** Six LEGO brick shapes. Any structure you will ever need is these six, stacked.
**Definition / table (verbatim content of `5:p4`):**

| Type | Example | Notes |
|---|---|---|
| string | `"Saintgits"` | Always double-quoted |
| number | `20` or `499.50` | No distinction between int and float |
| boolean | `true` / `false` | Lowercase, unquoted |
| null | `null` | Represents "no value" |
| object | `{ "city": "Kottayam" }` | Nested key–value pairs |
| array | `[88, 92, 79]` | Ordered list of any of the above |

**Snippet showing all six at once:**
```json
{
  "college": "Saintgits",
  "established": 2002,
  "autonomous": true,
  "affiliation": null,
  "address": { "city": "Kottayam", "pin": "686532" },
  "branches": ["CSE", "ECE", "ME"]
}
```
**Why it exists:** a tiny type set is why every language can implement JSON in a page of code. PHP has ~10 scalar types; JSON has 6, and one of them (`object`) absorbs PHP's associative array `5:p4`.
**Trap that is actually asked (Q279):** `true` boolean · `25` number · `"PHP"` string · `null` null · `[1,2]` array · `{"id":1}` object. Learn that six-item mapping cold.

### 2.4 Nesting — objects inside objects
**Story:** Russian dolls, but the dolls can also hold lists of dolls.
**Definition:** any value — including another object or array — can sit inside an object or array, without a depth limit `5:p5`.
**Snippet:**
```json
{
  "name": "Anu",
  "address": { "city": "Kottayam", "pin": "686532" },
  "courses": [
    { "code": "20CST461", "title": "Web Programming" }
  ]
}
```
**Why it exists:** nesting *is* the data model. "A student HAS an address, HAS a list of marks" `5:p5` — one document can carry an entire relationship tree, which is why a single API response replaces five SQL joins on the client side. Indentation is cosmetic only; it has **no effect on parsing** `5:p5`.

### 2.5 Designing a JSON document
**Story:** Design the shape of the answer sheet before you answer — the shape decides what questions are easy.
**Definition (mostly standard, partly `5:p5`):** document design = choosing your top-level container, your key names, and where you nest vs flatten.
**Rules of thumb:**
1. **Top level is an object** for a single entity, an **array** for a collection. Never a bare string.
2. **Name keys in `camelCase` or `snake_case` consistently** — pick one for the whole API.
3. **Plural key for lists** (`"students": [...]`), singular for one entity.
4. **Never encode type in the value** — use a real number for a mark, not `"88"`.
5. **Use `null` deliberately** for "known to be absent", and omit the key for "not applicable".
6. **Do not nest more than ~3 levels** — deep nesting is unqueryable.
**Snippet (a well-designed student document):**
```json
{
  "registerNo": "SJC22CS001",
  "name": "Anu Thomas",
  "semester": 7,
  "marks": [
    { "subject": "Web Programming", "mark": 88 },
    { "subject": "DBMS", "mark": 76 }
  ]
}
```
**Why it exists:** the document shape is the API contract. Change the shape later and every client breaks — so the shape is designed once, and (see §2.6) written down as a schema.

### 2.6 JSON Schema — the problem it solves
**Story:** JSON is a signed blank cheque. A schema is the printed rules on the cheque that say how much may be written.
**Definition:** JSON Schema is **a separate JSON document that describes the rules for another JSON document** — because JSON itself has no way to say "this field is required" or "this must be a number" `5:p6`.
**What it can specify `5:p6`:** required fields; expected type per field; value constraints (minimum/maximum, string patterns); the structure of nested objects and arrays.
**Snippet (smallest useful schema):**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["name"],
  "properties": { "name": { "type": "string" } }
}
```
**Why it exists `5:p6`:** before trusting incoming JSON (a JS form submission, another service's response), a schema validates the shape **automatically** instead of hand-writing an `if` per field. The deck's key phrase: valuable **"wherever JSON crosses a trust boundary"** `5:p6`. Used by API documentation tools, request-validation libraries, config-file validation.
**Do not confuse:** the deck's "schema" here is a *validation* schema. A "schema of a JSON document" (Q139) is just the *structure* of a document. Read the question: Q139 = structure; Q145/150 = the validation language.

### 2.7 JSON Schema keywords you must be able to write
**Story:** Six keywords cover 95% of real schemas — learn these and you can write any schema the paper asks for.
**Definition (standard, not in your deck):**

| Keyword | Sits at | Means |
|---|---|---|
| `$schema` | root | which **dialect/version** of the JSON Schema spec this document follows. Lets a validator know which rules apply. |
| `$id` | root | a **unique URI identifying this schema** so other schemas can `$ref` it and validators can cache/dedupe it. |
| `type` | any level | the allowed JSON type: `object`, `array`, `string`, `number`, `integer`, `boolean`, `null`. May be an array for a union. |
| `properties` | inside an object schema | map of key → sub-schema for each known key |
| `required` | inside an object schema | array of key **names** that must be present (presence, not truthiness) |
| `minimum` / `maximum` | inside a number schema | inclusive numeric bounds |
| `items` | inside an array schema | the schema every element must satisfy |
| `additionalProperties` | inside an object schema | `false` forbids keys not listed in `properties` |

**Snippet:**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/student.json",
  "type": "object",
  "required": ["registerNo", "name", "mark"],
  "properties": {
    "registerNo": { "type": "string" },
    "name": { "type": "string" },
    "mark": { "type": "number", "minimum": 0, "maximum": 100 }
  },
  "additionalProperties": false
}
```
**Why it exists:** it is JSON describing JSON — so schemas are themselves machine-readable, downloadable, diffable and shareable. That is the entire reason it is not XML Schema.
**Traps:** `required` does **not** mean non-empty; `""` satisfies `"type": "string"`. `type: "integer"` rejects `88.5` but JSON Schema accepts `88.0` as an integer. `minimum` is inclusive. A key present in `properties` is still optional unless also in `required`.

### 2.8 How validation errors are reported
**Story:** A schema validator is a strict invigilator: it does not stop at the first mistake — it hands you the whole list of mistakes with line numbers.
**Definition (standard, not in your deck):** validators return a boolean result **plus an array of error objects**, each carrying the `instancePath` (JSON Pointer to the offending value), the `schemaPath` (which keyword failed), a `keyword`, and a human `message`.
**Snippet (typical output shape):**
```json
[
  {
    "instancePath": "/mark",
    "schemaPath": "#/properties/mark/maximum",
    "keyword": "maximum",
    "message": "must be <= 100"
  },
  {
    "instancePath": "",
    "schemaPath": "#/required",
    "keyword": "required",
    "message": "must have required property 'registerNo'"
  }
]
```
The `""` instancePath means the failure is at the document root (a missing top-level field). Because each error points at a path, a UI can highlight the exact form field.
**Why it exists:** an all-errors report is what makes schema validation usable in a web form — you show every bad field at once, not one per submit. The alternative (manual `if`) returns only the first failure you happened to code.
**Exam phrasing for Q254(b):** *"validation errors are returned as a list of objects, each with the path of the failing instance, the failing schema keyword and a message; the document is valid iff that list is empty."*

### 2.9 `json_encode()` — PHP to JSON
**Story:** `json_encode` is a translator: PHP's nested arrays walk in, a JSON string walks out.
**Definition:** `json_encode($value)` returns a JSON-formatted string built from a PHP value `5:p7`.
**Snippet:**
```php
<?php
$student = [
    "name"  => "Anu",
    "marks" => [88, 92, 79]
];
echo json_encode($student);
// {"name":"Anu","marks":[88,92,79]}

echo json_encode($student, JSON_PRETTY_PRINT);
// {
//     "name": "Anu",
//     "marks": [88, 92, 79]
// }
?>
```
**The mapping rule you must memorise `5:p7`:** PHP **associative** arrays → JSON **object**; PHP **indexed** arrays → JSON **array**. It is decided automatically by whether the keys are sequential integers from 0.
**Why it exists:** output. Every "send this data to a JS front end / another service" path ends in `json_encode`.

### 2.10 `json_decode()` — JSON to PHP
**Story:** the return trip. Same translator, opposite direction — and it asks you one question at the border: object or array?
**Definition:** `json_decode($jsonString)` turns a JSON string back into usable PHP data `5:p8`.
**Snippet:**
```php
<?php
$json = '{"name":"Rahul","marks":[72,80]}';

$asObject = json_decode($json);
echo $asObject->name;        // Rahul   (object → ->)

$asArray = json_decode($json, true);
echo $asArray["name"];       // Rahul   (assoc array → ["..."])
?>
```
**Why the `true` exists:** `true` = "give me associative arrays". Objects are awkward in PHP (`->` and `isset` gymnastics, and `$obj->{"weird-key"}` for hyphenated keys); arrays are what `foreach`, `array_map` and `compact()` want. **Default answer to "which would you use?" = `json_decode($json, true)`** `5:p8`.
**Common use `5:p8`:** reading a JSON request body sent by a JavaScript `fetch()` call.

### 2.11 Flags and error handling
**Story:** `json_decode` fails silently — it returns `null` whether the JSON was `null` or garbage. Always ask the second question.
**Definition (flags from `5:p7`–`p8`, error handling standard):**

| Item | Effect |
|---|---|
| `JSON_PRETTY_PRINT` | 4-space indentation, readable output `5:p7` |
| `JSON_UNESCAPED_SLASHES` | keeps `https://x` instead of `https:\/\/x` |
| `JSON_UNESCAPED_UNICODE` | keeps `ക` instead of `\u0d15` |
| `JSON_THROW_ON_ERROR` | throws `JsonException` instead of returning `null` (PHP 7.3+) |
| `json_last_error()` | integer error code of the last encode/decode `5:p8` |
| `json_last_error_msg()` | human message, e.g. `Syntax error` |

**Snippet:**
```php
<?php
$json = '{"name":"Rahul","marks":[72,80]}';
$data = json_decode($json, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    echo "Invalid JSON: " . json_last_error_msg();
} else {
    echo $data["name"];   // Rahul
}
?>
```
**Why it exists:** untrusted input. `json_last_error()` compares against `JSON_ERROR_NONE` (which is `0`) — the deck's own wording, "checks whether decoding actually succeeded" `5:p8`. Without this check, `null` silently flows into your view and you debug for an hour.
**Trap:** `json_decode` also returns `null` for the perfectly valid document `null`. That is why the error check — not `=== null` — is the correct test.

### 2.12 PHP arrays ↔ JSON objects, the one asymmetry
**Story:** PHP has one container doing two jobs; JSON has two containers doing one job each.
**Definition:** JSON has **no separate associative-array type** — an object covers that role `5:p4`. So the mapping is many-to-one and lossy in one direction.
**Snippet:**
```php
<?php
// assoc → object
echo json_encode(["a" => 1, "b" => 2]);   // {"a":1,"b":2}

// indexed → array
echo json_encode([1, 2, 3]);              // [1,2,3]

// GOTCHA: a "list" with gaps is not sequential → becomes an object
echo json_encode([0 => "x", 2 => "y"]);   // {"0":"x","2":"y"}

// GOTCHA: force an object even when empty
echo json_encode([], JSON_FORCE_OBJECT);  // {}
echo json_encode([]);                     // []
?>
```
**Why it matters:** `json_decode($j, true)` gives arrays, but `json_encode` of an empty PHP array gives `[]`, not `{}` — so a JS client expecting an object gets an array. `JSON_FORCE_OBJECT` exists exactly for this. Say this in an answer and you sound like you have actually shipped something.

### 2.13 The real use: a database row as a JSON API response
**Story:** Module IV's `while` loop, minus the HTML — the same rows, wrapped in JSON instead of `<td>`.
**Definition `5:p9`:** fetch all rows into a plain PHP array, `json_encode` the whole array once after the loop, and set `Content-Type: application/json`.
**Snippet:**
```php
<?php
header("Content-Type: application/json");

$result = mysqli_query($conn, "SELECT name, marks FROM students");

$students = [];
while ($row = mysqli_fetch_assoc($result)) {
    $students[] = $row;          // append each row
}

echo json_encode($students);     // encode ONCE, after the loop
?>
```
**Why it exists:** this is the foundation of an API endpoint instead of an HTML page `5:p9`. Note the two design points the deck makes explicit: encode **after** the loop (not inside it — that produces concatenated invalid JSON), and send the header so the client parses it as data, not text.

### 2.14 JavaScript `JSON.parse()` / `JSON.stringify()`
**Story:** the same two functions, wearing JavaScript clothes: `parse` = string → object, `stringify` = object → string. The names are reversed from PHP's, which is the only hard part.
**Definition (standard, not in your deck — the deck covers only PHP-side conversion `5:p7`, `p8`):**
- `JSON.parse(text)` — takes a JSON **string**, returns a JS value. Throws `SyntaxError` on invalid JSON.
- `JSON.stringify(value)` — takes a JS value, returns a JSON **string**. Silent gotchas: `undefined` and functions are dropped from objects, `Date` becomes an ISO string, `NaN`/`Infinity` become `null`.
**Snippet:**
```javascript
const text = '{"name":"Anu","marks":[88,92]}';

const student = JSON.parse(text);      // string -> object
console.log(student.name);             // Anu
console.log(student.marks[0]);         // 88

student.marks.push(95);                // modify in JS
const out = JSON.stringify(student);   // object -> string
console.log(out);                      // {"name":"Anu","marks":[88,92,95]}

// round trip through the network
fetch('/api/students/1')
  .then(r => r.json())                 // == JSON.parse of the body
  .then(s => console.log(s.name));
```
**Why it exists:** `localStorage`, `fetch` bodies, `postMessage` and WebSocket frames all carry **strings**. You cannot send a live object over a wire; `stringify` at the sender, `parse` at the receiver. That sentence — *serialise at the boundary, parse at the boundary* — is the answer to any "why parse/stringify" sub-question.
**Trap:** the response of `fetch()` is not JSON yet; `.json()` is async and returns a promise. And `JSON.parse` on an already-parsed object throws.

### 2.15 Why a framework (and what Laravel is)
**Story:** Modules III–IV had you laying every brick by hand. A framework is the same house, with scaffolding, plumbing and a building code already in place.
**Definition:** Laravel is a free, open-source PHP framework supplying routing, database access via an ORM, templating, authentication and project structure out of the box `5:p10`.
**The problem it solves `5:p10`:** the hand-written connect → query → loop → render pattern works, but repeating it across dozens of pages gets repetitive and error-prone fast.
**The distinction to quote `5:p10`:** *"A library is something your code calls. A framework calls your code."* The framework owns the control flow and calls your controller; you fill in the behaviour.
**Snippet:**
```php
// raw PHP (Module IV)                     // Laravel
$r = mysqli_query($conn, "SELECT * FROM students");
while ($row = mysqli_fetch_assoc($r)) {    $students = Student::all();
    echo "<td>" . $row['name'] . "</td>";  return view('students.index', compact('students'));
}
```
**Why it exists:** common problems solved **once, consistently** `5:p10`. Security defaults (escaping, CSRF, hashed passwords) come free — that is the argument a 14-mark answer needs, not "it is faster".

### 2.16 MVC — the pattern Laravel enforces
**Story:** a restaurant. You (the user) order; the **waiter** (controller) takes the order; the **kitchen** (model) has the ingredients; the **plating** (view) is what reaches your table. The waiter never cooks and the kitchen never carries plates.
**Definition:** Model–View–Controller separates **data** (Model), **presentation** (View) and **request logic** (Controller), one job each `5:p11`.
**The deck's five boxes `5:p11`:** User → requests a page → **Controller** handles the request → **Model** talks to the database → **View** renders the response → Response sent back to the user. In practice the Controller calls the Model **first**, then hands its data to the View `5:p11`.
**Two rules the deck states outright `5:p11`:** *"the Controller never talks to the browser directly, and the Model never renders HTML."*
**Snippet (one request, three files):**
```php
// routes/web.php
Route::get('/students', [StudentController::class, 'index']);

// app/Http/Controllers/StudentController.php  (Controller)
public function index() {
    $students = Student::all();                      // Model
    return view('students.index', compact('students')); // View
}

// app/Models/Student.php  (Model)
class Student extends Model {
    protected $fillable = ['name', 'marks'];
}
```
```blade
{{-- resources/views/students/index.blade.php  (View) --}}
@foreach ($students as $s)
    <li>{{ $s->name }}</li>
@endforeach
```
**Why it exists:** three testable, replaceable pieces. Change the database, the view is untouched; restyle the UI, the SQL is untouched. That is "separation of concerns" — the phrase to open with.

### 2.17 Laravel's headline features
**Story:** four features, four jobs you would otherwise write yourself, badly.
**Definition `5:p12`:**

| Feature | What it does |
|---|---|
| **Eloquent ORM** | tables as PHP objects/methods — `Student::find(1)` instead of raw `mysqli_query()` |
| **Blade templating** | view layer; compiles `@if`, `@foreach` into plain PHP |
| **Artisan CLI** | scaffolding and tasks — `php artisan make:controller` |
| **Routing, middleware, migrations, auth** | URL→code mapping, request filtering, versioned DB schema, login |

**Snippet:**
```php
$student  = Student::find(1);            // Eloquent
$top      = Student::where('marks', '>', 80)->get();
```
```bash
php artisan make:controller StudentController
php artisan migrate
php artisan route:list
```
**Why they matter:** each replaces a category of boilerplate. In an answer, pair each feature with **the boilerplate it removes** — that is what earns the marks, not the feature name alone.

### 2.18 The application structure (and why it exists)
**Story:** a workshop with labelled drawers. You never ask "where does this go?".
**Definition `5:p13`:** the standard skeleton that makes the framework's conventions work — the framework *finds* your code by location, so location is part of the contract.

| Path | Holds | Deck ref |
|---|---|---|
| `app/Http/Controllers/` | controller classes | `5:p13` |
| `resources/views/` | Blade templates (`.blade.php`) | `5:p13`, `5:p22` |
| `routes/web.php` | URL → code mappings | `5:p13`, `5:p14` |
| `database/migrations/` | versioned schema changes | `5:p13` |

**The full tree (standard, not in your deck beyond the four above):**
```text
myapp/
├── app/                  application code (Models/, Http/Controllers/, Http/Middleware/)
├── bootstrap/            framework bootstrapping; app.php registers middleware & providers (L11+)
├── config/               configuration files (database.php, app.php, mail.php)
├── database/             migrations/, seeders/, factories/
├── public/               doc root — index.php front controller, CSS/JS/images
├── resources/views/      Blade templates
├── routes/               web.php, console.php, api.php
├── storage/              logs/, framework/cache, framework/sessions, app/uploads
├── tests/                PHPUnit/Pest tests
├── vendor/               Composer-installed packages (never edit)
├── .env                  environment secrets (DB password, APP_KEY)
└── artisan               the CLI entry point
```
**Why it exists:** "convention over configuration". Because `app/Http/Controllers` is a fixed address, `make:controller` can put the file there and the router can find it with zero config. Purpose answers (Q154) must say **predictability + onboarding + the framework locating your code automatically**.
**Security note worth a mark:** only `public/` is web-exposed. `.env`, `storage/` and `vendor/` sit above the doc root, so they cannot be downloaded.

### 2.19 Setup and Artisan basics
**Story:** three commands between an empty folder and a running site.
**Definition `5:p13`:** Laravel needs PHP, **Composer** (PHP's dependency manager) and a database.
**Snippet:**
```bash
composer create-project laravel/laravel myapp   # scaffold a project
cd myapp
php artisan serve                               # local dev server (http://127.0.0.1:8000)
```
```bash
# the artisan commands actually worth memorising
php artisan make:controller StudentController
php artisan make:controller StudentController --resource
php artisan make:model Student -m
php artisan make:middleware CheckAge
php artisan migrate
php artisan route:list
php artisan serve
```
**Why it exists:** `artisan` is the CLI half of the framework — scaffolding removes the "create file, write namespace, get the class name wrong" class of error. `composer` handles autoloading so you never write `require` again.

### 2.20 Routing: mapping a URL to code
**Story:** a switchboard. Each extension (URL) is wired to one phone (closure or controller method).
**Definition:** a route maps a URL to the code that handles it — the entry point for every request `5:p14`. Routes live in `routes/web.php` `5:p14`.
**Snippet:**
```php
<?php
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StudentController;

Route::get('/', function () {
    return "Welcome to Saintgits CSE";
});

Route::get('/students', [StudentController::class, 'index']);
?>
```
**Verb methods `5:p14`:** `Route::get()`, `Route::post()`, `Route::put()`, `Route::delete()` — one per HTTP method. A route points to a **closure** (inline function) or, more commonly, a **controller method** `5:p14`.
**Why it exists:** without routes, `index.php` becomes a 50-branch `if ($_SERVER['REQUEST_URI'])` ladder. Routing makes the URL→handler table declarative and inspectable (`php artisan route:list`).

### 2.21 Route parameters, constraints, names, groups
**Story:** a URL with slots. `/student/{id}` is a form letter; `{id}` is the blank.
**Definition (standard, not in your deck — the deck only introduces `{student}` via binding `5:p18`):**
```php
<?php
// required parameter
Route::get('/student/{id}', [StudentController::class, 'show']);

// optional parameter (must have a default in the method)
Route::get('/student/{id?}', [StudentController::class, 'show']);

// constraint: only digits
Route::get('/student/{id}', [StudentController::class, 'show'])->where('id', '[0-9]+');
Route::get('/post/{slug}', [PostController::class, 'show'])->where('slug', '[A-Za-z0-9-]+');

// named route -> URL generation, survives URL changes
Route::get('/students', [StudentController::class, 'index'])->name('students.index');

// route group with a prefix + name prefix
Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('/students', [StudentController::class, 'index'])->name('students.index');
    // URL: /admin/students   name: admin.students.index
});
?>
```
```php
// using a name anywhere
$url = route('students.index');        // http://host/students
return redirect()->route('students.show', ['id' => 5]);
```
**Why it exists:** parameters kill URL duplication; constraints turn a bad id into a 404 instead of a 500; **named routes** decouple your code from the URL string, so `/students` → `/students/all` is a one-line change instead of a grep across 30 files.

### 2.22 Sub-domain routing
**Story:** one codebase, many front doors — `cse.college.test` and `ece.college.test` both knock, the host name decides who answers.
**Definition (standard, not in your deck):** `Route::domain()` restricts a route (or a whole group) to one host, and `{parameter}` in the domain is passed to the handler like any other route parameter.
**Snippet:**
```php
<?php
Route::domain('{department}.college.test')->group(function () {
    Route::get('/students', [StudentController::class, 'index'])
        ->name('dept.students.index');
});

// fully fixed sub-domain
Route::domain('admin.college.test')->group(function () {
    Route::get('/dashboard', [AdminController::class, 'dashboard']);
});
?>
```
**Common use cases:** multi-tenant SaaS (each customer gets `customer.app.com`), separate admin vs public surfaces, per-department/per-campus portals, localisation (`en.`, `fr.`).
**Why it exists:** it moves a routing decision (which module owns this request) from *inside* your controller to *the router's table* — the request never reaches the wrong tenant's code.
**Trap:** sub-domain routes need the `{parameter}` in the domain declared **before** it is used in the URI, and local testing needs a hosts-file or `*.test` DNS entry.

### 2.23 Middleware — filtering requests
**Story:** airport security. Everyone walks the same corridor, but the guard can stop you before you reach the gate — or check your bag on the way out.
**Definition:** code that runs **before** a request reaches its controller (or after the response is built) — a filtering/processing layer wrapping the actual request handling `5:p16`.
**Common uses `5:p16`:** checking whether a user is logged in (auth), logging requests, checking permissions, rate-limiting.
**Snippet:**
```php
<?php
// applying it to one route  (deck, 5:p16)
Route::get('/dashboard', [DashboardController::class, 'index'])->middleware('auth');

// the full chain: route -> middleware -> controller  (deck, 5:p17)
Route::get('/students', [StudentController::class, 'index'])->middleware('auth');
?>
```
**Why it is separate from the controller `5:p16`:** so the same check ("is logged in") is not repeated inside every controller method that needs it. One line, one place, impossible to forget in a new method.
**Trap:** middleware runs **before** the route's controller resolves — so it cannot know what the controller found. It can only inspect the *request* (user, headers, IP, age, rate).

### 2.24 Global vs route middleware, `handle()`, and registration
**Story:** `handle()` is a doorway with a doorman standing in it. He either waves you through (`$next($request)`) or shuts the door (a redirect/abort).
**Definition (standard, not in your deck):** every middleware is a class with one method:
```php
public function handle(Request $request, Closure $next)
{
    // before the controller
    if (/* not allowed */) {
        return redirect('/login');     // short-circuit — controller never runs
    }
    $response = $next($request);       // pass the request deeper
    // after the controller — may modify $response
    return $response;
}
```
`$next($request)` means "carry on down the pipeline". **Not calling it** is the entire mechanism of blocking.
**Registration — two eras (both worth a line in an answer):**
```php
// Laravel 11+  bootstrap/app.php
->withMiddleware(function (Middleware $middleware) {
    $middleware->append(LogRequests::class);                  // global
    $middleware->alias(['auth' => Authenticate::class]);      // route alias
})

// Laravel 10 and earlier  app/Http/Kernel.php
protected $middleware = [ ... ];            // global: every request
protected $middlewareGroups = ['web' => [ ... ]];  // groups
protected $routeMiddleware = ['auth' => \App\Http\Middleware\Authenticate::class];
```
**Three categories:** *global* (every request), *group* (`web`, `api`), *route* (only where you attach it or `->middleware('auth')`).
**Why it exists:** the pipeline pattern. Each concern (session, CSRF, auth, logging) is one small class that can be added, removed or reordered without touching any controller.

### 2.25 Controllers
**Story:** a named desk for each resource. Instead of a wall of switches, one clerk per job.
**Definition:** controllers group related request-handling logic into a single class, keeping `routes/web.php` short and readable `5:p15`.
**Facts `5:p15`:** `php artisan make:controller StudentController` scaffolds the file; controllers live in `app/Http/Controllers/`; each public method typically handles one route; a method usually ends by returning a **view** or a **redirect**.
**Snippet:**
```php
<?php
namespace App\Http\Controllers;

use App\Models\Student;

class StudentController extends Controller
{
    public function index()
    {
        $students = Student::all();
        return view('students.index', compact('students'));
    }
}
```
**Why it exists:** routes stay declarative; the logic is testable in isolation; and a resource gets one predictable home. Q157's answer is three lines: *receives the request, asks the model for data, returns a view or redirect* — plus "keeps routes clean".

### 2.26 Resource controllers and the 7 RESTful actions
**Story:** IKEA's flat-pack: seven labelled parts that assemble any CRUD screen. You do not design it, you follow the sheet.
**Definition (standard, not in your deck):** a resource controller is a controller whose seven methods and route names follow a fixed convention, generated in one command:
```bash
php artisan make:controller StudentController --resource
```
and wired with:
```php
Route::resource('students', StudentController::class);
```
**The seven actions — memorise this table:**

| # | Method | Verb | URI | Route name | Job |
|---|---|---|---|---|---|
| 1 | `index()` | GET | `/students` | `students.index` | list all |
| 2 | `create()` | GET | `/students/create` | `students.create` | show empty form |
| 3 | `store()` | POST | `/students` | `students.store` | insert, then redirect |
| 4 | `show()` | GET | `/students/{student}` | `students.show` | display one |
| 5 | `edit()` | GET | `/students/{student}/edit` | `students.edit` | show form with data |
| 6 | `update()` | PUT/PATCH | `/students/{student}` | `students.update` | save changes |
| 7 | `destroy()` | DELETE | `/students/{student}` | `students.destroy` | delete |

**Snippet:**
```php
<?php
namespace App\Http\Controllers;

use App\Models\Student;
use Illuminate\Http\Request;

class StudentController extends Controller
{
    public function index()              { return view('students.index',   ['students' => Student::all()]); }
    public function create()             { return view('students.create'); }
    public function store(Request $r)    {
        Student::create($r->only('name', 'mark'));
        return redirect()->route('students.index')->with('success', 'Student added');
    }
    public function show(Student $student)   { return view('students.show', compact('student')); }
    public function edit(Student $student)   { return view('students.edit', compact('student')); }
    public function update(Request $r, Student $student) {
        $student->update($r->only('name', 'mark'));
        return redirect()->route('students.index')->with('success', 'Student updated');
    }
    public function destroy(Student $student) {
        $student->delete();
        return redirect()->route('students.index')->with('success', 'Student deleted');
    }
}
```
**Why it exists:** one line replaces seven `Route::get/post` lines, naming is predictable (so `route('students.edit', $id)` always works), and a new team member knows where every CRUD action lives without asking. `--only`/`--except` trim it: `Route::resource('students', StudentController::class)->only(['index','show']);`

### 2.27 Route model binding
**Story:** you give the concierge a room number and he returns the guest — you never walk to the filing cabinet yourself.
**Definition:** Laravel can automatically fetch the database record matching a route parameter and hand it to the controller — no manual query `5:p18`.
**Mechanism `5:p18`:** `{student}` is a URL placeholder; **type-hinting the matching parameter as a Model** triggers automatic lookup **by ID**; if no record exists, Laravel returns **404 automatically**; it saves writing `Student::find($id)` plus a null-check in every method.
**Snippet (implicit — the deck's version):**
```php
<?php
Route::get('/student/{student}', [StudentController::class, 'show']);

public function show(Student $student) {
    // $student is already the correct DB row
    return view('students.show', compact('student'));
}
?>
```
**The two types (standard, not in your deck):**
- **Implicit** — the parameter *name* matches the type-hinted model's variable name and the model's table key is `id`. `{student}` + `Student $student`. Override the column with `getRouteKeyName()` returning `'register_no'`, or in the route: `Route::get('/student/{student:register_no}', ...)`.
- **Explicit** — you declare the resolution yourself in `RouteServiceProvider` (or `AppServiceProvider`):
```php
Route::bind('student', function ($value) {
    return Student::where('register_no', $value)->firstOrFail();
});
```
**Why it exists:** it collapses three lines (`find`, `if null`, `abort(404)`) into a type-hint, and it makes controllers *unable* to forget the null check.

### 2.28 Views and passing data
**Story:** the controller writes the envelope (data), the view is the printed letter inside it.
**Definition:** `view('name', $data)` renders a Blade template passing it data; views live in `resources/views/` as `.blade.php` files `5:p19`.
**Snippet (three equivalent ways):**
```php
<?php
// 1. explicit array
return view('students.index', ['students' => $students]);

// 2. compact() — bundles a variable into an array keyed by its own name
return view('students.index', compact('students'));

// 3. with() chained
return view('students.index')->with('students', $students);
?>
```
**Dot notation `5:p19`:** `students.index` means `resources/views/students/index.blade.php`. The dot is a **folder separator**, not part of the filename.
**Why it exists:** the view receives only what it is given — no globals, no `global $conn`. That is what makes a view reusable and a controller testable.
**Extra (standard, not in your deck), for Q263(b)c:** share a variable with **all** views from a service provider:
```php
// app/Providers/AppServiceProvider.php  -> boot()
View::share('collegeName', 'Saintgits College of Engineering');
// now usable in every Blade file as {{ $collegeName }}
```

### 2.29 Redirections and flash data
**Story:** after the customer signs the form you do not hand the form back — you send them to the counter, with a sticky note saying "done".
**Definition `5:p20`:** `redirect('/path')` sends the browser to another route; `redirect()->back()` returns to the previous page (common after failed validation); `->with('key','value')` attaches **flash data** readable on the next request only.
**Snippet:**
```php
<?php
public function store(Request $request) {
    Student::create($request->all());
    return redirect('/students')
        ->with('message', 'Student added successfully!');
}
?>
```
```php
<?php
return redirect()->route('students.index')->with('success', 'Saved');  // by name
return back()->withInput()->withErrors(['mark' => 'Mark must be 0-100']); // back + old input
?>
```
**Why it exists `5:p20`:** *"redirecting after a successful POST prevents accidental duplicate form resubmission."* That is POST/Redirect/GET — refresh the page and you do not re-insert the student. Learn that sentence verbatim; it is the reason-mark in every redirection answer.
**Flash mechanics:** `with()` writes to the session for exactly one subsequent request; Blade reads it with `@if(session('success'))`.

### 2.30 The complete request lifecycle
**Story:** the deck's own six-step conveyor `5:p21`. Draw this from memory and you can answer a third of the Part B questions.
**Definition `5:p21`:** 1. **Route matches** the URL → 2. **Middleware runs checks** → 3. **Controller method runs** → 4a. **Model binding** fetches DB data → 5a. **`view()`** renders Blade, *or* 5b. **`redirect()`** to another route → **Response sent to the browser**.
**Snippet:**
```text
Browser GET /student/5
   │
   ├─ public/index.php  (front controller)
   ├─ Router: matches /student/{student}
   ├─ Middleware pipeline: auth, session, CSRF ...  ──fail──> redirect('/login')
   ├─ Controller: StudentController@show
   │     └─ Route model binding: SELECT * FROM students WHERE id = 5  ──none──> 404
   ├─ View: resources/views/students/show.blade.php  (Blade compiled + cached)
   └─ HTTP 200 response  →  browser
```
**The branch the deck insists on `5:p21`:** a **GET** that shows data ends in `view()`; a **POST** that changes data ends in `redirect()`.
**Why it exists:** it is the mental model that makes errors debuggable — "is this a routing 404, an auth redirect, or a controller exception?" is answered by knowing which stage you are in.

### 2.31 Blade — what it is
**Story:** PHP wearing a readable uniform. Same orders, no `<?php ?>` whiplash in the middle of your HTML.
**Definition `5:p22`:** Laravel's templating engine; you write directives (`@if`, `@foreach`) directly inside HTML instead of switching in and out of `<?php ?>` blocks.
**Three facts `5:p22`:** it **compiles to plain PHP** and caches it — so no real performance cost; files end in **`.blade.php`**; every `view()` call renders one of these files.
**Snippet:**
```blade
{{-- raw PHP you would have written in Module IV --}}
<?php foreach ($students as $s): ?>
    <li><?= htmlspecialchars($s->name) ?></li>
<?php endforeach; ?>

{{-- the Blade version --}}
@foreach ($students as $s)
    <li>{{ $s->name }}</li>
@endforeach
```
**Why it exists:** readability plus **safety by default** — `{{ }}` escapes for you, so you cannot forget `htmlspecialchars`.

### 2.32 Echoing and escaping
**Story:** `{{ }}` is a security guard who reads every value before it goes out. `{!! !!}` sends it out unchecked — use only on content you wrote.
**Definition `5:p23`:** `{{ $variable }}` echoes data **automatically escaped** (safe against XSS); `{!! $variable !!}` echoes **raw, unescaped HTML** — trusted content only.
**Snippet:**
```blade
<h2>Welcome, {{ $student->name }}</h2>
<p>{{ $bio ?? 'No bio provided.' }}</p>
{!! $trustedHtmlBlock !!}
{{-- This comment never reaches the browser --}}
```
**Why it exists:** escaping at the *output* boundary is the only reliable XSS defence. If `$student->name` is `<script>alert(1)</script>`, `{{ }}` renders it as visible text; `{!! !!}` executes it. Blade also supports full PHP expressions inside the braces `5:p23` — `{{ $name ?? 'Guest' }}`, `{{ count($students) }}`, `{{ number_format($mark, 2) }}`.
**Trap:** the HTML you write in the template is not escaped — only the *values* you echo. And `{{-- --}}` is a Blade comment; `<!-- -->` is an HTML comment that **does** reach the browser.

### 2.33 Conditionals
**Story:** four gates, each opened by a different question.
**Definition `5:p24`:** `@if/@elseif/@else/@endif` (branching), `@unless ... @endunless` (runs when false — inverse of `@if`), `@isset ... @endisset` (set and not null), `@empty ... @endempty` (empty).
**Snippet:**
```blade
@if (count($students) > 0)
    <p>{{ count($students) }} students found.</p>
@elseif ($searched)
    <p>No matches for your search.</p>
@else
    <p>No students yet.</p>
@endif

@unless ($isLoggedIn)
    <a href="/login">Please log in</a>
@endunless
```
**Why they exist:** they read as English at the exact indentation level of the markup, and they compile to plain PHP `if`. `@unless` exists because "if not" is the single most common shape in a view, and `@if(!$x)` reads badly.

### 2.34 Loops and the `$loop` variable
**Story:** `@foreach` is a conveyor belt — and it tells you your position on the belt for free.
**Definition `5:p25`:** `@foreach($items as $item) ... @endforeach` (most common), `@for($i=0; $i<10; $i++) ... @endfor`, `@while($cond) ... @endwhile`. Inside `@foreach`, `$loop->index`, `$loop->first`, `$loop->last` are available automatically.
**Snippet:**
```blade
<ul>
@foreach ($students as $s)
    <li>
        {{ $loop->iteration }}. {{ $s->name }}
        @if ($loop->last) (last student) @endif
    </li>
@endforeach
</ul>
```
**`$loop` members to know:** `index` (0-based), `iteration` (1-based), `first`, `last`, `count`, `remaining`, `even`/`odd`, `depth` (nesting level).
**Why it exists:** before Blade you tracked `$i` and compared it to `count($arr)-1` to decide the last comma. `$loop` removes that whole class of off-by-one bug.

### 2.35 Template inheritance
**Story:** a picture frame plus interchangeable photos. The frame (`layout`) never changes; each page is a photo (`section`) dropped into a hole (`@yield`).
**Definition `5:p26`:** `@extends('layout')` declares the parent layout; `@section('name') ... @endsection` defines a named block of content; `@yield('name')` in the **parent** marks where the child's section is inserted; `@include('partial')` pulls in a reusable chunk from another file.
**Snippet (`5:p26` verbatim shape):**
```blade
{{-- layout.blade.php --}}
<body>
    @include('partials.navbar')
    @yield('content')
</body>
```
```blade
{{-- students/index.blade.php --}}
@extends('layout')

@section('content')
    <h2>Student List</h2>
@endsection
```
**Why it exists:** without it, `header`/`footer`/`nav` markup is copy-pasted into 40 files — change the nav and you edit 40 files. With it, you edit one. **`@include` vs `@extends`:** include *pastes* a fragment in (no inheritance); extends *inherits* a whole skeleton and fills its holes.
**Trap:** `@extends` must be the **first** Blade construct in the child file, and a section defined but never yielded produces silence, not an error. Modern syntax `@extends('layouts.app')` is the same directive with a folder path — the dot is still a folder separator.

### 2.36 The directive quick-reference
**Definition `5:p27` table:**

| Directive | Purpose |
|---|---|
| `{{ $var }}` | Echo data, auto-escaped (safe) |
| `{!! $var !!}` | Echo raw HTML, unescaped (use with caution) |
| `@if / @elseif / @else / @endif` | Conditional rendering |
| `@foreach / @endforeach` | Loop over a collection or array |
| `@extends / @section / @yield` | Template inheritance — shared layouts |
| `@include('view')` | Insert a reusable partial template |

**The deck's closing note `5:p27`, worth quoting:** *"Every Blade directive is just a readable shorthand for plain PHP — nothing here is doing anything PHP itself couldn't do."* That single sentence is the correct answer to "why use Blade at all?" when the examiner is testing understanding rather than recall.
**Others you may safely use (standard, not in your deck):** `@php ... @endphp`, `@csrf` (hidden CSRF token — required in every Laravel POST form), `@method('PUT')` (method spoofing), `@auth/@guest`, `@empty/@endempty`, `@switch/@case/@endswitch`, `@error('field')`.

### 2.37 Components (only if the paper goes modern)
**Definition (standard, not in your deck — absent from these slides):** a Blade component is a reusable, parameterised view with a class:
```bash
php artisan make:component Alert
```
```blade
{{-- resources/views/components/alert.blade.php --}}
<div class="alert alert-{{ $type }}">{{ $slot }}</div>
```
```blade
<x-alert type="success">Student saved</x-alert>
```
**Why it exists:** `@include` shares markup but has no typed inputs; a component has declared props (`$type`), a slot, and an optional class for logic. Use it when a fragment needs *parameters and behaviour*, not just markup. **If the paper asks only `@extends/@section/@yield/@include` (as every question here does), answer with those and add one line noting components exist.**

---

## 3. PART 2 — Answer bank

### 3.1 3-mark answers (Part A)

Rules: **3–4 points, each one line**, then one code/JSON line if the question names a syntax item. Part A is marked fast — bullet points beat paragraphs. Where the bank asks the same thing twice, the answer is a **MASTER ANSWER** with an *also answers* list; learn the master, not the duplicates.

---

#### A1 — JSON as a data interchange format · *also answers Q143, half of Q130*
**Q130 "explain JSON as a data interchange format"; Q143 "define JSON + two advantages over XML".**

1. **Definition:** JSON (JavaScript Object Notation) is a lightweight, text-based, language-independent format for structured data, built from objects `{ }` and arrays `[ ]`.
2. **Interchange role:** it is the wire format between a client and a server (API responses, request bodies), between services, and for config files — both sides serialise to text and parse back to native structures.
3. **Advantage over XML 1:** far less verbose — no opening/closing tag pairs, so the same data is roughly half the bytes.
4. **Advantage over XML 2:** it maps directly onto structures every language already has (objects/maps, arrays/lists), so no translation layer, and it parses faster `5:p2`.
5. **Limit:** it is a data format, not a programming language — no functions, no comments, no logic `5:p2`.

```json
{ "name": "Anu", "age": 20, "marks": [88, 92, 79] }
```

---

#### A2 — PHP ⇄ JSON functions · *also answers Q131, Q151*
**Q151 "name the PHP functions"; Q131 "decode, modify, re-encode".**

1. **PHP → JSON:** `json_encode($value)` returns a JSON string. Associative arrays become objects, indexed arrays become arrays `5:p7`.
2. **JSON → PHP:** `json_decode($json)` returns objects; `json_decode($json, true)` returns associative arrays `5:p8`.
3. **Flags/errors:** `JSON_PRETTY_PRINT` for readable output; `json_last_error()` (compare with `JSON_ERROR_NONE`) to detect a parse failure `5:p7`, `p8`.

```php
<?php
$json  = '{"name":"Anu","marks":[88,92,79]}';
$data  = json_decode($json, true);
$data["marks"][1] = 95;                       // modify
echo json_encode($data, JSON_PRETTY_PRINT);   // re-encode
?>
```

---

#### A3 — Note on the Laravel framework · *also answers Q132, part of Q274*
1. **What:** a free, open-source **PHP framework** providing routing, an ORM (Eloquent), templating (Blade), authentication and project structure out of the box `5:p10`.
2. **Why:** the hand-written connect→query→loop→render pattern becomes repetitive and error-prone at scale; Laravel solves each common problem **once, consistently** `5:p10`.
3. **Framework vs library:** a library is something your code calls; **a framework calls your code** `5:p10`.
4. **Extras:** Artisan CLI for scaffolding, migrations for versioned schema, Composer for dependencies `5:p12`, `p13`.

---

#### A4 — Design pattern in Laravel · *also answers Q133, Q152*
1. **Primary pattern: MVC** (Model–View–Controller) — Model = data/DB, View = presentation, Controller = request logic, one job each `5:p11`.
2. **Also used:** *Front Controller* (every request enters via `public/index.php`), *Facade* (`Route::`, `DB::` static-looking access to services), *Repository/Service* (optional layering), *Dependency Injection* via the service container `5:p10` (standard, not in your deck).
3. **Pipeline pattern** for middleware — each layer wraps the next and may short-circuit `5:p16`.
4. **Convention over configuration** — file locations and names are the config `5:p13`.

---

#### A5 — Routing in Laravel · *also answers Q134, Q155*
1. **Definition:** a route maps a URL (+ HTTP verb) to the code that handles it — the entry point for every request `5:p14`.
2. **Where:** all web routes are declared in `routes/web.php` `5:p14`.
3. **Forms:** `Route::get()`, `Route::post()`, `Route::put()`, `Route::delete()` — one per HTTP method `5:p14`.
4. **Target:** a closure or, more commonly, a controller method `[StudentController::class, 'index']` `5:p14`.

```php
<?php
Route::get('/', function () { return "Welcome to Saintgits CSE"; });
Route::get('/students', [StudentController::class, 'index']);
Route::post('/students', [StudentController::class, 'store']);
?>
```

---

#### A6 — Middleware · *also answers Q135, Q146, Q156*
1. **Definition:** code that runs **before** a request reaches its controller (or after the response is built) — a filtering layer wrapping request handling `5:p16`.
2. **Uses:** login check (`auth`), request logging, permission checks, rate limiting `5:p16`.
3. **Applied:** `Route::get('/dashboard', ...)->middleware('auth');` — one line protects the route `5:p16`.
4. **Why separate:** the same check is not repeated in every controller method that needs it `5:p16`.
5. **Mechanism:** `handle($request, Closure $next)` — return a redirect/abort to block, or `return $next($request)` to continue (standard, not in your deck).

---

#### A7 — `@extends` · *also answers Q136, part of Q260(b)*
1. **Purpose:** declares which **parent layout** a child Blade view inherits, so header/footer/nav markup is written once `5:p26`.
2. **Pairs with:** `@section('content') ... @endsection` in the child, and `@yield('content')` at the insertion point in the parent `5:p26`.
3. **Rule:** `@extends` is the first Blade construct in the child file.

```blade
{{-- students/index.blade.php --}}
@extends('layout')
@section('content')
    <h2>Student List</h2>
@endsection
```

---

#### A8 — Route model binding · *also answers Q137, Q158, part of Q285*
1. **Definition:** Laravel auto-fetches the DB record matching a route parameter and injects it into the controller — no manual query `5:p18`.
2. **How (implicit):** `{student}` in the URI + a `Student $student` type-hint on the method ⇒ lookup **by id** `5:p18`.
3. **404 for free:** if no matching row exists, Laravel returns a 404 automatically `5:p18`.
4. **Saves:** `Student::find($id)` plus a null check in every method `5:p18`.

```php
Route::get('/student/{student}', [StudentController::class, 'show']);
public function show(Student $student) { return view('students.show', compact('student')); }
```

---

#### A9 — Resource controllers and CRUD · *also answers Q138, part of Q257*
1. **Definition:** a controller whose seven methods follow a fixed RESTful convention for one resource (standard, not in your deck).
2. **Generate + wire:** `php artisan make:controller StudentController --resource`, then `Route::resource('students', StudentController::class);` — one line creates seven routes.
3. **The seven actions:** `index, create, store, show, edit, update, destroy` (list / form / insert / display / edit-form / save / delete).
4. **Benefit:** convention-based naming (`students.index`) means URL generation and CRUD screens are predictable; `--only`/`--except` trim the set.

---

#### A10 — Schema of a JSON document + example · *also answers Q139*
*(This is the **structure** of a document, not the validation language of A14. Read the question.)*

1. **Schema = the document's shape**: top-level container, the keys, their types, and which values nest.
2. **Top level:** an object for one entity; an array for a collection.
3. **Keys:** consistent naming, plural for lists, real types for numbers.
4. **Example:**

```json
{
  "registerNo": "SJC22CS001",
  "name": "Anu Thomas",
  "semester": 7,
  "marks": [
    { "subject": "Web Programming", "mark": 88 },
    { "subject": "DBMS", "mark": 76 }
  ]
}
```
*Structure:* root object · three scalar fields (string, string, number) · one array of objects, each with a string and a number.

---

#### A11 — JSON data types · MASTER · *also answers Q140, Q144, Q148, part of Q262(a), Q271, Q279*
1. **The six types:** `string` (`"Saintgits"`, always double-quoted) · `number` (`20`, `499.50` — no int/float distinction) · `boolean` (`true`/`false`, lowercase, unquoted) · `null` (`null`, "no value") · `object` (`{"city":"Kottayam"}`) · `array` (`[88,92,79]`) `5:p4`.
2. **Two containers, four scalars.** Objects and arrays nest without limit; the other four are leaves.
3. **Structured data:** objects model an entity, arrays model repetition, nesting models relationships — a student *has* an address and a *list* of marks `5:p5`.
4. **No associative-array type:** JSON's `object` covers that role, unlike PHP `5:p4`.

```json
{
  "name": "Anu",
  "age": 20,
  "isActive": true,
  "address": null,
  "city": { "name": "Kottayam", "pin": "686532" },
  "marks": [88, 92, 79]
}
```

**Q279's six-item identification drill (learn verbatim):**

| Value | JSON type |
|---|---|
| `true` | boolean |
| `25` | number |
| `"PHP"` | string |
| `null` | null |
| `[1,2]` | array |
| `{"id":1}` | object |

---

#### A12 — `$schema` and `$id` · *also answers Q141*
1. **`$schema`** — root-level keyword giving the **URI of the JSON Schema dialect** the document is written in (e.g. `https://json-schema.org/draft/2020-12/schema`). It tells a validator **which set of rules to apply**.
2. **`$id`** — root-level keyword giving a **unique URI that identifies this schema itself**, so it can be referenced (`$ref`) by other schemas and cached/deduplicated by validators.
3. **Difference in one line:** `$schema` says *"which language am I written in"*; `$id` says *"who am I"*. *(standard, not in your deck — the deck covers only the concept of JSON Schema, `5:p6`.)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/student.json",
  "type": "object"
}
```

---

#### A13 — Three Laravel features · MASTER · *also answers Q142, Q153*
1. **Eloquent ORM** — tables as PHP objects/methods: `Student::find(1)` instead of raw `mysqli_query()` `5:p12`.
2. **Blade templating engine** — clean `@if`/`@foreach` directives compiled to plain PHP and cached `5:p12`.
3. **Artisan CLI** — scaffolding and tasks: `php artisan make:controller`, `php artisan migrate` `5:p12`.
4. *(fourth, if you want a spare)* **Routing, middleware, migrations and authentication** built in `5:p12`.

---

#### A14 — JSON Schema and its purpose · MASTER · *also answers Q145, Q150*
1. **Definition:** JSON Schema is a **separate JSON document that describes the rules another JSON document must satisfy** `5:p6`.
2. **Why it is needed:** JSON itself has no way to say "this field is required" or "this must be a number" `5:p6`.
3. **What it specifies:** required fields, per-field types, value constraints (minimum/maximum, patterns), and the structure of nested objects/arrays `5:p6`.
4. **Purpose:** automatic validation **wherever JSON crosses a trust boundary** — API request bodies, third-party responses, config files — instead of hand-writing an `if` per field `5:p6`.

---

#### A15 — GET vs POST vs route model binding · *also answers Q147, part of Q270(b)*
| | GET | POST | Route model binding |
|---|---|---|---|
| **Purpose** | retrieve/show data | submit/create/change data | resolve a route parameter into a model |
| **Data location** | query string / URL | request body | URL segment, e.g. `{student}` |
| **Idempotent** | yes | no | n/a — it is a resolution step, not a verb |
| **Ends in** | `view()` | `redirect()` | a model instance, or automatic 404 |
| **Deck ref** | `5:p14`, `5:p21` | `5:p14`, `5:p20` | `5:p18` |

**One-line answer:** GET *asks*, POST *tells*, route model binding *fetches the row the URL names* — the first two are HTTP methods, the third is a Laravel convenience that removes a manual `find()` + null-check.

---

#### A16 — JSON object vs JSON array · *also answers Q149*
1. **Object** `{ }`: **unordered** collection of **string-keyed** key–value pairs; look up by key; maps to a PHP associative array (or stdClass).
2. **Array** `[ ]`: **ordered** list of values; access by position; maps to a PHP indexed array.
3. **Keys:** an object's keys are always double-quoted strings; an array has no keys.
4. **Use:** object = one entity with named fields; array = a collection of entities/values. Both can nest inside each other.

```json
{ "student": { "name": "Anu" }, "marks": [88, 92, 79] }
```

---

#### A17 — Purpose of the application structure · *also answers Q154*
1. **Convention over configuration:** fixed locations mean the framework can *find* your code with zero configuration — controllers in `app/Http/Controllers/`, views in `resources/views/`, routes in `routes/web.php`, migrations in `database/migrations/` `5:p13`.
2. **Separation of concerns:** each concern gets one drawer, so a change touches one place `5:p11`.
3. **Security:** only `public/` is web-exposed; `.env`, `storage/`, `vendor/` sit above the doc root and cannot be downloaded (standard, not in your deck).
4. **Team scalability:** any Laravel developer can navigate any Laravel project; `artisan` generators always write to the right path `5:p12`.

---

#### A18 — Role of a controller · *also answers Q157*
1. **Receives the request** for its route and runs one public method per route `5:p15`.
2. **Asks the model** for data (`Student::all()`), applies the logic `5:p15`.
3. **Returns a response:** a `view()` with data, or a `redirect()` `5:p15`.
4. **Keeps `routes/web.php` short** by grouping related handling in one class `5:p15`.
5. **Never** renders HTML itself and never talks to the browser directly — the view does that `5:p11`.

---

#### A19 — What is Blade · *also answers Q159, part of Q265(b)*
1. **Definition:** Laravel's templating engine — clean directives (`@if`, `@foreach`) inside HTML instead of `<?php ?>` blocks `5:p22`.
2. **Compiles to plain PHP** and is cached, so there is no real performance cost `5:p22`.
3. **File convention:** `.blade.php`, stored in `resources/views/` `5:p22`.
4. **Safety by default:** `{{ }}` escapes output (XSS-safe); `{!! !!}` does not `5:p23`.
5. **Inheritance:** `@extends/@section/@yield/@include` remove repeated markup `5:p26`.

---

#### A20 — Purpose of `@foreach` · *also answers Q160*
1. **Purpose:** renders a block once per element of an array/collection — the most common loop in views `5:p25`.
2. **Syntax:** `@foreach ($students as $s) ... @endforeach` `5:p25`.
3. **Bonus:** inside it, `$loop->index / iteration / first / last / count` are available automatically `5:p25`.
4. **Why:** it replaces PHP's `foreach` + `endforeach` + manual counter and keeps the markup readable `5:p27`.

```blade
<ul>
@foreach ($students as $s)
    <li>{{ $loop->iteration }}. {{ $s->name }}</li>
@endforeach
</ul>
```

---

### 3.2 14-mark answers (Part B)

**How every Part B is marked.** Five things earn marks, in this order: (1) the **definition** stated in one sentence, (2) the **mechanism** — *how* it works, (3) **code/JSON that actually runs**, (4) a **worked example with real values**, (5) a **one-line justification** of why it exists. Answers that only define get 4/14. Answers that define + code + example get 11–12. The last 2 marks are the justification.

**Shape rule.** Count the split first (`7+7`, `8+6`, `10+4`, `6+8`, `5+9`). Give each half its proportional *space* — roughly 1 mark ≈ 2.5 lines of prose or 4 lines of code. Write the split as a heading inside your answer (`(a) ... [7]`). Examiners award per-part; a missing part cannot be recovered by a brilliant answer to the other.

**One master per theme.** Where the bank repeats a theme (JSON types appears in 6 questions; Blade in 4), there is one **MASTER ANSWER** here and the variants are listed with the *delta* you must add. Learn the master, then read the deltas — that is 5 minutes instead of 40.

---

#### B1 — JSON: syntax rules, data types, document design · MASTER
**Covers:** Q266 (7+7) · Q271 (a+b, 14) · Q278 (7+7) · Q262(a) first half (8) · Q279(a) (part) · Q139/Q263(a) first half.

**Variants and their delta:**

- **Q266** — (a) syntax rules [7] (b) student with marks array [7].
- **Q271** — (a) syntax **and all six types** [7] (b) student document with name, register no, course, marks, subjects [7].
- **Q278** — (a) syntax with object/array/nested examples [7] (b) **nested college → departments → students** [7]. Add the 3-level block from §4 D2.
- **Q262(a)** — (a) list the types + explain `JSON.parse()`/`stringify()` [8]. Add §B1.4.
- **Q279(a)** — identify the type of six given literals [7]. Add the six-row table.

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | Definition of JSON + the two container structures | 1 |
| (a) 2 | The five syntax rules, each with a legal/illegal pair | 4 |
| (a) 3 | The six data types with one example each | 2 |
| (b) 1 | The designed document (correct JSON) | 4 |
| (b) 2 | Walk-through: what each part of the shape models | 2 |
| (b) 3 | Why this shape (nesting models relationships) | 1 |

##### Full answer

**(a) JSON syntax rules [7]**

JSON (JavaScript Object Notation) is a lightweight, text-based, language-independent format for structured data. It is built from exactly **two** structures: an **object** `{ }` — an unordered set of key–value pairs — and an **array** `[ ]` — an ordered list of values. Everything else nests inside these two `5:p3`.

The rules for a *valid* JSON document:

1. **Keys are always double-quoted strings.** `{"name": "Anu"}` is valid; `{name: "Anu"}` and `{'name': 'Anu'}` are both invalid. This is the rule people break most, because JavaScript object literals allow bare and single-quoted keys — JSON does not.
2. **No comments of any kind.** Neither `//` nor `/* */` is legal. JSON is a data format, not a source file `5:p2`.
3. **No trailing comma** after the last member. `{"a":1,"b":2,}` is invalid.
4. **Exactly one top-level value.** A document is one object or one array (or, technically, one scalar). Two objects side by side is not a document.
5. **Strings use double quotes, and only these escapes are legal:** `\"  \\  \/  \b  \f  \n  \r  \t  \uXXXX`. Literal newlines inside a string are invalid.
6. **Numbers are plain decimal** — no leading `+`, no leading zeros, no hex, and `NaN`/`Infinity` do not exist.

The deck's own phrasing is worth quoting: JSON has *"strict syntax, unlike JavaScript object literals"* `5:p3` — the strictness is deliberate, because a parser must be unambiguous for two unrelated systems to interoperate.

```json
{
  "name": "Anu",
  "age": 20,
  "isActive": true,
  "marks": [88, 92, 79]
}
```

**(b) A student document [7]**

```json
{
  "registerNo": "SJC22CS001",
  "name": "Anu Thomas",
  "course": "B.Tech CSE",
  "semester": 7,
  "marks": [
    { "subject": "Web Programming", "mark": 88 },
    { "subject": "DBMS", "mark": 76 },
    { "subject": "Computer Networks", "mark": 81 }
  ]
}
```

**Why this shape:** the root is an **object** because it describes one entity. `registerNo`, `name`, `course` are `string`s and `semester` is a `number` — real types, not stringified values. `marks` is an **array of objects**, because "a student HAS many subject marks" is a one-to-many relationship, and each element pairs a subject name with a numeric mark so the two can never drift apart `5:p5`. Nesting is what lets a single document carry the whole relationship tree — the same reason an API response can replace several SQL joins on the client.

For **Q278(b)**, the same design at three levels — a college *has* departments, a department *has* students:

```json
{
  "college": "Saintgits College of Engineering",
  "departments": [
    {
      "code": "CSE",
      "hod": "Dr. Mathew",
      "students": [
        { "registerNo": "SJC22CS001", "name": "Anu", "mark": 88 },
        { "registerNo": "SJC22CS002", "name": "Rahul", "mark": 72 }
      ]
    },
    {
      "code": "ECE",
      "hod": "Dr. Nair",
      "students": [
        { "registerNo": "SJC22EC011", "name": "Meera", "mark": 91 }
      ]
    }
  ]
}
```
Read it aloud in the exam: *object → array of objects → array of objects*. That sentence is worth a mark on its own.

##### Traps
- Writing the example with **single quotes** — instantly invalid, and it is the most common lost mark in this question.
- Putting a trailing comma "for neatness" after the last array element.
- Saying "JSON supports comments" (it does not) or "JSON has a date type" (it does not — dates are strings).
- For Q278(b): producing siblings (`departments` and `students` at the same level) instead of **nesting students inside their department**. The nesting *is* the answer.
- Forgetting that indentation is cosmetic `5:p5` — say so, it shows you know what is and is not significant.

---

#### B2 — JSON Schema: keywords, validation, error reporting · MASTER
**Covers:** Q254 (8) · Q272 (a+b, 14) · Q280 (a+b, 14) · Q263(a) second half (schema for a Student document) · Q145/Q150 at 3-mark depth (see A14).

**Variants and their delta:**

- **Q254** — only "role of JSON Schema in validating (8) + how error handling is done". Skip the student schema; expand §B2.4.
- **Q272** — (a) Schema + `type`/`required`/`properties` [7] (b) schema for a student with required name + register number and a numeric mark [7].
- **Q280** — (a) how Schema validates + `type`/`properties`/`required`/`minimum`/`maximum` [7] (b) **course** object schema, credits 1–6 [7]. Use the course block below.
- **Q263(a)** — same as Q272(b), appended to a JSON-types answer.

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | Definition + the problem it solves | 1 |
| (a) 2 | What it can specify | 1 |
| (a) 3 | Keyword table: `$schema`, `$id`, `type`, `properties`, `required`, `minimum`, `maximum`, `items` | 3 |
| (a) 4 | How validation works, step by step | 2 |
| (b) 1 | The schema (correct JSON) | 4 |
| (b) 2 | A valid and an invalid instance, and what fails | 2 |
| (b) 3 | How the error is reported | 1 |

##### Full answer

**(a) JSON Schema and its keywords [7]**

JSON Schema is **a separate JSON document that describes the rules another JSON document must satisfy**. It exists because JSON itself has no way to say *"this field is required"* or *"this must be a number"* `5:p6`. Before trusting incoming JSON — a form submitted from JavaScript, a response from another service — a schema validates its shape automatically instead of hand-writing an `if` per field. It is valuable **wherever JSON crosses a trust boundary** `5:p6`.

| Keyword | Level | Meaning |
|---|---|---|
| `$schema` | root | the URI of the **dialect** — tells the validator which rule-set to apply |
| `$id` | root | a unique URI **identifying this schema**, so it can be `$ref`-ed and cached |
| `type` | any | allowed JSON type: `object`, `array`, `string`, `number`, `integer`, `boolean`, `null` |
| `properties` | inside an object | map of key → sub-schema for each known key |
| `required` | inside an object | array of key **names** that must be *present* |
| `minimum` / `maximum` | inside a number | inclusive numeric bounds |
| `items` | inside an array | the schema **every** element must satisfy |
| `additionalProperties` | inside an object | `false` forbids keys not in `properties` |

**How validation works:** the validator walks the instance and the schema together. At each level it checks `type` first; then, for an object, that every `required` name exists and that each present key's value satisfies its `properties` sub-schema; for an array, that every element satisfies `items`; for a number, that it lies within `minimum`/`maximum`. A document is **valid** if every check passes, **invalid** otherwise. Nested failures are found by recursion, so a bad `mark` inside `marks[2]` is caught.

**(b) Schema for a student [7]**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/student.json",
  "title": "Student",
  "type": "object",
  "required": ["registerNo", "name", "mark"],
  "properties": {
    "registerNo": { "type": "string", "pattern": "^SJC[0-9]{2}CS[0-9]{3}$" },
    "name":       { "type": "string", "minLength": 2 },
    "email":      { "type": "string" },
    "mark":       { "type": "number", "minimum": 0, "maximum": 100 },
    "subjects":   { "type": "array", "items": { "type": "string" } }
  },
  "additionalProperties": false
}
```

**Valid instance:**
```json
{ "registerNo": "SJC22CS001", "name": "Anu", "mark": 88 }
```
All three `required` names present, `mark` is a number inside 0–100, no unknown keys ⇒ valid.

**Invalid instance:**
```json
{ "registerNo": "SJC22CS001", "name": "Anu", "mark": 120 }
```
`mark` violates `maximum: 100`. Reported as:
```json
[
  {
    "instancePath": "/mark",
    "schemaPath": "#/properties/mark/maximum",
    "keyword": "maximum",
    "message": "must be <= 100"
  }
]
```

**For Q280(b), the course schema with credits 1–6** — the only changes are the property names and the bounds:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/course.json",
  "type": "object",
  "required": ["code", "title", "credits"],
  "properties": {
    "code":    { "type": "string" },
    "title":   { "type": "string" },
    "credits": { "type": "integer", "minimum": 1, "maximum": 6 }
  },
  "additionalProperties": false
}
```
`"credits": 2` passes; `0` fails `minimum`; `7` fails `maximum`; `"3"` fails `type`.

**(Error handling, the Q254 half, expanded):** a validator returns a boolean **plus an array of error objects**. Each carries `instancePath` (JSON Pointer to the offending value, `""` meaning the root), `schemaPath` (which keyword failed), `keyword` and a human-readable `message`. Because every error carries a path, a web form can highlight the exact field, and because *all* errors are collected rather than the first, the user sees every mistake in one pass. The document is valid **iff** that array is empty. That is the whole of "how error handling is done with JSON Schema" — *not* exceptions, *not* a single message, but a machine-readable list of failures keyed by path.

##### Traps
- Writing `"required": true` inside a property. `required` is an **array of key names** at the *object* level, not a boolean on a property. This is the single most common schema error in exams.
- Confusing "required" with "non-empty": `""` satisfies `{"type":"string"}`, so `minLength` is what forbids empties.
- Putting `minimum`/`maximum` on a `string`.
- Forgetting `"type": "object"` at the root — the schema then validates nothing useful.
- Claiming schema validation *throws* on error. Most validators **return** an error list; only some libraries throw.
- Using `type: "int"` — the correct JSON Schema type name is `"integer"`.

---

#### B3 — PHP ⇄ JSON: serialise, deserialise, round trip · MASTER
**Covers:** Q268 (8+6) · Q273 (a+b, 14) · Q267 (7+7) · Q279(b) (7) · Q131 at 3 marks (see A2).

**Variants and their delta:**

- **Q268** — (a) the process of serialising/deserialising [8] (b) encode an associative array of **employees**, then decode it back [6].
- **Q273** — (a) `json_encode`/`json_decode` with examples [7] (b) decode a student record, **change the mark**, re-encode [7].
- **Q267** — (a) compare JSON types with PHP types [7] (b) decode a JSON object and **display** values (HTML output) [7].
- **Q279(b)** — create an associative array, convert to JSON [7]. Two lines of code + the type-mapping explanation.

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | `json_encode` — signature, mapping rules, flags | 3 |
| (a) 2 | `json_decode` — signature, the `true` flag, return types | 3 |
| (a) 3 | Error handling (`json_last_error`) | 2 |
| (b) 1 | Working script, complete and runnable | 4 |
| (b) 2 | The actual output shown | 1 |
| (b) 3 | One line on why round-tripping is safe/lossy | 1 |

##### Full answer

**(a) The two functions [8]**

*Serialising* = converting an in-memory PHP value into a JSON **string** for transport or storage. *Deserialising* = parsing that string back into a PHP value.

**`json_encode($value, $flags = 0): string|false`** `5:p7`
- PHP **associative** arrays become JSON **objects**; PHP **indexed** arrays become JSON **arrays** — decided automatically by whether the keys are sequential integers from 0.
- PHP objects become JSON objects from their **public** properties.
- `JSON_PRETTY_PRINT` indents for readability; `JSON_UNESCAPED_SLASHES` and `JSON_UNESCAPED_UNICODE` keep `https://` and non-ASCII readable; `JSON_THROW_ON_ERROR` throws instead of returning `false`.
- Returns `false` on failure (e.g. invalid UTF-8).

**`json_decode($jsonString, bool $assoc = false, int $depth = 512): mixed`** `5:p8`
- With the default `$assoc = false` you get **`stdClass` objects** — access with `->`.
- With `$assoc = true` you get **associative arrays** — access with `["..."]`, and `foreach`/`array_map`/`compact()` all work naturally. This is the usual choice `5:p8`.
- Returns `null` on failure — *and* for the valid document `null`, which is why the error check matters.

**Error handling:** `json_last_error()` returns an integer code for the last operation; compare with `JSON_ERROR_NONE` (0). `json_last_error_msg()` gives the message (`Syntax error`, `Malformed UTF-8 characters`, ...) `5:p8`.

**Type mapping table (this is Q267(a), worth memorising):**

| JSON | PHP (assoc `true`) | PHP (default) |
|---|---|---|
| `string` | `string` | `string` |
| `number` (`20`) | `int` | `int` |
| `number` (`499.50`) | `float` | `float` |
| `boolean` | `bool` | `bool` |
| `null` | `null` | `null` |
| `object` | **associative array** | **`stdClass`** |
| `array` | indexed array | array |

The interesting rows are the last two: JSON has no associative-array type — its `object` covers that role `5:p4` — so PHP's two array kinds both map onto JSON's two containers, but come back as two *different* PHP things unless you pass `true`.

**(b) Decode → modify → re-encode [6]**

```php
<?php
$json = '{"registerNo":"SJC22CS001","name":"Anu","mark":72,"subjects":["WP","DBMS"]}';

// 1. deserialise into an associative array
$student = json_decode($json, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    die("Invalid JSON: " . json_last_error_msg());
}

// 2. modify
$student["mark"] = 88;
$student["result"] = ($student["mark"] >= 40) ? "Pass" : "Fail";

// 3. serialise back
$newJson = json_encode($student, JSON_PRETTY_PRINT);
echo $newJson;
?>
```

**Output:**
```json
{
    "registerNo": "SJC22CS001",
    "name": "Anu",
    "mark": 88,
    "subjects": ["WP", "DBMS"],
    "result": "Pass"
}
```

**For Q268(b), the employees version** (assoc array → JSON → decode back → prove the round trip):

```php
<?php
$employees = [
    ["id" => 1, "name" => "Anu",   "department" => "CSE", "salary" => 55000],
    ["id" => 2, "name" => "Rahul", "department" => "ECE", "salary" => 48000],
];

// serialise
$json = json_encode($employees, JSON_PRETTY_PRINT);
echo $json;

// deserialise
$decoded = json_decode($json, true);

// prove the round trip: values survive, types survive
foreach ($decoded as $e) {
    echo $e["name"] . " earns " . $e["salary"] . PHP_EOL;
}
var_dump($decoded === $employees);   // bool(true)
?>
```

**For Q267(b) — decode and *display* in HTML:**

```php
<?php
$json = '{"name":"Rahul","marks":[72,80,91]}';
$s = json_decode($json, true);
?>
<h2><?= htmlspecialchars($s["name"]) ?></h2>
<ul>
<?php foreach ($s["marks"] as $m): ?>
    <li><?= $m ?></li>
<?php endforeach; ?>
</ul>
<p>Total: <?= array_sum($s["marks"]) ?></p>
```
Use `htmlspecialchars()` on every echoed string — that is the non-Laravel equivalent of Blade's `{{ }}`.

**Why round-tripping is safe, and where it is not:** JSON is a *text* format with six types; PHP has more (resources, closures, objects with private state). Scalars and arrays round-trip exactly; resources and objects lose their identity (an object returns as `stdClass` or an array), and `NAN`/`INF` cannot be encoded at all (they become `0` or fail). So "serialise → deserialise" is **value-preserving for data, not for behaviour** — which is exactly what you want when the payload is a database row.

##### Traps
- Writing `json_decode($json, TRUE)` with the argument in the wrong position, or forgetting it and then using `$data["name"]` on a `stdClass` (fatal error: *Cannot use object of type stdClass as array*).
- Encoding **inside** the fetch loop — produces `{...}{...}{...}`, which is not a JSON document. Encode once, after the loop `5:p9`.
- Echoing the modified array without `json_encode` (prints `Array`).
- Not sending `header("Content-Type: application/json")` when the output is an API response `5:p9`.
- Forgetting `json_last_error()` — the deck lists it explicitly, so it is a marked point `5:p8`.

---

#### B4 — Laravel, MVC, features, structure, setup · MASTER (the biggest 14-marker)
**Covers:** Q255 (14) · Q261(a) (6) · Q269 (7+7) · Q274 (a+b, 14) · Q281 (7+7) · Q282 (7+7) · Q154 at 3 marks (A17).

**Variants and their delta:**

- **Q255** — MVC in Laravel **with an example** *and* how it handles an HTTP request. Add the request walk-through from §B4.5.
- **Q261(a)** — "with a neat diagram" [6]: draw the five-box chain and label it. Diagram marks are real marks: **box + arrow + label**.
- **Q269** — (a) MVC [7] (b) directory structure with roles [7]. Drop the setup half.
- **Q274** — (a) Laravel + MVC + features + purpose of the structure [7] (b) **setup steps** [7]. Add §B4.6.
- **Q281** — (a) MVC + responsibilities [7] (b) map a **student management application** onto M/V/C [7]. Use the mapping table.
- **Q282** — (a) important directories [7] (b) specifically `routes`, `resources`, `app`, `database` [7]. Same table, four rows expanded.

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | What Laravel is + why a framework | 2 |
| (a) 2 | MVC: the three roles, one line each | 3 |
| (a) 3 | The diagram (user → controller → model → view → response) | 3 |
| (a) 4 | Worked example: one URL, three files | 4 |
| (b) 1 | Features table (Eloquent, Blade, Artisan, routing/middleware/migrations/auth) | 2 |
| (b) 2 | Directory table with roles | 5 |
| (b) 3 | Setup commands | 3 |

##### Full answer

**(a) Laravel and MVC [8]**

Laravel is a free, open-source PHP framework that supplies routing, database access through an ORM, templating, authentication and a standard project structure out of the box `5:p10`. It exists because the hand-written *connect → query → loop → render* pattern from Modules III–IV works, but repeated across dozens of pages becomes repetitive and error-prone `5:p10`. The distinction worth stating: **a library is something your code calls; a framework calls your code** `5:p10` — Laravel owns the control flow and calls your controller.

Laravel implements **MVC**, which separates three concerns so that each has exactly one job `5:p11`:

- **Model** — the data layer. Talks to the database, holds business rules, knows nothing about HTML. In Laravel: an Eloquent class, `app/Models/Student.php`.
- **View** — the presentation layer. Renders HTML from data it is given. Knows nothing about SQL. In Laravel: a Blade file, `resources/views/students/index.blade.php`.
- **Controller** — the request handler. Receives the request, asks the model for data, hands it to a view (or redirects). In Laravel: `app/Http/Controllers/StudentController.php`.

Two rules the deck states outright, and which examiners look for `5:p11`: **the controller never talks to the browser directly, and the model never renders HTML.**

**The diagram (Q261a) — draw exactly this:**

```text
        ┌────────┐   requests a page   ┌──────────────┐
        │  User  │ ──────────────────▶ │  Controller  │
        └────────┘                     └──────┬───────┘
                  ◀──────────┐                 │ calls first
                             │                 ▼
                             │          ┌──────────────┐
                             │          │    Model     │
                             │          │ (database)   │
                             │          └──────┬───────┘
                             │                 │ returns data
                             │                 ▼
                             │          ┌──────────────┐
                             └───────── │     View     │
                                response└──────────────┘
```
Label the arrows: *request →*, *calls model*, *data*, *renders*, *response*. In practice the controller calls the model **first**, then hands its data to the view — the deck draws it as one left-to-right journey `5:p11`.

**Worked example (this is what makes it 14 and not 8) — `GET /students`:**

```php
// routes/web.php  — the URL the user typed
Route::get('/students', [StudentController::class, 'index']);
```
```php
// app/Http/Controllers/StudentController.php  — CONTROLLER
namespace App\Http\Controllers;
use App\Models\Student;

class StudentController extends Controller
{
    public function index()
    {
        $students = Student::all();                          // asks the MODEL
        return view('students.index', compact('students'));  // hands data to the VIEW
    }
}
```
```php
// app/Models/Student.php  — MODEL
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Student extends Model
{
    protected $fillable = ['name', 'mark'];
}
```
```blade
{{-- resources/views/students/index.blade.php  — VIEW --}}
<h2>Student List</h2>
<ul>
@foreach ($students as $s)
    <li>{{ $s->name }} — {{ $s->mark }}</li>
@endforeach
</ul>
```
The user never sees SQL; the model never sees HTML; the controller contains neither. That separation is the answer to "how does MVC organise application code".

**(b) Features and structure [6]**

| Feature | What it gives you | What it replaces |
|---|---|---|
| **Eloquent ORM** | tables as objects — `Student::find(1)` | hand-written `mysqli_query()` strings `5:p12` |
| **Blade** | `@if`/`@foreach` compiled to cached PHP | `<?php ?>` soup in templates `5:p12` |
| **Artisan CLI** | `make:controller`, `migrate`, `route:list` | manual file creation `5:p12` |
| **Routing / middleware / migrations / auth** | URL mapping, request filtering, versioned schema, login | hand-rolled `$_SERVER` switches and `ALTER TABLE` `5:p12` |

| Directory | Role |
|---|---|
| `app/` | your application code — `Models/`, `Http/Controllers/`, `Http/Middleware/`, `Providers/` |
| `routes/` | `web.php` (browser routes), `api.php`, `console.php` — the URL→code table `5:p13` |
| `resources/views/` | Blade templates (`.blade.php`) `5:p13` |
| `database/` | `migrations/` (versioned schema), `seeders/`, `factories/` `5:p13` |
| `public/` | the **only** web-exposed folder — `index.php` front controller, CSS/JS/images |
| `config/` | configuration (`database.php`, `app.php`) |
| `storage/` | logs, compiled Blade, cache, sessions, uploads — must be writable |
| `bootstrap/app.php` | wires middleware, providers, routing (Laravel 11+) |
| `vendor/` | Composer packages — never edit |

**Purpose of this structure (Q274a's last clause, Q154):** *convention over configuration*. Because `app/Http/Controllers` is a **fixed address**, `artisan` can write a controller there and the router can find it with zero configuration; any Laravel developer can navigate any Laravel project; and only `public/` is exposed, so `.env` (DB password, `APP_KEY`) and `storage/` cannot be downloaded.

**(b) Setup steps [for Q274(b)]**

```bash
# prerequisites: PHP >= 8.2, Composer, MySQL/SQLite
composer create-project laravel/laravel myapp   # 1. scaffold the project
cd myapp                                        # 2. enter it
php artisan serve                               # 3. run the dev server
#   -> http://127.0.0.1:8000
```
```bash
# 4. configure the database in .env   (DB_DATABASE, DB_USERNAME, DB_PASSWORD)
php artisan migrate        # 5. create the tables
php artisan make:controller StudentController   # 6. scaffold code
php artisan route:list     # 7. verify the URL map
```

**Student-management mapping (for Q281b):**

| Concern | Layer | Concrete artefact |
|---|---|---|
| `students` table, columns, relationships | **Model** | `app/Models/Student.php` + a migration |
| fetch all / find one / insert / update / delete | **Model** (queries) called by **Controller** | `Student::all()`, `::find()`, `->save()`, `->delete()` |
| list page, create form, edit form, detail page | **View** | `students/index`, `create`, `edit`, `show` `.blade.php` |
| validate input, decide view vs redirect, flash message | **Controller** | `StudentController@store` |
| which URL hits which method | **Router** | `Route::resource('students', StudentController::class)` |

##### Traps
- Drawing MVC as a **line** (User→Model→View→Controller). The controller is the entry point and it *calls* the model; the model never calls the view.
- Saying the **view queries the database**. It does not — that is the whole point of the split, and it is a marked negative.
- Listing "fast", "secure", "free" as Laravel *features*. Features are named subsystems: Eloquent, Blade, Artisan, routing, middleware, migrations, auth.
- Confusing `resources/views` (templates) with `public/` (assets + front controller).
- Q261(a) says **"with a neat diagram"** — no diagram, no diagram marks. Boxes and labelled arrows take 90 seconds.

---

#### B5 — Routing in detail · MASTER
**Covers:** Q258(a) (10) · Q270(a) (7) · Q284 (7+7) · Q275(a) (7) · Q261(b) (8) · Q134/Q155 at 3 marks (A5).

**Variants and their delta:**

- **Q258(a)** [10] — definition, where routes live, verbs, parameters, **named routes**, groups. All four sub-topics are named in the question, so all four must appear.
- **Q261(b)** [8] — "routing mechanisms": verbs, closures vs controllers, parameters, constraints, names, groups. Add `route:list`.
- **Q270(a)** [7] — routing with examples only.
- **Q284** — (a) GET/POST syntax + named routes [7] (b) routes for a **student form** and its submission [7]. Use the form block.
- **Q275(a)** (part of the hybrid) — routing + middleware + controllers together; add §B6's middleware line.

##### Structure
| Part | Content | Marks |
|---|---|---|
| 1 | Definition + `routes/web.php` + the front controller | 2 |
| 2 | Verb methods, closure vs controller target | 2 |
| 3 | Route parameters (+ optional) | 2 |
| 4 | Constraints (`->where`) | 1 |
| 5 | Named routes (`->name`, `route()`) | 2 |
| 6 | Groups (prefix, name prefix, middleware) | 1 |

##### Full answer

**Definition.** A route maps a URL and an HTTP verb to the code that handles it. It is the entry point of every request in a Laravel application, and all browser routes are declared in `routes/web.php` `5:p14`. Every request physically arrives at `public/index.php` (the *front controller*), which boots the framework and asks the router to match the path.

**1. Verbs.** One static method per HTTP method `5:p14`:

```php
<?php
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StudentController;

Route::get('/students', [StudentController::class, 'index']);    // read
Route::post('/students', [StudentController::class, 'store']);   // create
Route::put('/students/{id}', [StudentController::class, 'update']);   // full update
Route::patch('/students/{id}', [StudentController::class, 'update']); // partial
Route::delete('/students/{id}', [StudentController::class, 'destroy']);
?>
```
`Route::get()` handles GET; `Route::post()`, `Route::put()`, `Route::delete()` handle the others `5:p14`. A route can also answer several verbs at once with `Route::match(['get','post'], ...)` or all of them with `Route::any(...)`.

**2. Closure or controller.** A route's second argument is either an inline **closure** or a **controller method** array — `[StudentController::class, 'index']` — which is "more common" in real applications `5:p14`:

```php
Route::get('/', function () { return "Welcome to Saintgits CSE"; });   // closure
Route::get('/students', [StudentController::class, 'index']);          // controller
```
Closures are fine for a one-line landing page; anything with logic belongs in a controller, because closures cannot be cached by `route:cache` and cannot be unit-tested.

**3. Parameters.** A `{name}` segment is a placeholder captured from the URL and passed **positionally** to the handler:

```php
Route::get('/student/{id}', [StudentController::class, 'show']);        // required
Route::get('/student/{id?}', [StudentController::class, 'show']);       // optional

// the method receives it by name
public function show($id) { return "Student " . $id; }

// two parameters — order matters
Route::get('/student/{id}/subject/{sub}', [StudentController::class, 'subject']);
```

**4. Constraints.** `->where()` restricts a parameter with a regex, so a non-matching URL 404s at the router instead of erroring in the controller:

```php
Route::get('/student/{id}', [StudentController::class, 'show'])->where('id', '[0-9]+');
Route::get('/post/{slug}', [PostController::class, 'show'])->where('slug', '[A-Za-z0-9-]+');
// global pattern, in a service provider:
// Route::pattern('id', '[0-9]+');
```

**5. Named routes.** `->name()` attaches a symbolic name; `route('name')` builds the URL from it:

```php
Route::get('/students', [StudentController::class, 'index'])->name('students.index');
Route::get('/student/{id}', [StudentController::class, 'show'])->name('students.show');

$url = route('students.index');                       // http://host/students
$url = route('students.show', ['id' => 5]);           // http://host/student/5
return redirect()->route('students.index');           // redirect by name
```
**Why this matters (the justification mark):** without names, the string `/students` is duplicated in views, controllers and redirects. Change the URL and you must find every copy. With a name, the URL is defined **once**, in the route file, and every `route('students.index')` follows automatically. It also means a view never hard-codes a path.

**6. Groups.** Shared attributes (prefix, name prefix, middleware, domain) are declared once around a closure:

```php
Route::prefix('admin')->name('admin.')->middleware('auth')->group(function () {
    Route::get('/students', [StudentController::class, 'index'])->name('students.index');
    Route::get('/students/create', [StudentController::class, 'create'])->name('students.create');
});
// URL  /admin/students        name  admin.students.index      requires login
```
Groups are how a whole section gets protected by one `middleware('auth')` instead of seven.

**For Q284(b) — the form and its submission:**

```php
<?php
// show the empty form            GET  /students/create
Route::get('/students/create', [StudentController::class, 'create'])->name('students.create');

// process the submitted form     POST /students
Route::post('/students', [StudentController::class, 'store'])->name('students.store');
?>
```
```blade
{{-- resources/views/students/create.blade.php --}}
<form action="{{ route('students.store') }}" method="POST">
    @csrf
    <input type="text"   name="name"  placeholder="Name">
    <input type="number" name="mark"  placeholder="Mark">
    <button type="submit">Save</button>
</form>
```
Note the pairing: **GET shows the form, POST processes it, and the form's `action` uses `route()`** so the URL is never hard-coded. `@csrf` is mandatory — Laravel rejects a POST without the token.

**The request's journey through the router (for Q261b's "mechanisms"):**
```text
URL + verb  →  public/index.php  →  Router matches (method + URI + constraints)
            →  route's middleware stack runs
            →  handler: closure, or Controller@method resolved from the container
            →  parameters injected (route params, bound models, Request)
            →  return value: string | view | redirect | JsonResponse
```

##### Traps
- Using `Route::get()` for a form submission. The form must POST (or spoof with `@method('PUT')`) — GET puts data in the URL and can be re-triggered by a refresh.
- Forgetting `use App\Http\Controllers\StudentController;` — the class name resolves to the wrong namespace and you get a 500.
- Writing `'StudentController@index'` (Laravel 7 style). The modern form is the array `[StudentController::class, 'index']`; both work, the array is what the deck uses `5:p14`.
- Claiming named routes change the URL. They do not — they **decouple code from** the URL.
- A parameter used in the method in a different order than declared — parameters bind **positionally** for plain `$id` arguments.

---

#### B6 — Middleware: types, custom middleware, auth flow · MASTER
**Covers:** Q258(b) (4) · Q264(a) (8) · Q283 (7+7) · Q275(b) (7) · Q135/Q146/Q156 at 3 marks (A6).

**Variants and their delta:**

- **Q258(b)** [4] — "creating and using custom middleware": `make:middleware`, `handle()`, register, attach. Short.
- **Q264(a)** [8] — concept **with types** and an example: global / group / route, plus the `handle()` code.
- **Q283** — (a) middleware + authentication/filtering [7] (b) a route using auth middleware + **explain the request flow** [7].
- **Q275(b)** [7] — design a route protected by middleware and handled by a controller. That is 4 lines of code + a flow sentence.
- **Q146** (3 marks) — middleware + one use case only: see A6.

##### Structure
| Part | Content | Marks |
|---|---|---|
| 1 | Definition + where it sits in the pipeline | 2 |
| 2 | `handle($request, Closure $next)` + `$next` + short-circuit | 2 |
| 3 | The three types (global / group / route) + registration | 2 |
| 4 | A complete custom middleware class | 2 |
| 5 | Auth use case + the request flow, step by step | 2 |

##### Full answer

**(a) Concept [8]**

Middleware is code that runs **before** a request reaches its controller, or **after** the response has been built — a filtering/processing layer wrapped around the actual request handling `5:p16`. It is the airport-security layer of the framework: every passenger (request) walks the same corridor, and the guard can stop you before you reach the gate, or check your bag on the way out.

Its uses are exactly the cross-cutting concerns you would otherwise copy into every controller `5:p16`: checking whether a user is logged in (`auth`), logging requests, checking permissions/roles, rate-limiting how often an endpoint can be called, forcing HTTPS, setting locale, trimming input.

**Mechanism — one method, one decision.** Every middleware is a class with `handle()`:

```php
<?php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class CheckLoggedIn
{
    public function handle(Request $request, Closure $next)
    {
        // 1. BEFORE the controller — inspect the request
        if (! $request->session()->has('user_id')) {
            return redirect('/login');       // SHORT-CIRCUIT: controller never runs
        }

        // 2. pass the request deeper down the pipeline
        $response = $next($request);

        // 3. AFTER the controller — may modify the response
        $response->headers->set('X-App', 'Saintgits');

        return $response;
    }
}
```
The whole idea is `$next($request)`. Calling it means "carry on"; **not** calling it (returning a redirect or `abort(403)`) is precisely how a request is blocked. Code before `$next` runs on the way in, code after it runs on the way out.

**Three types, by where they are registered:**

| Type | Scope | Where registered |
|---|---|---|
| **Global** | every request, no opt-in | `bootstrap/app.php` `->withMiddleware(fn ($m) => $m->append(...))` (L11+) or `$middleware` in `app/Http/Kernel.php` (L10-) |
| **Group** | a named bundle, e.g. `web` (session, CSRF, cookies), `api` | `$middlewareGroups` / `$m->group()` |
| **Route** | only routes that name it | `->middleware('auth')`, `->middleware([A::class, B::class])`, or a group |

Registration and aliasing (both syntaxes are worth one line, because the Laravel version in your syllabus may be either):
```php
// Laravel 11+  bootstrap/app.php
->withMiddleware(function (Middleware $middleware) {
    $middleware->append(\App\Http\Middleware\LogRequests::class);          // global
    $middleware->alias(['loggedin' => \App\Http\Middleware\CheckLoggedIn::class]); // alias
})

// Laravel 10 and earlier  app/Http/Kernel.php
protected $routeMiddleware = [
    'auth'     => \App\Http\Middleware\Authenticate::class,
    'loggedin' => \App\Http\Middleware\CheckLoggedIn::class,
];
```

**Creating one:** `php artisan make:middleware CheckLoggedIn` writes `app/Http/Middleware/CheckLoggedIn.php`. Then attach it.

**(b) A protected route and the request flow [6]**

```php
<?php
// routes/web.php
Route::get('/dashboard', [DashboardController::class, 'index'])->middleware('auth');

// or with your own alias
Route::get('/students', [StudentController::class, 'index'])->middleware('loggedin');
?>
```
```php
// the controller is only reached when the check passes
public function index()
{
    $students = Student::all();
    return view('students.index', compact('students'));
}
```

**The flow, numbered — write it like this:**
1. Browser sends `GET /dashboard`.
2. `public/index.php` boots the app; the **router matches** the URI to the route.
3. The router assembles the route's **middleware stack** (global → group → route) and pushes the request through it, outermost first.
4. `auth` runs **before** the controller. Not logged in ⇒ it returns a redirect to `/login`; the controller is never constructed. Logged in ⇒ it calls `$next($request)`.
5. The **controller method** runs, queries the **model**, and returns a `view()`.
6. The response travels back **out** through the same middleware in reverse, so each can modify headers/content.
7. The response reaches the browser.

**Why it is separate from the controller `5:p16`:** so the same check is not repeated inside every controller method that needs it. One line on the route, one class, impossible to forget when a new method is added — and it can be removed or reordered globally without touching a single controller. That is the *justification mark*; do not skip it.

##### Traps
- Writing a middleware that *is* the login check but forgetting `return $next($request)` on the success path — the request dies silently and you get a blank page.
- Saying middleware "runs after the controller". It runs **before**, and optionally also after (around it).
- Confusing middleware with a **guard** or with **authorisation policies** — middleware filters the *request*; a policy decides about a *specific record*.
- Registering in `Kernel.php` on Laravel 11 (the file no longer exists) or in `bootstrap/app.php` on Laravel 8. Say "depending on version" and give both — safe.
- Attaching middleware *inside* the controller's constructor in modern Laravel — that was removed in Laravel 11; attach it on the route.

---

#### B7 — Controllers, resource controllers, third-party packages
**Covers:** Q257 (8+6) · Q275 (controller half) · Q157 at 3 marks (A18) · Q138 (A9).

**Variants and their delta:**

- **Q257(a)** [8] — benefits of resource controllers + convention-based routing. Add the 7-action table.
- **Q257(b)** [6] — third-party packages extending routing/middleware. Add §B7.4 — this half is **not in the deck**.
- **Q275** — routing + middleware + controllers *and* "design a route protected by middleware handled by a controller". Combine §B5 + §B6 + one controller method.

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | What a controller is; why not closures | 2 |
| (a) 2 | Resource controller + `--resource` + `Route::resource` | 2 |
| (a) 3 | The seven actions table | 3 |
| (a) 4 | Benefits: convention, less code, predictability | 1 |
| (b) 1 | How packages plug in (Composer + service provider) | 2 |
| (b) 2 | Packages that add routes / middleware | 2 |
| (b) 3 | How to use them well (middleware groups, route prefixes, config publish) | 2 |

##### Full answer

**(a) Controllers [8]**

A controller groups related request-handling logic into one class, so `routes/web.php` stays short and readable `5:p15`. `php artisan make:controller StudentController` scaffolds the file into `app/Http/Controllers/`; each public method typically handles one route; and a method usually ends by returning a **view** or a **redirect** `5:p15`.

```php
<?php
namespace App\Http\Controllers;

use App\Models\Student;

class StudentController extends Controller
{
    public function index()
    {
        $students = Student::all();
        return view('students.index', compact('students'));
    }
}
```

A **resource controller** goes further: it is a controller whose seven methods and route names follow a fixed RESTful convention for one resource. It is generated with the `--resource` flag and wired with a single line:

```bash
php artisan make:controller StudentController --resource
```
```php
Route::resource('students', StudentController::class);
```

**The seven actions (memorise this table — it is 3 of the 8 marks):**

| # | Method | Verb | URI | Name | Job |
|---|---|---|---|---|---|
| 1 | `index()` | GET | `/students` | `students.index` | list all |
| 2 | `create()` | GET | `/students/create` | `students.create` | show empty form |
| 3 | `store()` | POST | `/students` | `students.store` | insert + redirect |
| 4 | `show()` | GET | `/students/{student}` | `students.show` | display one |
| 5 | `edit()` | GET | `/students/{student}/edit` | `students.edit` | show filled form |
| 6 | `update()` | PUT/PATCH | `/students/{student}` | `students.update` | save changes |
| 7 | `destroy()` | DELETE | `/students/{student}` | `students.destroy` | delete |

**Benefits — the marks in (a)4:**
- **One line replaces seven.** `Route::resource(...)` generates all seven routes with the right verbs, so you cannot get a verb/URI pair wrong.
- **Convention over configuration.** Names are predictable (`students.edit` always exists), so `route()` and `redirect()->route()` calls can be written without looking anything up.
- **Uniform CRUD.** Every resource in the app — students, courses, departments — is structured identically, so a developer who has read one controller has read them all.
- **Trimmable.** `->only(['index','show'])` or `->except(['destroy'])` when a resource is read-only.
- **Consistent with REST.** The verb+URI pairs match what an API client or a JS `fetch()` expects.

**(b) Third-party packages and routing/middleware [6]** *(standard, not in your deck)*

Laravel packages are installed with Composer (`composer require vendor/package`) and auto-discovered through their **service provider**, which is the package's hook into the application: it can register bindings, publish config, load views, and — the part this question asks about — **register routes and middleware**.

1. **Packages that add routes.** A package ships its own route file and loads it from its provider:
```php
// inside the package's service provider
public function boot(): void
{
    $this->loadRoutesFrom(__DIR__.'/../routes/web.php');
    // or, to force a prefix + middleware on the package's routes:
    Route::middleware('web')
        ->prefix('admin')
        ->group(__DIR__.'/../routes/web.php');
}
```
This is exactly how a package like Laravel Breeze or Horizon exposes its screens — you install it and URLs appear, without touching your own `routes/web.php`.

2. **Packages that add middleware.** Either the package registers a global/group middleware, or it exposes an alias you attach yourself:
```php
// the package registers ...
$middleware->alias(['role' => \Spatie\Permission\Middleware\RoleMiddleware::class]);

// ... and you use it on your own routes
Route::get('/admin', [AdminController::class, 'index'])->middleware('role:admin');
```
Laravel Sanctum works exactly this way (`auth:sanctum`), as does `spatie/laravel-permission` (`role:`, `permission:`).

**Using them well:** prefer packages that ship a **service provider** (so config is publishable with `php artisan vendor:publish`), attach their middleware **by alias on the routes that need it** rather than globally, scope their routes behind your own `auth` middleware, and pin versions in `composer.json`. A package's global middleware runs on *every* request — including your login page — so the cheap, correct choice is route-level attachment.

##### Traps
- Mixing the **order** of `create` and `store`, or the verbs of `update`/`destroy`. `store` is POST to the collection; `update` is PUT to the member.
- Saying `Route::resource` creates a *controller*. It creates **routes**; `make:controller --resource` creates the controller.
- For Q257(b), answering with "Composer installs packages". That is 1 mark. The other 5 are **how routing and middleware are extended**: `loadRoutesFrom`, route groups with prefix/middleware, and middleware aliases.
- Forgetting `use App\Models\Student;` in the controller — the classic 500.

---

#### B8 — Route model binding · MASTER
**Covers:** Q276(a) (7) · Q285 (7+7) · Q262(b) (6) · Q270(b) (part) · Q137/Q158 at 3 marks (A8).

**Variants and their delta:**

- **Q262(b)** [6] — "what is route model binding + **which types** are supported": implicit and explicit, defined, with the 404 behaviour. Short, no views.
- **Q285** — (a) binding in detail + implicit vs explicit [7] (b) a controller method using a bound `Student` returning a Blade view [7]. Add the view file.
- **Q276** — the binding half of a hybrid; the example (display a student) is the same code as Q285(b).
- **Q270(b)** — differentiate GET / POST / binding: use table A15.
- **Q137** — implicit example only: three lines.

##### Structure
| Part | Content | Marks |
|---|---|---|
| 1 | Problem it solves (manual `find` + null-check repeated) | 1 |
| 2 | Implicit binding: `{student}` + `Student $student` | 2 |
| 3 | Automatic 404 when no row | 1 |
| 4 | Custom key (`{student:register_no}`, `getRouteKeyName()`) | 1 |
| 5 | Explicit binding via `Route::bind` | 2 |
| 6 | Controller method + Blade view | 1 |

##### Full answer

**(a) The concept and the two types [7]**

Consider the manual version first, because that is what binding replaces:

```php
// WITHOUT binding — repeated in every method that takes an id
public function show($id)
{
    $student = Student::find($id);
    if (! $student) {
        abort(404);
    }
    return view('students.show', compact('student'));
}
```
Three lines of ceremony, repeated in `show`, `edit`, `update`, `destroy`. Forget the `if` once and you get a "property on null" crash instead of a 404.

**Route model binding** makes Laravel do it: it automatically fetches the database record matching a route parameter and hands the model straight to the controller — no manual query `5:p18`. `{student}` is a placeholder in the URL, and **type-hinting the matching parameter as a Model** triggers an automatic lookup **by ID** `5:p18`. If no matching record exists, Laravel returns a **404 automatically** `5:p18`.

```php
<?php
Route::get('/student/{student}', [StudentController::class, 'show']);

public function show(Student $student)
{
    // $student is already the correct DB row
    return view('students.show', compact('student'));
}
?>
```

**Type 1 — implicit.** Nothing is declared: the parameter name `{student}` matches the type-hinted variable `$student`, and Laravel resolves `Student` by its primary key. That naming agreement *is* the binding. To bind on another column, either name the column in the route or override the model's key:

```php
// column in the route definition
Route::get('/student/{student:register_no}', [StudentController::class, 'show']);

// or, globally for this model
// app/Models/Student.php
public function getRouteKeyName(): string
{
    return 'register_no';
}
```

**Type 2 — explicit.** You declare the resolution yourself with `Route::bind()`, typically in `AppServiceProvider::boot()` (older versions: `RouteServiceProvider`). Use this when the lookup is not a simple key — a slug, a composite, a soft-deleted record, a tenant-scoped query:

```php
<?php
// app/Providers/AppServiceProvider.php
use App\Models\Student;
use Illuminate\Support\Facades\Route;

public function boot(): void
{
    Route::bind('student', function (string $value) {
        return Student::where('register_no', $value)->firstOrFail();
    });
}
```
`firstOrFail()` throws `ModelNotFoundException`, which Laravel renders as a 404 — the same behaviour implicit binding gives you for free.

**The difference in one table:**

| | Implicit | Explicit |
|---|---|---|
| Declared by | parameter name + type-hint | `Route::bind('param', fn)` |
| Where | the route + the method signature | a service provider |
| Key | primary key, or `{param:column}` | anything you write |
| Use when | 90% of cases — plain `id` lookups | slugs, composite keys, scoped queries |

**(b) Controller method + view [7]**

```php
<?php
// routes/web.php
use App\Http\Controllers\StudentController;
Route::get('/student/{student}', [StudentController::class, 'show'])->name('students.show');
?>
```
```php
<?php
// app/Http/Controllers/StudentController.php
namespace App\Http\Controllers;

use App\Models\Student;

class StudentController extends Controller
{
    public function show(Student $student)
    {
        return view('students.show', compact('student'));
    }
}
?>
```
```blade
{{-- resources/views/students/show.blade.php --}}
@extends('layout')

@section('content')
    <h2>{{ $student->name }}</h2>
    <p>Register No: {{ $student->register_no }}</p>
    <p>Mark: {{ $student->mark }}</p>

    @if ($student->mark >= 40)
        <p class="pass">Pass</p>
    @else
        <p class="fail">Fail</p>
    @endif

    <a href="{{ route('students.index') }}">Back to list</a>
@endsection
```
The controller contains **no query at all** — the type-hint did the work, and an invalid URL like `/student/9999` produces a clean 404 without a single line of error handling.

**Why it beats manual `find()` (the justification mark):** it removes a *repeated* three-line pattern, it makes the null-check **impossible to forget** (so a missing row is a 404, not a crash), and it keeps the controller method's signature self-documenting — `show(Student $student)` states exactly what the method needs.

##### Traps
- Parameter name and variable name must **match** for implicit binding: `{student}` with `Student $student`. `{id}` with `Student $student` does **not** bind — it injects the raw string.
- Type-hinting `$id` as `int` and expecting binding. Binding requires the **model** type-hint.
- Putting `Route::bind` in `routes/web.php` — it belongs in a service provider's `boot()`.
- Saying binding "checks permissions". It only *fetches*; authorisation is a policy/gate.
- For explicit binding, forgetting `firstOrFail()` — `first()` returns `null` and you are back to a null crash.

---

#### B9 — Views, passing data, sharing data, redirections · MASTER
**Covers:** Q259 (10+4) · Q263(b) (6) · Q276 (redirect half) · Q156–159 at 3 marks (A19).

**Variants and their delta:**

- **Q259(a)** [10] — the view system: creating views, `view()`, passing data (3 ways), controllers returning views, **closures vs controllers**.
- **Q259(b)** [4] — redirections: basic, with input, flash, named routes.
- **Q263(b)** [6] — (a) creating and rendering views (b) passing data (c) **sharing data with all views**. Part (c) is `View::share` / a view composer — *not* in the deck.
- **Q276(b)** [7] — display a student via binding, then **redirect to the list after saving**. Code below.

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | What a view is; where files live; dot notation | 2 |
| (a) 2 | `view()` — three ways to pass data (`['k'=>'v']`, `with()`, `compact()`) | 3 |
| (a) 3 | Controller returning views; closures vs controllers | 3 |
| (a) 4 | Sharing data with all views (`View::share`, composers) | 2 |
| (b) 1 | `redirect()`, `back()`, `route()` | 2 |
| (b) 2 | Flash data with `->with()` + `@if(session(...))` | 2 |

##### Full answer

**(a) The view system [10]**

A view is the **presentation layer**: a template that renders HTML from data it is handed. In Laravel views live in `resources/views/` and are named `*.blade.php` `5:p19`. `view('name', $data)` renders one, passing it data `5:p19`.

**Creating a view** is just creating a file:
```text
resources/views/students/index.blade.php     →  view('students.index')
resources/views/students/show.blade.php      →  view('students.show')
resources/views/layout.blade.php             →  view('layout')
```
**Dot notation maps to folders** `5:p19`: `students.index` means `resources/views/students/index.blade.php`. The dot is a *directory separator*, not part of the filename — this is asked often and answered wrong often.

**Passing data — three equivalent forms:**
```php
<?php
// 1. explicit associative array
return view('students.index', ['students' => $students, 'title' => 'All Students']);

// 2. compact() — builds ['students' => $students] from the variable's own name
return view('students.index', compact('students'));

// 3. with() chained on the view instance
return view('students.index')->with('students', $students);
?>
```
`compact('students')` is a shortcut that bundles a variable into an array keyed by its own name `5:p19`. Inside the template, each array key becomes a PHP variable: `['students' => $students]` is `$students` in the view.

**The controller's job here** — and this is the sentence to write: *a controller's most common job is choosing a view and handing it the data it needs* `5:p19`:
```php
public function index()
{
    $students = Student::all();
    return view('students.index', compact('students'));
}
```

**Closures vs controllers for rendering views:**

| | Closure in `routes/web.php` | Controller method |
|---|---|---|
| Where the logic lives | in the route file | in a class |
| Fine for | a one-line landing page, a quick prototype | anything with logic, queries, validation |
| Testable | no (anonymous function) | yes (instantiate and call) |
| Cacheable | no — `route:cache` refuses closures | yes |
| Reusable | no | yes — many routes can use one method |
| Grows well | no: 40 routes × inline logic = an unmaintainable file `5:p15` | yes |

```php
// closure — acceptable only for something this small
Route::get('/', function () { return view('welcome'); });

// controller — the normal choice
Route::get('/students', [StudentController::class, 'index']);
```
The deck's framing is that controllers exist to keep `routes/web.php` short and readable `5:p15` — use that as the justification.

**Sharing data with ALL views (Q263(b)c — standard, not in your deck):** when every page needs the same value (college name, nav menu, unread-count), do not pass it from every controller. Share it once in a service provider:
```php
<?php
// app/Providers/AppServiceProvider.php  -> boot()
use Illuminate\Support\Facades\View;

public function boot(): void
{
    View::share('collegeName', 'Saintgits College of Engineering');

    // or lazily, only for certain views, via a composer
    View::composer(['students.*', 'layout'], function ($view) {
        $view->with('departments', \App\Models\Department::all());
    });
}
```
`View::share` makes `$collegeName` available in **every** Blade template with no controller involvement; a **view composer** does the same but scoped to named views and executed only when they render.

**(b) Redirections [4]**

Not every controller method ends in a view — after a form submission, redirecting is usually the right move `5:p20`.

```php
<?php
// 1. basic — to a path
return redirect('/students');

// 2. to a named route (preferred: survives URL changes)
return redirect()->route('students.index');

// 3. back to the previous page — common after failed validation
return back()->withInput()->withErrors(['mark' => 'Mark must be 0-100']);

// 4. with flash data — available on the NEXT request only
return redirect()->route('students.index')->with('success', 'Student saved');

// 5. the deck's own store() example
public function store(Request $request) {
    Student::create($request->all());
    return redirect('/students')
        ->with('message', 'Student added successfully!');
}
?>
```
**Flash data** is written to the session for exactly one subsequent request `5:p20`. Read it in Blade:
```blade
@if (session('success'))
    <div class="alert alert-success">{{ session('success') }}</div>
@endif
```
Because it is consumed on read, a refresh does not show it twice — which is precisely what you want for "Saved" messages.

**Why redirect after POST `5:p20`:** *"redirecting after a successful POST prevents accidental duplicate form resubmission."* This is the POST/Redirect/GET pattern: the browser's final request is a GET, so F5 re-fetches the list instead of re-inserting the student.

**For Q276(b) — display via binding, redirect to the list after saving:**
```php
<?php
// routes
Route::get('/student/{student}', [StudentController::class, 'show'])->name('students.show');
Route::put('/student/{student}', [StudentController::class, 'update'])->name('students.update');
?>
```
```php
<?php
public function show(Student $student)          // binding fetches the row, or 404s
{
    return view('students.show', compact('student'));
}

public function update(Request $request, Student $student)
{
    $validated = $request->validate([
        'name' => 'required|string|max:100',
        'mark' => 'required|numeric|min:0|max:100',
    ]);

    $student->update($validated);

    return redirect()->route('students.index')->with('success', 'Student updated');
}
?>
```

##### Traps
- `view('students.index.php')` — the extension is never part of the view name, and dots are folder separators, so that name looks for a *folder* called `students`.
- Passing data as `view('x', $students)` (a bare collection). The second argument must be an **array keyed by variable name**.
- Claiming flash data persists. It survives **one** request only.
- Using `redirect('/students')` everywhere and then renaming the URL — 30 broken strings. Named routes exist for this.
- Answering Q263(b)c with "pass it from every controller". The question says *all* views: `View::share` or a composer.

---

#### B10 — Blade: inheritance, echoing, control structures · MASTER (highest-frequency Part B theme)
**Covers:** Q260(b) (7) · Q265(b) (9) · Q277 (7+7) · Q286 (7+7) · Q136/Q159/Q160 at 3 marks (A7, A19, A20).

**Variants and their delta:**

- **Q260(b)** [7] — **inheritance only**: base layout, `@extends`, `@section`, `@yield`, `@include`. Add §B10.1.
- **Q265(b)** [9] — "key features: template inheritance, directives, conditionals, loops, **data binding**". Five named things ⇒ five short blocks. Add the components line.
- **Q277** — (a) echoing + control structures [7] (b) a view showing a student's name with **pass/fail** and a **loop over subjects** [7].
- **Q286** — (a) echoing, conditionals, iteration with examples [7] (b) student details, "Pass" when mark ≥ 40 [7]. Same code as Q277(b).
- **Q136** — `@extends` purpose + example (3 marks): A7.

##### Structure
| Part | Content | Marks |
|---|---|---|
| 1 | What Blade is + `.blade.php` + compiles to cached PHP | 2 |
| 2 | Echoing: `{{ }}` vs `{!! !!}`, escaping, `{{-- --}}` | 2 |
| 3 | Conditionals: `@if/@elseif/@else/@endif`, `@unless`, `@isset`, `@empty` | 2 |
| 4 | Loops: `@foreach`, `$loop` | 2 |
| 5 | Inheritance: `@extends/@section/@yield/@include` with both files | 3 |

##### Full answer

**(a) What Blade is and how it echoes [9]**

Blade is Laravel's templating engine. It lets you write clean, readable directives (`@if`, `@foreach`) directly inside HTML instead of switching in and out of `<?php ?>` blocks `5:p22`. Templates are compiled into ordinary PHP and cached, so there is **no real performance cost** compared with hand-written PHP; the file extension `.blade.php` is how Laravel knows to compile it `5:p22`. Every `view()` call renders one of these files.

**Echoing — the security-critical choice `5:p23`:**

| Syntax | Behaviour |
|---|---|
| `{{ $variable }}` | echoes, **automatically escaped** — safe against XSS |
| `{!! $variable !!}` | echoes **raw, unescaped** HTML — trusted content only |
| `{{-- comment --}}` | Blade comment, never rendered |

```blade
<h2>Welcome, {{ $student->name }}</h2>
<p>{{ $bio ?? 'No bio provided.' }}</p>
{!! $trustedHtmlBlock !!}
{{-- This comment never reaches the browser --}}
```
`{{ }}` compiles to `echo htmlspecialchars($value)`. If `$student->name` were `<script>alert(1)</script>`, `{{ }}` prints it as visible text while `{!! !!}` would execute it — which is why the escaped form is the default and the raw form must be a deliberate decision `5:p28`. Blade also allows any PHP expression inside the braces: `{{ $name ?? 'Guest' }}`, `{{ count($students) }}`, `{{ number_format($mark, 2) }}`.

**(b) Conditionals [2]**

```blade
@if (count($students) > 0)
    <p>{{ count($students) }} students found.</p>
@elseif ($searched)
    <p>No matches for your search.</p>
@else
    <p>No students yet.</p>
@endif

@unless ($isLoggedIn)
    <a href="/login">Please log in</a>
@endunless
```
`@if/@elseif/@else/@endif` is standard branching; `@unless ... @endunless` runs when the condition is **false** (the inverse of `@if`); `@isset` and `@empty` test set-and-not-null and emptiness respectively `5:p24`. They all compile to plain PHP `if`/`else`.

**(c) Loops [2]**

```blade
<ul>
@foreach ($students as $s)
    <li>
        {{ $loop->iteration }}. {{ $s->name }}
        @if ($loop->last) (last student) @endif
    </li>
@endforeach
</ul>
```
`@foreach($items as $item) ... @endforeach` is the most common loop in views; `@for(...)` and `@while(...)` also exist `5:p25`. Inside `@foreach`, `$loop` is available automatically with `index` (0-based), `iteration` (1-based), `first`, `last`, `count` and `remaining` `5:p25` — which removes the manual counter and the off-by-one "is this the last item" bug.

**(d) Template inheritance [3]**

Rather than repeating header/footer markup on every page, Blade lets a child view inherit a shared layout `5:p26`. Four directives:

| Directive | Role |
|---|---|
| `@extends('layout')` | declares the parent layout this view inherits |
| `@section('name') ... @endsection` | defines a named block of content |
| `@yield('name')` | **in the parent** — marks where a child's section is inserted |
| `@include('partial')` | pulls in a reusable chunk from another file |

```blade
{{-- resources/views/layout.blade.php  — THE PARENT --}}
<!DOCTYPE html>
<html>
<head><title>@yield('title', 'Student Portal')</title></head>
<body>
    @include('partials.navbar')
    <main>
        @yield('content')
    </main>
    <footer>&copy; Saintgits CSE</footer>
</body>
</html>
```
```blade
{{-- resources/views/students/index.blade.php  — THE CHILD --}}
@extends('layout')

@section('title', 'Student List')

@section('content')
    <h2>Student List</h2>
    <ul>
    @foreach ($students as $s)
        <li>{{ $s->name }} — {{ $s->mark }}</li>
    @endforeach
    </ul>
@endsection
```
`@extends` must be the **first** Blade construct in the child. `@yield` can take a default (`@yield('title', 'Student Portal')`). `@section('name', 'value')` is the one-line form. `@include` is *not* inheritance — it pastes a fragment in with no parent/child relationship, which is exactly what you want for a navbar.

**(e) The pass/fail view the paper keeps asking for (Q277b, Q286b) [7]**

```blade
{{-- resources/views/students/result.blade.php --}}
@extends('layout')

@section('content')
    <h2>{{ $student->name }}</h2>
    <p>Register No: {{ $student->register_no }}</p>
    <p>Mark: {{ $student->mark }}</p>

    @if ($student->mark >= 40)
        <p class="pass">Result: PASS</p>
    @else
        <p class="fail">Result: FAIL</p>
    @endif

    <h3>Subjects</h3>
    <ul>
    @foreach ($student->subjects as $subject)
        <li>
            {{ $loop->iteration }}. {{ $subject->name }} — {{ $subject->mark }}
        </li>
    @endforeach
    </ul>
@endsection
```
If the marks arrive as a plain array, use `@forelse` (standard, not in your deck) so an empty list renders a message instead of nothing:
```blade
@forelse ($marks as $m)
    <li>{{ $m }}</li>
@empty
    <li>No marks recorded.</li>
@endforelse
```
And if the calculation belongs in code rather than markup, `@php ... @endphp` allows it — but prefer computing the result in the controller and passing `$result`, because a view should render, not decide.

##### Traps
- Using `{!! !!}` for user-supplied data. This is an instant "security" deduction and the deck flags it twice `5:p23`, `5:p28`.
- Writing `@extends` after other content, or `@endsection` missing — both produce confusing blank pages.
- Confusing `@section` (child defines) with `@yield` (parent inserts). Getting this backwards is the most common inheritance error.
- Using `<?php foreach ... ?>` inside a Blade file. It works, but it is what Blade exists to replace, and a "use Blade directives" instruction is implicit in every one of these questions.
- Using `$loop` **outside** `@foreach` — it is only defined inside the loop.
- Forgetting that `{{-- --}}` differs from `<!-- -->`: the HTML comment **is** sent to the browser.

---

#### B11 — Sub-domain routing · 7 marks (Q260a)
**Status:** *(standard, not in your deck — no slide covers sub-domains.)*

##### Structure
| Part | Content | Marks |
|---|---|---|
| 1 | What sub-domain routing is; `Route::domain()` | 2 |
| 2 | Code: fixed sub-domain + parameterised sub-domain | 2 |
| 3 | Two full use cases | 2 |
| 4 | Caveats: ordering, wildcard DNS, HTTPS/cookies | 1 |

##### Full answer

Sub-domain routing lets a **single application** serve different host names with different route tables. The host is matched as part of the route definition, so the router — not your controller — decides which module answers the request.

```php
<?php
use Illuminate\Support\Facades\Route;

// 1. a fixed sub-domain (admin panel)
Route::domain('admin.college.test')->group(function () {
    Route::get('/dashboard', [AdminController::class, 'index'])->name('admin.dashboard');
});

// 2. a parameterised sub-domain (multi-tenant / per-department)
Route::domain('{department}.college.test')->group(function () {
    Route::get('/students', [StudentController::class, 'index'])
        ->name('dept.students.index')
        ->middleware('auth');
});

// 3. combined with prefix + name prefix
Route::domain('{account}.myapp.test')
    ->prefix('api')
    ->name('api.')
    ->middleware('api')
    ->group(function () {
        Route::get('/users', [UserController::class, 'index'])->name('users.index');
    });
?>
```
The `{department}` placeholder in the domain is captured exactly like a URI parameter and can be type-hinted in the controller (`index(string $department)`), or used in a `Route::bind` to scope every query to that tenant.

**Common use cases:**
1. **Multi-tenant SaaS** — each customer gets `customer.app.com`; one codebase, one database (or one schema per sub-domain), isolation enforced in the route layer so a tenant can never address another tenant's data by URL.
2. **Separate administrative surface** — `admin.` vs the public site: different middleware stack, different views, and (typically) IP restriction or stronger auth on the admin host.
3. **Per-department / per-campus portals** — `cse.college.test`, `ece.college.test`, each rendering its own students with the same controller.
4. **Localisation** — `en.`, `fr.` — the sub-domain selects the locale in middleware.

**Caveats that earn the last mark:** the domain group must be defined with the parameter available before it is used; local development needs a hosts-file entry or a wildcard DNS record (`*.test` resolves to 127.0.0.1 with Valet/dnsmasq); and cookies/sessions must be scoped so they are not shared across tenants (`SESSION_DOMAIN`), otherwise a login on one sub-domain leaks to another. Sub-domain routing is **not** a substitute for authorisation — it decides *which routes exist*, and each route still needs its own check.

##### Traps
- Forgetting that `Route::domain()` takes a **host**, not a path — `Route::domain('/admin')` is wrong.
- Assuming the sub-domain parameter is a security boundary. It is routing, not authorisation.
- No fallback plan for local testing — say "hosts file or wildcard DNS", it is a real mark.

---

#### B12 — The HTTP request lifecycle, route → middleware → controller → response · 5 marks (Q265a)
**Status:** the six-step chain is in the deck `5:p21`; the front-controller detail is standard.

##### Structure
| Part | Content | Marks |
|---|---|---|
| 1 | Entry: `public/index.php`, router matches URL + verb | 1 |
| 2 | Middleware pipeline runs, may short-circuit | 1 |
| 3 | Controller runs; model binding fetches data | 1 |
| 4 | Controller returns `view()` or `redirect()` | 1 |
| 5 | Response travels back out and reaches the browser | 1 |

##### Full answer

Every request in a Laravel application takes the same path `5:p21`:

```text
Browser: GET /student/5
   │
   ▼
1. public/index.php            front controller — boots the framework, loads routes
   │
   ▼
2. Router                      matches GET + /student/{student}  ──no match──▶ 404
   │
   ▼
3. Middleware pipeline         auth, session, CSRF, log ...      ──fail──────▶ redirect('/login')
   │  (each may act before AND after)
   ▼
4. Controller@show             StudentController::show(Student $student)
   │     └─ Route model binding: SELECT * FROM students WHERE id = 5 ──none──▶ 404
   ▼
5. view()  ──or──  redirect()  Blade compiled + cached, rendered to HTML
   │
   ▼
6. Response                    travels back out through the middleware (headers may change)
   │
   ▼
Browser receives 200 OK
```

**Stage by stage:**
1. **Front controller.** Apache/Nginx is pointed at `public/`, so *every* URL arrives at `public/index.php`. It bootstraps the framework (config, service providers, error handling) and hands the request to the HTTP kernel.
2. **Routing.** The router matches the request's **method + URI** against the route table in `routes/web.php`, honouring constraints. No match ⇒ 404 before any of your code runs.
3. **Middleware.** The matched route's middleware stack (global → group → route) runs around the request. `auth` may stop an unauthenticated request here, and the controller is never invoked `5:p16`. Each middleware can act *before* calling `$next($request)` and *after* it returns.
4. **Controller + model.** The container resolves the controller and calls the method. Type-hinted route parameters are resolved by **route model binding** — the DB row is fetched, or a 404 is returned `5:p18`. The method then calls the **model** for whatever else it needs.
5. **The branch `5:p21`.** A **GET** that shows data ends in `view()`, which renders the Blade template (compiled to PHP and cached). A **POST** that changes data ends in `redirect()`, optionally with flash data — POST/Redirect/GET, so a refresh cannot duplicate the write `5:p20`.
6. **Response.** The response object travels back out through the same middleware in reverse, so any layer can add headers or modify the body, then it is sent to the browser.

The one-sentence version to open with: *Laravel funnels every request through a single front controller, matches it to a route, filters it through middleware, dispatches it to a controller that talks to models, and returns either a rendered view or a redirect — with each layer replaceable and each concern in one place.*

##### Traps
- Starting the answer at the controller. The route match happens **first**, and it is a mark.
- Saying middleware runs after the controller only. It wraps the controller — before *and* after.
- Forgetting that a 404 can come from **two** places: no route match, or a failed model binding.
- Missing the GET→view / POST→redirect branch, which the deck states explicitly `5:p21`.

---

#### B13 — Service providers and migrations · 10 + 4 (Q256)
**Status:** *(standard, not in your deck — neither topic has a slide. Answer it from general Laravel knowledge and do not claim the deck.)*

##### Structure
| Part | Content | Marks |
|---|---|---|
| (a) 1 | What a service provider is; the bootstrapping unit | 2 |
| (a) 2 | `register()` vs `boot()` — and why the split exists | 2 |
| (a) 3 | Role in the lifecycle: config → register all providers → boot | 2 |
| (a) 4 | Dependency injection: binding into the container | 2 |
| (a) 5 | A worked provider + a consumer | 2 |
| (b) 1 | What a migration is; why version the schema | 2 |
| (b) 2 | A migration class (`up`/`down`) + commands | 2 |

##### Full answer

**(a) Service providers [10]**

A **service provider** is the class where a Laravel application is *assembled*. Everything the framework ships — the router, the database layer, the queue, the view engine — is registered by a provider, and your own `app/Providers/AppServiceProvider.php` is the place to register yours. Laravel reads the provider list in `bootstrap/providers.php` (Laravel 11+) or `config/app.php` (earlier), instantiates each one, and calls two methods:

```php
<?php
namespace App\Providers;

use App\Services\ReportService;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    // 1. register(): bind things into the container. No other provider may be assumed ready.
    public function register(): void
    {
        $this->app->bind(ReportService::class, function ($app) {
            return new ReportService($app['config']['reports.key']);
        });
    }

    // 2. boot(): everything is registered — safe to use other services, routes, views, events.
    public function boot(): void
    {
        \Illuminate\Support\Facades\View::share('collegeName', 'Saintgits College of Engineering');
        \Illuminate\Support\Facades\Route::pattern('id', '[0-9]+');
    }
}
```

**`register()` vs `boot()` — the distinction that earns marks.** `register()` runs for **all** providers first, then `boot()` runs for all of them. So inside `register()` you may only *bind* things; you must not assume another provider's bindings exist. Inside `boot()` everything is available, so that is where you touch routes, views, events, Blade directives and migrations. Binding in `boot()` works but is fragile — the container resolves lazily, so a binding registered late may be missed by something that already asked for it.

**Role in the lifecycle:**

```text
composer autoload → bootstrap/app.php → load config (.env)
   → register all providers' register()   [bindings only]
   → boot all providers' boot()           [routes, views, events, directives]
   → handle the request (route → middleware → controller)
   → send the response → terminate (terminable middleware, queued work)
```

**Dependency injection and service management.** The **service container** is a keyed map of "how to build this class". A provider fills that map; the framework reads it whenever a controller, middleware or job type-hints a dependency:

```php
// binding — one interface, one implementation
$this->app->bind(
    \App\Contracts\PaymentGateway::class,
    \App\Services\RazorpayGateway::class
);

// singleton — one shared instance for the whole request
$this->app->singleton(\App\Services\ReportService::class);

// then, anywhere — no `new`, no config lookup:
public function __construct(private ReportService $reports) {}
```
That is the point: the controller asks for an abstraction and the provider decides the concrete class. Swapping Razorpay for Stripe becomes a **one-line provider change** with no controller edits — and in tests you bind a fake instead. This is what "facilitate dependency injection and service management" means in the question.

Deferred providers (implementing `DeferrableProvider`) register only when their binding is actually requested — a performance detail worth one clause.

**(b) Migrations [4]**

A **migration** is a version-controlled PHP file that describes one change to the database schema — creating a table, adding a column, adding an index. It is to schema what Git is to code: the schema is reproducible on any machine, reviewable in a pull request, and reversible.

```bash
php artisan make:migration create_students_table
php artisan migrate          # apply all pending migrations
php artisan migrate:rollback # undo the last batch (runs down())
php artisan migrate:fresh    # drop everything and re-run (dev only)
```

```php
<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('students', function (Blueprint $table) {
            $table->id();
            $table->string('register_no')->unique();
            $table->string('name');
            $table->integer('mark')->default(0);
            $table->timestamps();          // created_at, updated_at
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('students');
    }
};
```
`up()` applies the change; `down()` reverses it — which is why a migration must always be reversible. Laravel records which migrations have run in the `migrations` table, so `migrate` is idempotent: it only runs the ones not yet recorded. A model and its migration are usually generated together with `php artisan make:model Student -m`.

##### Traps
- Saying providers "run on every request to handle routing". They **bootstrap**; the router is one of the things they register.
- Putting route/view/event code in `register()`. It belongs in `boot()`.
- Calling a migration a "database backup" or "seeder". A migration changes **schema**; a seeder inserts **data**.
- Omitting `down()` — a migration that cannot be rolled back is a defect.
- Writing raw `CREATE TABLE` SQL instead of `Schema::create` when the question says "Laravel migrations".

---

## 4. PART 3 — Code you must write by hand

Fourteen drills. Do each one **on paper, from memory**, then check. If you can write these cold you can answer every code-bearing question in the bank (Q131, 137, 254, 262–286). Each drill ends with the one line worth memorising.

---

### D1 — A valid JSON student document
**Task:** one student, with a nested address, a marks array, and every JSON type represented at least once.

```json
{
  "registerNo": "SJC22CS001",
  "name": "Anu Thomas",
  "semester": 7,
  "hostel": false,
  "email": null,
  "address": {
    "city": "Kottayam",
    "pin": "686532"
  },
  "marks": [
    { "subject": "Web Programming", "mark": 88 },
    { "subject": "DBMS", "mark": 76 }
  ]
}
```
Six types check: string, number, boolean, null, object, array — all present. Root is an object; no trailing comma; every key double-quoted.

**Memorise:** `{ }` = object, `[ ]` = array, keys are double-quoted, and **the type is in the value, not in quotes**.

---

### D2 — Nested college → departments → students
**Task:** three levels, the Q278(b) shape. Count the brackets before you write.

```json
{
  "college": "Saintgits College of Engineering",
  "departments": [
    {
      "code": "CSE",
      "students": [
        { "registerNo": "SJC22CS001", "name": "Anu", "mark": 88 },
        { "registerNo": "SJC22CS002", "name": "Rahul", "mark": 72 }
      ]
    },
    {
      "code": "ECE",
      "students": [
        { "registerNo": "SJC22EC011", "name": "Meera", "mark": 91 }
      ]
    }
  ]
}
```

**Memorise:** *object → array of objects → array of objects*; each `[` gets its `]`, each `{` its `}`, and students live **inside** their department, never beside it.

---

### D3 — JSON Schema for a student: required fields + mark bounds
**Task:** required `registerNo`, `name`, `mark`; mark 0–100; subjects an array of strings; nothing extra allowed.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/student.json",
  "title": "Student",
  "type": "object",
  "required": ["registerNo", "name", "mark"],
  "properties": {
    "registerNo": { "type": "string" },
    "name":       { "type": "string", "minLength": 2 },
    "mark":       { "type": "number", "minimum": 0, "maximum": 100 },
    "subjects":   { "type": "array", "items": { "type": "string" } }
  },
  "additionalProperties": false
}
```

**Memorise:** `"required"` is an **array of names at the object level**; `properties` holds a sub-schema per key; `minimum`/`maximum` sit inside the number's schema, not at the root.

---

### D4 — Course-credits schema (credits 1–6)
**Task:** Q280(b) verbatim. `code`, `title`, `credits` all required; credits an integer 1–6.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/course.json",
  "type": "object",
  "required": ["code", "title", "credits"],
  "properties": {
    "code":    { "type": "string", "pattern": "^[0-9]{2}[A-Z]{4}[0-9]{3}$" },
    "title":   { "type": "string" },
    "credits": { "type": "integer", "minimum": 1, "maximum": 6 }
  },
  "additionalProperties": false
}
```
Test yourself against instances: `{"code":"20CST461","title":"WP","credits":4}` → valid. `credits: 0` → fails `minimum`. `credits: 7` → fails `maximum`. `credits: "4"` → fails `type`. `credits: 4.5` → fails `integer`.

**Memorise:** `"integer"`, not `"int"`; bounds are **inclusive**; a missing required key fails at the *root* path, not the property path.

---

### D5 — PHP decode → modify → re-encode
**Task:** Q131/Q273(b). Decode, bump the mark, add a computed result, re-encode pretty, and handle a parse error.

```php
<?php
$json = '{"registerNo":"SJC22CS001","name":"Anu","mark":72,"subjects":["WP","DBMS"]}';

$student = json_decode($json, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    die("Invalid JSON: " . json_last_error_msg());
}

$student["mark"]   = 88;
$student["result"] = $student["mark"] >= 40 ? "Pass" : "Fail";

echo json_encode($student, JSON_PRETTY_PRINT);
?>
```
Output:
```json
{
    "registerNo": "SJC22CS001",
    "name": "Anu",
    "mark": 88,
    "subjects": ["WP", "DBMS"],
    "result": "Pass"
}
```

**Memorise:** `json_decode($json, true)` → `["key"]`; `json_encode($data, JSON_PRETTY_PRINT)` → string; **always** the `json_last_error()` check.

---

### D6 — Encode an associative array of employees, then decode it back
**Task:** Q268(b). Two employees, encode, then decode and print — proving the round trip.

```php
<?php
$employees = [
    ["id" => 1, "name" => "Anu",   "department" => "CSE", "salary" => 55000],
    ["id" => 2, "name" => "Rahul", "department" => "ECE", "salary" => 48000],
];

$json = json_encode($employees, JSON_PRETTY_PRINT);
echo $json;

$decoded = json_decode($json, true);

foreach ($decoded as $e) {
    echo $e["id"] . " | " . $e["name"] . " | " .
         $e["department"] . " | " . $e["salary"] . PHP_EOL;
}

var_dump($decoded === $employees);   // bool(true)
?>
```
Note the shape: an **indexed** array of **associative** arrays → a JSON **array of objects**. That is the most common real payload there is.

**Memorise:** indexed array → `[ ]`, associative array → `{ }`, and the round trip is value-identical (`===` is `true`) for scalars.

---

### D7 — `JSON.parse()` / `JSON.stringify()` demo
**Task:** Q262(a). String → object, mutate, object → string, then a `fetch` round trip.

```javascript
// 1. JSON text -> JS object
const text = '{"registerNo":"SJC22CS001","name":"Anu","marks":[88,76]}';
const student = JSON.parse(text);

console.log(student.name);        // Anu
console.log(student.marks[1]);    // 76

// 2. mutate like any object
student.marks.push(91);
student.total = student.marks.reduce((a, b) => a + b, 0);

// 3. JS object -> JSON text
const out = JSON.stringify(student);
console.log(out);
// {"registerNo":"SJC22CS001","name":"Anu","marks":[88,76,91],"total":255}

// 4. pretty
console.log(JSON.stringify(student, null, 2));

// 5. the real use: a network boundary
fetch('/api/students/1')
  .then(res => res.json())          // parses the response body
  .then(s => console.log(s.name));
```
**Output of step 3 exactly:** `{"registerNo":"SJC22CS001","name":"Anu","marks":[88,76,91],"total":255}`

**Memorise:** `JSON.parse(string) → object`, `JSON.stringify(object) → string`; parse **throws** on bad JSON, stringify **drops** `undefined` and functions and turns `Date` into a string.

---

### D8 — A routes file: GET, POST, named, parameterised, constrained, grouped
**Task:** the route table for a student resource, written by hand.

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StudentController;

// closure route
Route::get('/', function () {
    return "Welcome to Saintgits CSE";
});

// named, parameterised, constrained
Route::get('/students', [StudentController::class, 'index'])->name('students.index');
Route::get('/student/{id}', [StudentController::class, 'show'])
    ->where('id', '[0-9]+')
    ->name('students.show');

// the form pair
Route::get('/students/create', [StudentController::class, 'create'])->name('students.create');
Route::post('/students', [StudentController::class, 'store'])->name('students.store');

// update + delete (browsers need @method spoofing)
Route::put('/student/{id}', [StudentController::class, 'update'])->name('students.update');
Route::delete('/student/{id}', [StudentController::class, 'destroy'])->name('students.destroy');

// a protected group
Route::prefix('admin')->name('admin.')->middleware('auth')->group(function () {
    Route::get('/students', [StudentController::class, 'index'])->name('students.index');
});
?>
```
Order matters: `/students/create` must be declared **before** `/student/{id}` style wildcards in real projects, or `create` is captured as an id.

**Memorise:** `Route::get('/path', [Controller::class, 'method'])->name('name');` and `->where('id','[0-9]+')`.

---

### D9 — `Route::resource` + a Student controller skeleton
**Task:** one line of routing, seven methods, the shape of each.

```php
<?php
// routes/web.php
use App\Http\Controllers\StudentController;
Route::resource('students', StudentController::class);
?>
```
```php
<?php
// app/Http/Controllers/StudentController.php
namespace App\Http\Controllers;

use App\Models\Student;
use Illuminate\Http\Request;

class StudentController extends Controller
{
    public function index()
    {
        $students = Student::all();
        return view('students.index', compact('students'));
    }

    public function create()
    {
        return view('students.create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:100',
            'mark' => 'required|numeric|min:0|max:100',
        ]);

        Student::create($validated);

        return redirect()->route('students.index')->with('success', 'Student added');
    }

    public function show(Student $student)
    {
        return view('students.show', compact('student'));
    }

    public function edit(Student $student)
    {
        return view('students.edit', compact('student'));
    }

    public function update(Request $request, Student $student)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:100',
            'mark' => 'required|numeric|min:0|max:100',
        ]);

        $student->update($validated);

        return redirect()->route('students.index')->with('success', 'Student updated');
    }

    public function destroy(Student $student)
    {
        $student->delete();
        return redirect()->route('students.index')->with('success', 'Student deleted');
    }
}
?>
```
Generate it: `php artisan make:controller StudentController --resource`

**Memorise:** the seven names in order — `index, create, store, show, edit, update, destroy` — and that `store`/`update` take `Request` **first**, the bound model second.

---

### D10 — Middleware that blocks unauthenticated users
**Task:** Q283(b)/Q275(b). The class, the registration, the protected route.

```php
<?php
// app/Http/Middleware/EnsureLoggedIn.php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;

class EnsureLoggedIn
{
    public function handle(Request $request, Closure $next)
    {
        if (! $request->session()->has('user_id')) {
            return redirect('/login');       // blocked: controller never runs
        }

        return $next($request);              // allowed: continue down the pipeline
    }
}
?>
```
Register it (version-dependent):
```php
<?php
// Laravel 11+ — bootstrap/app.php
->withMiddleware(function (Middleware $middleware) {
    $middleware->alias(['loggedin' => \App\Http\Middleware\EnsureLoggedIn::class]);
})
?>
```
```php
<?php
// Laravel 10 and earlier — app/Http/Kernel.php
protected $routeMiddleware = [
    'loggedin' => \App\Http\Middleware\EnsureLoggedIn::class,
];
?>
```
Attach it:
```php
<?php
Route::get('/students', [StudentController::class, 'index'])->middleware('loggedin');
?>
```
Generate the class with `php artisan make:middleware EnsureLoggedIn`.

**Memorise:** `public function handle(Request $request, Closure $next)` — block by returning a redirect/`abort(403)`, allow by `return $next($request);`.

---

### D11 — Route model binding in a controller method
**Task:** Q285(b). Route, method, view — no manual `find()` anywhere.

```php
<?php
// routes/web.php
Route::get('/student/{student}', [StudentController::class, 'show'])->name('students.show');
?>
```
```php
<?php
// app/Http/Controllers/StudentController.php
namespace App\Http\Controllers;

use App\Models\Student;

class StudentController extends Controller
{
    public function show(Student $student)
    {
        // no query, no null check: Laravel fetched the row or returned 404
        return view('students.show', compact('student'));
    }
}
?>
```
```blade
{{-- resources/views/students/show.blade.php --}}
@extends('layout')

@section('content')
    <h2>{{ $student->name }}</h2>
    <p>Register No: {{ $student->register_no }}</p>
    <p>Mark: {{ $student->mark }}</p>
    <a href="{{ route('students.index') }}">Back</a>
@endsection
```
For a non-id key: `Route::get('/student/{student:register_no}', ...)` or override `getRouteKeyName()`.

**Memorise:** the parameter name and the variable name must be **identical** — `{student}` + `Student $student`.

---

### D12 — Blade layout + child view with a loop and an if
**Task:** the parent with `@yield`, the child with `@extends`, `@section`, `@foreach`, `@if`, `$loop`.

```blade
{{-- resources/views/layout.blade.php --}}
<!DOCTYPE html>
<html>
<head>
    <title>@yield('title', 'Student Portal')</title>
</head>
<body>
    @include('partials.navbar')

    <main>
        @yield('content')
    </main>

    <footer>&copy; Saintgits CSE</footer>
</body>
</html>
```
```blade
{{-- resources/views/students/index.blade.php --}}
@extends('layout')

@section('title', 'Student List')

@section('content')
    <h2>Student List ({{ count($students) }})</h2>

    @if (count($students) > 0)
        <ul>
        @foreach ($students as $s)
            <li>
                {{ $loop->iteration }}. {{ $s->name }} — {{ $s->mark }}
                @if ($s->mark >= 40)
                    <span class="pass">Pass</span>
                @else
                    <span class="fail">Fail</span>
                @endif
            </li>
        @endforeach
        </ul>
    @else
        <p>No students yet.</p>
    @endif
@endsection
```

**Memorise:** child = `@extends` + `@section ... @endsection`; parent = `@yield`. `@foreach` gets `$loop->iteration` and `$loop->last` for free.

---

### D13 — Redirect after save with a flash message
**Task:** the POST/Redirect/GET pattern, message rendered on the next page.

```php
<?php
public function store(Request $request)
{
    $validated = $request->validate([
        'name' => 'required|string|max:100',
        'mark' => 'required|numeric|min:0|max:100',
    ]);

    Student::create($validated);

    return redirect()->route('students.index')
                     ->with('success', 'Student saved successfully');
}
?>
```
```blade
{{-- in the layout or the index view --}}
@if (session('success'))
    <div class="alert alert-success">{{ session('success') }}</div>
@endif
```

**Memorise:** `return redirect()->route('students.index')->with('success', 'Saved');` — flash lives for exactly one request.

---

### D14 — Validation + error display (the `$request->validate` drill)
**Task:** the other half of every CRUD answer — prove the input was checked and the errors are shown.

```php
<?php
$validated = $request->validate([
    'name' => 'required|string|max:100',
    'mark' => 'required|numeric|min:0|max:100',
    'email'=> 'nullable|email',
]);
?>
```
On failure Laravel **redirects back automatically** with the errors and the old input in the session — you write no `if`. On success `$validated` contains only the keys you named (so a malicious extra field cannot reach `create()`).

```blade
@if ($errors->any())
    <ul class="errors">
    @foreach ($errors->all() as $error)
        <li>{{ $error }}</li>
    @endforeach
    </ul>
@endif

<form action="{{ route('students.store') }}" method="POST">
    @csrf
    <input type="text" name="name" value="{{ old('name') }}">
    @error('name')
        <span class="error">{{ $message }}</span>
    @enderror

    <input type="number" name="mark" value="{{ old('mark') }}">
    @error('mark')
        <span class="error">{{ $message }}</span>
    @enderror

    <button type="submit">Save</button>
</form>
```

**Memorise:** `$request->validate([...])` returns the **safe** subset; `@csrf` is mandatory in every POST form; `old()` repopulates, `@error` / `$errors->all()` displays.

---

## 5. 🔴 Night-before memorize sheet

Read this table aloud twice. If you know only this page, you still pass Part A.

| Item | Exact syntax / signature | Why it is asked |
|---|---|---|
| Two JSON containers | `{ }` object, `[ ]` array | Opening line of every JSON answer `5:p3` |
| The six types | string, number, boolean, null, object, array | Appears in 6 questions (140, 144, 148, 262, 271, 279) `5:p4` |
| Key rule | `{"name": "Anu"}` — keys always double-quoted | The strictness trap `5:p3` |
| Forbidden | no comments, no trailing comma, one top-level value | Syntax 7-markers |
| PHP → JSON | `json_encode($data)` | Q151, 268, 273, 279 `5:p7` |
| PHP → JSON pretty | `json_encode($data, JSON_PRETTY_PRINT)` | Named in the question style |
| JSON → PHP object | `json_decode($json)` → `->key` | Q267 `5:p8` |
| JSON → PHP array | `json_decode($json, true)` → `["key"]` | The default right answer `5:p8` |
| Error check | `json_last_error() !== JSON_ERROR_NONE` | Deck lists it; a marked point `5:p8` |
| Type mapping | assoc array → object; indexed array → array | Explains half the PHP/JSON questions `5:p7` |
| API header | `header("Content-Type: application/json");` | The DB-row-to-JSON slide `5:p9` |
| Schema root | `"$schema": "https://json-schema.org/draft/2020-12/schema"` | Q141 |
| Schema id | `"$id": "https://host/schemas/student.json"` | Q141 |
| Required | `"required": ["name", "mark"]` | Array of names, object level |
| Bounds | `"minimum": 0, "maximum": 100` | Q280 credits 1–6 |
| Array items | `"items": { "type": "string" }` | Nested arrays |
| JS parse | `JSON.parse(text)` → object | Q262(a) |
| JS stringify | `JSON.stringify(obj)` → string | Q262(a) |
| Framework def. | "framework calls your code; a library is called by your code" | The 1-mark distinction `5:p10` |
| MVC | Model = data, View = presentation, Controller = logic | Every Laravel 14-marker `5:p11` |
| MVC rule | "controller never talks to the browser; model never renders HTML" | Quotable `5:p11` |
| Features | Eloquent ORM, Blade, Artisan, routing/middleware/migrations/auth | Q142, 153 `5:p12` |
| Setup | `composer create-project laravel/laravel myapp` then `php artisan serve` | Q274(b) `5:p13` |
| Routes file | `routes/web.php` | Every routing answer `5:p14` |
| Route to controller | `Route::get('/student/{id}', [StudentController::class,'show'])` | The canonical line `5:p14` |
| Named route | `->name('students.index')` + `route('students.index')` | Q258(a), 284 |
| Constraint | `->where('id', '[0-9]+')` | Q258(a) |
| Group | `Route::prefix('admin')->name('admin.')->middleware('auth')->group(...)` | Q258(a) |
| Resource routes | `Route::resource('students', StudentController::class)` | Q257(a) |
| Resource controller | `php artisan make:controller StudentController --resource` | Q138, 257 |
| The 7 actions | `index, create, store, show, edit, update, destroy` | Q138 table |
| Middleware method | `public function handle(Request $request, Closure $next)` | Q264(a), 283 |
| Middleware attach | `->middleware('auth')` | Q146, 283 `5:p16` |
| Middleware allow | `return $next($request);` | The mechanism |
| Middleware block | `return redirect('/login');` / `abort(403);` | Short-circuit |
| Binding route | `Route::get('/student/{student}', ...)` | Q137, 285 `5:p18` |
| Binding method | `public function show(Student $student)` | Implicit binding `5:p18` |
| Binding 404 | automatic when no row matches | A mark on its own `5:p18` |
| Explicit binding | `Route::bind('student', fn ($v) => Student::where(...)->firstOrFail())` | Q285(a) |
| View call | `return view('students.index', compact('students'));` | Q259 `5:p19` |
| Other data forms | `view('x', ['k' => 'v'])` and `view('x')->with('k','v')` | Q259(a) |
| Dot notation | `students.index` = `resources/views/students/index.blade.php` | Q259(a) `5:p19` |
| Redirect | `return redirect('/students');` | Q259(b) `5:p20` |
| Redirect by name | `return redirect()->route('students.index');` | Preferred form |
| Redirect back | `return back()->withInput();` | After failed validation `5:p20` |
| Flash | `->with('success','Saved');` | One request only `5:p20` |
| Blade echo | `{{ $var }}` escaped · `{!! $var !!}` raw | The security mark `5:p23` |
| Blade comment | `{{-- ... --}}` | Never rendered `5:p23` |
| Blade if | `@if ... @elseif ... @else ... @endif`, `@unless ... @endunless` | Q286 `5:p24` |
| Blade loop | `@foreach ($items as $item) ... @endforeach`, `$loop->iteration` | Q160, 277 `5:p25` |
| Inheritance child | `@extends('layouts.app')` + `@section('content') ... @endsection` | Q136, 260(b) `5:p26` |
| Inheritance parent | `@yield('content')` | Q260(b) `5:p26` |
| Include | `@include('partials.navbar')` | Q260(b) `5:p26` |
| Request lifecycle | route → middleware → controller → model → view/redirect → response | Q265(a) `5:p21` |
| Validation | `$request->validate([...])` | Every store/update |
| Full redirect line | `return redirect()->route('students.index')->with('success','Saved');` | Q276(b) |

---

## 6. 📐 Diagram + figure index

The deck is page-marked and **text-only** — its "diagrams" are drawn as SmartArt/shapes, which the PDF text layer flattens into loose phrases. So redraw them yourself from the description; that is also the best revision. No page here needs an image you cannot reconstruct from the words below.

| Page | What is on it | What to redraw / how to use it |
|---|---|---|
| `5:p3` | JSON syntax panel — code beside five bullet rules | Draw a two-column box: **legal** vs **illegal** for each rule. 90 seconds, covers a 7-mark syntax question. |
| `5:p4` | **Six-row data-type table** (type / example / notes) | This is the single most reusable table in the module. Copy it exactly, including the note that JSON has no associative-array type. |
| `5:p5` | Nested JSON code panel (address object + courses array) | Redraw as a tree: root → address → city/pin, and root → courses → [ ] → code/title. |
| `5:p6` | Four-quadrant "what/why/where" layout on JSON Schema | Four headings: problem · what it specifies · why for APIs · where used. That is the 3-mark answer's skeleton. |
| `5:p9` | PHP snippet: DB rows → array → `json_encode` | Flow: `mysqli_query` → `while fetch_assoc` → `$students[]` → one `json_encode` → header. Note *encode once, after the loop*. |
| `5:p10` | Four numbered points: problem at scale, what Laravel provides, framework vs library, fit in course | The "framework calls your code" line lives here — quote it. |
| `5:p11` | **MVC chain** — User → Controller → Model → View → Response, with the note that the controller calls the model *first* | **Redraw this for Q261(a).** Five boxes, four labelled arrows. Label the arrows, not just the boxes. |
| `5:p13` | Setup commands + a **four-branch folder tree** (`app/Http/Controllers/`, `resources/views/`, `routes/web.php`, `database/migrations/`) | Redraw the tree and add `public/`, `config/`, `storage/` from §2.18 — that is Q282 covered. |
| `5:p14` | Route definitions: a closure route and a controller route | Two-line code panel; learn the `[Controller::class, 'method']` array syntax. |
| `5:p16` | Four numbered points on middleware (what, uses, applying, why separate) | The "why separate" point is the justification mark. |
| `5:p17` | **Route → middleware → controller chain** as one code panel with comments | Redraw as three stacked boxes; this is the 3-piece chain Q275/Q283 ask for. |
| `5:p18` | Route + controller method showing binding, with "`$student` is already the correct DB row" | The comment is the answer. Redraw with the 404 branch added. |
| `5:p20` | Redirect options (basic, back, with) + a `store()` snippet | Redraw as a decision: GET→view, POST→redirect→flash. |
| `5:p21` | **Request lifecycle, six numbered steps with a 5a/5b branch** (view vs redirect) | **The most valuable diagram in the module.** Redraw twice: once as boxes, once as a numbered list. Answers Q265(a) and half of Q261. |
| `5:p23`–`5:p25` | Blade echoing, conditionals, loops — each a code panel beside bullet points | Copy the three code panels verbatim; they are exactly the Q277/Q286 answers. |
| `5:p26` | **Template inheritance** — `layout.blade.php` and `students/index.blade.php` side by side | Redraw as frame-and-photo: parent with a `@yield` hole, child with an `@section` photo. Then write both files from memory (D12). |
| `5:p27` | **Six-row Blade directive table** | Memorise the table; it is a guaranteed 3-mark question (Q136/159/160). |
| `5:p28` | Recap — eight one-line takeaways | Read as a checklist the night before; each line is a Part-A answer. |

**Diagrams you must be able to produce on a blank page (in order of exam value):**
1. The request lifecycle (`5:p21`) — Q265(a), Q261(b), Q283(b).
2. The MVC chain (`5:p11`) — Q255, Q261(a), Q269, Q281.
3. The Laravel directory tree (`5:p13` + standard) — Q269(b), Q282, Q274(a).
4. The route → middleware → controller chain (`5:p17`) — Q275, Q283.
5. Blade inheritance, parent + child (`5:p26`) — Q260(b).

---

## 7. Say-this-if-grilled defence lines

One sentence each. Say them plainly; they are the answers to "but *why*", which is where the last 2 marks live.

1. **Why MVC?** Because a change in one concern stops rippling: restyle the UI and the SQL is untouched; change the database and the templates are untouched — and each layer can be tested alone `5:p11`.
2. **What middleware really does?** It wraps the controller: it can inspect and reject the request before your code runs, or decorate the response after — and it is the *only* place a cross-cutting check can live once instead of in thirty methods `5:p16`.
3. **Why does route model binding beat manual `find()`?** `find()` plus a null-check is three lines you must remember in four methods; a type-hint is zero lines you cannot forget, and a missing row becomes a 404 instead of a crash `5:p18`.
4. **Why does Blade escape by default?** Because output escaping only works if it is the default — an opt-in `htmlspecialchars()` is one forgotten call away from XSS, and the safe path must be the shortest one `5:p23`.
5. **Why JSON Schema instead of manual `if` validation?** The rules become data, not code: they can be versioned, shared, published in API docs, and reused by any client in any language — and the validator reports *every* failure with a path, not just the first one you coded.
6. **Why Laravel over raw PHP?** Raw PHP gives you a language; Laravel gives you the decisions already made — routing, ORM, templating, auth, CSRF, hashing — so you spend your time on the application, not on reinventing a router `5:p10`.
7. **Why is JSON better than XML for APIs?** It is less verbose (no closing tags), it maps directly onto the objects and arrays every language already has, and it parses faster `5:p2`.
8. **Why is JSON so strict — no comments, no trailing commas?** Because two unrelated systems must agree exactly; every permitted dialect is a new incompatibility, and a parser cannot be lenient and unambiguous at the same time `5:p3`.
9. **Why does a controller end in `view()` or `redirect()` and not both?** They answer different verbs: a GET renders what you asked for; a POST changes state and then redirects, so a refresh re-reads instead of re-writing `5:p21`, `5:p20`.
10. **Why named routes?** The URL becomes an implementation detail defined in one file; every `route()` call follows a change automatically, so a rename is one edit, not a grep `5:p14`.
11. **Why resource controllers?** Seven conventional actions with predictable names replace seven hand-written routes, so CRUD is uniform across every resource and `route('students.edit', $id)` can be written without looking anything up.
12. **Why `compact()` rather than an array literal?** It builds `['students' => $students]` from the variable's own name, so the key can never disagree with the variable `5:p19`.
13. **Why does Blade compile to PHP instead of interpreting?** Because it compiles once and caches — you get readable templates at no runtime cost, which is why the deck can say the directives do nothing PHP could not do `5:p22`, `5:p27`.
14. **Why does `json_decode` need the error check if it returns `null` on failure?** Because `null` is also a *valid* JSON document, so `=== null` cannot distinguish "failed" from "legitimately empty" — only `json_last_error()` can `5:p8`.

