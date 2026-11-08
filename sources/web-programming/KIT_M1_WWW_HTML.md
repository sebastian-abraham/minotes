# MODULE 1 — World Wide Web & HTML5 · Complete Study Kit

> 20CST461 Web Technologies · ESE Part A = 3 marks, Part B = 14 marks · **2 Part-A questions and 1 of 2 Part-B questions come from this module**
> Sources: `WEB PROGRAMING MOD-1.md` (line refs `1:L27`), faculty `Question Bank.pdf` (Q1–Q36, Q161–Q185). Items marked **(standard, not in your deck)** are exam-standard knowledge the slides do not cover — learn them anyway; Q178 and Q167 need them.

---

## 0. How to use this kit

1. Read **Part 1** once, slowly — it is the story of the module, every term decoded.
2. **Part 2** is what you actually write in the exam. 3-mark answers are 3–4 numbered lines. 14-mark answers are skeleton + code + explanation.
3. **Part 3** is code you must reproduce by hand. Write each one twice, closed book.
4. **§5** is the night-before list. **§6** tells you which figures in the deck to go look at.

---

## 1. Module map + question coverage

### 1.1 Coverage table — every bank question in this module

| Q# | What it asks (short) | Marks | Answered at |
|---|---|---|---|
| 1 | Internet vs World Wide Web | 3 | §2.1 |
| 2 | Main components of a URL | 3 | §2.2 |
| 3 | MIME purpose in email | 3 | §2.4 |
| 4 | Role of web server in client-server | 3 | §2.6 |
| 5 | Purpose of `<!DOCTYPE html>` | 3 | §2.8 |
| 6 | Role of `<head>` element | 3 | §2.8 |
| 7 | Headings + accessibility/SEO | 3 | §2.10 |
| 8 | Embedding an image, essential `<img>` attributes | 3 | §2.11 |
| 9 | Significance of `alt` | 3 | §2.11 |
| 10 | Create a hyperlink + example | 3 | §2.12 |
| 11 | Internal link in the same document | 3 | §2.13 |
| 12 | `<ul>` vs `<ol>` vs `<li>` | 3 | §2.14 |
| 13 | Purpose of `<div>` and `<span>` | 3 | §2.16 |
| 14 | Basic HTML table, key elements | 3 | §2.17 |
| 15 | Purpose of the `<a>` tag | 3 | §2.12 |
| 16 | Hyperlink to an email address | 3 | §2.12 |
| 17 | Bullet-point list | 3 | §2.14 |
| 18 | `<ol>` vs `<ul>` + one scenario each | 3 | §2.14 |
| 19 | `target` attribute on `<a>` | 3 | §2.12 |
| 20 | `id` attribute for internal linking | 3 | §2.13 |
| 21 | HTML5 input types + validation | 3 | §2.19 |
| 22 | `autocomplete` attribute | 3 | §2.20 |
| 23 | `email` input type + validation | 3 | §2.19 |
| 24 | `text` vs `password` input | 3 | §2.19 |
| 25 | `<article>` vs `<section>` | 3 | §2.21 |
| 26 | Role of a web browser | 3 | §2.6 |
| 27 | Web servers vs web browsers | 3 | §2.6 |
| 28 | Discuss URIs and URLs | 3 | §2.2 |
| 29 | HTML for an image and a hyperlink | 3 | §2.11 |
| 30 | Role of `<meta>` in HTML5 | 3 | §2.18 |
| 31 | Define HTML5 semantic elements | 3 | §2.21 |
| 32 | URI vs URL with examples | 3 | §2.2 |
| 33 | MIME + role in web communication | 3 | §2.4 |
| 34 | Basic HTML5 structure + headings + `<img>` attributes | 3 | §2.8, §2.10, §2.11 |
| 35 | Special characters, `<hr>`, `<meta>` | 3 | §2.15, §2.18 |
| 36 | `<div>` vs `<span>` + table structure | 3 | §2.16, §2.17 |
| 161 | ARPANET vs modern Internet; browser↔server interaction | 14 | §3.1 |
| 162 | Internet milestones; HTML+HTTP+browsers adoption | 14 | §3.2 |
| 163 | Client-server model; URL structure | 14 | §3.3 |
| 164 | Importance of semantic elements; div vs semantic | 14 | §3.4 |
| 165 | Basic HTML5 structure; metadata in head | 14 | §3.5 |
| 166 | Headings h1–h6 for UX/SEO; heading structure for accessibility | 14 | §3.6 |
| 167 | Responsive images (`<picture>`, `srcset`); image optimisation | 14 | §3.7 |
| 168 | Nav menu with lists; div layout with CSS | 14 | §3.8 |
| 169 | `<meta>` for SEO/mobile; block vs inline elements | 14 | §3.9 |
| 170 | Product table + caption; special characters | 14 | §3.10 |
| 171 | Form with name/email/message + placeholders/labels; ol vs ul | 14 | §3.11 |
| 172 | Internal navigation; 3-section page code | 14 | §3.12 |
| 173 | Purpose of lists; ol + ul combined page | 14 | §3.13 |
| 174 | `<nav>` vs `<footer>`; structure with nav + footer | 14 | §3.14 |
| 175 | `<audio>` vs `<video>`; video with controls/autoplay/poster | 14 | §3.15 |
| 176 | Role of `<input>`; sample form with text/email/password | 14 | §3.16 |
| 177 | Image + ul code; explain `<textarea>`, `<span>`, `<tr>`, `<form>`, `<a>` | 14 | §3.17 |
| 178 | Webpage table; HTTP request/response format + `Host`/`Last-Modified` | 14 | §3.18 |
| 179 | Internet & WWW evolution; HTTP request–response cycle diagram | 14 | §3.2, §3.18 |
| 180 | Input elements; student registration form | 14 | §3.16 |
| 181 | Importance of tables; class timetable code | 14 | §3.10 |
| 182 | Evolution; URI, URL, MIME working together | 14 | §3.2, §3.3 |
| 183 | HTML5 structure diagram; heading + image attributes with accessibility | 14 | §3.5, §3.6 |
| 184 | Internal linking with id; ordered/unordered/definition lists | 14 | §3.12, §3.13 |
| 185 | HTML5 input types; datalist + autocomplete + page structure | 14 | §3.9, §3.19 |

### 1.2 Master themes (36 Part-A + 25 Part-B questions collapse into six)

