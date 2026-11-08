"""practice.py — renders the interactive drill page.

Kept separate from build.py because it is an app, not a Markdown page: it ships
its own CSS/JS and embeds the drill data as JSON.
"""

import html
import json

PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Practice — {{SUBJECT}}</title>
<style>{{BASE_CSS}}
/* ---------- practice app ---------- */
body{padding-bottom:60px}
.wrap{max-width:1240px;margin:0 auto;padding:26px 26px 40px;display:grid;
  grid-template-columns:310px minmax(0,1fr);gap:26px;align-items:start}
@media (max-width:900px){.wrap{grid-template-columns:1fr}}
.head{grid-column:1/-1;display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;
  border-bottom:1px solid var(--line);padding-bottom:14px}
.head h1{font-size:1.5rem;margin:0}
.head .sub{color:var(--muted);font-size:13px}
.head .grow{flex:1}
.head a{font-size:13px;color:var(--muted);text-decoration:none}
.head a:hover{color:var(--accent)}

aside{position:sticky;top:20px;max-height:calc(100vh - 40px);overflow:auto;padding-right:4px}
.filters{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}
.filters button{font:600 11.5px/1 var(--sans);letter-spacing:.04em;text-transform:uppercase;
  border:1px solid var(--line);background:var(--panel);color:var(--muted);border-radius:999px;
  padding:6px 10px;cursor:pointer}
.filters button.on{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}
.score{font-size:12px;color:var(--muted);margin:0 0 10px}
.bar{height:4px;background:var(--line);border-radius:2px;overflow:hidden;margin:0 0 14px}
.bar span{display:block;height:100%;background:var(--accent);width:0}
.list{display:flex;flex-direction:column;gap:2px}
.item{display:flex;gap:8px;align-items:flex-start;padding:6px 8px;border-radius:8px;cursor:pointer;
  border:1px solid transparent;font-size:13.2px;line-height:1.35;color:var(--muted)}
.item:hover{background:var(--accent-soft)}
.item.sel{background:var(--accent-soft);border-color:var(--accent);color:var(--ink)}
.item .dot{width:8px;height:8px;border-radius:50%;border:1.5px solid var(--line);margin-top:5px;flex:0 0 8px}
.item.ok .dot{background:var(--accent);border-color:var(--accent)}
.item .t{flex:1}
.item .m{font-family:var(--mono);font-size:10.5px;color:var(--muted);opacity:.8}
.grouphead{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  margin:12px 0 4px;font-weight:700}

article{min-width:0}
.card2{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px}
.tagrow{display:flex;gap:8px;align-items:center;margin-bottom:10px;flex-wrap:wrap}
.tag{font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;font-weight:700;color:var(--accent);
  background:var(--accent-soft);border-radius:999px;padding:3px 9px}
.tag.g{color:var(--muted);background:none;border:1px solid var(--line)}
.card2 h2{font-size:1.08rem;margin:.1em 0 .7em;line-height:1.35}
.hint{font-size:12.5px;color:var(--muted);margin:-4px 0 12px}

pre.scaf{background:var(--code-bg);border:1px solid var(--line);border-radius:10px;padding:16px 16px;
  overflow-x:auto;font-family:var(--mono);font-size:13.2px;line-height:2.1;white-space:pre-wrap}
pre.scaf input{font-family:var(--mono);font-size:13px;border:1px solid var(--line);border-bottom:2px solid var(--accent);
  border-radius:5px;background:var(--bg);color:var(--ink);padding:2px 6px;min-width:60px}
