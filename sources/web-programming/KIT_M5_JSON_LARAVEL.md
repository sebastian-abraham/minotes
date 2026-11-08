# MODULE 5 — JSON and Laravel · exam kit
> 20CST461 Web Technologies · Part A = 3 marks · Part B = 14 marks · 2 Part-A questions and 1 of 2 Part-B questions come from this module

`5:pN` = page N of `module5.md` (28 pages). **(standard, not in your deck)** = fully answerable, but no slide says it — do not claim the deck.

---

## 1. Coverage map

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

**Five themes.** JSON as a format — 17 of 64 questions · JSON Schema 7 · PHP ↔ JSON 6 · Laravel architecture 13 · request machinery (routing, middleware, controllers, binding, views, redirects, Blade) 21.

**Prediction.** Part A: one JSON items question + one Laravel one-liner. Part B: a 7+7 hybrid — 21 of the 33 Part-B questions are that shape.

---

## 2. Deep dive

### 2.1 JSON, and why it beat XML (`5:p2`)
**What:** a lightweight, text-based, language-independent format for structured data — readable by humans, parseable by machines, used by virtually every language.

- Two containers only: object `{ }`, array `[ ]`.
- Beat XML: no closing tags (≈half the bytes) · maps onto objects/arrays every language already has · parses faster.
- Not a programming language — no functions, no comments, no logic.

```json
{ "name": "Anu", "age": 20, "isActive": true, "marks": [88, 92, 79] }
```

**Trap:** Q143 = definition + *two* advantages over XML.

### 2.2 Syntax rules — the strictness page (`5:p3`)
**What:** exactly two structures, everything else nests inside them; keys always double-quoted, and stricter than a JavaScript object literal.

| # | Rule | Legal | Illegal |
|---|---|---|---|
| 1 | Keys are **always double-quoted strings** | `{"name": "Anu"}` | `{name: "Anu"}`, `{'name': 'Anu'}` |
| 2 | **No comments** of any kind | — | `{"a":1} // note`, `/* note */` |
| 3 | **No trailing comma** | `{"a":1,"b":2}` | `{"a":1,"b":2,}` |
| 4 | **Exactly one top-level value** | `{...}` or `[...]` | `{...} {...}` |
| 5 | Strings use **double quotes only**; only `\"  \\  \/  \b  \f  \n  \r  \t  \uXXXX` are legal escapes | `"say \"hi\""` | `'hi'`, raw newline inside a string |

```json
{
  "name": "Anu",
  "age": 20,
  "isActive": true,
  "marks": [88, 92, 79]
}
```

- Numbers: no leading `+`, no zero, no `.5`, no hex; `NaN`/`Infinity` do not exist; dates are strings, not a type.

**Trap:** `{a:1,}` is valid JS, invalid JSON — quote *"strict syntax, unlike JavaScript object literals"* `5:p3`.

### 2.3 The six data types (`5:p4`) — master table
| Type | Example | Notes |
|---|---|---|
| string | `"Saintgits"` | Always double-quoted |
| number | `20` or `499.50` | No distinction between int and float |
| boolean | `true` / `false` | Lowercase, unquoted |
| null | `null` | Represents "no value" |
| object | `{ "city": "Kottayam" }` | Nested key–value pairs |
| array | `[88, 92, 79]` | Ordered list of any of the above |

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

- Two containers, four scalars — a type set small enough that every language implements JSON in a page of code.
- PHP's associative array is absorbed by `object`; JSON has no separate type for it `5:p4`.

**Trap:** Q279 makes you *identify* six literals — `true` boolean · `25` number · `"PHP"` string · `null` null · `[1,2]` array · `{"id":1}` object.

### 2.4 Nesting (`5:p5`)
**What:** any value — including another object or array — sits inside an object or array, with no depth limit.

```json
{
  "name": "Anu",
  "address": { "city": "Kottayam", "pin": "686532" },
  "courses": [
    { "code": "20CST461", "title": "Web Programming" }
  ]
}
```

- Nesting *is* the data model: a student HAS an address, HAS a list of marks `5:p5`.
- Indentation is cosmetic — no effect on parsing `5:p5`.

### 2.5 Designing a document (`5:p5`, mostly standard)
**What:** choosing the top-level container, key names, and where to nest vs flatten — the shape is the API contract.

- Object for one entity, array for a collection; never a bare string at the root.
- `camelCase` or `snake_case`, one convention per API; plural key for lists; ≤3 nesting levels.
- Real types in values (`88`, not `"88"`); `null` = known absent, omit the key = not applicable.

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

### 2.6 JSON Schema — the problem it solves (`5:p6`)
**What:** a separate JSON document stating the rules another JSON document must satisfy — validation as data, not code.

- JSON alone cannot say "this field is required" or "this must be a number" `5:p6`.
- Specifies required fields · type per field · value constraints (minimum/maximum, patterns) · nested structure.
- Runs **wherever JSON crosses a trust boundary** — request bodies, third-party responses, config files.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["name"],
  "properties": { "name": { "type": "string" } }
}
```

**Trap:** "schema of a JSON document" (Q139) is the *structure*; Q145/150 are the *validation language*.

### 2.7 Schema keywords (`5:p6` concept; keywords standard)
**What:** eight keywords cover every schema the paper asks for.

| Keyword | Sits at | Means |
|---|---|---|
| `$schema` | root | which **dialect** — tells a validator which rules apply |
| `$id` | root | unique URI **identifying this schema**, for `$ref` and caching |
| `type` | any level | `object`, `array`, `string`, `number`, `integer`, `boolean`, `null`; array for a union |
| `properties` | in an object | map of key → sub-schema |
| `required` | in an object | array of key **names** that must be present (presence, not truthiness) |
| `minimum` / `maximum` | in a number | inclusive numeric bounds |
| `items` | in an array | the schema every element must satisfy |
| `additionalProperties` | in an object | `false` forbids keys not in `properties` |

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

**Traps:** `"required": true` inside a property is wrong — array of names at *object* level · `"integer"`, never `"int"`.

### 2.8 How validation errors come back (standard, not in your deck)
**What:** a validator returns a boolean **plus an array of error objects** — `instancePath`, `schemaPath`, `keyword`, `message`.

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

- `""` instancePath = failure at the document root — a missing top-level key.
- Missing key → error at the object's path; wrong type → error at the property's path.
- All errors collected, not just the first; valid **iff** the array is empty.

**Exam line (Q254b):** *"errors come back as a list of objects giving the failing instance's path, the failing keyword and a message; the document is valid iff that list is empty."*

### 2.9 `json_encode()` — PHP → JSON (`5:p7`)
**What:** `json_encode($value)` returns a JSON-formatted string built from a PHP value.

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

- **Associative** array → object; **indexed** array → array — decided by whether keys are sequential integers from 0.
- PHP objects encode from their **public** properties; `false` on failure (invalid UTF-8).

### 2.10 `json_decode()` — JSON → PHP (`5:p8`)
**What:** turns a JSON string back into PHP data; the second argument decides object or array.

```php
<?php
$json = '{"name":"Rahul","marks":[72,80]}';

$asObject = json_decode($json);
echo $asObject->name;        // Rahul   (object → ->)

$asArray = json_decode($json, true);
echo $asArray["name"];       // Rahul   (assoc array → ["..."])
?>
```

- Default (`false`) = `stdClass` → `->name`; `true` = associative array → `["name"]`, which is what `foreach`, `array_map` and `compact()` want `5:p8`.
- Common use: a JSON request body sent by `fetch()` `5:p8`.

### 2.11 Flags and error handling (`5:p7`–`p8`; error handling standard)
| Item | Effect |
|---|---|
| `JSON_PRETTY_PRINT` | 4-space indentation, readable output `5:p7` |
| `JSON_UNESCAPED_SLASHES` | keeps `https://x` instead of `https:\/\/x` |
| `JSON_UNESCAPED_UNICODE` | keeps `ക` instead of `\u0d15` |
| `JSON_THROW_ON_ERROR` | throws `JsonException` instead of returning `null` (PHP 7.3+) |
| `json_last_error()` | integer error code of the last encode/decode `5:p8` |
| `json_last_error_msg()` | human message, e.g. `Syntax error` |

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

**Trap:** `json_decode` returns `null` for failure *and* for the valid document `null` — only `json_last_error()` distinguishes them.

### 2.12 Arrays ↔ objects: the one asymmetry (`5:p4`)
**What:** JSON has no associative-array type; `object` covers that role, so PHP's two array kinds map many-to-one.

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

- `json_encode([])` gives `[]`, not `{}` — a JS client expecting an object needs `JSON_FORCE_OBJECT`.

### 2.13 The real use: a DB row as an API response (`5:p9`)
**What:** fetch rows into a plain PHP array, encode **once after** the loop, send `Content-Type: application/json`.

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

- Encode inside the loop and you get `{...}{...}`, which is not a JSON document `5:p9`.

### 2.14 `JSON.parse()` / `JSON.stringify()` (standard; deck covers the PHP side only)
**What:** the two boundary functions — `parse` = string → value, `stringify` = value → string.

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

- `parse` throws `SyntaxError` on bad JSON; `stringify` drops `undefined`/functions, `Date` becomes an ISO string, `NaN`/`Infinity` become `null`.
- `fetch().json()` is already a parse, and it is async. Sentence for any sub-question: *serialise at the boundary, parse at the boundary.*

### 2.15 Why a framework; what Laravel is (`5:p10`)
**What:** a free, open-source PHP framework — routing, ORM, templating, auth and project structure out of the box.

- The hand-written connect → query → loop → render pattern repeats badly at scale `5:p10`.
- *"A library is something your code calls. A framework calls your code."*

```php
// raw PHP (Module IV)                     // Laravel
$r = mysqli_query($conn, "SELECT * FROM students");
while ($row = mysqli_fetch_assoc($r)) {    $students = Student::all();
    echo "<td>" . $row['name'] . "</td>";  return view('students.index', compact('students'));
}
```

- Security defaults (escaping, CSRF, hashed passwords) come free — that, not "it is faster", is the 14-mark argument.