1. **Evolution & infrastructure** — Internet vs WWW, ARPANET timeline, client-server, browser vs server, HTTP.
2. **Addressing** — URI, URL anatomy, URN, percent-encoding, MIME types.
3. **Document skeleton** — `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, `<meta>`, headings, semantic page structure.
4. **Content primitives** — images, hyperlinks (external/internal/mailto), lists, div/span, tables, special characters, `<hr>`.
5. **Forms** — `<form>`, `<label>`, `<input>` types, validation attributes, `<datalist>`, `autocomplete`, `<textarea>`.
6. **Media & good practice** — audio/video/`<track>`, responsive images, accessibility and SEO reasoning.

---

## 2. PART 1 — Deep dive, from zero

### 2.1 Internet vs World Wide Web — the road network vs the traffic on it (`1:L27–66`)

**Story:** the Internet is the *road network*; the Web is *one kind of traffic* that runs on it (email and FTP are other kinds of traffic on the same roads).

- **Internet** = a global network of networks speaking one common language, **TCP/IP**. It is **packet-switched**: a message is chopped into packets, each packet is routed independently, and the receiver reassembles them. No single company or country owns it. That decentralised design is why it survives partial failures — if one path dies, packets take another (`1:L27–29`).
- **WWW** = a *service* running on top of that network: documents written in HTML, addressed by URLs, fetched with HTTP, displayed by a browser (`1:L50–66`).
- **Three pillars of the original Web (Berners-Lee, 1989–91)**: HTML (structure + hyperlinks), URI/URL (a universal address), HTTP (the request/response protocol). Remove any one and the Web cannot exist (`1:L70–74`).
- **Generations**: Web 1.0 read-only static pages → Web 2.0 read-write (user-generated content, AJAX, social) → Web 3.0 semantic/decentralised (`1:L76–81`).
- **Dates that earn marks** (`1:L34–48`): ARPA 1957 · ARPANET live 1969 (UCLA, SRI, UCSB, Utah) · first email + `@` 1971 · TCP spec 1974 (Cerf & Kahn) · TCP/IP adopted 1983 ("birth of the Internet") · WWW proposal at CERN 1989 · first browser/server 1990 · Web public 1991 · Mosaic 1993 · Netscape + W3C 1994 · JavaScript 1995 · "Web 2.0" 2004 · HTML5 W3C Recommendation 2014.

**Why it exists:** the exam asks this constantly because it tests whether you know the Web is an *application*, not the network — the single most common student error.

### 2.2 Addressing: URI, URL, URN and the anatomy of a URL (`1:L87–135`)

**Story:** a URI is "a name for a thing"; a URL is "a name that also tells you where to find it and how to fetch it"; a URN is "a name that only says what it is" (like an ISBN).

- **URI (Uniform Resource Identifier)** — any compact string identifying a resource. Two subtypes: **URL** (locator — how + where) and **URN** (name — what, e.g. `urn:isbn:0-486-27557-4`). Rule: *all URLs are URIs, not all URIs are URLs* (`1:L87–91`).
- **URL components** (`1:L93–110`), using `https://www.saintgits.org:443/dept/cse/faculty.html?year=2026&dept=cse#profile`:

| Part | In the example | Job |
|---|---|---|
| Scheme | `https://` | Which protocol to speak (http, https, ftp, mailto, file, tel) |
| Host / authority | `www.saintgits.org` | Which machine (domain name or IP) |
| Port | `:443` | Which door on that machine (80 http, 443 https — omitted when default) |
| Path | `/dept/cse/faculty.html` | Which resource on that machine (filesystem-like) |
| Query string | `?year=2026&dept=cse` | Key=value data for the server; starts with `?`, pairs joined by `&` |
| Fragment | `#profile` | A place *inside* the resource; handled by the browser only — never sent to the server |

- **Absolute vs relative** (`1:L112–123`): absolute = full scheme + host + path (`https://saintgits.in/images/logo.png`); relative = resolved against the current document (`images/logo.png`, `../css/style.css`).
- **Percent-encoding** (`1:L125–135`): URLs may only carry a safe subset of ASCII; everything else becomes `%XX` — space `%20`, `#` `%23`, `&` `%26`, `/` `%2F`, `?` `%3F`.

### 2.3 Client-server model (`1:L4–6` context; standard framing)

**Story:** a restaurant. You (client/browser) order from a menu; the kitchen (server) cooks and hands over a plate; you never enter the kitchen.

- **Client** = the program that *asks*: browser, mobile app, `curl`. It initiates the request.
- **Server** = the program that *listens on a port, waits, and answers*: Apache/Nginx + PHP-FPM, Node, Tomcat.
- **The exchange:** browser resolves DNS → opens TCP (usually TLS) → sends an **HTTP request** (method, path, headers, optional body) → server runs code, maybe queries MySQL → returns an **HTTP response** (status code, headers, body: HTML/CSS/JS/JSON).
- **Statelessness:** HTTP forgets each request. That is why cookies and sessions exist (Module 4).
- **Why it matters:** it explains *where* each technology lives — HTML/CSS/JS execute on the client; PHP executes on the server *before* HTML is sent.

### 2.4 MIME types — the label on the parcel (`1:L141–167`)

**Story:** a parcel with a label saying "fragile glassware" tells the handler how to treat it. A `Content-Type` header does that for bytes.

- **MIME = Multipurpose Internet Mail Extensions**, born to let *email* carry non-text attachments, then adopted by HTTP (`1:L141–143`).
- **Syntax**: `type/subtype[;parameter]`, e.g. `text/html; charset=UTF-8`. `type` = broad category, `subtype` = specific format, parameter adds detail (`1:L145–148`).
- **Common values** (`1:L150–165`): `text/html`, `text/css`, `text/plain`, `application/javascript`, `application/json`, `application/pdf`, `application/xml`, `image/jpeg|png|gif|svg+xml`, `audio/mpeg`, `video/mp4`, `multipart/form-data` (form with file upload), `application/octet-stream` (unknown binary).
- **Role in web communication**: the server sends `Content-Type`; the browser uses it to decide *render as page / show as image / play / download*. Get it wrong (e.g. serving CSS as `text/plain`) and the browser refuses to apply the styles (`1:L167`).

### 2.5 HTTP — what actually travels (standard, not in your deck, but Q178/Q179 need it)

- **Request format:**
```
METHOD /path?query HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
<blank line>
name=Anjali&email=a%40b.com
```
  Line 1 = **request line** (method, target, version) · following lines = **headers** (name: value) · blank line · optional **body**.
- **Response format:**
```
HTTP/1.1 200 OK
Date: Mon, 09 Nov 2026 10:00:00 GMT
Server: Apache/2.4
Content-Type: text/html; charset=UTF-8
Content-Length: 5120
Last-Modified: Fri, 06 Nov 2026 08:00:00 GMT
<blank line>
<!DOCTYPE html> ...
```
  Line 1 = **status line** (version, status code, reason) · headers · blank line · body.
