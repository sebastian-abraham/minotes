# Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

WEB PROGRAMMING
Module 1 - Lecture Notes
Introduction to the Web and HTML5

## Topics Covered

| # | Topic | Hrs |
|---|---|---|
| 1 | Evolution of the Internet and World Wide Web; Web Basics URIs and URLS; MIME | 1 |
| 2 | Structuring and Editing an HTML5 Document Fundamentals of HTML; Headings; Images | 1 |
| 3 | Hyperlinks Internal Linking; Lists | 1 |
| 4 | Special Characters and Horizontal Rules; meta Elements; div and span; Tables; Forms | 2 |
| 5 | HTML5 Form Input Types input and datalist Elements; autocomplete Attribute; Page Structure Elements | 1 |
| 6 | HTML5 Audio and Video Elements Multimedia | 1 |

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

## 1. Evolution of the Internet and the World Wide Web

### 1.1 What is the Internet?
The Internet is a global network of interconnected computer networks that communicate using a common set of rules called protocols, principally TCP/IP (Transmission Control Protocol / Internet Protocol). It is a network of networks it does not belong to any single organisation or country, and no central authority controls it.
It carries many services: email, file transfer (FTP), remote login, and the World Wide Web.
It is packet-switched: data is broken into small packets, routed independently, and reassembled at the destination.
Its decentralised design makes it fault-tolerant - if one path fails, packets are rerouted.

### 1.2 Historical Timeline

| Year | Milestone |
|---|---|
| 1957 | Sputnik launch prompts the US to form ARPA (Advanced Research Projects Agency). |
| 1969 | ARPANET goes live - the first four nodes connect UCLA, SRI, UCSB and University of Utah. |
| 1971 | Ray Tomlinson sends the first network email and introduces the '@' addressing convention. |
| 1974 | Vint Cerf and Bob Kahn publish the TCP protocol specification. |
| 1983 | ARPANET formally adopts TCP/IP; this date is often cited as the 'birth of the Internet'. |
| 1989 | Tim Berners-Lee, at CERN, proposes an information management system the origin of the www. |
| 1990 | Berners-Lee writes the first web browser/editor (WorldWide Web) and the first web server. |
| 1991 | The World Wide Web is made publicly available on the Internet. |
| 1993 | NCSA Mosaic, the first popular graphical browser, is released. |
| 1994 | Netscape Navigator launches; W3C (World Wide Web Consortium) is founded by Berners-Lee. |
| 1995 | JavaScript is created; e-commerce (Amazon, eBay) begins. |
| 2004 | Term 'Web 2.0' popularised user-generated content, social media, AJAX-driven interactivity. |
| 2014 | HTML5 becomes an official W3C Recommendation. |

### 1.3 Internet vs World Wide Web
A very common point of confusion: the Internet and the Web are not the same thing.

| Aspect | Internet | World Wide Web |
|---|---|---|
| What it is | Physical/logical network infrastructure | A service that runs on top of the Internet |
| Protocols | TCP/IP, UDP, etc. | HTTP/HTTPS (uses TCP/IP underneath) |

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming Module 1 Lecture Notes

| Aspect | Internet | World Wide Web |
|---|---|---|
| Unit of information | Data packets | Web pages/resources identified by URLs |
| Analogy | The road network | One type of vehicle traffic (there are others: email, FTP) |
| Introduced | 1969 (ARPANET) | 1989-1991 (Tim Berners-Lee, CERN) |

Introduction to the Web & HTML5

### 1.4 Three Pillars of the Original Web (Berners-Lee, 1989)
1. HTML (HyperText Markup Language) a language to structure documents with hyperlinks.
2. URI/URL a uniform way to address any resource on the network.
3. HTTP (HyperText Transfer Protocol) a protocol to request and transfer those resources.
Together these three inventions made it possible to link and retrieve documents stored on different machines anywhere in the world, using a browser - this combination is what we call the World Wide Web.