pre.scaf input.ok{border-bottom-color:#2e7d32;background:#e8f5e9;color:#1b5e20}
pre.scaf input.bad{border-bottom-color:#c62828;background:#fdecea;color:#b71c1c}
html[data-theme="dark"] pre.scaf input.ok{background:#12301a;color:#a5d6a7}
html[data-theme="dark"] pre.scaf input.bad{background:#3a1717;color:#ef9a9a}

textarea.ans{width:100%;min-height:150px;background:var(--code-bg);border:1px solid var(--line);
  border-radius:10px;color:var(--ink);font-family:var(--mono);font-size:13px;line-height:1.6;padding:12px 14px}
textarea.ans:focus{outline:2px solid var(--accent);outline-offset:0}
pre.code{background:var(--code-bg);border:1px solid var(--line);border-radius:10px;padding:14px 16px;
  overflow-x:auto;font-family:var(--mono);font-size:13px;line-height:1.55;white-space:pre}

.row{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px;align-items:center}
button.act{font:600 13px/1 var(--sans);border-radius:9px;padding:9px 14px;cursor:pointer;
  border:1px solid var(--line);background:var(--panel);color:var(--ink)}
button.act:hover{border-color:var(--accent);color:var(--accent)}
button.act.primary{background:var(--accent);border-color:var(--accent);color:#fff}
button.act.primary:hover{filter:brightness(1.06);color:#fff}
button.act:disabled{opacity:.5;cursor:default}
.verdict{font-size:13.5px;font-weight:650;margin-top:12px}
.verdict.ok{color:#2e7d32}
.verdict.bad{color:#c62828}
html[data-theme="dark"] .verdict.ok{color:#81c784}
html[data-theme="dark"] .verdict.bad{color:#ef9a9a}
.reveal{margin-top:14px;border-top:1px solid var(--line);padding-top:14px}
.reveal h3{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
.reveal ul{margin:.4em 0;padding-left:1.2em}
.opts{display:flex;flex-direction:column;gap:8px;margin-top:6px}
.opt{text-align:left;font:inherit;font-size:13.6px;border:1px solid var(--line);background:var(--panel);
  color:var(--ink);border-radius:10px;padding:11px 13px;cursor:pointer}
.opt:hover{border-color:var(--accent)}
.opt.ok{border-color:#2e7d32;background:#e8f5e9;color:#1b5e20}
.opt.bad{border-color:#c62828;background:#fdecea;color:#b71c1c}
html[data-theme="dark"] .opt.ok{background:#12301a;color:#a5d6a7}
html[data-theme="dark"] .opt.bad{background:#3a1717;color:#ef9a9a}
#tutor{margin-top:16px;border-top:1px solid var(--line);padding-top:14px;display:none}
#tutor.on{display:block}
#tutor .t{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
#tutor .body{font-size:13.4px;line-height:1.6}
#tutor .body p{margin:.35em 0}
#tutor .body ul{margin:.35em 0;padding-left:1.2em}
#tutor .body pre{background:var(--code-bg);padding:10px 12px;border-radius:8px;font-size:12.2px;overflow-x:auto}
#tutor .body .cursor:after{content:"▍";color:var(--accent);animation:blink 1s steps(2) infinite}
@keyframes blink{50%{opacity:0}}
.emptynote{color:var(--muted);font-size:14px}
</style>
</head>
<body>
<div class="wrap">
  <div class="head">
    <h1>Practice</h1>
    <span class="sub">{{SUBJECT}} · syntax drills, checked in the browser</span>
    <span class="grow"></span>
    <a href="index.html">← {{SUBJECT}}</a>
  </div>

  <aside>
    <div class="filters" id="mfilters"></div>
    <div class="filters" id="tfilters"></div>
    <p class="score" id="score">0 of 0 done</p>
    <div class="bar"><span id="barfill"></span></div>
    <div class="list" id="list"></div>
  </aside>

  <article id="stage"><div class="card2"><p class="emptynote">Pick a drill on the left. Fill mode gives you the scaffolding and you type only the missing syntax; output mode asks what the code prints; write mode is a full answer you can hand to the tutor for grading.</p></div></article>
</div>

<div class="tools"><button id="theme" title="Toggle light / dark">☾</button></div>
<script>{{BASE_JS}}</script>
<script>
const DRILLS = {{DRILLS}};
const STORE = "mn-drills-v1";
let state = {};
try { state = JSON.parse(localStorage.getItem(STORE) || "{}"); } catch (e) { state = {}; }
const save = () => localStorage.setItem(STORE, JSON.stringify(state));

let modFilter = 0, typeFilter = "";
const root = document.getElementById("stage");
const listEl = document.getElementById("list");

const TYPES = { fill: "fill the blanks", output: "predict the output", write: "write it", mcq: "multiple choice" };
const esc = (s) => String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
const norm = (s) => String(s).replace(/\\r/g, "").trim().replace(/[ \\t]+/g, " ").toLowerCase();
const normCode = (s) => String(s).replace(/\\r/g, "").split("\\n").map((l) => l.trim()).filter(Boolean).join("\\n").toLowerCase();

/* ---------------- filters + list ---------------- */
function buildFilters() {
  const mf = document.getElementById("mfilters");
  mf.innerHTML = ["All", "M1", "M2", "M3", "M4", "M5"].map((label, i) =>
    `<button data-m="${i}" class="${modFilter === i ? "on" : ""}">${label}</button>`).join("");
  mf.onclick = (e) => {
    const b = e.target.closest("button"); if (!b) return;
    modFilter = Number(b.dataset.m); buildFilters(); renderList();
  };
  const tf = document.getElementById("tfilters");
  tf.innerHTML = ["All types", "fill", "output", "write", "mcq"].map((label, i) =>
    `<button data-t="${i === 0 ? "" : label}" class="${typeFilter === (i === 0 ? "" : label) ? "on" : ""}">${label}</button>`).join("");
  tf.onclick = (e) => {
    const b = e.target.closest("button"); if (!b) return;
    typeFilter = b.dataset.t; buildFilters(); renderList();
  };
}

function visible() {
  return DRILLS.filter((d) => (modFilter === 0 || d.m === modFilter) && (!typeFilter || d.type === typeFilter));
}

function renderList() {
  const items = visible();
  let html = "", lastM = null;
  for (const d of items) {
    if (d.m !== lastM) { html += `<div class="grouphead">Module ${d.m}</div>`; lastM = d.m; }
    const done = state[d.id] === "done";
    html += `<div class="item ${done ? "ok" : ""}" data-id="${d.id}">
      <span class="dot"></span><span class="t">${esc(d.topic)} — ${esc(d.q).slice(0, 52)}…</span>
      <span class="m">${d.type}</span></div>`;
  }
  listEl.innerHTML = html || '<p class="emptynote">Nothing matches that filter.</p>';
  listEl.querySelectorAll(".item").forEach((el) => {
    el.onclick = () => openDrill(el.dataset.id);
  });
  const doneCount = DRILLS.filter((d) => state[d.id] === "done").length;
  document.getElementById("score").textContent = `${doneCount} of ${DRILLS.length} done`;
  document.getElementById("barfill").style.width = `${(doneCount / DRILLS.length) * 100}%`;
  if (current) {
    const sel = listEl.querySelector(`[data-id="${current.id}"]`);
    if (sel) sel.classList.add("sel");
  }
}

/* ---------------- drill rendering ---------------- */
let current = null;

function openDrill(id) {
  current = DRILLS.find((d) => d.id === id);
  renderList();
  render();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function fillMarkup(d) {
  // {{1}} … → inline inputs sized to the answer
  return d.scaffold.split(/(\\{\\{\\d+\\}\\})/).map((part) => {
    const m = part.match(/\\{\\{(\\d+)\\}\\}/);
    if (!m) return esc(part);
    const i = Number(m[1]) - 1;
    const w = Math.max(6, Math.min(34, (d.answers[i] || "").length + 3));
    return `<input class="blank" data-i="${i}" size="${w}" spellcheck="false" autocomplete="off">`;
  }).join("");
}

function render() {
  const d = current;
  if (!d) return;
  const head = `<div class="tagrow">
      <span class="tag">${d.type === "fill" ? "fill" : d.type}</span>
      <span class="tag g">Module ${d.m}</span>
      <span class="tag g">${esc(d.topic)}</span>
      <span class="tag g">${esc(d.id)}</span>
    </div><h2>${esc(d.q)}</h2>`;

  let body = "";
  if (d.type === "fill") {
    body = `${d.hint ? `<p class="hint">${esc(d.hint)}</p>` : ""}
      <pre class="scaf">${fillMarkup(d)}</pre>
      <div class="row">
        <button class="act primary" id="check">Check</button>
        <button class="act" id="show">Show answer</button>
        <button class="act" id="tutorbtn">Ask the tutor</button>
        <span style="flex:1"></span>
        <button class="act" id="markdone">Mark done</button>
      </div>
      <div id="verdict" class="verdict"></div>
      <div id="reveal"></div>`;
  } else if (d.type === "output") {
    body = `<pre class="code">${esc(d.code)}</pre>
      <textarea class="ans" id="ans" placeholder="What does it print? (one answer per line)"></textarea>
      <div class="row">
        <button class="act primary" id="check">Check</button>
        <button class="act" id="show">Show answer</button>
        <button class="act" id="tutorbtn">Ask the tutor</button>
        <span style="flex:1"></span>
        <button class="act" id="markdone">Mark done</button>
      </div>
      <div id="verdict" class="verdict"></div>
      <div id="reveal"></div>`;
  } else if (d.type === "write") {
    body = `<textarea class="ans" id="ans" style="min-height:230px" placeholder="Write your answer…"></textarea>
      <div class="row">
        <button class="act primary" id="tutorbtn">Grade with tutor</button>
        <button class="act" id="show">Show model answer</button>
        <span style="flex:1"></span>
        <button class="act" id="markdone">Mark done</button>
      </div>
      <div id="verdict" class="verdict"></div>
      <div id="reveal"></div>`;
  } else {
    body = `<div class="opts" id="opts">${d.options.map((o, i) =>
      `<button class="opt" data-i="${i}">${esc(o)}</button>`).join("")}</div>
      <div id="verdict" class="verdict"></div>
      <div class="row"><span style="flex:1"></span><button class="act" id="markdone">Mark done</button></div>
      <div id="reveal"></div>`;
  }

  root.innerHTML = `<div class="card2">${head}${body}
    <div id="tutor" class="tutor">
      <div class="t">Tutor</div>
      <div class="body" id="tutorbody"></div>
    </div></div>`;

  wire(d);
}

function verdict(kind, text) {
  const v = document.getElementById("verdict");
  v.className = "verdict " + (kind === true ? "ok" : kind === false ? "bad" : "");
  v.textContent = text;
}

function reveal(d) {
  const box = document.getElementById("reveal");
  let html = `<h3>Model answer</h3>`;
  if (d.type === "fill") {
    html += `<pre class="code">${esc(d.scaffold.replace(/\\{\\{(\\d+)\\}\\}/g, (_, n) => d.answers[Number(n) - 1]))}</pre>`;
    html += `<h3 style="margin-top:12px">Blanks</h3><ul>${d.answers.map((a, i) =>
      `<li><code>${esc(a)}</code></li>`).join("")}</ul>`;
  } else if (d.type === "output") {
    html += `<pre class="code">${esc(d.out)}</pre>`;
  } else if (d.type === "write") {
    html += `<pre class="code">${esc(d.model)}</pre>`;
    if (d.points) html += `<h3 style="margin-top:12px">Marks are for</h3><ul>${d.points.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>`;
  } else {
    html += `<p>${esc(d.why || "")}</p>`;
  }
  box.innerHTML = `<div class="reveal">${html}</div>`;
}

function wire(d) {
  const show = document.getElementById("show");
  if (show) show.onclick = () => reveal(d);

  const done = document.getElementById("markdone");
  if (done) done.onclick = () => {
    state[d.id] = state[d.id] === "done" ? undefined : "done";
    if (state[d.id] === undefined) delete state[d.id];
    save(); renderList();
    verdict(true, state[d.id] === "done" ? "Marked done." : "Marked not done.");
  };

  if (d.type === "fill") {
    const inputs = [...document.querySelectorAll("pre.scaf input")];
    // a blank may appear more than once in the scaffold (same {{n}}): check it once
    const ids = [...new Set(inputs.map((x) => x.dataset.i))];
    const group = (i) => inputs.filter((x) => x.dataset.i === i);
    document.getElementById("check").onclick = () => {
      let ok = 0;
      ids.forEach((i) => {
        const want = norm(d.answers[i]);
        const got = norm(group(i)[0].value);
        const alt = (d.alts && d.alts[i] ? d.alts[i] : []).map(norm);
        const good = got === want || alt.includes(got);
        group(i).forEach((inp) => { inp.classList.toggle("ok", good); inp.classList.toggle("bad", !good); });
        if (good) ok++;
      });
      const all = ok === ids.length;
      verdict(all, all ? `All ${ids.length} blanks correct.` : `${ok} of ${ids.length} correct — red blanks are wrong or empty.`);
      if (all) { state[d.id] = "done"; save(); renderList(); }
    };
    inputs.forEach((inp, i) => {
      inp.addEventListener("keydown", (e) => { if (e.key === "Enter") inputs[i + 1] ? inputs[i + 1].focus() : document.getElementById("check").click(); });
    });
    inputs[0] && inputs[0].focus();
  }

  if (d.type === "output") {
    document.getElementById("check").onclick = () => {
      const got = normCode(document.getElementById("ans").value);
      const want = normCode(d.out);
      if (!got) return verdict(null, "Write what it prints first.");
      if (got === want) { verdict(true, "Correct."); state[d.id] = "done"; save(); renderList(); }
      else verdict(false, "Not quite — compare with the model answer below.");
    };
  }

  if (d.type === "mcq") {
    document.querySelectorAll(".opt").forEach((b) => {
      b.onclick = () => {
        const i = Number(b.dataset.i);
        document.querySelectorAll(".opt").forEach((x) => (x.disabled = true));
        document.querySelector(`.opt[data-i="${d.correct}"]`).classList.add("ok");
        if (i === d.correct) {
          verdict(true, "Correct.");
          state[d.id] = "done"; save(); renderList();
        } else {
          b.classList.add("bad");
          verdict(false, "Not that one.");
        }
        reveal(d);
      };
    });
  }

  const t = document.getElementById("tutorbtn");
  if (t) t.onclick = () => gradeWithTutor(d, t);
}

/* ---------------- tutor grading ---------------- */
async function gradeWithTutor(d, btn) {
  const box = document.getElementById("tutor");
  const body = document.getElementById("tutorbody");
  box.classList.add("on");
  const mine = d.type === "fill"
    ? [...document.querySelectorAll("pre.scaf input")].map((x, i) => `blank ${i + 1}: ${x.value || "(empty)"}`).join("\\n")
    : (document.getElementById("ans") ? document.getElementById("ans").value : "");
  if (!mine.trim()) { body.textContent = "Write something first, then ask the tutor."; return; }

  const model = d.type === "fill" ? d.scaffold.replace(/\\{\\{(\\d+)\\}\\}/g, (_, n) => d.answers[Number(n) - 1])
              : d.type === "output" ? d.out
              : d.type === "write" ? d.model
              : d.options[d.correct];

  const q = `Grade my answer to this exam drill. Question: ${d.q}\\n\\nMy answer:\\n${mine}\\n\\nModel answer:\\n${model}\\n\\nSay: correct / partly / wrong, then the exact syntax or logic mistakes and the fix. Max 90 words.`;
  body.innerHTML = '<span class="cursor"></span>';
  btn.disabled = true;
  let acc = "";
  try {
    const res = await fetch("/api/chat", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ q, page: "Practice — " + d.topic, section: "Module " + d.m + " drill " + d.id, outline: "" }),
    });
    if (!res.ok) throw new Error((await res.json().catch(() => ({}))).error || "HTTP " + res.status);
    const reader = res.body.getReader(), dec = new TextDecoder();
    let buf = "";
    for (;;) {
      const r = await reader.read(); if (r.done) break;
      buf += dec.decode(r.value, { stream: true });
      const lines = buf.split("\\n"); buf = lines.pop() || "";
      for (const line of lines) {
        const l = line.trim(); if (!l.startsWith("data:")) continue;
        const data = l.slice(5).trim(); if (data === "[DONE]") continue;
        try { const o = JSON.parse(data); if (o.d) { acc += o.d; body.innerHTML = md(acc) + '<span class="cursor"></span>'; } } catch (e) {}
      }
    }
    body.innerHTML = md(acc || "_no answer_");
  } catch (e) {
    body.textContent = "Tutor unavailable — it only works on the deployed site.";
  } finally { btn.disabled = false; }
}

function md(src) {
  const parts = src.split(/```/); let out = "";
  for (let i = 0; i < parts.length; i++) {
    if (i % 2) { out += "<pre><code>" + esc(parts[i].replace(/^\\w*\\n/, "")) + "</code></pre>"; continue; }
    let t = esc(parts[i]).replace(/`([^`\\n]+)`/g, "<code>$1</code>").replace(/\\*\\*([^*]+)\\*\\*/g, "<b>$1</b>");
    const lines = t.split("\\n"); let html = "", ul = false;
    for (const line of lines) {
      if (/^\\s*[-*]\\s+/.test(line)) { if (!ul) { html += "<ul>"; ul = true; } html += "<li>" + line.replace(/^\\s*[-*]\\s+/, "") + "</li>"; }
      else { if (ul) { html += "</ul>"; ul = false; } if (line.trim()) html += "<p>" + line + "</p>"; }
    }
    if (ul) html += "</ul>";
    out += html;
  }
  return out;
}

buildFilters(); renderList();
</script>
</body>
</html>
"""


def build(drills, subject_title, base_css, base_js):
    rows = json.dumps(drills, ensure_ascii=False, indent=1)
    # "</" inside the embedded JSON would close the surrounding <script> tag.
    rows = rows.replace("</", "<\\/")
    return (PAGE
            .replace("{{SUBJECT}}", html.escape(subject_title))
            .replace("{{BASE_CSS}}", base_css)
            .replace("{{BASE_JS}}", base_js)
            .replace("{{DRILLS}}", rows))