- **Headers asked about:** `Host` — request only, names the site being requested (one IP can serve many sites). `Last-Modified` — response only, when the resource last changed (used for caching / `If-Modified-Since`). `Content-Type` — both (request: what I am sending; response: what I am returning).
- **Status codes to name:** 200 OK, 301 moved permanently, 304 not modified, 400 bad request, 403 forbidden, 404 not found, 500 server error.
- **Request–response cycle:** type URL → DNS lookup → TCP + TLS handshake → HTTP request → server processes (PHP/MySQL) → HTTP response → browser parses HTML → requests CSS/JS/images (repeat cycle) → renders → JS may issue further (AJAX) requests.

### 2.6 Browser vs web server (`1:L4–6` framing)

| | Web browser (client) | Web server |
|---|---|---|
| Runs on | User's device | Host machine, listening on port 80/443 |
| Job | Request resources, parse HTML, apply CSS, execute JS, render | Store/serve files, execute server-side code, talk to databases, return responses |
| Speaks | HTTP as a client | HTTP as a server |
| Examples | Chrome, Firefox, Safari, Edge | Apache, Nginx, IIS, Tomcat |
| Security position | Untrusted; user can see/modify everything it receives | Trusted; holds credentials and data |

The browser is the **interface between the user and the Web**: it turns a typed URL into a request, and bytes into a page; it also sandboxes JS so a page cannot read your files.

### 2.7 What HTML is (`1:L176–180`)

HTML = **HyperText Markup Language**. It is *not* a programming language — no variables, no loops, no logic. It is markup: tags annotate plain text to declare **structure and meaning** (semantics). *HyperText* = text containing links. HTML5 adds semantic elements, native audio/video, richer forms and JS APIs.

### 2.8 The HTML5 document skeleton (`1:L182–207`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
</head>
<body>
  <h1>Welcome</h1>
  <p>This is a paragraph.</p>
</body>
</html>
```

| Line | Job |
|---|---|
| `<!DOCTYPE html>` | Tells the browser "standards mode, HTML5". It is a *declaration*, not a tag — no closing tag. Without it browsers fall back to quirks mode and render inconsistently. |
| `<html lang="en">` | Root element wrapping everything; `lang` helps screen readers and search engines. |
| `<head>` | Machine-facing container: title, charset, viewport, meta description, CSS `<link>`, `<script>`. Nothing here is displayed as page content (except `<title>`, shown in the tab). |
| `<meta charset="UTF-8">` | Character encoding — without it `₹`, `é`, `→` render as garbage. Must appear in the first 1024 bytes. |
| `<title>` | Tab/window text, bookmark default, and the clickable headline in search results. |
| `<body>` | Everything the user sees. |

**Element anatomy** (`1:L209–222`, figure at `1:L216`): opening tag `<p class="intro">` + content `Hello World` + closing tag `</p>`. `class` = attribute name, `"intro"` = attribute value. **Void elements** have no content or closing tag: `<br> <hr> <img> <input> <meta> <link>`. Elements nest but must not overlap.

### 2.9 Text-level basics (headings, paragraphs, emphasis) (`1:L224–237`)

`<h1>`–`<h6>` declining importance; one `<h1>` per page; do not skip levels; use CSS for size, headings for structure. Paragraph `<p>`, line break `<br>`, emphasis `<em>` (stress), `<strong>` (importance).

### 2.10 Headings: three jobs — structure, SEO, accessibility (`1:L224–237`)

1. **Structure** — headings form the document outline, like a table of contents; a reader can skim.
2. **SEO** — search engines weight `<h1>`/`<h2>` text and use the outline to understand topics; a page whose `<h1>` says "Web Programming Notes" ranks for that phrase.
3. **Accessibility** — screen-reader users navigate by jumping heading to heading (NVDA/JAWS "heading list"). A page styled with bold text instead of headings is a page they cannot skim.

### 2.11 Images (`1:L239–267`)

```html
<img src="logo.png" alt="Saintgits College of Engineering logo" width="200" height="100" loading="lazy">
```

| Attribute | Purpose |
|---|---|
| `src` | Path/URL of the image — **required** |
| `alt` | Text alternative: shown when the image fails, read aloud by screen readers, used by search engines. **Required** for accessibility |
| `width` / `height` | Display size in px; also lets the browser reserve space and avoid layout shift |
| `title` | Tooltip on hover (optional) |
| `loading="lazy"` | Defers off-screen images until needed |

Formats: JPEG (photos, lossy), PNG (transparency, lossless), GIF (simple animation), SVG (vector, scales cleanly), WebP (modern, small). Image as a link = wrap `<img>` inside `<a>` (`1:L262–267`). `alt=""` is correct for purely decorative images so screen readers skip them.

**Accessibility/SEO rules that earn marks:** never use an image for text; keep `alt` descriptive but short; always set dimensions; compress and serve the right size.

### 2.12 Hyperlinks — the `<a>` element (`1:L276–296`)

```html
<a href="https://www.saintgits.org" target="_blank" rel="noopener noreferrer">Visit Saintgits</a>
<a href="about.html">About Us</a>              <!-- internal, relative -->
<a href="mailto:info@saintgits.org">Email us</a>
<a href="tel:+914812345678">Call us</a>
<a href="report.pdf" download>Download PDF</a>
```

| Attribute | Meaning |
|---|---|
| `href` | Destination (Hypertext REFerence) — required for a working link |
| `target` | `_self` (default, same tab), `_blank` (new tab), `_parent`, `_top` |
| `rel` | Relationship; `noopener noreferrer` is the security pairing for `_blank` (the new page must not get a handle on your page's `window`) |
| `download` | Download instead of navigate |

`target="_blank"` does not change *what* is fetched, only *where it is displayed* — plus it keeps your page open, which is why "open social links in a new tab" is the standard scenario.

### 2.13 Internal linking with fragments (`1:L298–322`)

**Story:** a bookmark inside a book. Give a section an `id`, then link to `#thatId`.

```html
<nav>
  <a href="#syllabus">Syllabus</a> |
  <a href="#contact">Contact</a>
</nav>
...
<h2 id="syllabus">Syllabus</h2>
<h2 id="contact">Contact</h2>
```
Rules: `id` must be unique in the document; case-sensitive; `href="#top"` scrolls to the top; cross-page works too (`page.html#section2`); the fragment is resolved by the browser, never sent to the server.

### 2.14 Lists (`1:L324–380`)

- **`<ul>` unordered** — order irrelevant, bullets. Nav menus, feature lists.
- **`<ol>` ordered** — order matters, numbering. Recipes, ranked steps. `type="1|A|a|I|i"`, `start="n"`, `reversed`.
- **`<li>`** — the item; valid only inside `<ul>`/`<ol>`.
- **`<dl>` description list** — `<dt>` term + `<dd>` definition; glossaries, spec tables.
- **Nesting** — a sub-list goes *inside* the `<li>` it belongs to, not beside it.

