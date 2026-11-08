# Module 1 — World Wide Web & HTML5

**20CST461 Web Technologies · ESE:** Part A = 3 marks, Part B = 14 marks · this module supplies 2 Part-A questions and one of two Part-B questions.
Sources: `WEB PROGRAMING MOD-1.md` (`1:L27`), `question_bank.md` (Q1–Q36, Q161–Q185). Items marked **(standard)** are exam-standard but not on the slides.

---

## 1. Coverage — every bank question

| Q | Asks | Marks | Answer at |
|---|---|---|---|
| 1 | Internet vs WWW | 3 | §2.1 |
| 2 | URL components | 3 | §3.1 B |
| 3 | MIME in email | 3 | §3.1 D |
| 4 | Web server role | 3 | §3.1 E |
| 5 | `<!DOCTYPE html>` purpose | 3 | §2.5 |
| 6 | Role of `<head>` | 3 | §2.5 |
| 7 | Headings, a11y/SEO | 3 | §3.1 G |
| 8 | Embedding an image | 3 | §2.6 |
| 9 | Why `alt` matters | 3 | §3.1 H |
| 10 | Create a hyperlink | 3 | §2.7 |
| 11 | Internal link | 3 | §2.7 |
| 12 | `<ul>` vs `<ol>` vs `<li>` | 3 | §3.1 K |
| 13 | Purpose of `<div>`/`<span>` | 3 | §2.11 |
| 14 | Basic table + elements | 3 | §2.11 |
| 15 | Purpose of `<a>` | 3 | §3.1 I |
| 16 | Email hyperlink | 3 | §2.7 |
| 17 | Bullet-point list | 3 | §3.1 K |
| 18 | `<ol>` vs `<ul>` + scenario | 3 | §3.1 K |
| 19 | `target` attribute | 3 | §3.1 I |
| 20 | `id` for internal linking | 3 | §2.7 |
| 21 | HTML5 input types | 3 | §3.1 N |
| 22 | `autocomplete` | 3 | §2.13 |
| 23 | `email` input | 3 | §3.1 N |
| 24 | `text` vs `password` | 3 | §3.1 N |
| 25 | `<article>` vs `<section>` | 3 | §3.1 P |
| 26 | Role of a browser | 3 | §3.1 E |
| 27 | Servers vs browsers | 3 | §3.1 E |
| 28 | URIs and URLs | 3 | §2.2 |
| 29 | Code: image + hyperlink | 3 | §3.1 H |
| 30 | Role of `<meta>` | 3 | §3.1 Q |
| 31 | Semantic elements | 3 | §3.1 P |
| 32 | URI vs URL + examples | 3 | §3.1 C |
| 33 | MIME in web communication | 3 | §3.1 D |
| 34 | Skeleton + headings + `<img>` | 3 | §3.1 F |
| 35 | Entities, `<hr>`, `<meta>` | 3 | §3.1 Q |
| 36 | div vs span + table | 3 | §3.1 L, M |
| 161 | ARPANET vs Internet; browser↔server | 14 | §3.2.1 |
| 162 | Milestones; HTML+HTTP+browsers | 14 | §3.2.2 |
| 163 | Client-server; URL structure | 14 | §3.2.3 |
| 164 | Semantic elements; div vs semantic | 14 | §3.2.4 |
| 165 | HTML5 structure; metadata | 14 | §3.2.5 |
| 166 | Headings: UX/SEO/a11y | 14 | §3.2.6 |
| 167 | Responsive images; optimisation | 14 | §3.2.7 |
| 168 | Nav menu; div layout | 14 | §3.2.8 |
| 169 | `<meta>`; block vs inline | 14 | §3.2.9 |
| 170 | Table + caption; entities | 14 | §3.2.10 |
| 171 | Form + labels; ol vs ul | 14 | §3.2.11 |
| 172 | Internal navigation + code | 14 | §3.2.12 |
| 173 | Lists purpose; ol+ul page | 14 | §3.2.13 |
| 174 | `<nav>` vs `<footer>` | 14 | §3.2.14 |
| 175 | audio vs video; video snippet | 14 | §3.2.15 |
| 176 | Role of `<input>`; sample form | 14 | §3.2.11 |
| 177 | Image+list code; 5 tags | 14 | §3.2.16 |
| 178 | Table page; HTTP messages | 14 | §3.2.17 |
| 179 | Evolution; request-response cycle | 14 | §3.2.2 |
| 180 | Input elements; registration form | 14 | §3.2.11 |
| 181 | Tables; timetable code | 14 | §3.2.10 |
| 182 | Evolution; URI/URL/MIME | 14 | §3.2.2 |
| 183 | Structure; headings + image a11y | 14 | §3.2.5 |
| 184 | Internal links; list types | 14 | §3.2.12 |
| 185 | Input types; datalist; structure | 14 | §3.2.18 |

