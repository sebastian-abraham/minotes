# module 5.pdf -> markdown

Converted from the PDF text layer (pymupdf). Page markers `### p<N>` map 1:1 to PDF pages. `[Image Description: ...]` blocks are placeholders: the page is diagram/figure-heavy and must be rendered and viewed, not guessed.


### p1

MODULE 5
JSON and Laravel
7 Hours of Content Delivery
•
JSON syntax & data types — 1 Hr
•
JSON schema & PHP manipulation — 1 Hr
•
Laravel overview, MVC & setup — 1 Hr
•
Routing, middleware & controllers — 1 Hr
•
Route model binding, views & redirections — 1 Hr
•
Blade templating — 2 Hrs
Web Programming | Saintgits College of Engineering
1


### p2

MODULE V · 1 HR TOPIC
What is JSON & Why It Matters
20CST461
1
JSON = JavaScript Object Notation
A lightweight, text-based format for representing structured data — readable by humans and easy for machines to parse. Despite the name, it's used by virtually 
every programming language, not just JavaScript.
2
Why it replaced XML for most APIs
JSON is far less verbose than XML (no closing tags), maps directly onto common data structures (objects, arrays) that most languages already have, and parses 
faster.
3
Where it shows up
API responses, configuration files, the request/response bodies of almost every modern web service — including the database rows from Module IV, once 
converted.
4
What it is NOT
JSON is a data format, not a programming language — it has no functions, no comments, no logic. It only describes data.
Web Programming | Saintgits College of Engineering
2


### p3

MODULE V · 1 HR TOPIC
JSON Syntax — Objects & Arrays
20CST461
JSON is built from exactly two structures: objects (key-value pairs) and arrays (ordered lists) — everything else nests inside these.
•
{ } defines an object: unordered key-value pairs
•
[ ] defines an array: an ordered list of values
•
Keys are ALWAYS double-quoted strings — single quotes 
are invalid
•
No comments and no trailing commas — strict syntax, 
unlike JavaScript object literals
JSON
{
"name": "Anu",
"age": 20,
"isActive": true,
"marks": [88, 92, 79]
}
Web Programming | Saintgits College of Engineering
3


### p4

MODULE V · 1 HR TOPIC
JSON Data Types
20CST461
Type
Example
Notes
string
"Saintgits"
Always double-quoted
number
20 or 499.50
No distinction between int/float
boolean
true / false
Lowercase, unquoted
null
null
Represents 'no value'
object
{ "city": "Kottayam" }
Nested key-value pairs
array
[88, 92, 79]
Ordered list of any of the above
Note: Unlike PHP arrays, JSON has no separate 'associative array' type — an object covers that role.
Web Programming | Saintgits College of Engineering
4


### p5

MODULE V · 1 HR TOPIC
Nested JSON — Objects Within Objects
20CST461
Real-world JSON is usually nested several levels deep — objects containing arrays of objects, and so on.
•
Any value (including another object or array) can sit inside 
an object or array
•
Nesting models real relationships: a student HAS an 
address, HAS a list of marks
•
Indentation is just for human readability — it has no 
effect on parsing
•
This is the shape API responses typically take, including 
ones built by Laravel later in this module
JSON
{
"name": "Anu",
"address": {
"city": "Kottayam",
"pin": "686532"
},
"courses": [
{ "code": "20CST461", "title": "Web Programming" }
]
}
Web Programming | Saintgits College of Engineering
5


### p6

MODULE V · 1 HR TOPIC
What is JSON Schema?
20CST461
1
The problem it solves
JSON itself has no built-in way to say 'this field is required' or 'this must be a number' — JSON Schema is a separate JSON document that describes those rules for 
another piece of JSON.
2
What it can specify
Required fields, expected data types per field, value constraints (minimum/maximum, string patterns), and the structure of nested objects/arrays.
3
Why it matters for APIs
Before trusting incoming JSON (e.g. from a form submitted via JavaScript, or another service), a schema lets you validate its shape automatically instead of writing 
manual checks for every field.
4
Where it's used
API documentation tools, request validation libraries, and configuration file validation — not required for every JSON use case, but valuable wherever JSON 
crosses a trust boundary.
Web Programming | Saintgits College of Engineering
6