```html
<ul>
  <li>Frontend
    <ul><li>HTML</li><li>CSS</li></ul>
  </li>
  <li>Backend</li>
</ul>
```

### 2.15 Special characters and `<hr>` (`1:L389–414`)

Characters that clash with markup, or are not on the keyboard, are written as entities `&name;` or `&#number;`: `&lt;` `<`, `&gt;` `>`, `&amp;` `&`, `&quot;` `"`, `&apos;` `'`, `&nbsp;` non-breaking space, `&copy;` ©, `&reg;` ®, `&#8377;` ₹, `&ndash;` –.

Why: writing `<b>` in body text makes the browser bold something instead of showing the characters; `&lt;b&gt;` displays them literally. `<hr>` is a *thematic break* — a void element drawing a horizontal rule between sections.

### 2.16 `<div>` vs `<span>` (`1:L440–455`)

| | `<div>` | `<span>` |
|---|---|---|
| Display | Block — starts a new line, fills the width | Inline — flows inside a line, only as wide as its content |
| Use | Grouping page regions, layout wrappers, cards | Wrapping a few words to style/script them |
| Semantics | None | None |

Neither carries meaning — that is exactly why HTML5 added semantic elements. Rule: **use the semantic element when one exists; `<div>` only when nothing fits.**

### 2.17 Tables (`1:L457–503`)

```html
<table border="1">
  <caption>Semester Result</caption>
  <thead>
    <tr><th scope="col">Course</th><th scope="col">Credits</th><th scope="col">Grade</th></tr>
  </thead>
  <tbody>
    <tr><td>Web Programming</td><td>4</td><td>A</td></tr>
    <tr><td>Data Structures</td><td>4</td><td>A+</td></tr>
  </tbody>
  <tfoot>
    <tr><td colspan="2">Total Credits</td><td>8</td></tr>
  </tfoot>
</table>
```