### 1.5 Generations of the Web
Web 1.0 (mid-1990s): Static, read-only pages. Content is published by a few and consumed by many.
Web 2.0 (2000s): Read-write web. User-generated content, blogs, wikis, social networks, AJAX for dynamic pages without full reloads.
Web 3.0 (emerging): Semantic/intelligent web, decentralisation, machine-readable data, and increasingly Al-driven services.
Exam tip:
Be ready to distinguish 'Internet' (the network) from 'Web' (an application/service riding on the Internet), and to place ARPANET (1969) vs the Web's invention at CERN (1989-91) correctly on a timeline.

### 1.6 Web Basics
URI and URL
Every resource on the Web a page, an image, a video, a script needs a unique address so that it can be located and retrieved. This addressing scheme is defined by URIs.

#### 1.6.1 URI (Uniform Resource Identifier)
A URI is a compact string of characters that identifies an abstract or physical resource. It is the umbrella term, and it has two sub-types:
URL (Uniform Resource Locator) identifies a resource AND tells you how/where to access it (its location).
URN (Uniform Resource Name) identifies a resource by name in a particular namespace, without necessarily specifying how to locate it, e.g. an ISBN: urn:isbn:0-486-27557-4.
Rule of thumb: "All URLs are URIs, but not all URIs are URLs." A URL always tells you where and how; a URN only tells you what.

#### 1.6.2 Anatomy of a URL

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

| Component | Example | Purpose |
|---|---|---|
| Scheme / Protocol | https:// | Rule used to access the resource (http, https, ftp, mailto, file) |
| Host (Domain) | www.saintgits.org | Name/IP address of the server holding the resource |
| Port | :443 | TCP port the server listens on (80 for HTTP, 443 for HTTPS by default, often omitted) |
| Path | /dept/cse/faculty.html | Location of the resource on the server (like a file-system path) |
| Query String | ?year=2026&dept=cse | Key-value pairs sent to the server, starting with '?', pairs joined by '&' |
| Fragment / Anchor | #profile | Points to a specific part within the resource itself (handled by the browser, not sent to the server) |

https://www.saintgits.org:443/dept/cse/faculty.html?year=2026&dept=cse#profile
scheme host port path query fragment

#### 1.6.3 Absolute vs Relative URLs
Absolute URL: gives the complete address scheme, host and path, e.g. https://saintgits.in/images/logo.png
Relative URL: gives the path relative to the current document's location, e.g. images/logo.png or ../css/style.css

```html
<!-- Absolute -->
<a href="https://icscst2026.saintgits.in/schedule.html">Schedule</a>
<!-- Relative, same folder -->
<a href="schedule.html">Schedule</a>
<!-- Relative, parent folder -->
<a href="../index.html">Home</a>
```