### 2.16 MVC (`5:p11`)
**What:** separates data (Model), presentation (View) and request logic (Controller) — one job each.

- Chain: User → Controller → Model → View → Response; the controller calls the model **first** `5:p11`.
- Two quotable rules: *the controller never talks to the browser directly, the model never renders HTML.*

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

- "Separation of concerns": restyle the UI and the SQL is untouched; change the database and the views are untouched.

### 2.17 Headline features (`5:p12`)
| Feature | What it does |
|---|---|
| **Eloquent ORM** | tables as PHP objects/methods — `Student::find(1)` instead of raw `mysqli_query()` |
| **Blade templating** | view layer; compiles `@if`, `@foreach` into plain PHP |
| **Artisan CLI** | scaffolding and tasks — `php artisan make:controller` |
| **Routing, middleware, migrations, auth** | URL→code mapping, request filtering, versioned DB schema, login |

```php
$student  = Student::find(1);            // Eloquent
$top      = Student::where('marks', '>', 80)->get();
```

```bash
php artisan make:controller StudentController
php artisan migrate
php artisan route:list
```

- Pair each feature with **the boilerplate it removes**. The name alone scores nothing.

### 2.18 Application structure (`5:p13`)
**What:** the standard skeleton that makes conventions work — Laravel *finds* your code by location, so location is part of the contract.

| Path | Holds | Deck ref |
|---|---|---|
| `app/Http/Controllers/` | controller classes | `5:p13` |
| `resources/views/` | Blade templates (`.blade.php`) | `5:p13`, `5:p22` |
| `routes/web.php` | URL → code mappings | `5:p13`, `5:p14` |
| `database/migrations/` | versioned schema changes | `5:p13` |

Full tree (standard, not in your deck beyond the four rows above):

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

- Purpose (Q154): predictability + onboarding + the framework locating code automatically = *convention over configuration*.
- Only `public/` is web-exposed; `.env`, `storage/`, `vendor/` sit above the doc root.

### 2.19 Setup and Artisan (`5:p13`)
**What:** PHP + **Composer** + a database; three commands to a running site.

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

- `composer` handles autoloading (you never write `require`); `artisan` is the CLI half of the framework.

### 2.20 Routing (`5:p14`)
**What:** a route maps a URL (+ verb) to the code that handles it — every request's entry point; all browser routes in `routes/web.php`.

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

- One static method per verb: `Route::get/post/put/delete` `5:p14`.
- Target: a closure, or more commonly `[StudentController::class, 'index']` `5:p14`.
- `php artisan route:list` prints the URL→handler table.

### 2.21 Parameters, constraints, names, groups (standard; deck shows `{student}` only at `5:p18`)
**What:** `{name}` is a placeholder captured from the URL and passed positionally; shared attributes are declared once around a group.

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

- Constraints turn a bad id into a 404 at the router, not a 500 in the controller.
- Names decouple code from the URL: one rename, no grep. `Route::match([...])`/`Route::any()` cover several verbs.

### 2.22 Sub-domain routing (standard, not in your deck)
**What:** `Route::domain()` restricts a route or group to one host; `{param}` in the domain arrives like a URI parameter.

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

- Cases: multi-tenant SaaS · admin vs public surface · per-department portals · localisation.
**Traps:** takes a **host**, not a path · local testing needs hosts/wildcard DNS · routing, not authorisation.

### 2.23 Middleware (`5:p16`)
**What:** code running **before** a request reaches its controller, or after the response — a filtering layer around request handling.

- Uses `5:p16`: login check (`auth`), logging, permissions, rate limiting.
- Separate from the controller so one check lives in one place and cannot be forgotten.

```php
<?php
// applying it to one route  (deck, 5:p16)
Route::get('/dashboard', [DashboardController::class, 'index'])->middleware('auth');

// the full chain: route -> middleware -> controller  (deck, 5:p17)
Route::get('/students', [StudentController::class, 'index'])->middleware('auth');
?>
```

**Trap:** it runs before the controller resolves, so it sees only the *request* — never what the controller found.

### 2.24 `handle()`, and the three registrations (standard, not in your deck)
**What:** every middleware is a class with one method; `$next($request)` means "carry on", and *not* calling it is how you block.

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

- Three categories: **global** (every request) · **group** (`web`, `api`) · **route** (only where attached).
- Code before `$next` runs inbound; after it runs outbound.

### 2.25 Controllers (`5:p15`)
**What:** one class grouping related request handling, so `routes/web.php` stays short; `make:controller` scaffolds it into `app/Http/Controllers/`.

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

- One public method per route; a method ends in a `view()` or a `redirect()` `5:p15`.

### 2.26 Resource controllers and the 7 RESTful actions (standard, not in your deck)
**What:** seven methods and route names following a fixed RESTful convention — generated with `--resource`, wired with one line.

```bash
php artisan make:controller StudentController --resource
```

```php
Route::resource('students', StudentController::class);
```

- Actions in order: `index, create, store, show, edit, update, destroy` — the full table is in §B7.
- One line replaces seven `Route::get/post` lines; `->only([...])` / `->except([...])` trim the set.

### 2.27 Route model binding (`5:p18`)
**What:** Laravel fetches the record named by a route parameter and injects it — `{student}` + `Student $student` ⇒ lookup by id; no row ⇒ **automatic 404**.

```php
<?php
Route::get('/student/{student}', [StudentController::class, 'show']);

public function show(Student $student) {
    // $student is already the correct DB row
    return view('students.show', compact('student'));
}
?>
```