### p7

MODULE V · 1 HR TOPIC
json_encode() — PHP to JSON
20CST461
PHP's built-in json_encode() converts a PHP array or object directly into a JSON-formatted string.
•
json_encode($value) returns a JSON string built from the 
given PHP value
•
PHP associative arrays become JSON objects automatically
•
PHP indexed arrays become JSON arrays automatically
•
JSON_PRETTY_PRINT flag formats the output with 
readable indentation
PHP
<?php
$student = [
"name" => "Anu",
"marks" => [88, 92, 79]
];
echo json_encode($student);
echo json_encode($student, JSON_PRETTY_PRINT);
?>
Web Programming | Saintgits College of Engineering
7


### p8

MODULE V · 1 HR TOPIC
json_decode() — JSON to PHP
20CST461
json_decode() does the reverse — turning a JSON string back into usable PHP data.
•
json_decode($jsonString) returns a PHP object by default
•
json_decode($jsonString, true) returns an associative 
array instead — usually more convenient
•
json_last_error() checks whether decoding actually 
succeeded
•
Common use: reading a JSON request body sent by a 
JavaScript fetch() call
PHP
<?php
$json = '{"name":"Rahul","marks":[72,80]}';
$asObject = json_decode($json);
echo $asObject->name;
$asArray = json_decode($json, true);
echo $asArray["name"];
?>
Web Programming | Saintgits College of Engineering
8


### p9

MODULE V · 1 HR TOPIC
Putting It Together: A Database Row as JSON
20CST461
Combining Module IV's database pattern with json_encode() turns a query result into a ready-to-use API response — no HTML involved at all.
•
Fetch all rows into a plain PHP array first
•
json_encode() the whole array at once, after the loop
•
header("Content-Type: application/json") tells the client 
what kind of response this is
•
This is the foundation of building an API endpoint instead 
of an HTML page
PHP
<?php
header("Content-Type: application/json");
$result = mysqli_query($conn, "SELECT name, marks FROM students");
$students = [];
while ($row = mysqli_fetch_assoc($result)) {
$students[] = $row;
}
echo json_encode($students);
?>
Web Programming | Saintgits College of Engineering
9


### p10

MODULE V · 1 HR TOPIC
What is Laravel & Why Use a Framework?
20CST461
1
The problem at scale
Modules III and IV's hand-written connect → query → loop → render pattern works, but repeating it across dozens of pages in a real application gets repetitive 
and error-prone fast.
2
What Laravel provides
A free, open-source PHP framework that supplies routing, database access (via an ORM), templating, authentication, and project structure out of the box — so 
common problems are solved once, consistently.
3
'Framework' vs. 'library'
A library (like a single PHP function file) is something your code calls. A framework calls your code — it defines the overall structure, and you fill in the specific 
behaviour it asks for.
4
Where it fits in this course
Everything from here builds on the PHP and MySQL fundamentals already covered — Laravel doesn't replace that knowledge, it organizes and accelerates it.
Web Programming | Saintgits College of Engineering
10


### p11

MODULE V · 1 HR TOPIC
The MVC Design Pattern
20CST461
Laravel enforces a separation of concerns: data, logic, and presentation each live in their own place.
User
Requests a page
Controller
Handles the request
Model
Talks to the database
View
Renders the response
Response
Sent back to the user
In practice the Controller calls the Model first, then hands its data to the View — drawn here as one left-to-right journey.
Controller never talks to the browser directly, and the Model never renders HTML — each layer has exactly one job.
Web Programming | Saintgits College of Engineering
11


### p12