#### 1.6.4 URL Encoding (Percent-Encoding)
URLs can only safely contain a limited set of ASCII characters. Reserved and unsafe characters (spaces, &, #, ?, non-ASCII characters, etc.) must be percent-encoded as %XX, where XX is the hexadecimal ASCII/UTF-8 code.

| Character | Encoded |
|---|---|
| space | %20 (or + in query strings) |
| # | %23 |
| & | %26 |
| / | %2F |
| ? | %3F |
| : | %3A |

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes

### 1.7 MIME (Multipurpose Internet Mail Extensions)
Introduction to the Web & HTML5
MIME types (also called media types or content types) tell a receiving application what kind of data a file contains, so it knows how to handle or render it. Originally designed to let email carry non-text attachments, MIME types are now fundamental to how HTTP transfers content every HTTP response carries a Content-Type header stating the MIME type of the body.

#### 1.7.1 Syntax
type/subtype [;parameter]
Example: text/html; charset=UTF-8
The 'type' is a general category and the 'subtype' identifies the specific format within it. An optional parameter (like charset) can add more detail.

#### 1.7.2 Common MIME Types

| MIME Type | Used For |
|---|---|
| text/html | HTML documents |
| text/css | CSS stylesheets |
| text/plain | Plain text files |
| application/javascript (or text/javascript) | JavaScript files |
| application/json | JSON data |
| application/pdf | PDF documents |
| application/xml | XML documents |
| image/jpeg, image/png, image/gif, image/svg+xml | Image formats |
| audio/mpeg, audio/ogg, audio/wav | Audio formats |
| video/mp4, video/webm, video/ogg | Video formats |
| multipart/form-data | Form submissions that include file uploads |
| application/octet-stream | Generic binary data (unknown type) |

The server sends the MIME type in the HTTP Content-Type response header, e.g. Content-Type: text/html; charset=UTF-8. The browser uses this to decide whether to render the content as a page, display an image, play audio/video, or prompt a download.

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

## 2. Structuring and Editing an HTML5 Document

### 2.1 What is HTML?
HTML (HyperText Markup Language) is not a programming language - it is a markup language that describes the structure and meaning (semantics) of content using elements made up of tags. Browsers parse HTML and render it as a visual (or audible, for screen readers) page.
HyperText: text containing links to other text/resources.
Markup: annotations (tags) added to plain text to describe structure headings, paragraphs, lists, etc.
HTML5 is the fifth and current major version of HTML, standardised by the W3C/WHATWG, adding semantic elements, multimedia support, form enhancements, and APIs (Canvas, Geolocation, Local Storage, etc.).

### 2.2 Basic Structure of an HTML5 Document
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

#### 2.2.1 Line-by-line Explanation

| Line | Meaning |
|---|---|
| `<!DOCTYPE html>` | Document type declaration. Tells the browser to use HTML5 standards mode. Must be the very first line. |
| `<html lang="en">` | Root element enclosing the whole document; lang aids accessibility and search engines. |
| `<head>` | Container for meta-information not displayed directly on the page (title, meta tags, links to CSS/JS). |
| `<meta charset="UTF-8">` | Declares character encoding so text (including special/international characters) displays correctly. |
| `<title>` | Text shown in the browser tab/window title and used as the default bookmark name. |
| `<body>` | Contains all visible page content. |

### 2.3 Anatomy of an HTML Element

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

*[Image Description: A diagram illustrating the anatomy of an HTML element. It displays the code `<p class="intro">Hello World</p>` with lines pointing to its specific parts: `<p` is labelled as the "opening tag / tag name", `class` is the "attribute name", `"intro"` is the "attribute value", `Hello World` is the "content", and `</p>` is the "closing tag".]*

Most elements have an opening tag `<tagname>` and closing tag `</tagname>`, enclosing content.
Empty/void elements have no content and no closing tag: `<br>`, `<hr>`, `<img>`, `<input>`, `<meta>`, `<link>`.
Attributes are `name="value"` pairs inside the opening tag that configure or describe the element (id, class, src, href, etc.).
HTML is (mostly) case-insensitive for tags, but the convention/best practice is lowercase.
Elements can be nested, but nesting must not overlap a properly nested document is essential for valid HTML.

### 2.4 Headings
HTML provides six levels of section headings, `<h1>` through `<h6>`, in decreasing order of importance/size.
```html
<h1>Main Page Title</h1>
<h2>Section Heading</h2>
<h3>Sub-section Heading</h3>
<h4>Minor Heading</h4>
<h5>Smaller Heading</h5>
<h6>Smallest Heading</h6>
```
`<h1>` should be used once per page to represent the main topic - important for SEO and accessibility.
Headings should be used to convey document structure/outline, not merely to make text bigger or bold use CSS for pure styling.
Heading levels should not be skipped arbitrarily (e.g. jumping from `<h1>` directly to `<h4>`) for a well-formed outline, though browsers will not enforce this.
Screen readers let users navigate a page by jumping between headings, so semantic use matters for accessibility.

### 2.5 Images
The `<img>` tag embeds an image into the page. It is a void (self-closing) element.
```html
<img src="logo.png" alt="Saintgits College Logo" width="200" height="100">
```

| Attribute | Purpose |
|---|---|
| src | Path/URL to the image file (required). |
| alt | Alternative text describing the image shown if the image fails to load and read aloud by screen readers. Required for accessibility. |
| width / height | Sets display dimensions (in pixels by default); helps the browser reserve space before the image loads, reducing layout shift. |

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes

| Attribute | Purpose |
|---|---|
| title | Tooltip text shown on hover (optional). |
| loading | 'lazy' defers off-screen image loading for performance. |

Introduction to the Web & HTML5
Supported common image formats: JPEG/JPG (photographs, lossy compression), PNG (supports transparency, lossless), GIF (supports simple animation), SVG (vector graphics, scales without quality loss), WebP (modern, efficient compression).
Using an image as a link: wrap the `<img>` tag inside an `<a>` tag.
```html
<a href="https://saintgits.org">
<img src="logo.png" alt="Saintgits Home">
</a>
```

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

## 3. Hyperlinks and Lists

### 3.1 Hyperlinks - The <a> Element
The anchor element `<a>` is what makes HTML 'hypertext' it creates a clickable link to another resource: another page, another site, a file, an email address, a phone number, or a location within the same page.
```html
<a href="https://www.saintgits.org" target="_blank" rel="noopener noreferrer">
Visit Saintgits
</a>
```

| Attribute | Purpose |
|---|---|
| href | Destination URL (Hypertext REFerence) - required for the link to be functional. |
| target | Where to open the link: _self (default, same tab), _blank (new tab/window), _parent, _top. |
| rel | Relationship to the target; rel="noopener noreferrer" is a security best practice with target="_blank". |
| download | Prompts the browser to download the linked resource rather than navigate to it. |

#### 3.1.1 Types of Links
External link: points to another website. e.g. `<a href="https://www.w3.org">W3C</a>`
Internal link: points to another page within the same site, usually with a relative URL. e.g. `<a href="about.html">About Us</a>`
Email link: uses the mailto: scheme. e.g. `<a href="mailto:info@saintgits.org">Email us</a>`
Telephone link: uses the tel: scheme. e.g. `<a href="tel:+914812345678">Call us</a>`
Fragment/anchor link: jumps to a specific point within a page (see below).

#### 3.1.2 Internal Linking (Same-page navigation with Fragments)
To link to a specific section within a page, give the target element an id attribute, then point the href at #id.
```html
<!-- Table of contents at the top of the page -->
<nav>
<a href="#section1">Introduction</a> |
<a href="#section2">Syllabus</a> |
<a href="#section3">Contact</a>
</nav>
<!-- Later in the same document -->
<h2 id="section1">Introduction</h2>
<p>...</p>
<h2 id="section2">Syllabus</h2>
<p>...</p>
<h2 id="section3">Contact</h2>
<p>...</p>
```

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming Module 1 Lecture Notes
Introduction to the Web & HTML5
id values must be unique within a page (no two elements share the same id).
A link to "#top" (or an empty fragment, href="#") conventionally scrolls to the top of the page.
You can also link to a section of a different page: page.html#section2.

### 3.2 Lists
HTML provides three list types to present grouped/sequenced content.

#### 3.2.1 Unordered List <ul>
Used when the order of items does not matter; items are marked with bullets by default.
```html
<ul>
<li>HTML</li>
<li>CSS</li>
<li>JavaScript</li>
</ul>
```

#### 3.2.2 Ordered List <ol>
Used when sequence/order matters; items are numbered automatically.
```html
<ol type="1" start="1">
<li>Boil water</li>
<li>Add tea leaves</li>
<li>Simmer for 2 minutes</li>
</ol>
```
type attribute controls the marker style: "1" (default, numbers), "A", "a", "I", "i" (letters/roman numerals).
start attribute sets the starting number/letter.
reversed attribute counts the list down instead of up.

#### 3.2.3 Description List <dl>
Used for name-value / term-description pairs, such as a glossary.
```html
<dl>
<dt>HTML</dt>
<dd>HyperText Markup Language</dd>
<dt>CSS</dt>
<dd>Cascading Style Sheets</dd>
</dl>
```

#### 3.2.4 Nested Lists
```html
<ul>
<li>Frontend
<ul>
<li>HTML</li>
<li>CSS</li>
</ul>
```

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
```html
</li>
<li>Backend</li>
</ul>
```
Introduction to the Web & HTML5
A nested list is placed as a child of the `<li>` element it belongs under, not as a sibling of the outer `<ul>`/`<ol>`.

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

## 4. Special Characters, Horizontal Rules, meta, div/span, Tables and Forms

### 4.1 Special Characters (Character/Entity References)
Some characters have special meaning in HTML markup (like < and >) or are not easily typed on a keyboard (like or non-breaking space). These must be written using character entities, in the form `&name;` or `&#number;`.

| Character | Entity Name | Numeric |
|---|---|---|
| < | `&lt;` | `&#60;` |
| > | `&gt;` | `&#62;` |
| & | `&amp;` | `&#38;` |
| " | `&quot;` | `&#34;` |
| ' | `&apos;` | `&#39;` |
| Non-breaking space | `&nbsp;` | `&#160;` |
| © | `&copy;` | `&#169;` |
| ® | `&reg;` | `&#174;` |
| ₹ (Rupee) | `&#8377;` | `&#8377;` |
| – (en dash) | `&ndash;` | `&#8211;` |

Why it matters: writing `<b>bold</b>` in a paragraph would be interpreted as an actual tag by the browser; you must write `&lt;b&gt; bold&lt;/b&gt;` to display the literal angle brackets.

### 4.2 Horizontal Rule
`<hr>`
The `<hr>` element inserts a thematic break a horizontal line used to separate content into distinct sections (e.g., a change of topic within a chapter). It is a void element with no closing tag.
```html
<p>Section one content...</p>
<hr>
<p>Section two content...</p>
```

### 4.3 The <meta> Element
meta elements provide metadata about the HTML document - information about the page that isn't displayed but is used by browsers, search engines, and other web services. They live inside `<head>` and are void elements.
```html
<meta charset="UTF-8">
<meta name="description" content="Department of CSE, Saintgits College of Engineering">
<meta name="keywords" content="HTML, CSS, JavaScript, Web Programming">
<meta name="author" content="Justin Mathew">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="30">
```

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming Module 1 Lecture Notes

| Attribute Combination | Purpose |
|---|---|
| charset | Declares the character encoding of the document. |
| name + content | General metadata: description, keywords, author, viewport (responsive design), robots. |
| http-equiv + content | Simulates an HTTP response header, e.g. auto-refresh, content-type. |

Introduction to the Web & HTML5
The 'description' meta tag is often shown as the snippet text in search-engine results, and the 'viewport' meta tag is essential for making a page render correctly on mobile devices.

### 4.4 div and span - Generic Containers
div and span are content-neutral generic containers used purely for grouping content so that CSS/JavaScript can target the group they carry no semantic meaning of their own.

| | `<div>` | `<span>` |
|---|---|---|
| Display type | Block-level (starts on a new line, takes full available width) | Inline (flows within a line of text, only as wide as its content) |
| Typical use | Grouping larger sections: headers, containers, cards, layout wrappers | Wrapping a small piece of text/inline content to style or script it individually |

```html
<div class="card">
<h3>Faculty Profile</h3>
<p>Justin Mathew is an <span class="highlight">Assistant Professor</span> in the Department of CSE.</p>
</div>
```
Best practice:
Prefer semantic elements (header, nav, main, article, section, footer see 5.3) over div where a meaningful equivalent exists; reserve div/span for cases with no semantic fit.

### 4.5 Tables
Tables present tabular data in rows and columns using `<table>`, `<tr>` (table row), `<th>` (header cell) and `<td>` (data cell).
```html
<table border="1">
<caption>Semester Result</caption>
<thead>
<tr>
<th>Course</th>
<th>Credits</th>
<th>Grade</th>
</tr>
</thead>
<tbody>
<tr>
<td>Web Programming</td>
```

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
```html
<td>4</td>
<td>A</td>
</tr>
<tr>
<td>Data Structures</td>
<td>4</td>
<td>A+</td>
</tr>
</tbody>
<tfoot>
<tr><td colspan="2">Total Credits</td><td>8</td></tr>
</tfoot>
</table>
```

| Tag/Attribute | Purpose |
|---|---|
| `<table>` | Defines the table. |
| `<caption>` | Title/description of the table, displayed above it. |
| `<thead>` / `<tbody>`/`<tfoot>` | Groups header, body and footer rows respectively (semantic + allows independent scrolling/styling). |
| `<tr>` | Table row. |
| `<th>` | Header cell bold and centred by default; scope="col" or scope="row" improves accessibility. |
| `<td>` | Standard data cell. |
| colspan / rowspan | Merge a cell across multiple columns / rows. |

Introduction to the Web & HTML5

### 4.6 Forms
The `<form>` element collects user input and submits it to a server for processing.
```html
<form action="/submit" method="POST">
<label for="name">Name:</label>
<input type="text" id="name" name="name" required>

<label for="email">Email:</label>
<input type="email" id="email" name="email" required>

<button type="submit">Submit</button>
</form>
```

| Attribute | Purpose |
|---|---|
| action | URL that will process the submitted data. |
| method | HTTP method used: GET (appends data to the URL, visible, for non-sensitive/small data) or POST (sends data in the request body, used for sensitive/large data). |
| autocomplete | Whether the browser may auto-fill fields (on/off) see also Section 5. |
| enctype | How data is encoded when submitting; must be multipart/form-data for file uploads. |

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5
The `<label>` element, linked via a matching for/id pair, associates descriptive text with a control - clicking the label focuses/activates the control, and it is essential for accessibility.

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5

## 5. HTML5 Form Input Types, datalist, autocomplete and Page Structure

### 5.1 HTML5 Form Input Types
HTML5 introduced many new values for the type attribute of `<input>`, giving browsers built-in validation and specialised Ul controls (date-pickers, colour swatches, sliders, on-screen numeric keypads on mobile) without needing JavaScript.

| type value | Purpose / Behaviour |
|---|---|
| text | Single-line free text (the default type). |
| email | Validates a well-formed email address; shows an email-optimised mobile keyboard. |
| password | Masks entered characters. |
| number | Numeric-only entry with up/down steppers; supports min, max, step. |
| range | A slider control between a min and max value. |
| date/month/week/time/ datetime-local | Native date/time pickers. |
| color | A colour-swatch picker returning a hex value. |
| tel | Telephone number (no built-in format validation, but triggers a numeric keypad). |
| url | Validates a well-formed URL. |
| search | A text field styled/optimised for search (may show a clear ('x') button). |
| checkbox | Toggle for one or more options from a set (multiple can be selected). |
| radio | Selects exactly one option from a named group (share the same name attribute). |
| file | Uploads one or more files from the user's device (accept attribute restricts file types). |
| hidden | Not rendered; used to submit data the user shouldn't see/edit. |
| submit/reset/button | Form action buttons. |

```html
<input type="email" name="email" required>
<input type="number" name="age" min="18" max="60" step="1">
<input type="range" name="volume" min="0" max="100" value="50">
<input type="date" name="dob">
<input type="color" name="favcolor" value="#2E5E4E">
<input type="checkbox" name="subject" value="html"> HTML
<input type="radio" name="gender" value="male"> Male
<input type="file" name="resume" accept=".pdf,.doc,.docx">
```

#### 5.1.1 Built-in Validation Attributes
required field must be filled before submission.

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5
min/max/step numeric or date bounds and increments.
minlength / maxlength character-count bounds for text.
pattern a regular expression the value must match, e.g. pattern="[0-9]{6}" for a 6-digit PIN code.
placeholder - greyed-out hint text shown when the field is empty (not a substitute for a `<label>`).

### 5.2 The datalist Element and autocomplete Attribute

#### 5.2.1 datalist
`<datalist>` provides a predefined set of suggestions for an `<input>`, linked using the input's list attribute matching the datalist's id. Unlike a `<select>` dropdown, the user can still type a free-text value not present in the list - it behaves as an editable combo box.
```html
<label for="browser">Choose a browser:</label>
<input type="text" id="browser" name="browser" list="browsers">
<datalist id="browsers">
<option value="Chrome">
<option value="Firefox">
<option value="Edge">
<option value="Safari">
</datalist>
```
Useful for search boxes, city/country pickers, or any field where you want to guide input while still allowing custom values.
Browser rendering of the suggestion list (as a dropdown) is native and cannot be styled with CSS the way a custom JS component could.

#### 5.2.2 The autocomplete Attribute
autocomplete controls whether the browser may offer to auto-fill a field based on values the user previously entered (name, address, card number, etc.). It can be set on the `<form>` element (applying to all its controls) or on an individual field to override the form-level setting.
```html
<form autocomplete="on">
<input type="text" name="name" autocomplete="name">
<input type="email" name="email" autocomplete="email">
<input type="text" name="otp" autocomplete="off">
</form>
```

| Value | Meaning |
|---|---|
| on | Browser may auto-fill this field (default for most fields). |
| off | Browser should not auto-fill this field (e.g. for one-time codes/OTP, CAPTCHA-adjacent fields). |
| name/email/tel/street-address / cc-number, etc. | Named autofill tokens that tell the browser exactly what category of stored data to suggest, improving autofill accuracy. |

### 5.3 Page Structure (Semantic) Elements

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes
Introduction to the Web & HTML5
HTML5 introduced semantic sectioning elements that describe the role of a region of the page, replacing generic `<div>`-only layouts of earlier HTML. This improves accessibility (screen readers can jump between regions), SEO, and code readability.

| Element | Represents |
|---|---|
| `<header>` | Introductory content for the page or a section typically logo, title, navigation. |
| `<nav>` | A block of primary navigation links. |
| `<main>` | The dominant, unique content of the document (used once per page). |
| `<section>` | A thematic grouping of content, typically with its own heading. |
| `<article>` | Self-contained content that could be distributed/reused independently (a blog post, a news story, a forum post). |
| `<aside>` | Content tangentially related to the main content (sidebars, pull-quotes, ads). |
| `<footer>` | Footer for its nearest sectioning ancestor or the page typically copyright, contact links. |
| `<figure>`/`<figcaption>` | Self-contained media (image, diagram, code) with an optional caption. |

```html
<body>
<header>
<h1>Saintgits CSE Department</h1>
<nav>
<a href="#about">About</a> <a href="#faculty">Faculty</a>
</nav>
</header>

<main>
<section id="about">
<h2>About the Department</h2>
<p>...</p>
</section>

<article>
<h2>ICSCST 2026 Conference Highlights</h2>
<p>...</p>
</article>

<aside>
<h3>Quick Links</h3>
</aside>
</main>

<footer>
<p>&copy; 2026 Saintgits College of Engineering</p>
</footer>
</body>
```

Key distinction:

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming Module 1 Lecture Notes
Introduction to the Web & HTML5
`<section>` groups related content under its own heading as part of the document outline; `<article>` is content that would still make complete sense if pulled out and syndicated on its own (an RSS post, a card in a news feed).

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes

## 6. Multimedia
Introduction to the Web & HTML5
HTML5 Audio and Video Elements

### 6.1 Why Native Multimedia Elements?
Before HTML5, playing audio/video in a browser required third-party plugins such as Flash or Silverlight, which had security, performance, and mobile-compatibility problems. HTML5 introduced `<audio>` and `<video>` as native elements so browsers can play media directly, with a consistent scripting API (via JavaScript) and no plugins.

### 6.2 The <audio> Element
```html
<audio controls autoplay loop muted preload="auto">
<source src="lecture.mp3" type="audio/mpeg">
<source src="lecture.ogg" type="audio/ogg">
Your browser does not support the audio element.
</audio>
```

| Attribute | Purpose |
|---|---|
| controls | Displays the browser's built-in play/pause/volume/seek UI. |
| autoplay | Starts playback automatically on load (many browsers block this unless muted, to prevent unwanted noise). |
| loop | Restarts playback automatically when it ends. |
| muted | Starts with audio muted. |
| preload | Hints how much to buffer ahead: none, metadata, or auto. |
| `<source>` | Provides one candidate file per format; the browser picks the first one it can play allows fallback across formats. |

### 6.3 The <video> Element
```html
<video width="640" height="360" controls poster="thumbnail.jpg">
<source src="demo.mp4" type="video/mp4">
<source src="demo.webm" type="video/webm">
<track kind="subtitles" src="subs-en.vtt" srclang="en" label="English">
Your browser does not support the video tag.
</video>
```

| Attribute | Purpose |
|---|---|
| width / height | Display dimensions in pixels. |
| controls | Shows the native playback control bar. |
| poster | Image shown before playback starts (e.g., a thumbnail). |
| autoplay/loop/muted/ preload | Same meaning as for `<audio>`. |
| playsinline | On mobile, plays inline rather than forcing fullscreen (iOS Safari especially). |

WEB PROGRAMMING
JUSTIN MATHEW
Web Programming - Module 1 Lecture Notes

| Attribute | Purpose |
|---|---|
| `<track>` | Adds timed text tracks - subtitles, captions, descriptions from a WebVTT (.vtt) file; kind can be subtitles, captions, descriptions, chapters. |

Introduction to the Web & HTML5

### 6.4 Supported Formats (Container/Codec Compatibility)

| Media | Common Formats | Typical Codec |
|---|---|---|
| Audio | MP3, OGG, WAV, AAC | MP3 (MPEG-1 Layer 3), Vorbis (OGG), PCM (WAV) |
| Video | MP4, WebM, OGG | H.264/AVC (MP4), VP8/VP9 (WebM), Theora (OGG) |

Because no single format is supported by every browser, providing multiple `<source>` elements (as shown above) lets the browser choose the first format it can play, ensuring cross-browser compatibility. The fallback text inside the tag ("Your browser does not support...") is shown only in very old browsers with no support at all.

### 6.5 Scripting Media with JavaScript
Both `<audio>` and `<video>` expose a common HTMLMediaElement API, so the same JavaScript methods/properties work for either, enabling custom player controls.
```javascript
const vid = document.querySelector("video");
vid.play(); // start playback
vid.pause(); // pause playback
vid.currentTime = 30; // seek to 30 seconds
vid.volume = 0.5; // set volume (0.0-1.0)
vid.playbackRate = 1.5; // 1.5x speed
vid.addEventListener("ended", () => {
console.log("Playback finished");
});
```

### 6.6 Accessibility Considerations
Always provide captions/subtitles via `<track>` for video content, benefiting deaf/hard-of-hearing users and anyone viewing without sound.
Avoid autoplay with unmuted sound disruptive and often blocked by browsers by default; if autoplay is used, pair it with muted.
Provide a text transcript alternative for audio-only content where practical.
Summary:
HTML5's `<audio>` and `<video>` elements removed the dependency on browser plugins by building playback natively into the markup, with the `<source>` element handling format fallback and the `<track>` element handling accessibility through captions/subtitles.

WEB PROGRAMMING
JUSTIN MATHEW