- **Implicit** (deck's version): parameter name matches the type-hinted variable; override the column with `{student:register_no}` or `getRouteKeyName()`.
- **Explicit** (standard): declare the resolution in a service provider.

```php
Route::bind('student', function ($value) {
    return Student::where('register_no', $value)->firstOrFail();
});
```

- Collapses `find()` + `if null` + `abort(404)` into a type-hint.

### 2.28 Views and passing data (`5:p19`)
**What:** `view('name', $data)` renders a `.blade.php` file; views live in `resources/views/`.

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

- Dot notation is a **folder separator**: `students.index` = `students/index.blade.php` `5:p19`.
- The view receives only what it is given — no globals, no `global $conn`.
- Share with **all** views (standard):

```php
// app/Providers/AppServiceProvider.php  -> boot()
View::share('collegeName', 'Saintgits College of Engineering');
// now usable in every Blade file as {{ $collegeName }}
```

### 2.29 Redirections and flash data (`5:p20`)
**What:** `redirect('/path')`, `redirect()->back()`, and `->with('key','value')` = flash readable on the next request only.

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

- Reason-mark sentence `5:p20`: *"redirecting after a successful POST prevents accidental duplicate form resubmission."* That is POST/Redirect/GET.

### 2.30 The request lifecycle (`5:p21`)
**What:** route match → middleware checks → controller → model binding → `view()` or `redirect()` → response.

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

- GET that shows data ends in `view()`; POST that changes data ends in `redirect()` `5:p21`.

### 2.31 Blade (`5:p22`)
**What:** Laravel's templating engine — directives inside HTML instead of `<?php ?>` blocks; compiles to plain PHP and caches it, so no runtime cost.

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

- Files end in `.blade.php`; every `view()` renders one; `{{ }}` escapes so you cannot forget `htmlspecialchars`.

### 2.32 Echoing and escaping (`5:p23`)
**What:** `{{ $v }}` echoes escaped (XSS-safe); `{!! $v !!}` echoes raw HTML — trusted content only.

```blade
<h2>Welcome, {{ $student->name }}</h2>
<p>{{ $bio ?? 'No bio provided.' }}</p>
{!! $trustedHtmlBlock !!}
{{-- This comment never reaches the browser --}}
```

- `{{ }}` compiles to `echo htmlspecialchars($value)`; any PHP expression works inside: `{{ count($students) }}`, `{{ $mark ?? 0 }}`.

**Traps:** the HTML you *write* is not escaped, only values you echo · `{{-- --}}` never reaches the browser, `<!-- -->` does.

### 2.33 Conditionals (`5:p24`)
**What:** `@if/@elseif/@else/@endif`, `@unless` (runs when false), `@isset` (set and not null), `@empty`.

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

- All compile to plain PHP `if`; `@unless` exists because `@if(!$x)` reads badly.

### 2.34 Loops and `$loop` (`5:p25`)
**What:** `@foreach`, `@for`, `@while`; `$loop` is provided automatically inside `@foreach`.

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

- `$loop`: `index` (0-based) · `iteration` (1-based) · `first` · `last` · `count` · `remaining` · `even/odd` · `depth`.
- Removes the manual counter and the "is this the last item" off-by-one.

### 2.35 Template inheritance (`5:p26`)
**What:** `@extends` names the parent; `@section ... @endsection` defines a block; `@yield` marks where it goes in the parent; `@include` pastes a partial.

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

- `@extends` must be the **first** construct in the child; `@yield('title', 'default')` takes a default; a section never yielded is silence, not an error.

**Trap:** `@include` is not inheritance — no parent/child, just insertion. Exactly right for a navbar.

### 2.36 The directive quick-reference (`5:p27`)
| Directive | Purpose |
|---|---|
| `{{ $var }}` | Echo data, auto-escaped (safe) |
| `{!! $var !!}` | Echo raw HTML, unescaped (use with caution) |
| `@if / @elseif / @else / @endif` | Conditional rendering |
| `@foreach / @endforeach` | Loop over a collection or array |
| `@extends / @section / @yield` | Template inheritance — shared layouts |
| `@include('view')` | Insert a reusable partial template |

- Quote `5:p27`: *"Every Blade directive is just a readable shorthand for plain PHP"* — the answer to "why Blade at all".
- Safe extras (standard): `@csrf` (mandatory in every POST form), `@method('PUT')`, `@php`, `@auth/@guest`, `@switch`, `@error('field')`, `@forelse`.

### 2.37 Components (standard, only if the paper goes modern)
**What:** a reusable, parameterised view with a class — declared props, a `$slot`, optional logic.

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

- `@include` shares markup with no typed inputs; a component has props and a slot. Every question here asks only `@extends/@section/@yield/@include` — answer with those plus one line that components exist.

## 3. Answer bank

### 3.1 Part A — 3 marks (A1–A20)

Three numbered lines, ≤18 words each, bold lead word. Where the bank asks the same thing repeatedly there is one **master** answer and an *also answers* list.

#### A1 — JSON as a data interchange format · *also answers Q143, half of Q130*
1. **Definition:** lightweight, text-based, language-independent format for structured data — objects `{ }`, arrays `[ ]`.
2. **Interchange:** the wire format for API bodies and config; both sides serialise to text, parse back.
3. **Over XML:** no closing tags (≈half the bytes), maps onto native objects/arrays, parses faster `5:p2`.

```json
{ "name": "Anu", "age": 20, "marks": [88, 92, 79] }
```

#### A2 — PHP ⇄ JSON functions · *also answers Q131, Q151*
1. **PHP → JSON:** `json_encode($value)` returns a string; associative arrays become objects, indexed arrays arrays `5:p7`.
2. **JSON → PHP:** `json_decode($j)` objects, `json_decode($j, true)` associative arrays `5:p8`.
3. **Check:** `json_last_error() !== JSON_ERROR_NONE`; `JSON_PRETTY_PRINT` for readable output `5:p8`.

```php
<?php
$json  = '{"name":"Anu","marks":[88,92,79]}';
$data  = json_decode($json, true);
$data["marks"][1] = 95;                       // modify
echo json_encode($data, JSON_PRETTY_PRINT);   // re-encode
?>
```

#### A3 — Note on the Laravel framework · *also answers Q132, part of Q274*
1. **What:** free, open-source PHP framework — routing, Eloquent, Blade, auth, structure out of the box `5:p10`.
2. **Why:** connect → query → loop → render repeats everywhere; Laravel solves each problem once `5:p10`.
3. **Framework vs library:** a library is called by your code; a framework calls your code `5:p10`.

#### A4 — Design pattern in Laravel · *also answers Q133, Q152*
1. **Primary: MVC** — Model data, View presentation, Controller request logic, one job each `5:p11`.
2. **Also:** Front Controller, Facade (`Route::`), Pipeline (middleware), DI container (standard).
3. **Convention over configuration** — file locations and names are the config `5:p13`.

#### A5 — Routing in Laravel · *also answers Q134, Q155*
1. **Definition:** a route maps a URL + verb to its handler — every request's entry point `5:p14`.
2. **Where:** `routes/web.php`; one method per verb — `Route::get/post/put/delete` `5:p14`.
3. **Target:** a closure, or more commonly `[StudentController::class, 'index']` `5:p14`.

```php
<?php
Route::get('/', function () { return "Welcome to Saintgits CSE"; });
Route::get('/students', [StudentController::class, 'index']);
Route::post('/students', [StudentController::class, 'store']);
?>
```

#### A6 — Middleware · *also answers Q135, Q146, Q156*
1. **Definition:** code running before the controller — or after the response — wrapping request handling `5:p16`.
2. **Uses:** login check (`auth`), logging, permissions, rate limiting `5:p16`.
3. **Applied:** `->middleware('auth')`; block with a redirect, allow with `$next($request)` (standard).

#### A7 — `@extends` · *also answers Q136, part of Q260(b)*
1. **Purpose:** declares the parent layout a child inherits, so header/footer/nav markup is written once `5:p26`.
2. **Pairs with:** `@section('content')` in the child, `@yield('content')` in the parent `5:p26`.
3. **Rule:** `@extends` is the first Blade construct in the child. Example: §2.35.

#### A8 — Route model binding · *also answers Q137, Q158, part of Q285*
1. **Definition:** Laravel auto-fetches the row matching a route parameter and injects it `5:p18`.
2. **How (implicit):** `{student}` + a `Student $student` type-hint ⇒ lookup by id `5:p18`.
3. **Free 404:** no matching row ⇒ automatic 404; saves `find()` plus a null check `5:p18`.

```php
Route::get('/student/{student}', [StudentController::class, 'show']);
public function show(Student $student) { return view('students.show', compact('student')); }
```

#### A9 — Resource controllers and CRUD · *also answers Q138, part of Q257*
1. **Definition:** a controller whose seven methods follow a fixed RESTful convention (standard).
2. **Wire:** `make:controller --resource`, then `Route::resource('students', StudentController::class)`.
3. **Names:** `index, create, store, show, edit, update, destroy`; `--only`/`--except` trim.

#### A10 — Schema of a JSON document · *also answers Q139*
1. **Means:** the document's *shape* — container, keys, types, nesting. Not the validation language.
2. **Top level:** object for one entity, array for a collection; consistent keys, real types.
3. **Structure:** root object · three scalars · one array of objects. Example: §2.5.

#### A11 — JSON data types · MASTER · *also answers Q140, Q144, Q148, Q262(a), Q271, Q279*
1. **Six types:** string · number · boolean · null · object · array — two containers, four scalars `5:p4`.
2. **Structured data:** objects model an entity, arrays repetition, nesting the relationships `5:p5`.
3. **No associative-array type:** JSON's `object` covers that role, unlike PHP `5:p4`.

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

Q279's six-item drill, learn verbatim:

| Value | JSON type |
|---|---|
| `true` | boolean |
| `25` | number |
| `"PHP"` | string |
| `null` | null |
| `[1,2]` | array |
| `{"id":1}` | object |

#### A12 — `$schema` and `$id` · *also answers Q141*
1. **`$schema`:** root keyword giving the **dialect** URI — which rule-set a validator applies.
2. **`$id`:** root keyword giving a **unique URI for this schema**, so others `$ref` it and validators cache it.
3. **One line:** `$schema` = *which language am I written in*; `$id` = *who am I* (standard).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://saintgits.example/schemas/student.json",
  "type": "object"
}
```

#### A13 — Three Laravel features · MASTER · *also answers Q142, Q153*
1. **Eloquent ORM:** tables as objects — `Student::find(1)` instead of `mysqli_query()` `5:p12`.
2. **Blade:** `@if`/`@foreach` compiled to plain PHP and cached `5:p12`.
3. **Artisan CLI:** `make:controller`, `migrate`, `route:list` — plus routing, middleware, migrations, auth `5:p12`.

#### A14 — JSON Schema and its purpose · MASTER · *also answers Q145, Q150*
1. **Definition:** a separate JSON document describing rules another document must satisfy `5:p6`.
2. **Why needed:** JSON cannot say "this field is required" or "this must be a number" `5:p6`.
3. **Purpose:** automatic validation wherever JSON crosses a trust boundary, not an `if` per field `5:p6`.

#### A15 — GET vs POST vs route model binding · *also answers Q147, part of Q270(b)*
| | GET | POST | Route model binding |
|---|---|---|---|
| **Purpose** | retrieve/show data | submit/create/change data | resolve a route parameter into a model |
| **Data location** | query string / URL | request body | URL segment, e.g. `{student}` |
| **Idempotent** | yes | no | n/a — a resolution step, not a verb |
| **Ends in** | `view()` | `redirect()` | a model instance, or automatic 404 |
| **Deck ref** | `5:p14`, `5:p21` | `5:p14`, `5:p20` | `5:p18` |

**One line:** GET *asks*, POST *tells*, binding *fetches the row the URL names*.

#### A16 — JSON object vs JSON array · *also answers Q149*
1. **Object** `{ }`: unordered, string-keyed pairs; look up by key; assoc array or `stdClass`.
2. **Array** `[ ]`: ordered list; access by position; indexed array.
3. **Use:** object = one entity, array = a collection; either nests in the other.

```json
{ "student": { "name": "Anu" }, "marks": [88, 92, 79] }
```

#### A17 — Purpose of the application structure · *also answers Q154*
1. **Convention over configuration:** fixed locations let the framework find code with zero config `5:p13`.
2. **Separation of concerns:** one drawer per concern, so a change touches one place `5:p11`.
3. **Security + teams:** only `public/` is exposed; any Laravel developer navigates any project.

#### A18 — Role of a controller · *also answers Q157*
1. **Receives** the request for its route, one public method per route `5:p15`.
2. **Asks the model** for data (`Student::all()`) and applies the logic `5:p15`.
3. **Returns** a `view()` or a `redirect()`; never renders HTML itself `5:p11`.

#### A19 — What is Blade · *also answers Q159, part of Q265(b)*
1. **Definition:** templating engine — `@if`/`@foreach` inside HTML instead of `<?php ?>` blocks `5:p22`.
2. **Compiles** to plain PHP and caches it — no real performance cost `5:p22`.
3. **Safety + inheritance:** `{{ }}` escapes, `{!! !!}` does not; `@extends/@section/@yield` `5:p23`.

#### A20 — Purpose of `@foreach` · *also answers Q160*
1. **Purpose:** renders a block once per element of an array or collection `5:p25`.
2. **Syntax:** `@foreach ($students as $s) ... @endforeach` `5:p25`.
3. **Bonus:** `$loop->index/iteration/first/last/count` available automatically `5:p25`.

```blade
<ul>
@foreach ($students as $s)
    <li>{{ $loop->iteration }}. {{ $s->name }}</li>
@endforeach
</ul>
```

### 3.2 Part B — 14 marks (B1–B13)

**Mark shape.** Definition · mechanism · runnable code · worked example · one justification line: define only = 4/14, define + code + example = 11–12. Count the split and write it as `(a) ... [7]`; a missing part cannot be recovered by a brilliant other half.

**Split rule.** Give each half space proportional to its marks — roughly 1 mark ≈ 2.5 lines of prose or 4 lines of code.

---

#### B1 — JSON: syntax, types, document design · MASTER
**Covers:** Q266 (7+7) · Q271 (14) · Q278 (7+7) · Q262(a) (8) · Q279(a) (7) · Q139/Q263(a) first half.

**Deltas.** Q266 (7+7): rules + student doc · Q271 (14): rules + all six types + student doc · Q278 (7+7): nested college→departments→students, add §D2 · Q262(a) (8): types + parse/stringify, add §2.14 · Q279(a) (7): identify six literals, add A11's table.

**Structure (a 7):** definition + two containers 1 · five syntax rules with legal/illegal pairs 4 · six types 2. **(b 7):** the document 4 · walk-through 2 · why this shape 1.

**Answer:**

**(a)** JSON is a lightweight, text-based, language-independent format for structured data, built from exactly **two** structures — an **object** `{ }` (unordered key-value pairs) and an **array** `[ ]` (an ordered list); everything else nests inside them `5:p3`. The rules for a valid document:

1. **Keys are always double-quoted strings** — `{"name": "Anu"}` valid, `{name: "Anu"}` and `{'name': 'Anu'}` invalid. JS allows both; JSON does not.
2. **No comments** — neither `//` nor `/* */`; JSON is data, not a source file `5:p2`.
3. **No trailing comma**: `{"a":1,"b":2,}` is invalid.
4. **Exactly one top-level value** — two objects side by side is not a document.
5. **Double quotes only**, escapes limited to `\"  \\  \/  \b  \f  \n  \r  \t  \uXXXX`.
6. **Numbers plain decimal** — no leading `+` or zero, no hex; `NaN`/`Infinity` do not exist.