---

## 2. Core concepts

### 2.1 Internet vs World Wide Web (`1:L27–66`)

**Internet** = packet-switched network of networks speaking TCP/IP; no owner, fault-tolerant by design (`1:L27`).
**WWW** = hypertext service on top of it: HTML documents, URL addresses, HTTP transfer, browser rendering (`1:L50–66`).

| | Internet | WWW |
|---|---|---|
| What | Infrastructure | Service running on it |
| Protocol | TCP/IP | HTTP/HTTPS over TCP/IP |
| Unit | Packet | Page/resource at a URL |
| Born | 1969, ARPANET | 1989–91, CERN (Berners-Lee) |
| Analogy | Roads | One kind of traffic |

Three pillars (1989): HTML (structure) + URI/URL (address) + HTTP (transfer) (`1:L70–74`). Generations: 1.0 read-only → 2.0 read-write/AJAX → 3.0 semantic/decentralised (`1:L76–81`).

Timeline (`1:L34–48`): 1957 ARPA · 1969 ARPANET (4 nodes) · 1971 email + `@` · 1974 TCP (Cerf, Kahn) · 1983 TCP/IP adopted ("birth of the Internet") · 1989 WWW proposal · 1990 first browser + server · 1991 Web public · 1993 Mosaic · 1994 Netscape + W3C · 1995 JavaScript, e-commerce · 2004 Web 2.0 · 2014 HTML5 Recommendation.

### 2.2 URI, URL, URN (`1:L87–135`)

**URI** identifies a resource; two subtypes: **URL** = where + how, **URN** = name only (`urn:isbn:0-486-27557-4`).
Rule: all URLs are URIs; not all URIs are URLs.

| URL part | Example | Job |
|---|---|---|
| Scheme | `https://` | Protocol (http, https, ftp, mailto, tel, file) |
| Host | `www.saintgits.org` | Server name or IP |
| Port | `:443` | Door number (80 http, 443 https; omitted when default) |
| Path | `/dept/cse/faculty.html` | Resource on that server |
| Query | `?year=2026&dept=cse` | Key=value data, `?` then `&` |
| Fragment | `#profile` | Position inside the page — browser-only, never sent |

**Absolute** = scheme + host + path; **relative** = resolved against the current document (`../css/style.css`) (`1:L112–123`).
**Percent-encoding**: reserved/unsafe characters become `%XX` — space `%20`, `#` `%23`, `&` `%26`, `/` `%2F`, `?` `%3F` (`1:L125–135`).

### 2.3 Client–server and HTTP (`1:L4–6`; standard)

**Client** (browser) initiates; **server** (Apache/Nginx + PHP) listens, executes, answers. HTTP is stateless — hence cookies and sessions.