`<table>` container · `<caption>` title (must be the first child) · `<thead>/<tbody>/<tfoot>` row groups · `<tr>` row · `<th>` header cell (bold, centred; `scope="col"`/`"row"` for accessibility) · `<td>` data cell · `colspan`/`rowspan` merge cells. Tables are **only** for tabular data — never for page layout (that is CSS's job now).

### 2.18 `<meta>` — the invisible part of the page (`1:L416–438`)

| Form | Example | Job |
|---|---|---|
| `charset` | `<meta charset="UTF-8">` | Character encoding |
| `name` + `content` | `description`, `keywords`, `author`, `viewport`, `robots` | Describe the page to browsers/engines |
| `http-equiv` + `content` | `refresh`, `content-type` | Simulate an HTTP response header |

Two that change real behaviour: `<meta name="viewport" content="width=device-width, initial-scale=1.0">` makes mobile browsers stop pretending to be 980px wide — without it responsive CSS is wasted; `<meta name="description" content="...">` is usually the grey snippet under the title in Google.

### 2.19 Forms and HTML5 input types (`1:L505–581`)

**Story:** a form is a paper application; each `<input>` is one box to fill; `action` is the office you send it to; `method` is whether you staple it to the outside (GET) or seal it in an envelope (POST).

```html
<form action="/submit.php" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Anjali" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <button type="submit">Submit</button>
</form>
```

| `type` | Behaviour |
|---|---|
| `text` | Single-line free text (default) |
| `email` | Browser validates a well-formed address + email keyboard on mobile |
| `password` | Characters masked (`•••`); value still sent in clear unless HTTPS |
| `number` | Numeric only, steppers, `min`/`max`/`step` |
| `range` | Slider between min and max |
| `date` / `month` / `week` / `time` / `datetime-local` | Native pickers |
| `color` | Colour swatch returning hex |
| `tel` | Numeric keypad; no format validation built in |
| `url` | Validates a well-formed URL |
| `search` | Search-styled text field with a clear button |
| `checkbox` | Multi-select from a set |
| `radio` | Exactly one per shared `name` |
| `file` | Upload; `accept` restricts types |
| `hidden` | Not shown; submitted anyway |
| `submit` / `reset` / `button` | Action buttons |

**Validation attributes:** `required`, `min`/`max`/`step`, `minlength`/`maxlength`, `pattern` (regex, e.g. `pattern="[0-9]{6}"`), `placeholder` (hint only — not a label, not validation). HTML5 validation is **client-side convenience, never security** — the server must re-validate (Module 3).

`<label for="id">` links text to control: clicking the label focuses the box, and screen readers announce it. `<textarea>` = multi-line text; `<select>/<option>` = dropdown.

### 2.20 `<datalist>` and `autocomplete` (`1:L583–614`)

- **`<datalist>`** — a set of *suggestions* for a text input via `list="datalistId"`. Unlike `<select>`, the user may type a value not in the list (editable combo box).
```html
<input type="text" name="browser" list="browsers">
<datalist id="browsers">
  <option value="Chrome"><option value="Firefox"><option value="Edge">
</datalist>
```
- **`autocomplete`** — may the browser auto-fill from stored values? `on` (default), `off` (OTPs, sensitive fields), or a named token (`name`, `email`, `tel`, `street-address`, `cc-number`) that tells the browser exactly which stored value to suggest. Can be set on the `<form>` (inherited) or per field (overrides).

### 2.21 Semantic page structure (`1:L616–676`)

| Element | Represents |
|---|---|
| `<header>` | Intro content for page or section: logo, title, nav |
| `<nav>` | Block of primary navigation links |
| `<main>` | The dominant unique content — once per page |
| `<section>` | Thematic grouping, normally with its own heading |
| `<article>` | Self-contained content that would still make sense syndicated alone (blog post, card, forum post) |
| `<aside>` | Tangentially related: sidebar, pull-quote, ad |
| `<footer>` | Footer of its nearest sectioning ancestor or the page |
| `<figure>`/`<figcaption>` | Self-contained media + optional caption |

```html
<body>
  <header>
    <h1>Saintgits CSE</h1>
    <nav><a href="#about">About</a> <a href="#faculty">Faculty</a></nav>
  </header>
  <main>
    <section id="about"><h2>About</h2><p>...</p></section>
    <article><h2>Conference Highlights</h2><p>...</p></article>
    <aside><h3>Quick Links</h3></aside>
  </main>
  <footer><p>&copy; 2026 Saintgits</p></footer>
</body>
```

**`<section>` vs `<article>`** — an article survives being pulled out and republished; a section only makes sense as part of this page. A news feed is a section containing many articles.

Why semantics: accessibility (screen readers list landmarks — "navigation", "main", "contentinfo"), SEO (engines read region roles), maintainability (a human can read the markup).

### 2.22 Multimedia: `<audio>`, `<video>`, `<source>`, `<track>` (`1:L678–759`)

Before HTML5, audio/video needed Flash — insecure, slow, dead on mobile. HTML5 made them native elements with a shared JS API.

```html
<video width="640" height="360" controls autoplay muted poster="thumb.jpg" playsinline>
  <source src="demo.mp4" type="video/mp4">
  <source src="demo.webm" type="video/webm">
  <track kind="subtitles" src="subs-en.vtt" srclang="en" label="English" default>
  Your browser does not support the video tag.
</video>
```

| Attribute | Meaning |
|---|---|
| `controls` | Native play/pause/volume/seek bar |
| `autoplay` | Start on load — usually blocked unless `muted` |
| `loop`, `muted`, `preload` (`none|metadata|auto`) | Repeat / start silent / how much to buffer |
| `poster` | Still image before playback (video only) |
| `playsinline` | iOS: play inline instead of forcing fullscreen |
| `<source>` | One candidate format each; browser takes the first it can play |
| `<track>` | WebVTT subtitles/captions/descriptions (`kind`, `srclang`, `label`) |

Formats: audio MP3/OGG/WAV/AAC; video MP4 (H.264)/WebM (VP8/VP9)/OGG (Theora). **No single format is universal** — that is why multiple `<source>` elements exist. JS API: `play()`, `pause()`, `currentTime`, `volume`, `playbackRate`, `ended` event.

Accessibility: always provide `<track>` captions; never autoplay unmuted; provide a transcript for audio-only.

---

## 3. PART 2 — Answer bank

### 3.1 3-mark answers (Part A)

> **Rule for 3 marks:** three numbered points, one line each, plus a tiny example if the question says "example". Do not write an essay — the third point is where marks are lost.

**MASTER A — Internet vs WWW (Q1).** (1) The Internet is the global packet-switched network of networks using TCP/IP, born from ARPANET (1969); (2) the WWW is a *service on top of it* — hypertext documents written in HTML, addressed by URLs and transferred by HTTP, invented by Berners-Lee at CERN (1989–91); (3) so the Internet carries other services too (email, FTP), and you can have the Internet without the Web, never the Web without the Internet.

**MASTER B — URL components (Q2, also feeds Q28, Q32, Q163b).** (1) scheme/protocol (`https://`); (2) host/domain and optional port (`www.saintgits.org:443`); (3) path (`/dept/cse/faculty.html`); (4) optional query string (`?year=2026&dept=cse`) and fragment (`#profile`). Example line to write: `https://host:443/path?query#fragment`.

**MASTER C — URI vs URL (Q28, Q32).** (1) A URI is any compact string that *identifies* a resource; a URL is a URI that also says *where it is and how to fetch it*; (2) URI has two subtypes — URL (locator) and URN (name only, e.g. `urn:isbn:0-486-27557-4`); (3) all URLs are URIs, but not all URIs are URLs; example pair: `https://saintgits.org/index.html` (URL) vs `urn:isbn:978-81-0000` (URN).

**MASTER D — MIME (Q3, Q33).** (1) MIME = Multipurpose Internet Mail Extensions — a `type/subtype` label for content, e.g. `text/html; charset=UTF-8`; (2) it began to let email carry attachments and is now the `Content-Type` header of every HTTP response; (3) the browser uses it to decide to render, display, play or download — CSS served as `text/plain` simply does not apply.

**MASTER E — Client-server / browser vs server (Q4, Q26, Q27).** (1) The client (browser) initiates: resolves DNS, opens a connection, sends an HTTP request; (2) the server listens on port 80/443, runs server-side code, may query a database, and returns an HTTP response; (3) browser = untrusted renderer of HTML/CSS/JS on the user's device; server = trusted holder of data, files and credentials; HTTP is the language between them.

**MASTER F — `<!DOCTYPE html>` and the skeleton (Q5, Q6, Q34).** (1) `<!DOCTYPE html>` is a declaration (not a tag) that puts the browser in HTML5 standards mode; (2) `<head>` holds non-displayed metadata — charset, viewport, `<title>`, description, CSS/JS links; (3) `<body>` holds all rendered content; `<html lang="en">` wraps both and declares the language.

**MASTER G — Headings (Q7, also Q166).** (1) Six levels `<h1>`–`<h6>` expressing hierarchy, one `<h1>` per page, no skipped levels; (2) SEO: search engines read heading text and the outline to understand topics; (3) accessibility: screen readers let users jump between headings, so structural headings make the page navigable; (4) never use headings just to make text big — that is CSS.

**MASTER H — Images (Q8, Q9, Q29).** (1) `<img src="..." alt="..." width="..." height="...">` is a void element that embeds an image; (2) `src` is required; `alt` is the text alternative — read aloud by screen readers, shown when loading fails, indexed by search engines; (3) `width`/`height` reserve space and prevent layout shift; `loading="lazy"` defers off-screen images; (4) image as link = `<a href="..."><img ...></a>`.

**MASTER I — Hyperlinks (Q10, Q15, Q16, Q19).** (1) `<a href="URL">text</a>` creates a hyperlink; `href` is the destination; (2) `target="_self"` (default, same tab), `_blank` (new tab — pair with `rel="noopener noreferrer"`); (3) `mailto:` opens a mail client — `<a href="mailto:info@saintgits.org?subject=Enquiry">Email</a>`; `tel:` dials; `download` downloads; (4) the anchor text should describe the destination ("Download syllabus"), not "click here".

**MASTER J — Internal linking (Q11, Q20).** (1) Give the target element an `id`: `<h2 id="contact">`; (2) link to it with a fragment: `<a href="#contact">Contact</a>`; (3) `id` must be unique in the document; the fragment is handled by the browser and not sent to the server; cross-page form `page.html#contact`.

**MASTER K — Lists (Q12, Q17, Q18).** (1) `<ul>` = unordered, bullets, order irrelevant (features, nav menus); (2) `<ol>` = ordered, auto-numbered, order meaningful (recipe steps, rankings) with `type`/`start`/`reversed`; (3) both contain `<li>` items only; `<dl>` with `<dt>`/`<dd>` handles term–definition pairs; (4) nested lists go inside the owning `<li>`.

**MASTER L — `<div>` vs `<span>` (Q13, Q36a).** (1) `<div>` is block-level: starts a new line, fills available width, used to group page regions; (2) `<span>` is inline: sits inside a line, only as wide as its content, used to style a few words; (3) neither is semantic — prefer `<header>/<nav>/<section>/<article>` where the meaning is known.

**MASTER M — Tables (Q14, Q36b).** (1) `<table>` wraps rows; `<caption>` titles it; `<tr>` is a row; `<th>` a header cell (`scope="col"/"row"`), `<td>` a data cell; (2) `<thead>`/`<tbody>`/`<tfoot>` group header/body/footer rows; (3) `colspan`/`rowspan` merge cells; use tables for data only, never layout.

**MASTER N — HTML5 input types (Q21, Q23, Q24, also Q176, Q185a).** (1) HTML5 added `email`, `url`, `number`, `range`, `date`/`month`/`week`/`time`, `color`, `search`, `tel`, `file`, plus `checkbox`/`radio`/`hidden`; (2) `email` triggers built-in format validation and an email keyboard; `date` a native picker; `number` steppers with `min`/`max`/`step`; (3) `text` echoes characters, `password` masks them — both submit plain text, so HTTPS is what actually protects them; (4) `required`, `pattern`, `minlength` add validation without JavaScript — but server-side validation is still mandatory.

**MASTER O — `autocomplete` and `<datalist>` (Q22, Q185b).** (1) `autocomplete="on|off"` on `<form>` (inherited) or a field (overrides) controls browser auto-fill; (2) named tokens (`name`, `email`, `tel`, `cc-number`) tell the browser which stored value to suggest, improving accuracy; `off` for OTPs/sensitive fields; (3) `<datalist id="x">` + `<input list="x">` gives suggestions while still allowing free text — an editable combo box, unlike `<select>`.

**MASTER P — Semantic elements (Q25, Q31).** (1) Semantic elements name a region's role: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>`; (2) `<article>` = self-contained and syndicatable (blog post, card); `<section>` = thematic grouping meaningful only within this page; (3) benefit: screen-reader landmarks, better SEO, readable markup — replacing "div soup".

**MASTER Q — `<meta>`, entities, `<hr>` (Q30, Q35).** (1) `<meta>` supplies invisible metadata: `charset`, `name`+`content` (description, keywords, author, viewport, robots), `http-equiv`+`content` (refresh, content-type); (2) entities `&lt; &gt; &amp; &quot; &nbsp; &copy;` display characters that would otherwise be parsed as markup or cannot be typed; (3) `<hr>` is a void element marking a thematic break between sections.

**MASTER R — Accessibility/SEO one-liners** (use to extend any answer): `lang` on `<html>`; descriptive `alt`; `<label for>` on every input; `scope` on `<th>`; logical heading order; captions via `<track>`; never encode text in images.

### 3.2 14-mark answers (Part B)

Format to write: **(a) definition/explanation with numbered points → (b) code/example → (c) one line on why it matters.** 14 marks ≈ 1.5–2 pages plus code.

#### §3.1 Q161 — ARPANET vs modern Internet; browser ↔ server
**Structure:** (a) 6 marks: origin, scale, protocols, ownership, services, speed/security. (b) 8 marks: define browser and server, then the 6-step exchange.
(a) ARPANET (1969): four university nodes, military/research funded (ARPA), closed community, NCP before TCP/IP, designed for survivable communication. Modern Internet: millions of networks, commercial and public, TCP/IP + TLS + HTTP/2-3, no central owner, carries Web/mail/streaming/VoIP/cloud. ARPANET contributed: packet switching, TCP/IP lineage, the email convention, the culture of open standards — it *became* the Internet when TCP/IP was adopted in 1983.
(b) Browser: client software that requests resources and renders HTML/CSS, executing JS in a sandbox. Server: software on a host listening on a port, serving files or running server-side code and returning responses. Interaction: URL typed → DNS resolves host to IP → TCP + TLS connection → HTTP request (method, path, headers, body) → server runs PHP/queries MySQL → HTTP response (status, headers, body) → browser parses HTML, requests sub-resources, renders, JS runs. State that this loop is *stateless per request* — hence cookies/sessions later.

#### §3.2 Q162 / Q179a / Q182a — Evolution of the Internet and WWW
**Structure:** (a) timeline as a table (year → milestone → impact). (b) For Q162b: how HTML + HTTP + browsers reinforced each other.
Timeline rows to write: 1957 ARPA · 1969 ARPANET 4 nodes · 1971 email + `@` · 1974 TCP (Cerf/Kahn) · 1983 TCP/IP adopted · 1989 Berners-Lee proposal · 1990 first browser + server · 1991 Web public · 1993 Mosaic (graphical, mass adoption) · 1994 Netscape + W3C (standards body) · 1995 JavaScript, e-commerce · 1998 CSS2/Google era · 2004 Web 2.0, AJAX · 2007 iPhone (mobile Web) · 2014 HTML5 Recommendation · today: HTTP/2-3, cloud, Web 3.0.
Impact line you must include: each step lowered the cost of publishing or the cost of access — ARPANET connected machines, TCP/IP connected networks, the Web connected documents, browsers made documents readable by non-experts, HTML5 made them work on phones.
Part (b): HTML gave a universal, forgiving document format anyone could author; HTTP gave a trivial request/response protocol any server could implement; browsers gave one program that could render any page. Together: a page written once was instantly readable everywhere — the network effect that made the Web grow faster than any previous hypertext system.

#### §3.3 Q163 / Q182b — Client-server model + URL structure
(a) Client = initiator (browser/app); server = responder (Apache/Nginx + PHP, database behind it). Separation of concerns: clients stay thin and untrusted, servers hold data and logic. Explain request→process→response, statelessness, and that one server serves many clients concurrently. Diagram: client box → request arrow → server box → DB cylinder → response arrow back.
(b) Full URL anatomy table (six components) + one labelled example + absolute vs relative + percent-encoding. End with "the fragment never reaches the server".

#### §3.4 Q164 — Semantic elements; div vs semantic
(a) 7 marks: name five semantic elements and their roles; three benefits (accessibility landmarks, SEO, maintainability); note `<main>` once per page; `<article>` vs `<section>` distinction.
(b) Comparison: `<div>` = meaning-free block container, useful for layout wrappers; `<section>` = themed block with heading; `<article>` = independently distributable; `<header>/<footer>` = intro/outro of page or section; `<nav>` = navigation block. Give a short code block showing div-only markup vs the same page with semantics.

#### §3.5 Q165 / Q183a — HTML5 document structure and metadata
(a) Code the skeleton; explain each of `<!DOCTYPE>`, `<html lang>`, `<head>`, `<meta charset>`, `<meta viewport>`, `<title>`, `<body>`. Draw the tree: html → (head, body) → (title, meta, link | header, main, footer).
(b) Metadata: charset (correct rendering), viewport (mobile scaling — without it responsive CSS is void), description (search snippet), keywords (largely ignored), author, robots (index/noindex), http-equiv refresh. Say plainly: metadata is not displayed but it changes *how* the page is indexed, cached, scaled and announced.

#### §3.6 Q166 / Q183b — Headings for UX, SEO, accessibility
(a) UX: outline/scanability; SEO: heading text and hierarchy signal topic and structure, `<h1>` carries the page's main topic; (b) accessibility: screen-reader heading navigation; logical order (`h1→h2→h3`) creates a usable outline; skipped levels and bold-text pseudo-headings break it. Add the rule: one `<h1>`, no skipped levels, style with CSS not tags.

#### §3.7 Q167 — Responsive images and optimisation (**standard, not in your deck**)
(a) `<img srcset="small.jpg 480w, large.jpg 1200w" sizes="(max-width:600px) 100vw, 50vw" src="fallback.jpg" alt="...">` lets the browser choose a file by viewport/DPR; `<picture>` with `<source media="...">` / `type="image/webp"` selects by media condition or format; `<source srcset>` + `x` descriptors pick by pixel density.
(b) Optimisation: compress (JPEG quality ~75, WebP/AVIF), size the file to the display size (never 4000px for a 400px slot), lazy-load below the fold, set width/height to avoid layout shift, use SVG for icons/logos, serve from a CDN with caching. Impact: images are typically the largest payload, so this is the cheapest performance win and it directly affects Core Web Vitals (LCP/CLS).

#### §3.8 Q168 — Navigation menu with lists; div layout + CSS
(a) Nav = `<nav>` containing `<ul>` of `<li><a>`. Why a list: a menu *is* a list of links — semantics, screen readers announce "list of 3 items", CSS can style uniformly, and it degrades gracefully without CSS. Give the code.
(b) Layout: `div#header`, `div#content`, `div#footer` with a CSS grid or flex shell:
```css
#header{border-bottom:2px solid #333;padding:10px}
#content{display:flex;gap:20px;padding:20px}
#footer{border-top:1px solid #999;text-align:center;padding:10px}
```
Explain each rule's effect. Note the modern preference: use `<header>/<main>/<footer>` instead of divs.

#### §3.9 Q169 / Q185b — `<meta>` for SEO/mobile; block vs inline
(a) `description` (snippet), `viewport` (mobile), `robots`, Open Graph (`og:title`) **(standard)**, `theme-color` **(standard)**; charset for correct rendering.
(b) Block: starts on a new line, takes full width, honours width/height/margin — `<div>`, `<p>`, `<h1>`, `<ul>`, `<table>`, `<form>`. Inline: flows within text, only content width, vertical margins ignored — `<span>`, `<a>`, `<img>`, `<strong>`, `<input>`. State `display` can change this in CSS.

#### §3.10 Q170 / Q181 — Product table + caption; timetable
(a) Table with `<caption>`, `<thead>` headers (`Product | Price | Availability`), three data rows, `border-collapse:collapse` + zebra striping in CSS. Caption goes first inside `<table>`.
(b) Importance of tables: aligned comparison of multi-attribute data, readable dense information, accessible via `scope` — and the warning that tables are not layout tools.
Timetable: 6 columns (Day, 9–10, 10–11, 11–12, 1–2, 2–3), `rowspan` for lab blocks, `th scope="col"`.

#### §3.11 Q171 / Q176 / Q180 / Q177a — Forms
(a) Form with name (text), email (email), message (textarea); `<label for>` for every field (click-to-focus + screen readers); `placeholder` shows an example, never replaces a label; `required` for mandatory fields; `maxlength`; `method="POST"` because the message is not URL-safe.
(b) `text` vs `email` vs `password` table; `<input>` is the generic control element whose `type` selects the widget and validation.
Student registration form (Q180b): name, roll number (`pattern="[0-9]{6}"`), email, password+confirm, date of birth, gender radios, department `<select>`, address `<textarea>`, terms checkbox, submit. Show the code with labels.

#### §3.12 Q172 / Q184a — Internal navigation
Steps: (1) assign unique `id`s to sections; (2) build `<nav>` with `href="#id"` links; (3) the browser scrolls to the element and updates the URL fragment; the server never sees it. 8-mark version: full page with `<nav>` + three `<section id>` blocks and a "back to top" link. Add `scroll-behavior:smooth` **(standard)** as a bonus, and explain why `id` must be unique and not start with a digit **(standard)**.

#### §3.13 Q173 / Q184b — Lists in depth
(a) Purpose: group related items so the structure itself conveys meaning (sequence vs set vs glossary). ol vs ul scenarios: procedure/ranking vs features/ingredients.
(b) Combined page: `<ol>` of brewing steps + `<ul>` of product features, plus `<dl>` for a glossary. Explain how each type communicates order vs equality.

#### §3.14 Q174 — `<nav>` vs `<footer>`
(a) `<nav>` = block of primary navigation links (site menu, breadcrumb) — a landmark screen readers can jump to; `<footer>` = closing content of the page or nearest section (copyright, contact, legal links) — landmark "contentinfo". One page may have several `<nav>` and `<footer>` elements, but only one page-level footer outside sections.
(b) Code: `<header>` with `<h1>` + `<nav><ul>`; `<main>`; `<footer>` with `&copy;` and contact links. Explain each part.

#### §3.15 Q175 — audio vs video
(a) Both are native HTML5 media elements with a shared `HTMLMediaElement` API; `audio` has no visual track (no width/height/poster), `video` adds `width`, `height`, `poster`, `playsinline`; both support `controls`, `autoplay` (usually muted), `loop`, `muted`, `preload`, `<source>` fallbacks, `<track>` captions.
(b) Video snippet with `controls autoplay muted poster="thumb.jpg"` + two `<source>` + `<track>`; explain every attribute, why `muted` is required for autoplay, and why two sources exist.

#### §3.16 Q176 / Q180 — `<input>` and a real form
Deliver: role of `<input>` (generic control, behaviour driven by `type`, `name` is the key sent to the server, `value` the current data), then the form. Remember `name` — without it the field is not submitted at all; that is a classic 1-mark loss.

#### §3.17 Q177 — Image + list code; explain five tags
```html
<img src="flower.jpg" alt="A red rose in bloom" width="300" height="200">
<ul><li>tea</li><li>coffee</li><li>milk</li></ul>
```
Then a five-row table: `<textarea>` multi-line text (rows/cols/name) · `<span>` inline generic container · `<tr>` table row · `<form>` input-collection container with `action`/`method` · `<a>` hyperlink with `href`.

#### §3.18 Q178 — Table page + HTTP message formats
(a) Product/price table with caption, `th scope`, `colspan` in a totals row.
(b) Request: request line → headers → blank line → body. Response: status line → headers → blank line → body. `Host` = request only (virtual hosting); `Last-Modified` = response only (caching); `Content-Type`/`Content-Length` = both. Add status codes 200/301/404/500.

#### §3.19 Q185 — Input types + datalist + page structure
Combine MASTER N, MASTER O and §2.21: five input types with code, then `<datalist>` + `autocomplete`, then `<header>/<nav>/<section>/<article>/<footer>` skeleton with one line each.

---

## 4. PART 3 — Markup you must be able to write by hand

**D1. Full HTML5 skeleton** — doctype, html+lang, head (charset, viewport, title), body with h1+p. *Memorise the order.*
**D2. Image with all attributes + as a link** — `src`, `alt`, `width`, `height`, wrapped in `<a>`.
**D3. Three link types** — external (`target="_blank" rel="noopener noreferrer"`), internal relative, `mailto:` with `?subject=`.
**D4. Internal nav + three sections** — `id` on each `<h2>`, `<nav>` with fragments.
**D5. Nested list** — `<ul>` inside the correct `<li>`.
**D6. Description list** — three `<dt>/<dd>` pairs.
**D7. Result table** — caption, thead/tbody/tfoot, `scope`, one `colspan`.
**D8. Timetable** — 5 rows × 6 columns with two `rowspan` lab cells.
**D9. Registration form** — label+input pairs for text/email/password/date/radio/select/textarea/checkbox, `required`, `pattern`, submit button.
**D10. `datalist` combo box** — input `list` + datalist `id`.
**D11. Semantic page** — header/nav/main/section/article/aside/footer with `&copy;`.
**D12. Video with poster, two sources, captions** — plus fallback text.
**D13. Entities sentence** — "Use `&lt;b&gt;` for bold and `&amp;` for ampersand, `&copy;` 2026" rendered correctly.
**D14. `<meta>` block** — charset, viewport, description, author, keywords, refresh.

Drill rule: write each from memory, then compare to §2. If you miss an attribute, write the snippet five times — hand memory is what the exam tests.

---

## 5. 🔴 Night-before memorize sheet

| Item | Exact thing to recall | Why it is asked |
|---|---|---|
| Three pillars | HTML, URI/URL, HTTP (Berners-Lee 1989) | Every evolution question |
| Key years | 1969 ARPANET · 1983 TCP/IP · 1989 proposal · 1991 public · 1993 Mosaic · 1994 W3C · 2014 HTML5 Rec | Q162, Q179, Q182 |
| URL parts | scheme, host, port, path, query, fragment | Q2, Q163b, Q182b |
| URI rule | all URLs are URIs; URN names only | Q28, Q32 |
| MIME syntax | `type/subtype; charset=UTF-8` | Q3, Q33 |
| Void elements | `br hr img input meta link` | Any code question |
| Doctype | `<!DOCTYPE html>`, first line, standards mode | Q5 |
| Skeleton order | doctype → html[lang] → head(meta charset, meta viewport, title) → body | Q34, Q165, Q183 |
| Viewport meta | `width=device-width, initial-scale=1.0` | Q169, Q185 |
| Heading rule | one `h1`, no skipped levels, CSS for size | Q7, Q166 |
| `alt` | text alternative: fail case + screen reader + SEO | Q9 |
| `target` values | `_self _blank _parent _top`; `_blank` + `rel="noopener noreferrer"` | Q19 |
| `mailto` | `href="mailto:a@b.com?subject=X"` | Q16 |
| Table tags | table, caption, thead, tbody, tfoot, tr, th, td, colspan, rowspan | Q14, Q36, Q170 |
| Input types | text email password number range date color search tel url file checkbox radio hidden submit | Q21, Q185 |
| Validation attrs | required, pattern, min, max, step, minlength, maxlength, placeholder | Q21, Q23 |
| datalist | `<input list="x">` + `<datalist id="x">` | Q22, Q185 |
| autocomplete | `on` / `off` / named tokens (`name`,`email`,`cc-number`) | Q22 |
| Entities | `&lt; &gt; &amp; &quot; &nbsp; &copy;` | Q35, Q170b |
| Semantic set | header, nav, main, section, article, aside, footer, figure | Q25, Q31, Q164 |
| HTTP request line | `GET /path HTTP/1.1` | Q178 |
| Headers | Host (req), Last-Modified (res), Content-Type (both) | Q178 |
| Status codes | 200, 301, 304, 400, 403, 404, 500 | Q178, Q179 |

---

## 6. 📐 Diagram + figure index (go and study these)

| Figure | Where | What to draw in the exam |
|---|---|---|
| Anatomy of an HTML element | `WEB PROGRAMING MOD-1.md` ~L216 (`[Image Description]`) | `tag + attribute + content + closing tag` labels |
| URL anatomy | `1:L93–110` (table) | six-part labelled URL line |
| Three pillars of the Web | `1:L70–74` | HTML + URL + HTTP circle diagram |
| HTTP request–response cycle | not in deck; use §2.5 | client → DNS → TCP/TLS → request → server+DB → response → render |
| Block vs inline | `1:L443–455` table | two boxes: full-width block vs in-line span |
| Box model | Module 2, `2:p11` | nested margin/border/padding/content boxes |
| Semantic page layout | `1:L636–663` code | header/nav/main/section/article/aside/footer regions |

---

## 7. Say-this-if-grilled defence lines

1. "The Web is an application on the Internet — the Internet is TCP/IP infrastructure, the Web is HTML over HTTP addressed by URLs."
2. "A URL is a URI that tells you *how* to fetch the resource; a URN only tells you *what* it is."
3. "The fragment is client-side — it is never sent to the server, which is why `#section` needs no server support."
4. "MIME is not decoration: the browser chooses renderer versus downloader from `Content-Type` alone."
5. "`<!DOCTYPE html>` is a standards-mode switch, not a tag — without it browsers use quirks mode."
6. "`<head>` is for machines, `<body>` is for humans."
7. "Headings are the document outline — screen readers and search engines both navigate by them, which is why size belongs in CSS."
8. "`alt` is not a caption: it is the image's replacement when the image is unavailable to a user or a crawler."
9. "`_blank` without `rel="noopener"` gives the new page a handle on your window — that is a real attack, not a style note."
10. "`<div>` and `<span>` have no meaning by design; semantics live in `<nav>`, `<article>`, `<main>`."
11. "HTML5 validation is UX, not security — the server must validate again because the client can be bypassed."
12. "Tables are for data, not layout — `div`+CSS replaced table layout because tables couple content to presentation and break screen-reader flow."