Deck line to quote: *"strict syntax, unlike JavaScript object literals"* `5:p3` — deliberate, because two unrelated systems must agree exactly.

```json
{
  "name": "Anu",
  "age": 20,
  "isActive": true,
  "marks": [88, 92, 79]
}
```

**(b) A student document.**

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

**Why this shape:** the root is an **object** because it describes one entity; `registerNo`, `name`, `course` are strings and `semester` a number, not stringified values; `marks` is an **array of objects** because "a student HAS many subject marks" is one-to-many, and pairing subject with mark stops the two drifting apart `5:p5`. Nesting is what lets one document carry the whole relationship tree.

**Q278(b) — the same design at three levels:**

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

Say it aloud in the exam: *object → array of objects → array of objects*. That sentence is worth a mark.

**Traps:** single quotes or a trailing comma — instantly invalid, the commonest lost mark · for Q278(b), putting `departments` and `students` side by side instead of nesting students **inside** their department (the nesting *is* the answer).

---

#### B2 — JSON Schema: keywords, validation, error reporting · MASTER
**Covers:** Q254 (8) · Q272 (14) · Q280 (14) · Q263(a) second half · Q145/150 at 3 marks (A14).

**Deltas.** Q254 (8): role + error handling, skip the student schema, expand the error paragraph · Q272 (14): schema + `type/required/properties`, then the student schema · Q280 (14): keyword walk + **course** schema, credits 1–6 · Q263(a): Q272(b) appended to a types answer.

**Structure (a 7):** definition + problem 1 · what it specifies 1 · keyword table 3 · validation walk 2. **(b 7):** schema 4 · valid + invalid instance 2 · error report 1.

**Answer:**

**(a)** JSON Schema is **a separate JSON document that describes the rules another JSON document must satisfy**. JSON itself cannot say *"this field is required"* or *"this must be a number"* `5:p6`. It is valuable **wherever JSON crosses a trust boundary** — a JS form submission, another service's response `5:p6`.

| Keyword | Level | Meaning |
|---|---|---|
| `$schema` | root | URI of the **dialect** — which rule-set the validator applies |
| `$id` | root | unique URI **identifying this schema**, so it can be `$ref`-ed and cached |
| `type` | any | `object`, `array`, `string`, `number`, `integer`, `boolean`, `null` |
| `properties` | inside an object | map of key → sub-schema |
| `required` | inside an object | array of key **names** that must be *present* |
| `minimum` / `maximum` | inside a number | inclusive numeric bounds |
| `items` | inside an array | the schema **every** element must satisfy |
| `additionalProperties` | inside an object | `false` forbids keys not in `properties` |

**How validation works:** the validator walks instance and schema together: `type` at every level; for an object, that every `required` name exists and each present key satisfies its `properties` sub-schema; every element satisfies `items`; every number lies within `minimum`/`maximum`. Recursion catches a bad `mark` inside `marks[2]`. Valid iff every check passes.

**(b)** Schema for a student:

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

**Valid:** all three `required` names present, `mark` a number in 0–100, no unknown keys.

```json
{ "registerNo": "SJC22CS001", "name": "Anu", "mark": 88 }
```

**Invalid** — `mark` violates `maximum: 100`:

```json
{ "registerNo": "SJC22CS001", "name": "Anu", "mark": 120 }
```

Reported as:

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

**Q280(b) — course schema, credits 1–6.** Only the property names and bounds change:

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

`"credits": 2` passes · `0` fails `minimum` · `7` fails `maximum` · `"3"` fails `type`.

**(Error handling — the Q254 half.)** A validator returns a boolean **plus an array of error objects**: `instancePath` (JSON Pointer, `""` = root), `schemaPath` (the keyword that failed), `keyword`, `message`. Because each error carries a path, a form can highlight the exact field; because all errors are collected, the user sees every mistake at once. The document is valid **iff** the array is empty — not exceptions, not one message.

**Traps:** `"required": true` inside a property — `required` is an **array of names** at the object level · claiming validation *throws* on error, or confusing "required" with "non-empty" (`""` satisfies `{"type":"string"}`; `minLength` is what forbids it).

---

#### B3 — PHP ⇄ JSON: serialise, deserialise, round trip · MASTER
**Covers:** Q268 (8+6) · Q273 (14) · Q267 (7+7) · Q279(b) (7) · Q131 at 3 marks (A2).

**Deltas.** Q268 (8+6): serialise/deserialise, then the employees array · Q273 (14): the two functions, then decode → change mark → re-encode · Q267 (7+7): JSON vs PHP types, then decode and display · Q279(b) (7): assoc array → JSON, two lines plus the mapping rule.

**Structure (a 8):** encode 3 · decode 3 · error handling 2. **(b 6):** runnable script 4 · the output 1 · round-trip honesty 1.

**Answer:**

**(a)** *Serialising* = converting an in-memory PHP value into a JSON **string**. *Deserialising* = parsing that string back into a PHP value.

**`json_encode($value, $flags = 0): string|false`** `5:p7`

- PHP **associative** arrays → JSON **objects**; PHP **indexed** arrays → JSON **arrays** — decided automatically by whether keys are sequential integers from 0.
- PHP objects become JSON objects from their **public** properties.
- `JSON_PRETTY_PRINT` indents; `JSON_UNESCAPED_SLASHES`/`_UNICODE` keep `https://` and non-ASCII readable; `JSON_THROW_ON_ERROR` throws instead of returning `false`. Returns `false` on failure (e.g. invalid UTF-8).

**`json_decode($jsonString, bool $assoc = false, int $depth = 512): mixed`** `5:p8`

- Default `$assoc = false` gives **`stdClass` objects** — access with `->`.
- `$assoc = true` gives **associative arrays** — `["..."]`, and `foreach`/`array_map`/`compact()` work naturally. This is the usual choice `5:p8`.
- Returns `null` on failure — *and* for the valid document `null`, which is why the error check matters.

**Error handling:** `json_last_error()` returns an integer code; compare with `JSON_ERROR_NONE` (0). `json_last_error_msg()` gives the message (`Syntax error`, `Malformed UTF-8 characters`) `5:p8`.

**Type mapping (this is Q267(a)):**

| JSON | PHP (assoc `true`) | PHP (default) |
|---|---|---|
| `string` | `string` | `string` |
| `number` (`20`) | `int` | `int` |
| `number` (`499.50`) | `float` | `float` |
| `boolean` | `bool` | `bool` |
| `null` | `null` | `null` |
| `object` | **associative array** | **`stdClass`** |
| `array` | indexed array | array |

JSON has no associative-array type — `object` covers that role `5:p4` — so PHP's two array kinds map onto JSON's two containers but come back as two *different* PHP things unless you pass `true`.

**(b) Decode → modify → re-encode.**

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

**Q268(b) — employees, proving the round trip:**

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

**Q267(b) — decode and display in HTML:**

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

Use `htmlspecialchars()` on every echoed string — the non-Laravel equivalent of Blade's `{{ }}`.

**Round trip: safe for data, lossy for behaviour.** Scalars and arrays survive exactly; resources and objects lose identity (an object returns as `stdClass` or an array); `NaN`/`INF` cannot be encoded at all — which is exactly right when the payload is a database row.

**Traps:** forgetting `true` and then writing `$data["name"]` on a `stdClass` — *Cannot use object of type stdClass as array* · encoding **inside** the fetch loop, which produces `{...}{...}` `5:p9`.

---

#### B4 — Laravel, MVC, features, structure, setup · MASTER (the biggest 14-marker)
**Covers:** Q255 (14) · Q261(a) (6) · Q269 (7+7) · Q274 (14) · Q281 (7+7) · Q282 (7+7) · Q154 at 3 marks (A17).

**Deltas.** Q255 (14): MVC + the request walk-through · Q261(a) (6): the diagram alone — box + arrow + label · Q269 (7+7): MVC, then directories · Q274 (14): + **setup steps** · Q281 (7+7): + the student-app mapping · Q282 (7+7): directories, four rows expanded.

**Structure (a 8):** what Laravel is + why 2 · MVC roles 3 · diagram 3 · worked example inside the roles. **(b 6):** features 2 · directories 3 · setup 1.

**Answer:**

**(a)** Laravel is a free, open-source PHP framework supplying routing, an ORM, templating, authentication and a standard project structure out of the box `5:p10` — because *connect → query → loop → render* works but becomes repetitive and error-prone at scale. **A library is something your code calls; a framework calls your code** `5:p10`.

Laravel implements **MVC**, one job each `5:p11`:

- **Model** — data layer: talks to the database, holds business rules, knows nothing about HTML. `app/Models/Student.php`.
- **View** — presentation: renders HTML from the data it is given, knows nothing about SQL. `resources/views/students/index.blade.php`.
- **Controller** — request handler: receives the request, asks the model, hands data to a view or redirects. `app/Http/Controllers/StudentController.php`.

Two rules examiners look for `5:p11`: **the controller never talks to the browser directly, and the model never renders HTML.**

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

Label the arrows: *request →*, *calls model*, *data*, *renders*, *response*. The controller calls the model **first**, then hands its data to the view `5:p11`.