Request:
```
GET /dept/cse/faculty.html?year=2026 HTTP/1.1
Host: www.saintgits.org
User-Agent: Mozilla/5.0
Accept: text/html
```
Response:
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 5120
Last-Modified: Fri, 06 Nov 2026 08:00:00 GMT
```
- Line 1 = request line (method, target, version) or status line (version, code, reason); then headers; blank line; optional body.
- `Host` = request only (virtual hosting). `Last-Modified` = response only (caching). `Content-Type`/`Content-Length` = both.
- Codes: 200 OK · 301 moved · 304 not modified · 400 bad request · 403 forbidden · 404 not found · 500 server error.
- Cycle: URL → DNS → TCP+TLS → request → server (PHP/MySQL) → response → parse HTML → fetch CSS/JS/images → render.

### 2.4 MIME types (`1:L141–167`)

**MIME** = Multipurpose Internet Mail Extensions: a `type/subtype` label telling the receiver how to treat the bytes. Born for email attachments, now the HTTP `Content-Type` header.
Syntax `type/subtype[;parameter]` — `text/html; charset=UTF-8`.
Common: `text/html`, `text/css`, `text/plain`, `application/javascript`, `application/json`, `application/pdf`, `application/xml`, `image/jpeg|png|gif|svg+xml`, `audio/mpeg`, `video/mp4`, `multipart/form-data`, `application/octet-stream`.

### 2.5 Document skeleton, elements, headings (`1:L182–237`)

**HTML** = HyperText Markup Language: markup, not programming — tags declare structure and meaning; there are no variables or loops.

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
- `<!DOCTYPE html>` — declaration, not a tag; switches the browser to standards mode. Left out → quirks mode.
- `<html lang>` — root; `lang` feeds screen readers and search engines.
- `<head>` — machine-facing: charset, viewport, title, description, `<link>`, `<script>`. Nothing here is page content. Charset must appear in the first 1024 bytes.
- `<body>` — everything the user sees.
- Element anatomy (`1:L209–222`): opening tag + attributes + content + closing tag. Void elements: `br hr img input meta link`.
- Text level: `p` paragraph · `em` stress · `strong` importance · `br` line break.
- Headings `h1`–`h6`: one `h1`, no skipped levels, size belongs in CSS (`1:L224–237`).

### 2.6 Images (`1:L239–267`)

```html
<img src="logo.png" alt="Saintgits College of Engineering logo" width="200" height="100" loading="lazy">
```
`src` required · `alt` = text alternative (load failure, screen reader, SEO) · `width`/`height` reserve space, avoid layout shift · `loading="lazy"` defers off-screen · `title` tooltip.
Formats: JPEG (photos, lossy) · PNG (transparency, lossless) · GIF (animation) · SVG (vector) · WebP (modern).
Image as link: `<a href="..."><img ...></a>`.

### 2.7 Hyperlinks (`1:L276–322`)

```html
<a href="https://www.saintgits.org" target="_blank" rel="noopener noreferrer">Visit</a>
<a href="about.html">About</a>
<a href="mailto:info@saintgits.org?subject=Enquiry">Email</a>
<a href="tel:+914812345678">Call</a>
<a href="report.pdf" download>Download</a>
```
- `href` required; `target` = `_self` (default) · `_blank` (new tab, pair with `rel="noopener noreferrer"`) · `_parent` · `_top`.
- Internal link: give the target `id`, link `href="#id"`; ids unique; `#top` scrolls up; cross-page `page.html#section2`; fragment never reaches the server.

### 2.8 Lists (`1:L324–380`)

- `<ul>` — order irrelevant, bullets (nav menus, features).
- `<ol>` — order matters, numbered; `type="1|A|a|I|i"`, `start`, `reversed`.
- `<li>` — item, only inside `ul`/`ol`.
- `<dl>` — `<dt>` term + `<dd>` definition (glossary).
- Nest inside the owning `<li>`, never beside the outer list.

### 2.9 Entities and `<hr>` (`1:L389–414`)

`&lt;` `<` · `&gt;` `>` · `&amp;` `&` · `&quot;` `"` · `&apos;` `'` · `&nbsp;` · `&copy;` © · `&reg;` ® · `&#8377;` ₹ · `&ndash;` –.
Why: a literal `<b>` in body text is parsed as a tag; `&lt;b&gt;` displays it. `<hr>` = thematic break, void element.

### 2.10 `<meta>` (`1:L416–438`)

| Form | Example | Effect |
|---|---|---|
| charset | `<meta charset="UTF-8">` | Correct rendering of ₹, é, → |
| name+content | `description`, `keywords`, `author`, `viewport`, `robots` | Search snippet, mobile scaling, indexing |
| http-equiv+content | `refresh`, `content-type` | Simulated HTTP header |

Two that change behaviour: viewport (without it mobile lays out at ~980px and zooms out) and description (usually the grey search snippet).

### 2.11 div, span, tables (`1:L440–503`)

| | `<div>` | `<span>` |
|---|---|---|
| Display | Block: new line, full width | Inline: inside a line, content width |
| Use | Group page regions, wrappers, cards | Style/script a few words |
| Semantics | None | None |

```html
<table>
  <caption>Semester Result</caption>
  <thead><tr><th scope="col">Course</th><th scope="col">Grade</th></tr></thead>
  <tbody><tr><td>Web Programming</td><td>A</td></tr></tbody>
  <tfoot><tr><td colspan="2">Total credits: 4</td></tr></tfoot>
</table>
```
`table` → `caption` (first child) → `thead`/`tbody`/`tfoot` → `tr` → `th` (`scope`) / `td`; `colspan`/`rowspan` merge. Tables are for data only.

### 2.12 Forms (`1:L505–534`)