MODULE V · 1 HR TOPIC
Key Laravel Features
20CST461
1
Eloquent ORM
Lets you work with database tables as PHP objects and methods (Student::find(1)) instead of writing raw mysqli_query() SQL strings by hand.
2
Blade templating engine
Laravel's view layer — compiles clean directives like @if and @foreach into plain PHP behind the scenes (covered in depth later in this module).
3
Artisan CLI
A command-line tool for scaffolding (php artisan make:controller), running migrations, and many other repetitive setup tasks.
4
Routing, middleware, migrations & auth
Built-in systems for mapping URLs to code, filtering requests, version-controlling database schema changes, and handling user login — each covered as its own 
topic in this module.
Web Programming | Saintgits College of Engineering
12


### p13

MODULE V · 1 HR TOPIC
Setting Up & Application Structure
20CST461
Laravel requires PHP, Composer (PHP's dependency manager), and a database — setup is a few command-line steps.
•
composer create-project laravel/laravel myapp —
scaffolds a new project
•
php artisan serve — runs a local development server
•
app/Http/Controllers/ — your controller classes
•
resources/views/ — your Blade template files
•
routes/web.php — where URL-to-code mappings are 
defined
Shell + Folder Structure
composer create-project laravel/laravel myapp
cd myapp
php artisan serve
myapp/
├── app/Http/Controllers/
├── resources/views/
├── routes/web.php
└── database/migrations/
Web Programming | Saintgits College of Engineering
13


### p14

MODULE V · 1 HR TOPIC
Defining Routes
20CST461
A route maps a URL to the code that should handle it — the entry point for every request in a Laravel app.
•
Routes are defined in routes/web.php
•
Route::get('/path', function) — handles GET requests to 
that path
•
Route::post(), Route::put(), Route::delete() — handle 
other HTTP methods
•
A route can point to a closure (inline function) or, more 
commonly, a controller method
PHP (Laravel)
use Illuminate\Support\Facades\Route;
Route::get('/', function () {
return "Welcome to Saintgits CSE";
});
Route::get('/students', [StudentController::class, 'index']);
Web Programming | Saintgits College of Engineering
14


### p15

MODULE V · 1 HR TOPIC
Controllers
20CST461
Controllers group related request-handling logic into a single class, keeping routes/web.php short and readable.
•
php artisan make:controller StudentController scaffolds a 
new controller file
•
Controllers live in app/Http/Controllers/
•
Each public method typically handles one route
•
A controller method usually ends by returning a view or a 
redirect
PHP (Laravel)
<?php
namespace App\Http\Controllers;
class StudentController extends Controller {
public function index() {
$students = Student::all();
return view('students.index', compact('students'));
}
}
Web Programming | Saintgits College of Engineering
15


### p16

MODULE V · 1 HR TOPIC
Middleware — Filtering Requests
20CST461
1
What middleware does
Code that runs BEFORE a request reaches its controller (or after the response is built) — a filtering/processing layer that wraps around the actual request 
handling.
2
Common uses
Checking whether a user is logged in (auth middleware), logging requests, checking permissions, or rate-limiting how often an endpoint can be called.
3
Applying middleware to a route
Route::get('/dashboard', ...)->middleware('auth'); — this single line ensures the dashboard route only runs its controller logic for logged-in users.
4
Why it's separate from the controller
Keeping this logic out of the controller means the same check (e.g. 'is logged in') doesn't need to be repeated inside every single controller method that needs it.
Web Programming | Saintgits College of Engineering
16


### p17

MODULE V · 1 HR TOPIC
Connecting Routes to Controllers
20CST461
Here's the full picture: a route, protected by middleware, pointing to a controller method.
•
The route declares the URL and which controller method 
should run
•
Middleware (if any) runs first, and can stop the request 
before it reaches the controller
•
The controller method runs last, doing the actual work
•
This three-piece chain — route, middleware, controller —
handles every request in a Laravel app
PHP (Laravel)
// routes/web.php
Route::get('/students', [StudentController::class, 'index'])
->middleware('auth');
// app/Http/Controllers/StudentController.php
public function index() {
$students = Student::all();
return view('students.index', compact('students'));
}
Web Programming | Saintgits College of Engineering
17


### p18

MODULE V · 1 HR TOPIC
Route Model Binding
20CST461
Laravel can automatically fetch a database record matching a route parameter, handing it straight to the controller — no manual query needed.
•
Route::get('/student/{student}', ...) — {student} is a 
placeholder in the URL
•
Type-hinting the matching parameter as a Model triggers 
automatic lookup by ID
•
If no matching record exists, Laravel automatically returns 
a 404 response
•
Saves writing Student::find($id) and a null-check by hand 
in every method
PHP (Laravel)
Route::get('/student/{student}',
[StudentController::class, 'show']);
public function show(Student $student) {
// $student is already the correct DB row
return view('students.show', compact('student'));
}
Web Programming | Saintgits College of Engineering
18


### p19

MODULE V · 1 HR TOPIC
Views — Rendering Blade Templates
20CST461
A controller's most common job is choosing a view and handing it the data it needs to display.
•
view('name', $data) renders a Blade template, passing 
data to it
•
Views live in resources/views/ as .blade.php files
•
compact('students') is a shortcut that bundles a variable 
into an array keyed by its own name
•
Dot notation in view names maps to folders: 
students.index means 
resources/views/students/index.blade.php
PHP (Laravel)
public function index() {
$students = Student::all();
return view('students.index', compact('students'));
}
// equivalent to:
return view('students.index', ['students' => $students]);
Web Programming | Saintgits College of Engineering
19


### p20

MODULE V · 1 HR TOPIC
Redirections
20CST461
Not every controller method ends in a view — after a form submission, redirecting to another route is usually the right move.
•
redirect('/path') sends the browser to a different route
•
redirect()->back() returns to the previous page —
common after a failed validation
•
->with('key', 'value') attaches flash data the next page can 
read (e.g. a success message)
•
Redirecting after a successful POST prevents accidental 
duplicate form resubmission
PHP (Laravel)
public function store(Request $request) {
Student::create($request->all());
return redirect('/students')
->with('message', 'Student added successfully!');
}
Web Programming | Saintgits College of Engineering
20


### p21

MODULE V · 1 HR TOPIC
A Typical Laravel Request, Start to Finish
20CST461
1. Route matches
the URL
2. Middleware
runs checks
3. Controller
method runs
4a. Model Binding
fetches DB data
5a. view()
renders Blade
5b. redirect()
to another route
Response sent to the browser
Step 5 branches: a GET request to show data usually ends in a view; a POST that changes data usually ends in 
a redirect.
Web Programming | Saintgits College of Engineering
21


### p22

MODULE V · 2 HR TOPIC
What is Blade?
20CST461
1
Laravel's templating engine
Blade lets you write clean, readable directives (@if, @foreach) directly inside HTML, instead of constantly switching in and out of <?php ?> blocks like the raw PHP 
from Module IV.
2
It compiles to plain PHP
Behind the scenes, Blade templates are compiled into ordinary PHP code and cached — so there's no real performance cost compared to writing PHP by hand.
3
File naming convention
Blade files end in .blade.php (e.g. index.blade.php) — Laravel uses this extension to know a file should be compiled as a Blade template.
4
Why it matters for this module
Every view() call from the previous topic renders a Blade file — this is the syntax used inside those files to actually display data and control what's shown.
Web Programming | Saintgits College of Engineering
22


### p23

MODULE V · 2 HR TOPIC
Echoing Data with Blade
20CST461
Blade's curly-brace syntax is the most-used feature — and the choice between the two forms matters for security.
•
{{ $variable }} — echoes data, automatically escaped (safe 
against XSS)
•
{!! $variable !!} — echoes raw, UNESCAPED HTML — only 
use for trusted content
•
{{ $name ?? 'Guest' }} — Blade supports normal PHP 
expressions inside the braces
•
Comments use {{-- comment --}}, never rendered in the 
output
Blade (.blade.php)
<h2>Welcome, {{ $student->name }}</h2>
<p>{{ $bio ?? 'No bio provided.' }}</p>
{!! $trustedHtmlBlock !!}
{{-- This comment never reaches the browser --}}
Web Programming | Saintgits College of Engineering
23


### p24

MODULE V · 2 HR TOPIC
Blade Conditionals
20CST461
Blade wraps PHP's if/else logic in cleaner directives that read naturally inside HTML.
•
@if / @elseif / @else / @endif — standard conditional 
branching
•
@unless($condition) ... @endunless — runs when the 
condition is false (inverse of @if)
•
@isset($variable) ... @endisset — checks a variable is set 
and not null
•
@empty($variable) ... @endempty — checks a variable is 
empty
Blade (.blade.php)
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
Web Programming | Saintgits College of Engineering
24


### p25

MODULE V · 2 HR TOPIC
Blade Loops
20CST461
Blade's loop directives mirror PHP's, plus a handy built-in $loop variable inside @foreach.
•
@foreach($items as $item) ... @endforeach — the most 
common loop in views
•
@for($i = 0; $i < 10; $i++) ... @endfor — counted loops
•
@while($condition) ... @endwhile — condition-based 
loops
•
$loop->index, $loop->first, $loop->last — available 
automatically inside @foreach
Blade (.blade.php)
<ul>
@foreach ($students as $s)
<li>
{{ $loop->iteration }}. {{ $s->name }}
@if ($loop->last) (last student) @endif
</li>
@endforeach
</ul>
Web Programming | Saintgits College of Engineering
25


### p26

MODULE V · 2 HR TOPIC
Template Inheritance
20CST461
Rather than repeating the header/footer markup on every page, Blade lets child views inherit a shared layout.
•
@extends('layout') — declares which parent layout this 
view inherits
•
@section('name') ... @endsection — defines a named 
block of content
•
@yield('name') — in the PARENT layout, marks where a 
child's section gets inserted
•
@include('partial') — pulls in a reusable chunk of Blade 
from another file
Blade (.blade.php)
{{-- layout.blade.php --}}
<body>
@include('partials.navbar')
@yield('content')
</body>
{{-- students/index.blade.php --}}
@extends('layout')
@section('content')
<h2>Student List</h2>
@endsection
Web Programming | Saintgits College of Engineering
26


### p27

MODULE V · 2 HR TOPIC
Blade Directives — Quick Reference
20CST461
Directive
Purpose
{{ $var }}
Echo data, auto-escaped (safe)
{!! $var !!}
Echo raw HTML, unescaped (use with caution)
@if / @elseif / @else / @endif
Conditional rendering
@foreach / @endforeach
Loop over a collection or array
@extends / @section / @yield
Template inheritance — shared layouts
@include('view')
Insert a reusable partial template
Note: Every Blade directive is just a readable shorthand for plain PHP — nothing here is doing anything PHP itself couldn't do.
Web Programming | Saintgits College of Engineering
27


### p28

MODULE 5 RECAP
Key Takeaways
20CST461
JSON uses { } for objects and [ ] for arrays; keys are always double-
quoted.
json_encode() turns PHP data into JSON; json_decode() does the 
reverse.
Laravel implements MVC: Model (data), View (presentation), Controller 
(logic) — each with one job.
Routes (routes/web.php) map a URL to a controller method; 
middleware filters requests before that.
Route model binding auto-fetches a DB record from a route parameter 
— no manual query needed.
Controllers typically end by returning a view() or a redirect().
Blade's {{ }} auto-escapes output for safety; {!! !!} does not — use 
deliberately.
@extends/@section/@yield let views inherit a shared layout, avoiding 
repeated markup.
Web Programming | Saintgits College of Engineering
28