**Worked example — `GET /students`:**

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

The user never sees SQL, the model never sees HTML, the controller contains neither — that separation is the answer to "how does MVC organise application code".

**(b) Features and structure.**

| Feature | What it gives you | What it replaces |
|---|---|---|
| **Eloquent ORM** | tables as objects — `Student::find(1)` | hand-written `mysqli_query()` `5:p12` |
| **Blade** | `@if`/`@foreach` compiled to cached PHP | `<?php ?>` soup `5:p12` |
| **Artisan CLI** | `make:controller`, `migrate`, `route:list` | manual file creation `5:p12` |
| **Routing / middleware / migrations / auth** | URL mapping, request filtering, versioned schema, login | `$_SERVER` switches and `ALTER TABLE` `5:p12` |

| Directory | Role |
|---|---|
| `app/` | your code — `Models/`, `Http/Controllers/`, `Http/Middleware/`, `Providers/` |
| `routes/` | `web.php`, `api.php`, `console.php` — the URL→code table `5:p13` |
| `resources/views/` | Blade templates `5:p13` |
| `database/` | `migrations/` (versioned schema), `seeders/`, `factories/` `5:p13` |
| `public/` | the **only** web-exposed folder — `index.php` front controller, assets |
| `config/` | configuration (`database.php`, `app.php`) |
| `storage/` | logs, compiled Blade, cache, sessions, uploads — must be writable |
| `bootstrap/app.php` | wires middleware, providers, routing (Laravel 11+) |
| `vendor/` | Composer packages — never edit |

**Purpose of the structure (Q274a, Q154):** *convention over configuration* — `app/Http/Controllers` is a fixed address, so `artisan` writes there and the router finds it with zero config; any Laravel developer navigates any project; only `public/` is exposed, so `.env` and `storage/` cannot be downloaded.

**Setup steps (Q274b):**

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

**Student-management mapping (Q281b):**

| Concern | Layer | Concrete artefact |
|---|---|---|
| `students` table, columns, relationships | **Model** | `app/Models/Student.php` + a migration |
| fetch all / find one / insert / update / delete | **Model** (queries) called by **Controller** | `Student::all()`, `::find()`, `->save()`, `->delete()` |
| list page, create form, edit form, detail page | **View** | `students/index`, `create`, `edit`, `show` |
| validate input, decide view vs redirect, flash | **Controller** | `StudentController@store` |
| which URL hits which method | **Router** | `Route::resource('students', StudentController::class)` |

**Traps:** drawing MVC as a **line** (User→Model→View→Controller) — the controller is the entry point and *calls* the model · saying the **view queries the database**, which is a marked negative.

---

#### B5 — Routing in detail · MASTER
**Covers:** Q258(a) (10) · Q270(a) (7) · Q284 (7+7) · Q275(a) (7) · Q261(b) (8) · Q134/155 at 3 marks (A5).

**Deltas.** Q258(a) (10): all six named sub-topics · Q261(b) (8): mechanisms, plus `route:list` · Q270(a) (7): examples only · Q284 (7+7): GET/POST + named, then the form and its submission · Q275(a): add B6's middleware line.

**Structure (10):** definition + `web.php` + front controller 2 · verbs and targets 2 · parameters 2 · constraints 1 · named routes 2 · groups 1.

**Answer:**

A route maps a URL and an HTTP verb to the code that handles it — the entry point of every request; all browser routes live in `routes/web.php` `5:p14`. Every request physically arrives at `public/index.php` (the *front controller*), which boots the framework and asks the router to match the path.

**1. Verbs** — one static method per HTTP method `5:p14`:

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

`Route::match(['get','post'], ...)` answers several verbs, `Route::any(...)` all of them.

**2. Closure or controller** — the second argument is an inline closure or a controller method array, the latter "more common" `5:p14`:

```php
Route::get('/', function () { return "Welcome to Saintgits CSE"; });   // closure
Route::get('/students', [StudentController::class, 'index']);          // controller
```

Closures suit a one-line landing page; anything with logic belongs in a controller, because closures cannot be cached by `route:cache` or unit-tested.

**3. Parameters** — `{name}` is captured from the URL and passed **positionally**:

```php
Route::get('/student/{id}', [StudentController::class, 'show']);        // required
Route::get('/student/{id?}', [StudentController::class, 'show']);       // optional

// the method receives it by name
public function show($id) { return "Student " . $id; }

// two parameters — order matters
Route::get('/student/{id}/subject/{sub}', [StudentController::class, 'subject']);
```

**4. Constraints** — `->where()` restricts a parameter with a regex, so a non-matching URL 404s at the router:

```php
Route::get('/student/{id}', [StudentController::class, 'show'])->where('id', '[0-9]+');
Route::get('/post/{slug}', [PostController::class, 'show'])->where('slug', '[A-Za-z0-9-]+');
// global pattern, in a service provider:
// Route::pattern('id', '[0-9]+');
```

**5. Named routes** — `->name()` attaches a symbol, `route('name')` builds the URL:

```php
Route::get('/students', [StudentController::class, 'index'])->name('students.index');
Route::get('/student/{id}', [StudentController::class, 'show'])->name('students.show');

$url = route('students.index');                       // http://host/students
$url = route('students.show', ['id' => 5]);           // http://host/student/5
return redirect()->route('students.index');           // redirect by name
```

**Justification mark:** without names, `/students` is duplicated in views, controllers and redirects and a rename means finding every copy; with a name the URL is defined **once** and every `route()` call follows.

**6. Groups** — prefix, name prefix, middleware and domain declared once:

```php
Route::prefix('admin')->name('admin.')->middleware('auth')->group(function () {
    Route::get('/students', [StudentController::class, 'index'])->name('students.index');
    Route::get('/students/create', [StudentController::class, 'create'])->name('students.create');
});
// URL  /admin/students        name  admin.students.index      requires login
```

**Q284(b) — the form and its submission:**

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

**GET shows the form, POST processes it, the `action` uses `route()`** so the URL is never hard-coded. `@csrf` is mandatory — Laravel rejects a POST without the token.

**The request's journey through the router:**

```text
URL + verb  →  public/index.php  →  Router matches (method + URI + constraints)
            →  route's middleware stack runs
            →  handler: closure, or Controller@method resolved from the container
            →  parameters injected (route params, bound models, Request)
            →  return value: string | view | redirect | JsonResponse
```

**Traps:** using `Route::get()` for a form submission — it puts data in the URL and a refresh re-triggers it · claiming named routes change the URL (they decouple code *from* it).

---

#### B6 — Middleware: types, custom middleware, auth flow · MASTER
**Covers:** Q258(b) (4) · Q264(a) (8) · Q283 (7+7) · Q275(b) (7) · Q135/146/156 at 3 marks (A6).

**Deltas.** Q258(b) (4): `make:middleware`, `handle()`, register, attach · Q264(a) (8): concept **with types** plus the `handle()` code · Q283 (7+7): auth/filtering, then a protected route and the flow · Q275(b) (7): one protected route — 4 lines plus a flow sentence.

**Structure (8):** definition + pipeline position 2 · `handle()` and `$next` 2 · three types + registration 2 · a complete class 2.

**Answer:**

Middleware is code that runs **before** a request reaches its controller, or **after** the response is built `5:p16` — the cross-cutting concerns you would otherwise copy into every controller: `auth`, logging, permissions, rate limiting, forced HTTPS, locale, input trimming.

**Mechanism — one method, one decision:**

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

The whole idea is `$next($request)`: calling it means "carry on", **not** calling it (returning a redirect or `abort(403)`) is precisely how a request is blocked. Before `$next` runs on the way in, after it on the way out.

**Three types, by where they are registered:**

| Type | Scope | Where registered |
|---|---|---|
| **Global** | every request, no opt-in | `bootstrap/app.php` `->withMiddleware(...)` (L11+) or `$middleware` in `app/Http/Kernel.php` (L10-) |
| **Group** | a named bundle — `web` (session, CSRF, cookies), `api` | `$middlewareGroups` / `$m->group()` |
| **Route** | only routes that name it | `->middleware('auth')`, `->middleware([A::class, B::class])` |

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

**A protected route and the request flow:**

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

1. Browser sends `GET /dashboard`.
2. `public/index.php` boots the app; the **router matches** the URI.
3. The router assembles the **stack** (global → group → route) and pushes the request through, outermost first.
4. `auth` runs **before** the controller: not logged in ⇒ redirect to `/login`, controller never constructed; logged in ⇒ `$next($request)`.
5. The **controller** runs, queries the **model**, returns a `view()`.
6. The response travels back **out** through the same middleware in reverse, modified if needed.
7. The response reaches the browser.

**Why separate from the controller `5:p16`:** one line on the route, one class, impossible to forget — and removable or reorderable without touching a controller. That is the justification mark.

**Traps:** forgetting `return $next($request)` on the success path — the request dies silently and you get a blank page · saying middleware "runs after the controller" (it wraps it).

---

#### B7 — Controllers, resource controllers, third-party packages
**Covers:** Q257 (8+6) · Q275 (controller half) · Q157 at 3 marks (A18) · Q138 (A9).

**Deltas.** Q257(a) (8): benefits + the 7-action table · Q257(b) (6): packages extending routing/middleware, **not in the deck** · Q275: B5 + B6 + one controller method.

**Structure (a 8):** controller + why not closures 2 · resource + `--resource` + `Route::resource` 2 · seven actions 3 · benefits 1. **(b 6):** Composer + service provider 2 · packages that add routes/middleware 2 · using them well 2.

**Answer:**

**(a)** A controller groups related request-handling logic into one class, so `routes/web.php` stays short `5:p15`. `php artisan make:controller StudentController` scaffolds into `app/Http/Controllers/`; each public method handles one route and ends in a **view** or a **redirect**.

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

A **resource controller** goes further: seven methods and route names following a fixed RESTful convention, generated with `--resource` and wired with one line.

```bash
php artisan make:controller StudentController --resource
```

```php
Route::resource('students', StudentController::class);
```