```html
<form action="/submit.php" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" placeholder="Anjali" required>
  <button type="submit">Submit</button>
</form>
```
- `action` = URL that processes it; `method` = GET (in URL, visible) / POST (in body, for sensitive or large data).
- `name` is the key sent to the server — without it the field is not submitted.
- `<label for>` links text to control: click focuses, screen readers announce.
- `enctype="multipart/form-data"` for file uploads.

### 2.13 Input types, datalist, autocomplete (`1:L539–614`)

`text` · `email` (validates + email keyboard) · `password` (masked; still plain text on the wire) · `number` (steppers, min/max/step) · `range` · `date|month|week|time|datetime-local` · `color` · `tel` · `url` · `search` · `checkbox` · `radio` (same `name` = one choice) · `file` (`accept`) · `hidden` · `submit|reset|button`.

Validation attributes: `required`, `min`/`max`/`step`, `minlength`/`maxlength`, `pattern` (e.g. `[0-9]{6}`), `placeholder` (hint, not a label).
- `<datalist id="x">` + `<input list="x">` = suggestions, free text still allowed (unlike `<select>`).
- `autocomplete` on form or field: `on` / `off` (OTP, sensitive) / named tokens (`name`, `email`, `cc-number`).
- Client-side validation is UX only; the server must re-validate.

### 2.14 Semantic page structure (`1:L616–676`)

`header` intro · `nav` primary links · `main` unique content (once) · `section` themed block with heading · `article` self-contained, syndicatable · `aside` tangential · `footer` closing block · `figure`/`figcaption` media + caption.
Benefits: screen-reader landmarks, SEO region roles, readable markup. `<article>` survives being pulled out; `<section>` only makes sense in this page.

### 2.15 Audio and video (`1:L678–759`)

```html
<video width="640" height="360" controls autoplay muted poster="thumb.jpg" playsinline>
  <source src="demo.mp4" type="video/mp4">
  <source src="demo.webm" type="video/webm">
  <track kind="subtitles" src="subs-en.vtt" srclang="en" label="English" default>
  Your browser does not support the video tag.
</video>
```
- `controls` · `autoplay` (blocked unless `muted`) · `loop` · `muted` · `preload="none|metadata|auto"` · `poster` (video) · `playsinline` (iOS).
- `<source>` = one format per line; the browser takes the first it can play — no single format is universal.
- `<track>` = WebVTT captions/subtitles (accessibility).
- Formats: MP3/OGG/WAV audio; MP4 (H.264)/WebM/OGG video — no single format is universal, hence multiple `<source>`.
- JS API: `play()`, `pause()`, `currentTime`, `volume`, `playbackRate`, `ended`.

---

## 3. Answer bank

### 3.1 Three-mark answers

**A — Internet vs WWW (Q1).** 1. **Internet** — packet-switched network of networks on TCP/IP, from ARPANET 1969. 2. **WWW** — hypertext service on it: HTML + URL + HTTP, CERN 1989–91. 3. **Relation** — the Internet carries other services too (email, FTP); Web needs the Internet, not the reverse.

**B — URL components (Q2).** 1. **Scheme** — `https://`. 2. **Host + port** — `www.saintgits.org:443`. 3. **Path** — `/dept/cse/faculty.html`. 4. **Query + fragment** — `?year=2026&dept=cse#profile`.

**C — URI vs URL (Q28, Q32).** 1. **URI** — any string identifying a resource. 2. **URL** — a URI that also says how and where to fetch it; **URN** names only (`urn:isbn:…`). 3. **Rule** — all URLs are URIs; not all URIs are URLs.

**D — MIME (Q3, Q33).** 1. **Definition** — `type/subtype` label, e.g. `text/html; charset=UTF-8`. 2. **Origin** — email attachments, now HTTP `Content-Type`. 3. **Effect** — the browser picks renderer, player or downloader from it.

**E — Browser vs server (Q4, Q26, Q27).** 1. **Client** — resolves DNS, sends the request, renders HTML/CSS/JS. 2. **Server** — listens on 80/443, runs code, queries the database, returns the response. 3. **Split** — browser is untrusted and visible; server holds data and logic; HTTP is the contract.

**F — Skeleton (Q5, Q6, Q34).** 1. **Doctype** — `<!DOCTYPE html>` = standards mode. 2. **`<head>`** — charset, viewport, title, description, CSS/JS links. 3. **`<body>`** — rendered content; `<html lang="en">` wraps both.

**G — Headings (Q7).** 1. **Structure** — `h1`–`h6`, one `h1`, no skipped levels. 2. **SEO** — engines read heading text as the topic outline. 3. **Accessibility** — screen readers jump heading to heading.

**H — Images and `alt` (Q8, Q9, Q29).** 1. **Syntax** — `<img src alt width height>` is a void element. 2. **`alt`** — shown on failure, read aloud, indexed by search. 3. **Code** — `<a href="p.html"><img src="flower.jpg" alt="Red rose"></a>`.

**I — Links (Q10, Q15, Q16, Q19).** 1. **Syntax** — `<a href="url">text</a>`. 2. **`target`** — `_self` same tab, `_blank` new tab (+ `rel="noopener noreferrer"`). 3. **Schemes** — `mailto:` mail client, `tel:` dial, `download` save.

**J — Internal links (Q11, Q20).** 1. **Target** — `<h2 id="contact">`. 2. **Link** — `<a href="#contact">`. 3. **Rules** — ids unique, fragment handled by browser, cross-page `page.html#contact`.

**K — Lists (Q12, Q17, Q18).** 1. **`<ul>`** — bullets, order irrelevant. 2. **`<ol>`** — numbers, order matters, `type`/`start`. 3. **`<li>`** — the item; `<dl>` with `<dt>`/`<dd>` for term–definition.

**L — div vs span (Q13, Q36a).** 1. **`<div>`** — block container, new line, full width. 2. **`<span>`** — inline, content width. 3. **Neither is semantic** — prefer `header`/`nav`/`section` when the role is known.

**M — Tables (Q14, Q36b).** 1. **Structure** — `table`, `caption`, `tr`, `th`, `td`. 2. **Groups** — `thead`/`tbody`/`tfoot`; `scope` on headers. 3. **Merge** — `colspan`/`rowspan`; never use tables for layout.

**N — Input types (Q21, Q23, Q24).** 1. **Types** — `email`, `url`, `number`, `range`, `date`, `color`, `search`, `tel`, `file`. 2. **Validation** — `email` checks format, `date` gives a picker, `number` adds steppers. 3. **text vs password** — password masks characters; both send plain text, HTTPS protects them.

**O — datalist/autocomplete (Q22).** 1. **`autocomplete`** — `on`/`off`/named tokens, set on form or field. 2. **Effect** — `off` for OTP and sensitive fields; tokens improve autofill accuracy. 3. **`<datalist>`** — suggestions for an input via `list`/`id`, free text still allowed.