| # | Method | Verb | URI | Name | Job |
|---|---|---|---|---|---|
| 1 | `index()` | GET | `/students` | `students.index` | list all |
| 2 | `create()` | GET | `/students/create` | `students.create` | show empty form |
| 3 | `store()` | POST | `/students` | `students.store` | insert + redirect |
| 4 | `show()` | GET | `/students/{student}` | `students.show` | display one |
| 5 | `edit()` | GET | `/students/{student}/edit` | `students.edit` | show filled form |
| 6 | `update()` | PUT/PATCH | `/students/{student}` | `students.update` | save changes |
| 7 | `destroy()` | DELETE | `/students/{student}` | `students.destroy` | delete |

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

**Benefits:** one line replaces seven, so a verb/URI pair cannot be got wrong · names are predictable, so `route('students.edit', $id)` needs no lookup · every resource is structured identically · `->only()`/`->except()` trim it · the pairs match what `fetch()` expects.

**(b) Third-party packages** *(standard, not in your deck)*. Installed with Composer and auto-discovered through their **service provider** — the package's hook into the application: it registers bindings, publishes config, loads views and **registers routes and middleware**.

1. **Packages that add routes** — the provider loads its own route file:

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

This is how Breeze or Horizon exposes its screens: install it and URLs appear without touching your `routes/web.php`.

2. **Packages that add middleware** — a global/group registration, or an alias you attach yourself:

```php
// the package registers ...
$middleware->alias(['role' => \Spatie\Permission\Middleware\RoleMiddleware::class]);

// ... and you use it on your own routes
Route::get('/admin', [AdminController::class, 'index'])->middleware('role:admin');
```

Sanctum (`auth:sanctum`) and `spatie/laravel-permission` (`role:`, `permission:`) work exactly this way.

**Using them well:** prefer packages that ship a service provider (`vendor:publish`), attach their middleware **by alias on the routes that need it**, scope their routes behind your own `auth`, and pin versions. A package's global middleware runs on *every* request, including your login page.

**Traps:** mixing the order of `create`/`store` or the verbs of `update`/`destroy` — `store` is POST to the collection, `update` PUT to the member · saying `Route::resource` creates a *controller* (it creates **routes**).

---

#### B8 — Route model binding · MASTER
**Covers:** Q276(a) (7) · Q285 (7+7) · Q262(b) (6) · Q270(b) (part) · Q137/158 at 3 marks (A8).

**Deltas.** Q262(b) (6): what binding is + the two types + the 404, no views · Q285 (7+7): implicit vs explicit, then controller + view · Q276: the binding half of a hybrid · Q270(b): table A15 · Q137: implicit example only, three lines.

**Structure (7):** problem it solves 1 · implicit binding 2 · automatic 404 1 · custom key 1 · explicit binding 1 · controller + view 1.

**Answer:**

**(a)** The manual version first — that is what binding replaces:

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

Three lines of ceremony, repeated in `show`, `edit`, `update`, `destroy`; forget the `if` once and a "property on null" crash replaces a 404.

**Route model binding** makes Laravel do it: it fetches the record matching a route parameter and hands the model to the controller — no manual query `5:p18`. `{student}` is a placeholder, and **type-hinting the matching parameter as a Model** triggers lookup **by ID**; no matching record ⇒ **automatic 404** `5:p18`.

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

**Type 1 — implicit.** Nothing is declared: the parameter name `{student}` matches the type-hinted `$student` and Laravel resolves `Student` by primary key. That naming agreement *is* the binding. To bind another column, name it in the route or override the model's key:

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

**Type 2 — explicit.** You declare the resolution with `Route::bind()`, typically in `AppServiceProvider::boot()` (older: `RouteServiceProvider`), when the lookup is not a simple key — a slug, a composite, a soft-deleted record, a tenant-scoped query:

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

`firstOrFail()` throws `ModelNotFoundException`, rendered as a 404 — what implicit binding gives free.

| | Implicit | Explicit |
|---|---|---|
| Declared by | parameter name + type-hint | `Route::bind('param', fn)` |
| Where | route + method signature | a service provider |
| Key | primary key, or `{param:column}` | anything you write |
| Use when | 90% of cases — plain `id` lookups | slugs, composite keys, scoped queries |

**(b) Controller method + view.**

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

The controller contains **no query at all** — the type-hint did the work, and `/student/9999` is a clean 404.

**Why it beats manual `find()`:** it removes a repeated three-line pattern, makes the null check **impossible to forget**, and keeps the signature self-documenting.

**Traps:** parameter and variable names must **match** — `{id}` with `Student $student` does not bind, it injects the raw string · `Route::bind` belongs in a service provider's `boot()`, not in `routes/web.php`.

---

#### B9 — Views, passing data, sharing data, redirections · MASTER
**Covers:** Q259 (10+4) · Q263(b) (6) · Q276 (redirect half) · Q156–159 at 3 marks (A19).

**Deltas.** Q259(a) (10): views, three ways to pass data, closures vs controllers · Q259(b) (4): basic, back, flash, named · Q263(b) (6): + **sharing with all views** · Q276(b) (7): display via binding, then redirect.

**Structure (a 10):** what a view is + dot notation 2 · three ways to pass data 3 · controller returning views + closures vs controllers 3 · sharing with all views 2. **(b 4):** `redirect`/`back`/`route` 2 · flash + `session()` 2.

**Answer:**

**(a)** A view is the **presentation layer**: a template rendering HTML from the data it is handed. Views live in `resources/views/` as `*.blade.php` `5:p19`; `view('name', $data)` renders one.

**Creating a view is creating a file:**

```text
resources/views/students/index.blade.php     →  view('students.index')
resources/views/students/show.blade.php      →  view('students.show')
resources/views/layout.blade.php             →  view('layout')
```

Dot notation maps to folders `5:p19`: `students.index` is `resources/views/students/index.blade.php` — the dot is a *directory separator*.

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

`compact('students')` bundles a variable into an array keyed by its own name `5:p19`; inside the template each key becomes a PHP variable.

**The controller's job here** — *a controller's most common job is choosing a view and handing it the data it needs* `5:p19`:

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
| Fine for | a one-line landing page, a prototype | anything with logic, queries, validation |
| Testable | no | yes |
| Cacheable | no — `route:cache` refuses closures | yes |
| Reusable | no | yes — many routes, one method |
| Grows well | no: 40 routes × inline logic = an unmaintainable file `5:p15` | yes |

```php
// closure — acceptable only for something this small
Route::get('/', function () { return view('welcome'); });

// controller — the normal choice
Route::get('/students', [StudentController::class, 'index']);
```

**Sharing data with ALL views (Q263(b)c — standard, not in your deck).** When every page needs the same value, share it once in a service provider instead of from every controller:

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

`View::share` makes `$collegeName` available in **every** template; a **view composer** does the same scoped to named views, run only when they render.

**(b) Redirections.** Not every method ends in a view — after a form submission, redirecting is usually right `5:p20`.

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

Flash data is written to the session for exactly one subsequent request `5:p20`:

```blade
@if (session('success'))
    <div class="alert alert-success">{{ session('success') }}</div>
@endif
```

Because it is consumed on read, a refresh does not show it twice.

**Why redirect after POST** `5:p20`: *"redirecting after a successful POST prevents accidental duplicate form resubmission"* — POST/Redirect/GET, so F5 re-fetches the list instead of re-inserting.

**Q276(b) — display via binding, redirect to the list after saving:**

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

**Traps:** `view('students.index.php')` — the extension is never part of the name, and dots are folder separators · passing a bare collection as the second argument (it must be an array keyed by variable name).

---

#### B10 — Blade: inheritance, echoing, control structures · MASTER (highest-frequency Part B theme)
**Covers:** Q260(b) (7) · Q265(b) (9) · Q277 (7+7) · Q286 (7+7) · Q136/159/160 at 3 marks (A7, A19, A20).

**Deltas.** Q260(b) (7): inheritance only · Q265(b) (9): five named features — inheritance, directives, conditionals, loops, **data binding** — five short blocks · Q277 (7+7): echoing + control structures, then the pass/fail view · Q286 (7+7): the same view, "Pass" at mark ≥ 40.

**Structure (9):** what Blade is 2 · echoing and escaping 2 · conditionals 2 · loops 2 · inheritance 3.

**Answer:**

**(a) What Blade is.** Laravel's templating engine: directives (`@if`, `@foreach`) inside HTML instead of switching in and out of `<?php ?>` `5:p22`. Templates compile to ordinary PHP and are cached, so there is **no real performance cost**.

**Echoing — the security-critical choice `5:p23`:**

| Syntax | Behaviour |
|---|---|
| `{{ $variable }}` | echoes, **automatically escaped** — XSS-safe |
| `{!! $variable !!}` | echoes **raw, unescaped** HTML — trusted content only |
| `{{-- comment --}}` | Blade comment, never rendered |

```blade
<h2>Welcome, {{ $student->name }}</h2>
<p>{{ $bio ?? 'No bio provided.' }}</p>
{!! $trustedHtmlBlock !!}
{{-- This comment never reaches the browser --}}
```

`{{ }}` compiles to `echo htmlspecialchars($value)`: `<script>alert(1)</script>` prints as text under `{{ }}` and executes under `{!! !!}` `5:p28`. Any PHP expression works inside the braces.

**(b) Conditionals.**

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

`@unless` runs when the condition is **false**; `@isset` and `@empty` test set-and-not-null and emptiness `5:p24`. All compile to plain PHP.

**(c) Loops.**

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

`@for(...)` and `@while(...)` also exist `5:p25`; `$loop` carries `index`, `iteration`, `first`, `last`, `count`, `remaining`, which removes the manual counter.

**(d) Template inheritance.**

| Directive | Role |
|---|---|
| `@extends('layout')` | declares the parent layout |
| `@section('name') ... @endsection` | defines a named block of content |
| `@yield('name')` | **in the parent** — where a child's section is inserted |
| `@include('partial')` | pulls in a reusable chunk |

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

`@extends` must be the **first** construct in the child; `@yield` takes a default; `@section('name', 'value')` is the one-line form; `@include` is *not* inheritance.

**(e) The pass/fail view the paper keeps asking for (Q277b, Q286b):**

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

If the marks arrive as a plain array, `@forelse` renders a message for an empty list (standard, not in your deck):

```blade
@forelse ($marks as $m)
    <li>{{ $m }}</li>
@empty
    <li>No marks recorded.</li>
@endforelse
```

**Traps:** `{!! !!}` on user-supplied data — an instant security deduction, flagged twice by the deck `5:p23`, `5:p28` · confusing `@section` (child defines) with `@yield` (parent inserts).

---

#### B11 — Sub-domain routing · 7 marks (Q260a)
**Status:** *(standard, not in your deck — no slide covers sub-domains.)*

**Structure (7):** what it is + `Route::domain()` 2 · code, fixed and parameterised 2 · two use cases 2 · caveats 1.

**Answer:**

Sub-domain routing lets a **single application** serve different host names from different route tables; the host is part of the route, so the router — not your controller — decides which module answers.

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

`{department}` is captured like a URI parameter and can be type-hinted (`index(string $department)`) or used in a `Route::bind` to scope queries per tenant.

**Use cases:** multi-tenant SaaS (isolation in the route layer) · a separate admin surface with its own middleware · per-department portals · localisation (`en.`, `fr.`).

**Caveats that earn the last mark:** the domain parameter must be declared before use; local testing needs a hosts entry or wildcard DNS; cookies/sessions must be scoped (`SESSION_DOMAIN`) or a login leaks across tenants. It is **not** authorisation.

**Traps:** `Route::domain()` takes a **host**, not a path · assuming the sub-domain is a security boundary.

---

#### B12 — The HTTP request lifecycle, route → middleware → controller → response · 5 marks (Q265a)
**Status:** the six-step chain is in the deck `5:p21`; the front-controller detail is standard.

**Structure (5):** entry + router match 1 · middleware 1 · controller + binding 1 · view or redirect 1 · response out 1.

**Answer:**

Every request takes the same path `5:p21`:

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

1. **Front controller.** Nginx/Apache points at `public/`, so every URL arrives at `public/index.php`, which bootstraps config, providers and error handling, then hands the request to the kernel.
2. **Routing.** The router matches **method + URI** against `routes/web.php`, honouring constraints; no match ⇒ 404 before your code runs.
3. **Middleware.** The route's stack (global → group → route) runs around the request; `auth` may stop it, and the controller is never invoked `5:p16`.
4. **Controller + model.** The container resolves the controller; type-hinted parameters resolve by **route model binding** — row or 404 `5:p18` — then the method calls the model.
5. **The branch `5:p21`.** A **GET** ends in `view()`, a **POST** in `redirect()` with flash data, so a refresh cannot duplicate the write `5:p20`.
6. **Response.** Back out through the same middleware in reverse, then to the browser.

**Opener:** *Laravel funnels every request through a single front controller, matches it to a route, filters it through middleware, dispatches it to a controller that talks to models, and returns a rendered view or a redirect.*

**Traps:** starting at the controller — the route match happens first and is a mark · forgetting a 404 comes from **two** places: no route match, or failed model binding.

---

#### B13 — Service providers and migrations · 10 + 4 (Q256)
**Status:** *(standard, not in your deck — neither topic has a slide. Do not claim the deck.)*

**Structure (a 10):** what a provider is 2 · `register()` vs `boot()` 2 · role in the lifecycle 2 · DI and the container 2 · worked provider + consumer 2. **(b 4):** what a migration is 2 · class and commands 2.

**Answer:**

**(a) Service providers.** A provider is where a Laravel application is *assembled*: everything the framework ships — router, database layer, queue, view engine — is registered by one, and `AppServiceProvider.php` is where you register yours. Laravel reads the list in `bootstrap/providers.php` (L11+) or `config/app.php`, then calls two methods:

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

**`register()` vs `boot()`.** `register()` runs for **all** providers first, then `boot()` for all of them — so in `register()` you may only *bind*, never assume another provider's bindings exist; in `boot()` everything is available, so routes, views, events and Blade directives go there. Binding in `boot()` works but is fragile.

**Role in the lifecycle:**

```text
composer autoload → bootstrap/app.php → load config (.env)
   → register all providers' register()   [bindings only]
   → boot all providers' boot()           [routes, views, events, directives]
   → handle the request (route → middleware → controller)
   → send the response → terminate (terminable middleware, queued work)
```

**Dependency injection.** The **service container** is a keyed map of "how to build this class"; a provider fills it and the framework reads it whenever a controller, middleware or job type-hints a dependency:

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

The controller asks for an abstraction, the provider picks the concrete class: swapping Razorpay for Stripe is a one-line provider change, and tests bind a fake. That is what "facilitate dependency injection and service management" means; deferred providers register only when requested.

**(b) Migrations.** A migration is a version-controlled PHP file describing one change to the schema — it is to schema what Git is to code: reproducible, reviewable, reversible.

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

`up()` applies, `down()` reverses — hence a migration must be reversible. Laravel records which ran in the `migrations` table, so `migrate` is idempotent; `make:model Student -m` writes model and migration together.

**Traps:** putting route/view/event code in `register()` (it belongs in `boot()`) · calling a migration a "backup" or a "seeder" — a migration changes **schema**, a seeder inserts **data**.

---

## 4. Code you must write by hand

Fourteen drills. Do each **on paper, from memory**, then check. Write these cold and every code-bearing question in the bank (Q131, 137, 254, 262–286) is covered.

### D1 — A valid JSON student document
One student, nested address, marks array, every JSON type at least once.

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

Six types check: string, number, boolean, null, object, array. Root is an object, no trailing comma, every key double-quoted.

**Memorise:** `{ }` = object, `[ ]` = array, keys double-quoted, and **the type is in the value, not in quotes**.

### D2 — Nested college → departments → students
Three levels, the Q278(b) shape. Count brackets before you write.

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

**Memorise:** *object → array of objects → array of objects*; each `[` gets its `]`, and students live **inside** their department.

### D3 — JSON Schema for a student: required fields + mark bounds
Required `registerNo`, `name`, `mark`; mark 0–100; subjects an array of strings; nothing extra.

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

**Memorise:** `"required"` is an **array of names at the object level**; `minimum`/`maximum` sit inside the number's schema, not at the root.

### D4 — Course-credits schema (credits 1–6)
Q280(b) verbatim. `code`, `title`, `credits` required; credits an integer 1–6.

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

Test yourself: `credits: 4` valid · `0` fails `minimum` · `7` fails `maximum` · `"4"` fails `type` · `4.5` fails `integer`.

**Memorise:** `"integer"`, not `"int"`; bounds are **inclusive**; a missing required key fails at the *root* path.

### D5 — PHP decode → modify → re-encode
Q131/Q273(b). Decode, bump the mark, add a computed result, re-encode pretty, handle a parse error.

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

**Memorise:** `json_decode($json, true)` → `["key"]`; `json_encode($data, JSON_PRETTY_PRINT)`; **always** the `json_last_error()` check.

### D6 — Encode an associative array of employees, then decode it back
Q268(b). Two employees, encode, decode, print — proving the round trip.

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

An **indexed** array of **associative** arrays → a JSON **array of objects**: the commonest real payload there is.

**Memorise:** indexed → `[ ]`, associative → `{ }`, and the round trip is value-identical (`===` is `true`) for scalars.

### D7 — `JSON.parse()` / `JSON.stringify()` demo
Q262(a). String → object, mutate, object → string, then a `fetch` round trip.

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

**Memorise:** `JSON.parse(string) → object`, `JSON.stringify(object) → string`; parse **throws** on bad JSON, stringify **drops** `undefined` and functions and turns `Date` into a string.

### D8 — A routes file: GET, POST, named, parameterised, constrained, grouped
The route table for a student resource, written by hand.

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

Order matters: `/students/create` must be declared **before** `/student/{id}`, or `create` is captured as an id.

**Memorise:** `Route::get('/path', [Controller::class, 'method'])->name('name');` and `->where('id','[0-9]+')`.

### D9 — `Route::resource` + a Student controller skeleton
One line of routing, seven methods, the shape of each.

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

Generated with `php artisan make:controller StudentController --resource`.

**Memorise:** the seven names in order — `index, create, store, show, edit, update, destroy` — and `store`/`update` take `Request` **first**, the bound model second.

### D10 — Middleware that blocks unauthenticated users
Q283(b)/Q275(b). The class, the registration, the protected route.

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

Generated with `php artisan make:middleware EnsureLoggedIn`.

**Memorise:** `public function handle(Request $request, Closure $next)` — block with a redirect or `abort(403)`, allow with `return $next($request);`.

### D11 — Route model binding in a controller method
Q285(b). Route, method, view — no manual `find()` anywhere.

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

**Memorise:** parameter and variable names must be **identical** — `{student}` + `Student $student`.

### D12 — Blade layout + child view with a loop and an if
Parent with `@yield`, child with `@extends`, `@section`, `@foreach`, `@if`, `$loop`.

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

**Memorise:** child = `@extends` + `@section ... @endsection`; parent = `@yield`; `@foreach` gets `$loop->iteration` and `$loop->last` free.

### D13 — Redirect after save with a flash message
The POST/Redirect/GET pattern, message rendered on the next page.

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

### D14 — Validation + error display
The other half of every CRUD answer: prove the input was checked and the errors are shown.

```php
<?php
$validated = $request->validate([
    'name' => 'required|string|max:100',
    'mark' => 'required|numeric|min:0|max:100',
    'email'=> 'nullable|email',
]);
?>
```

On failure Laravel **redirects back automatically** with the errors and old input — you write no `if`. On success `$validated` holds only the keys you named, so a malicious extra field cannot reach `create()`.

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

**Memorise:** `$request->validate([...])` returns the **safe** subset; `@csrf` is mandatory in every POST form; `old()` repopulates, `@error`/`$errors->all()` displays.

---

## 5. Night-before memorise sheet

Read aloud twice. If you know only this page, you still pass Part A.