**P — Semantic elements (Q25, Q31).** 1. **Set** — `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `figure`. 2. **article vs section** — article stands alone when syndicated; section is a themed part of this page. 3. **Payoff** — landmarks for screen readers, region roles for SEO.

**Q — meta, entities, hr (Q30, Q35).** 1. **`<meta>`** — charset, name+content, http-equiv+content. 2. **Entities** — `&lt; &gt; &amp; &nbsp; &copy;` for markup characters and symbols. 3. **`<hr>`** — void element marking a thematic break.

### 3.2 Fourteen-mark answers

Write: **Structure (marks)** → **Answer** → **Traps**.

#### 3.2.1 Q161 — ARPANET vs modern Internet; browser ↔ server
**Structure (6 + 8).** (a) origin, scale, protocol, ownership, services. (b) define both, then the six-step exchange.
(a) ARPANET 1969: four university nodes, ARPA-funded, closed research community, NCP before TCP/IP, built for survivable communication. Modern Internet: millions of networks, commercial and public, TCP/IP + TLS + HTTP/2-3, no central owner, carries Web/mail/streaming/cloud. ARPANET's contribution: packet switching, the TCP/IP lineage, the email `@` convention, open standards — it became the Internet when TCP/IP was adopted in 1983.
(b) Browser = client that requests resources and renders HTML/CSS, running JS sandboxed. Server = host process listening on a port, running server-side code. Exchange: URL → DNS → TCP+TLS → HTTP request (method, path, headers, body) → PHP/MySQL → HTTP response (status, headers, body) → parse HTML → fetch sub-resources → render. Stateless per request, hence cookies later.

#### 3.2.2 Q162 / Q179a / Q182a — Evolution of the Internet and WWW
**Structure (7 + 7 / 7 + 7).** Timeline table, then the mutual reinforcement of HTML, HTTP and browsers.
Use §2.1 timeline as a three-column table (year | milestone | impact). Impact line to include: each step lowered either the cost of publishing or the cost of access — ARPANET connected machines, TCP/IP connected networks, the Web connected documents, browsers made documents readable by non-experts, HTML5 made them work on phones.
(b) HTML: a forgiving document format anyone could author. HTTP: a trivial request/response protocol any server could implement. Browsers: one program that renders any page. Together, a page written once is readable everywhere — the network effect that outran earlier hypertext systems. For Q182b add: URI gives each document a global address, MIME tells the browser what it received, HTTP moves it — remove any one and the Web cannot function.

#### 3.2.3 Q163 — Client-server model + URL structure
**Structure (7 + 7).** (a) roles, flow, statelessness, why split. (b) six components with a labelled example.
(a) Client initiates, server responds; thin untrusted client, data-bearing server; one server serves many clients; flow: request → process → response. Diagram: client box → request arrow → server box → DB cylinder → response arrow.
(b) Use the §2.2 table plus one labelled URL, then absolute vs relative and percent-encoding. End with "the fragment never reaches the server".

#### 3.2.4 Q164 — Semantic elements; div vs semantic
**Structure (7 + 7).** Name five elements and their roles; then compare div-only markup with the semantic version.
(a) §2.14 element list, three benefits (landmarks, SEO, maintainability), `main` once per page, article vs section.
(b) `<div>` is meaning-free and useful only as a layout wrapper; `<section>` is themed and headings-bearing; `<article>` is independently distributable; `header`/`footer` bracket page or section; `<nav>` marks navigation. Show the same page as div soup and as semantics.

#### 3.2.5 Q165 / Q183a — Structure and metadata
**Structure (7 + 7).** Skeleton code with line-by-line roles; then what metadata changes.
(a) §2.5 skeleton; draw the tree html → (head: title, meta, link | body: header, main, footer).
(b) charset (correct glyphs), viewport (mobile scaling — without it responsive CSS is void), description (search snippet), keywords (largely ignored), author, robots (index/noindex), http-equiv refresh (self-redirect). Metadata is not displayed, but it decides how the page is indexed, cached, scaled and announced.

#### 3.2.6 Q166 — Headings for UX, SEO, accessibility
**Structure (7 + 7).** (a) scanning and ranking. (b) screen-reader navigation and outline order.
(a) Headings are the table of contents: a reader skims `h2`s; engines weight heading text and hierarchy; `h1` carries the page topic.
(b) Screen readers list and jump headings; logical order `h1→h2→h3` builds a usable outline; skipped levels and bold-text pseudo-headings break it. Rule: one `h1`, no skips, style with CSS.

#### 3.2.7 Q167 — Responsive images and optimisation **(standard)**
**Structure (7 + 7).** (a) `srcset`/`sizes` and `<picture>`. (b) compression, sizing, lazy loading, formats.
(a) `<img srcset="small.jpg 480w, large.jpg 1200w" sizes="(max-width:600px) 100vw, 50vw" src="fallback.jpg" alt="…">` lets the browser choose by viewport/DPR; `<picture>` with `<source media>` or `type="image/webp"` selects by condition or format.
(b) Compress (JPEG ~75, WebP/AVIF), size the file to the display size, lazy-load below the fold, set width/height to avoid layout shift, SVG for icons, CDN caching. Images are usually the largest payload, so this is the cheapest performance win and it moves LCP/CLS.

#### 3.2.8 Q168 — Nav menu; div layout
**Structure (6 + 8).** (a) nav as a list, why. (b) header/content/footer divs plus CSS.
(a) `<nav><ul><li><a>` — a menu *is* a list; screen readers announce the item count; CSS styles it uniformly; it degrades gracefully.
(b)
```css
#header{border-bottom:2px solid #333;padding:10px}
#content{display:flex;gap:20px;padding:20px}
#footer{border-top:1px solid #999;text-align:center;padding:10px}
```
Explain each rule, then note the modern preference for `header`/`main`/`footer`.

#### 3.2.9 Q169 — `<meta>` for SEO/mobile; block vs inline
**Structure (7 + 7).** (a) the tags that matter. (b) the two display models.
(a) `description` (snippet), `viewport` (mobile), `robots`, charset; Open Graph `og:title` and `theme-color` **(standard)** share the page elsewhere.
(b) Block: new line, full width, honours width/height and vertical margins — `div`, `p`, `h1`, `ul`, `table`, `form`. Inline: flows in text, content width, vertical margins ignored — `span`, `a`, `img`, `strong`, `input`. `display` can change either.

#### 3.2.10 Q170 / Q181 — Tables with captions; timetable
**Structure (8 + 6 / 7 + 7).** (a) product table markup. (b) why tables, then the timetable.
(a) `caption` first, `thead` with `scope="col"`, three rows, `tfoot` with `colspan`; CSS `border-collapse:collapse` and zebra rows.
(b) Tables align multi-attribute data for comparison and support `scope` for accessibility — and are not a layout tool.
Timetable: columns Day + five periods, `rowspan="2"` for lab blocks, `th scope="col"` per period.

#### 3.2.11 Q171 / Q176 / Q180 / Q177a — Forms
**Structure (8 + 6 / 7 + 7).** (a) markup with labels and placeholders. (b) input roles; then the registration form.
(a) name (text), email (email), message (textarea); `<label for>` for each; placeholder shows an example only; `required`; `method="POST"` because a message is not URL-safe.
(b) `<input>` is one generic control whose `type` picks widget and validation; `name` becomes the submitted key.
Registration: name, roll number (`pattern="[0-9]{6}"`), email, password + confirm, date of birth, gender radios, department `<select>`, address `<textarea>`, terms checkbox, submit — every field with a label.

#### 3.2.12 Q172 / Q184a — Internal navigation
**Structure (6 + 8 / 7 + 7).** (a) the three steps. (b) working page with three sections.
(a) unique `id` per section → `<nav>` links `href="#id"` → browser scrolls and updates the fragment; server never sees it.
(b) `<nav>` with three links, three `<section id>` blocks with headings, "back to top" link; add `scroll-behavior:smooth` **(standard)**; ids unique, may not start with a digit **(standard)**.

#### 3.2.13 Q173 / Q184b — Lists in depth
**Structure (6 + 8 / 7 + 7).** (a) purpose and the two ordered models. (b) combined page.
(a) Lists express set membership vs sequence vs term-definition; ol for procedures and rankings, ul for features and ingredients, dl for glossaries.
(b) `<ol>` of brewing steps + `<ul>` of features + `<dl>` glossary; explain how numbering vs bullets conveys sequence vs equality.

#### 3.2.14 Q174 — `<nav>` vs `<footer>`
**Structure (6 + 8).** (a) roles and landmarks. (b) page skeleton.
(a) `nav` = primary navigation block, a jump target for screen readers; `footer` = closing content (copyright, contact), landmark "contentinfo"; several `nav` per page is fine, one page-level footer.
(b) `header` with `h1` + `nav><ul>`, `main`, `footer` with `&copy;` and contact links; explain each region.

#### 3.2.15 Q175 — audio vs video
**Structure (7 + 7).** (a) shared API, different attributes. (b) video snippet explained.
(a) Both are HTML5 media elements with the same `HTMLMediaElement` API; audio has no visual track, so no width/height/poster; video adds those plus `playsinline`; both take `controls`, `autoplay` (muted), `loop`, `muted`, `preload`, `<source>` fallbacks, `<track>` captions.
(b) The §2.15 snippet: name every attribute, why `muted` is required for autoplay, why two `<source>` elements exist.

#### 3.2.16 Q177 — Image + list code; five tags
**Structure (4 + 10).** Two snippets, then a five-row table.
```html
<img src="flower.jpg" alt="A red rose in bloom" width="300" height="200">
<ul><li>tea</li><li>coffee</li><li>milk</li></ul>
```
`<textarea>` multi-line text with rows/cols/name · `<span>` inline container · `<tr>` table row · `<form>` input collection with `action`/`method` · `<a>` hyperlink with `href`.

#### 3.2.17 Q178 — Table page; HTTP messages
**Structure (8 + 6).** (a) product table. (b) request/response formats and the three headers.
(a) §3.2.10(a) markup adapted to product/price/availability.
(b) Request: request line → headers → blank line → body. Response: status line → headers → blank line → body. `Host` request-only, `Last-Modified` response-only, `Content-Type`/`Content-Length` both. Add status codes 200/301/404/500.

#### 3.2.18 Q185 — Input types; datalist; page structure
**Structure (7 + 7).** Five input types with code, then `<datalist>` + `autocomplete`, then the semantic skeleton.
Combine §2.13 and §2.14: `email`, `date`, `number`, `range`, `color` with one line each; `list`/`id` datalist example; `header/nav/section/article/footer` skeleton with one line per region.

---

## 4. Markup to write from memory

1. Skeleton — doctype, html+lang, head (charset, viewport, title), body h1+p.
2. Image with all attributes, plus wrapped in a link.
3. Three link types — external `_blank` + `rel`, relative, `mailto:` with subject.
4. Internal nav with three `id` sections.
5. Nested list inside the correct `<li>`.
6. Description list, three pairs.
7. Result table — caption, thead/tbody/tfoot, `scope`, one `colspan`.
8. Timetable — 5 rows × 6 columns, two `rowspan`.
9. Registration form — text/email/password/date/radio/select/textarea/checkbox, `required`, `pattern`.
10. datalist combo box.
11. Semantic page with header/nav/main/section/article/aside/footer.
12. Video with poster, two sources, captions, fallback text.
13. Entities sentence rendering `&lt;b&gt;` and `&amp;` correctly.
14. `<meta>` block — charset, viewport, description, author, keywords, refresh.

---

## 5. Night-before memorize

| Item | Recall | Why |
|---|---|---|
| Pillars | HTML + URI + HTTP (1989) | Every evolution answer |
| Years | 1969 ARPANET · 1983 TCP/IP · 1989 proposal · 1991 public · 1993 Mosaic · 1994 W3C · 2014 HTML5 | Q162, Q179, Q182 |
| URL parts | scheme, host, port, path, query, fragment | Q2, Q163b |
| URI rule | all URLs are URIs; URN names only | Q28, Q32 |
| MIME | `type/subtype; charset=UTF-8` | Q3, Q33 |
| Void elements | `br hr img input meta link` | Any code answer |
| Doctype | `<!DOCTYPE html>` first line, standards mode | Q5 |
| Skeleton order | doctype → html[lang] → head → body | Q34, Q165 |
| Viewport | `width=device-width, initial-scale=1.0` | Q169, Q185 |
| Headings | one h1, no skips, CSS for size | Q7, Q166 |
| `alt` | failure text + screen reader + SEO | Q9 |
| `target` | `_self _blank _parent _top`; `_blank` needs `noopener` | Q19 |
| `mailto` | `href="mailto:a@b.com?subject=X"` | Q16 |
| Table tags | table, caption, thead, tbody, tfoot, tr, th, td, colspan, rowspan | Q14, Q170 |
| Input types | text email password number range date color search tel url file checkbox radio hidden | Q21 |
| Validation | required, pattern, min, max, step, minlength, maxlength, placeholder | Q21, Q23 |
| datalist | `<input list="x">` + `<datalist id="x">` | Q22 |
| autocomplete | on / off / named tokens | Q22 |
| Entities | `&lt; &gt; &amp; &quot; &nbsp; &copy;` | Q35 |
| Semantics | header nav main section article aside footer figure | Q25, Q164 |
| Request line | `GET /path HTTP/1.1` | Q178 |
| Headers | Host (req), Last-Modified (res), Content-Type (both) | Q178 |
| Codes | 200, 301, 304, 400, 403, 404, 500 | Q177, Q178 |

---

## 6. Diagram index

| Figure | Where | Draw |
|---|---|---|
| Element anatomy | `1:L216` | tag + attribute + content + closing tag |
| Three pillars | `1:L70–74` | HTML + URL + HTTP |
| URL anatomy | `1:L100–110` | six-part labelled URL |
| Request–response cycle | §2.3 | client → DNS → TCP/TLS → server+DB → response |
| Block vs inline | `1:L443–455` | full-width box vs in-line span |
| Semantic layout | `1:L636–663` | header/nav/main/section/article/aside/footer |
| Box model | `2:p11` (M2) | margin/border/padding/content |

---

## 7. Say-this-if-grilled

1. "The Web is an application on the Internet — TCP/IP is the network, HTML over HTTP at a URL is the Web."
2. "A URL is a URI that also says how to fetch the resource; a URN only names it."
3. "The fragment is client-side — it never reaches the server, which is why `#section` needs no server support."
4. "MIME decides renderer versus downloader from `Content-Type` alone."
5. "`<!DOCTYPE html>` is a standards-mode switch, not a tag; without it browsers use quirks mode."
6. "`<head>` is for machines, `<body>` is for humans."
7. "Headings are the document outline — screen readers and crawlers both navigate by them, so size belongs in CSS."
8. "`alt` is the image's replacement when the image is unavailable to a user or a crawler."
9. "`_blank` without `rel=noopener` hands the new page a handle on your window."
10. "`<div>` and `<span>` have no meaning by design; semantics live in `nav`, `article`, `main`."
11. "HTML5 validation is UX, not security — the client can be bypassed."
12. "Tables are for data; div+CSS replaced table layout because tables couple content to presentation and break screen-reader flow."