| Item | Exact syntax / signature | Why it is asked |
|---|---|---|
| Two JSON containers | `{ }` object, `[ ]` array | opening line `5:p3` |
| The six types | string, number, boolean, null, object, array | 6 questions (140, 144, 148, 262, 271, 279) `5:p4` |
| Key rule | `{"name": "Anu"}` — keys always double-quoted | the strictness trap `5:p3` |
| Forbidden | no comments, no trailing comma, one top-level value | syntax 7-markers |
| PHP → JSON | `json_encode($data)` | Q151, 268, 273, 279 `5:p7` |
| PHP → JSON pretty | `json_encode($data, JSON_PRETTY_PRINT)` | named in the question |
| JSON → PHP object | `json_decode($json)` → `->key` | Q267 `5:p8` |
| JSON → PHP array | `json_decode($json, true)` → `["key"]` | the default right answer `5:p8` |
| Error check | `json_last_error() !== JSON_ERROR_NONE` | a marked point `5:p8` |
| Type mapping | assoc array → object; indexed array → array | half the PHP/JSON questions `5:p7` |
| API header | `header("Content-Type: application/json");` | the DB→JSON slide `5:p9` |
| Schema root | `"$schema": "https://json-schema.org/draft/2020-12/schema"` | Q141 |
| Schema id | `"$id": "https://host/schemas/student.json"` | Q141 |
| Required | `"required": ["name", "mark"]` | array of names, object level |
| Bounds | `"minimum": 0, "maximum": 100` | Q280 credits 1–6 |
| Array items | `"items": { "type": "string" }` | nested arrays |
| JS parse | `JSON.parse(text)` → object | Q262(a) |
| JS stringify | `JSON.stringify(obj)` → string | Q262(a) |
| Framework def. | "framework calls your code; a library is called by your code" | the 1-mark distinction `5:p10` |
| MVC | Model = data, View = presentation, Controller = logic | every Laravel 14-marker `5:p11` |
| MVC rule | "controller never talks to the browser; model never renders HTML" | quotable `5:p11` |
| Features | Eloquent ORM, Blade, Artisan, routing/middleware/migrations/auth | Q142, 153 `5:p12` |
| Setup | `composer create-project laravel/laravel myapp` then `php artisan serve` | Q274(b) `5:p13` |
| Routes file | `routes/web.php` | every routing answer `5:p14` |
| Route to controller | `Route::get('/student/{id}', [StudentController::class,'show'])` | the canonical line `5:p14` |
| Named route | `->name('students.index')` + `route('students.index')` | Q258(a), 284 |
| Constraint | `->where('id', '[0-9]+')` | Q258(a) |
| Group | `Route::prefix('admin')->name('admin.')->middleware('auth')->group(...)` | Q258(a) |
| Resource routes | `Route::resource('students', StudentController::class)` | Q257(a) |
| Resource controller | `php artisan make:controller StudentController --resource` | Q138, 257 |
| The 7 actions | `index, create, store, show, edit, update, destroy` | Q138 table |
| Middleware method | `public function handle(Request $request, Closure $next)` | Q264(a), 283 |
| Middleware attach | `->middleware('auth')` | Q146, 283 `5:p16` |
| Middleware allow | `return $next($request);` | the mechanism |
| Middleware block | `return redirect('/login');` / `abort(403);` | short-circuit |
| Binding route | `Route::get('/student/{student}', ...)` | Q137, 285 `5:p18` |
| Binding method | `public function show(Student $student)` | implicit binding `5:p18` |
| Binding 404 | automatic when no row matches | a mark on its own `5:p18` |
| Explicit binding | `Route::bind('student', fn ($v) => Student::where(...)->firstOrFail())` | Q285(a) |
| View call | `return view('students.index', compact('students'));` | Q259 `5:p19` |
| Other data forms | `view('x', ['k' => 'v'])` and `view('x')->with('k','v')` | Q259(a) |
| Dot notation | `students.index` = `resources/views/students/index.blade.php` | Q259(a) `5:p19` |
| Redirect | `return redirect('/students');` | Q259(b) `5:p20` |
| Redirect by name | `return redirect()->route('students.index');` | preferred form |
| Redirect back | `return back()->withInput();` | after failed validation |
| Flash | `->with('success','Saved');` | one request only `5:p20` |
| Blade echo | `{{ $var }}` escaped · `{!! $var !!}` raw | the security mark `5:p23` |
| Blade comment | `{{-- ... --}}` | never rendered `5:p23` |
| Blade if | `@if ... @elseif ... @else ... @endif`, `@unless ... @endunless` | Q286 `5:p24` |
| Blade loop | `@foreach ($items as $item) ... @endforeach`, `$loop->iteration` | Q160, 277 `5:p25` |
| Inheritance child | `@extends('layouts.app')` + `@section('content') ... @endsection` | Q136, 260(b) `5:p26` |
| Inheritance parent | `@yield('content')` | Q260(b) `5:p26` |
| Include | `@include('partials.navbar')` | Q260(b) `5:p26` |
| Request lifecycle | route → middleware → controller → model → view/redirect → response | Q265(a) `5:p21` |
| Validation | `$request->validate([...])` | every store/update |
| Full redirect line | `return redirect()->route('students.index')->with('success','Saved');` | Q276(b) |

---

## 6. Diagram + figure index

The deck is page-marked and text-only — its diagrams are SmartArt the PDF flattens into phrases. Redraw them from the description; that is also the best revision.

| Page | What is on it | What to redraw |
|---|---|---|
| `5:p3` | JSON syntax panel — code beside five bullet rules | two columns, legal vs illegal per rule (covers a 7-mark question) |
| `5:p4` | Six-row data-type table | copy it exactly, including "no associative-array type" |
| `5:p5` | Nested JSON panel (address + courses array) | a tree: root → address → city/pin; root → courses → code/title |
| `5:p6` | Four-quadrant what/why/where on JSON Schema | problem · what it specifies · why for APIs · where used |
| `5:p9` | DB rows → array → `json_encode` | `mysqli_query` → `while fetch_assoc` → `$students[]` → one encode → header |
| `5:p10` | Problem at scale, what Laravel provides, framework vs library | the "framework calls your code" line lives here |
| `5:p11` | **MVC chain** — User → Controller → Model → View → Response | five boxes, four **labelled** arrows (Q261a) |
| `5:p13` | Setup commands + four-branch folder tree | add `public/`, `config/`, `storage/` from §2.18 (Q282) |
| `5:p14` | Route definitions: closure and controller routes | learn the `[Controller::class, 'method']` syntax |
| `5:p16` | Four points on middleware | the "why separate" point is the justification mark |
| `5:p17` | Route → middleware → controller chain, one commented panel | three stacked boxes (Q275, Q283) |
| `5:p18` | Route + method showing binding, "$student is already the correct DB row" | redraw with the 404 branch |
| `5:p20` | Redirect options + a `store()` snippet | a decision: GET → view, POST → redirect → flash |
| `5:p21` | **Request lifecycle**, six numbered steps with a 5a/5b branch | the most valuable diagram here — draw as boxes, then as a list (Q265a) |
| `5:p23`–`5:p25` | Blade echoing, conditionals, loops — code beside bullets | copy the three panels; they are the Q277/Q286 answers |
| `5:p26` | Template inheritance — layout and index side by side | parent with a `@yield` hole, child with a `@section` photo (D12) |
| `5:p27` | Six-row Blade directive table | memorise it — a guaranteed 3-marker (Q136/159/160) |
| `5:p28` | Recap — eight one-line takeaways | a night-before checklist; each line is a Part-A answer |

**Draw on a blank page, in order of value:** 1. request lifecycle (`5:p21`) — Q265(a), Q261(b), Q283(b) · 2. MVC chain (`5:p11`) — Q255, Q261(a), Q269, Q281 · 3. directory tree (`5:p13`) — Q269(b), Q282 · 4. route → middleware → controller (`5:p17`) — Q275, Q283 · 5. Blade inheritance (`5:p26`) — Q260(b).

---

## 7. Say-this-if-grilled defence lines

One sentence each. They answer "but *why*", which is where the last 2 marks live.

1. **Why MVC?** A change in one concern stops rippling — restyle the UI and the SQL is untouched, change the database and the templates are untouched, and each layer tests alone `5:p11`.
2. **What middleware really does?** It wraps the controller: reject the request before your code runs or decorate the response after, with the check in one place instead of thirty methods `5:p16`.
3. **Why binding over manual `find()`?** Three lines you must remember in four methods become zero lines you cannot forget, and a missing row is a 404 not a crash `5:p18`.
4. **Why does Blade escape by default?** Escaping only works when it is the default — an opt-in `htmlspecialchars()` is one forgotten call from XSS `5:p23`.
5. **Why JSON Schema instead of manual `if` validation?** The rules become data: versionable, shareable, publishable in API docs, reusable by any client — and every failure comes back with a path.
6. **Why Laravel over raw PHP?** Raw PHP gives you a language; Laravel gives the decisions already made — routing, ORM, templating, auth, CSRF, hashing `5:p10`.
7. **Why is JSON better than XML for APIs?** Less verbose, maps directly onto the objects and arrays every language has, and parses faster `5:p2`.
8. **Why is JSON so strict?** Two unrelated systems must agree exactly: every permitted dialect is an incompatibility, and a parser cannot be lenient and unambiguous at once `5:p3`.
9. **Why `view()` or `redirect()` and not both?** Different verbs — a GET renders what you asked for, a POST changes state then redirects so a refresh re-reads instead of re-writing `5:p21`, `5:p20`.
10. **Why named routes?** The URL becomes an implementation detail in one file, so a rename is one edit, not a grep `5:p14`.
11. **Why resource controllers?** Seven conventional actions with predictable names replace seven hand-written routes, so CRUD is uniform and `route('students.edit', $id)` needs no lookup.
12. **Why `compact()`?** It builds `['students' => $students]` from the variable's own name, so the key can never disagree with the variable `5:p19`.
13. **Why does Blade compile to PHP?** Compile once, cache, and you get readable templates at no runtime cost — the directives do nothing PHP could not `5:p22`, `5:p27`.
14. **Why does `json_decode` need the error check?** `null` is also a valid JSON document, so `=== null` cannot tell "failed" from "empty" — only `json_last_error()` can `5:p8`.
