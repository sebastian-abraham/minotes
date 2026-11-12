#!/usr/bin/env python3
"""build.py — render every subject's Markdown notes into a static site.

Layout produced:

    index.html                     hub: one card per subject
    <subject>/index.html           library page: every document, grouped
    <subject>/<slug>.html          one page per note

No build step is needed on the host: the output is plain static HTML with
inline CSS/JS, so Vercel (or GitHub Pages) can serve the repo as-is.

Add a subject: append a dict to SUBJECTS. Add a document: add a row to that
subject's `docs` list, then run `tools/build.py`.
"""

import os
import re
import sys
import html as html_mod

import markdown
from markdown.extensions.toc import slugify_unicode

import drills as drill_data
import ehs_drills as ehs_drill_data
import ise_drills as ise_drill_data
import practice as practice_page

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                 # repo root = site root
SOURCES = os.path.join(ROOT, "sources")

# ---------------------------------------------------------------------------
# Site content.  docs rows: (md file in sources/<slug>/, sidebar label, sub,
#                            card blurb, card title, group, output slug)
# ---------------------------------------------------------------------------
SUBJECTS = [
    {
        "slug": "web-programming",
        "title": "Web Programming",
        "code": "20CST461",
        "tagline": "Semester 7 · ESE",
        "blurb": "Five module kits covering all 286 faculty-bank questions, plus the "
                 "lecture notes, coverage tracker and drill logs they were built from.",
        "docs": [
            ("START_HERE.md", "Start here", "Plan + how to use the kits",
             "Plan, attack order, cross-module links", "Start here — the plan", "start", "start-here"),
            ("KIT_M1_WWW_HTML.md", "M1 · WWW & HTML5", "Q1–36 · Q161–185",
             "61 bank questions", "Module 1 · WWW & HTML5", "kits", "m1-html"),
            ("KIT_M2_CSS_JS.md", "M2 · CSS & JavaScript", "Q37–67 · Q186–202 · Q222–228",
             "55 bank questions", "Module 2 · CSS & JavaScript", "kits", "m2-css-js"),
            ("KIT_M3_PHP.md", "M3 · PHP", "Q68–91 · Q203–221",
             "43 bank questions", "Module 3 · PHP", "kits", "m3-php"),
            ("KIT_M4_PHP_MYSQL.md", "M4 · PHP + MySQL", "Q92–129 · Q229–253",
             "63 bank questions", "Module 4 · PHP + MySQL", "kits", "m4-php-mysql"),
            ("KIT_M5_JSON_LARAVEL.md", "M5 · JSON & Laravel", "Q130–160 · Q254–286",
             "64 bank questions", "Module 5 · JSON & Laravel", "kits", "m5-json-laravel"),
            ("question_bank.md", "Question bank", "286 questions · 14 pages",
             "All 286 questions", "Faculty question bank", "source", "question-bank"),
            ("WEB PROGRAMING MOD-1.md", "Notes · M1", "Lecture notes, 762 lines",
             "WWW / HTML5 deck", "Module 1 lecture notes", "source", "notes-m1"),
            ("module2_fixed.md", "Notes · M2", "Lecture notes, 985 lines",
             "CSS / JavaScript deck", "Module 2 lecture notes", "source", "notes-m2"),
            ("module3.md", "Notes · M3", "Lecture notes, 774 lines",
             "PHP deck", "Module 3 lecture notes", "source", "notes-m3"),
            ("module4.md", "Notes · M4", "Lecture notes, 859 lines",
             "PHP + MySQL deck", "Module 4 lecture notes", "source", "notes-m4"),
            ("module5.md", "Notes · M5", "Lecture notes, 760 lines",
             "JSON / Laravel deck", "Module 5 lecture notes", "source", "notes-m5"),
            ("wp_study_tracker.md", "Tracker", "Progress + prediction map",
             "Coverage tracker", "Study tracker", "progress", "tracker"),
            ("wp_revision.md", "Revision log", "Append-only session notes",
             "Session deep dives", "Revision log", "progress", "revision-log"),
            ("wp_code_drills.md", "Drill key", "Model answers to drills",
             "Drill answers", "Code drill answer key", "progress", "drill-key"),
        ],
    },
    {
        "slug": "ehs",
        "title": "Environmental Health & Safety",
        "code": "20CET453",
        "tagline": "Semester 7 · Civil · ESE",
        "blurb": "Five module kits built from the syllabus, because no ESE paper or question bank exists for this course. "
                 "The three internal papers are here as style evidence — they never once asked Module 5.",
        "drills": "ehs",
        "docs": [
            ("START_HERE.md", "Start here", "Scope, answer shapes, how to work",
             "Syllabus-first plan and the Module 5 warning", "Start here — the plan", "start", "start-here"),
            ("KIT_M1_TOXICOLOGY.md", "M1 · Health & toxicology", "20% ESE · CO1",
             "Occupational diseases, toxicology, industrial hygiene", "Module 1 · Occupational health & toxicology", "kits", "m1-toxicology"),
            ("KIT_M2_CHEMICAL_BIOLOGICAL_NOISE.md", "M2 · Chemical, bio, noise", "20% ESE · CO2",
             "Dust to gases, bio-agents, noise", "Module 2 · Chemical & biological hazards, noise", "kits", "m2-chemical-bio-noise"),
            ("KIT_M3_CONSTRUCTION_ELECTRICAL_RADIATION.md", "M3 · Construction hazards", "20% ESE · CO3",
             "Scaffolding, welding, excavation, shock, radiation", "Module 3 · Construction, electrical & radiation", "kits", "m3-construction"),
            ("KIT_M4_AIR_WATER_POLLUTION_WASTE.md", "M4 · Pollution & waste", "20% ESE · CO4",
             "Air, water, ozone, clean coal, waste", "Module 4 · Air & water pollution, waste", "kits", "m4-pollution-waste"),
            ("KIT_M5_SAFE_WORKING_ENVIRONMENT.md", "M5 · Safe environment", "20% ESE · CO5",
             "Inspection, first aid, welfare, PPE — never examined internally", "Module 5 · Safe working environment", "kits", "m5-safe-environment"),
            ("syllabus.md", "Syllabus", "All five modules, verbatim",
             "The only reliable scope", "Syllabus (verbatim)", "source", "syllabus"),
            ("internal_questions.md", "Internal papers", "3 papers · 2 formats",
             "What was actually asked, and what never was", "Internal question papers", "source", "internal-papers"),
            ("friend_notes_site.md", "Notes · friend's", "Long-form study notes",
             "The HTML notes this subject started from", "Friend's notes (HTML → markdown)", "source", "notes-friend"),
        ],
    },
    {
        "slug": "ise",
        "title": "Industrial Safety Engineering",
        "code": "20MCN401",
        "tagline": "Semester 7 · CSE · 0-credit, still 100 marks",
        "blurb": "Five module kits answering all 172 questions of the department bank, written as plain-English explainers "
                 "with a mark anchor and an exam trap in every section.",
        "drills": "ise",
        "docs": [
            ("START_HERE.md", "Start here", "Scope, answer shapes, order of attack",
             "How to use the kits and where the marks are", "Start here — the plan", "start", "start-here"),
            ("KIT_M1_INTRO.md", "M1 · Intro & accident theory", "20% ESE · 32 questions",
             "Theories, safety organisation, roles", "Module 1 · Introduction to industrial safety", "kits", "m1-intro"),
            ("KIT_M2_PPE.md", "M2 · PPE & monitoring", "20% ESE · 32 questions",
             "PPE, the four rates, housekeeping, permits", "Module 2 · Personal protection in the work environment", "kits", "m2-ppe"),
            ("KIT_M3_CONSTRUCTION.md", "M3 · Construction safety", "20% ESE · 31 questions",
             "Excavation, shoring, scaffolds, blasting, NBC", "Module 3 · Construction industry and safety", "kits", "m3-construction"),
            ("KIT_M4_MACHINERY.md", "M4 · Machinery & handling", "20% ESE · 30 questions",
             "Guarding, presses, machine tools, slings", "Module 4 · Machinery safeguard and material handling", "kits", "m4-machinery"),
            ("KIT_M5_HAZARD_ID.md", "M5 · Hazard identification", "20% ESE · 47 questions",
             "Fire, Dow index, PHA, HAZOP, MSDS", "Module 5 · Hazard identification and control", "kits", "m5-hazard-id"),
            ("syllabus.md", "Syllabus", "Five modules, verbatim", "The scope, module by module", "Syllabus (verbatim)", "source", "syllabus"),
            ("question_map.md", "Question bank", "172 questions, mapped", "Every bank question and which kit answers it", "Question bank (172, mapped)", "source", "question-bank"),
        ],
    },
]

GROUPS = [
    ("start", "Start"),
    ("practice", "Practice — type it until it sticks"),
    ("kits", "Module kits — every bank question answered"),
    ("source", "Source material — the notes and the bank"),
    ("progress", "Progress &amp; drills"),
]

CSS = """
:root{
  --bg:#fbfaf8; --panel:#ffffff; --ink:#232120; --muted:#5f5a53; --line:#e6e1da;
  --accent:#7a4fd0; --accent-soft:#f1ecfb; --code-bg:#f5f2ee; --code-ink:#2b2a28;
  --warn-bg:#fff8e6; --warn-line:#f0d9a0;
  --sans:"Inter","Segoe UI",system-ui,-apple-system,"Noto Sans",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,"Fira Code",monospace;
}
html[data-theme="dark"]{
  --bg:#141317; --panel:#1b1a20; --ink:#e8e4de; --muted:#a8a199; --line:#2f2c36;
  --accent:#b79cf5; --accent-soft:#241f33; --code-bg:#22202a; --code-ink:#e8e4de;
  --warn-bg:#2a2417; --warn-line:#4a3d22;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink); font-family:var(--sans);
  font-size:16.5px; line-height:1.72; -webkit-font-smoothing:antialiased;
}
#progress{position:fixed;top:0;left:0;height:3px;width:0;background:var(--accent);z-index:50;transition:width .1s linear}

.wrap{display:flex;align-items:flex-start;min-height:100vh}
.sidebar{
  position:sticky;top:0;height:100vh;width:300px;flex:0 0 300px;overflow-y:auto;
  padding:26px 20px 60px;border-right:1px solid var(--line);background:var(--panel);
}
.sidebar h1{font-size:15px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);
  margin:0 0 4px;font-weight:600}
.sidebar .sub{font-size:12.5px;color:var(--muted);margin:0 0 18px}
.sidebar nav{font-size:14px}
.sidebar .toc>ul{padding-left:0}
.sidebar ul{list-style:none;margin:0;padding-left:12px}
.sidebar ul ul{border-left:1px solid var(--line);margin-left:4px;padding-left:10px}
.sidebar li{margin:3px 0}
.sidebar a{color:var(--ink);text-decoration:none;display:block;padding:3px 8px;border-radius:8px;
  line-height:1.35;transition:background .12s,color .12s}
.sidebar a:hover{background:var(--accent-soft);color:var(--accent)}
.sidebar a.active{background:var(--accent-soft);color:var(--accent);font-weight:600}
.sidebar .home{display:inline-flex;align-items:center;gap:6px;margin-bottom:16px;font-size:13.5px;
  color:var(--muted);text-decoration:none;border:1px solid var(--line);padding:5px 10px;border-radius:999px}
.sidebar .home:hover{color:var(--accent);border-color:var(--accent)}

main{flex:1;min-width:0;padding:46px 56px 120px;max-width:980px;margin:0 auto}
.doc-head{border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:34px}
.doc-head .kicker{font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);
  font-weight:700;margin-bottom:8px}
.doc-head .meta{font-size:13.5px;color:var(--muted)}

h1,h2,h3,h4{line-height:1.25;font-weight:700;letter-spacing:-.01em}
h1{font-size:2.05rem;margin:.2em 0 .5em}
h2{font-size:1.55rem;margin:2.4em 0 .7em;padding-bottom:.35em;border-bottom:1px solid var(--line)}
h3{font-size:1.2rem;margin:1.9em 0 .55em}
h4{font-size:1.03rem;margin:1.5em 0 .45em;color:var(--muted)}
h2 .anchor,h3 .anchor{opacity:0;margin-left:.35em;font-size:.8em;color:var(--muted);text-decoration:none}
h2:hover .anchor,h3:hover .anchor{opacity:1}
p{margin:.75em 0}
a{color:var(--accent);text-underline-offset:2px}
strong{font-weight:650}
hr{border:0;border-top:1px solid var(--line);margin:2.6em 0}
ul,ol{margin:.7em 0;padding-left:1.4em}
li{margin:.3em 0}
li>ul,li>ol{margin:.25em 0}
blockquote{
  margin:1.3em 0;padding:12px 18px;background:var(--warn-bg);border-left:3px solid var(--warn-line);
  border-radius:0 10px 10px 0;color:var(--ink)
}
blockquote p{margin:.3em 0}

code{font-family:var(--mono);font-size:.87em;background:var(--code-bg);color:var(--code-ink);
  padding:.15em .38em;border-radius:6px;border:1px solid var(--line);
  box-decoration-break:clone;-webkit-box-decoration-break:clone;overflow-wrap:anywhere}
pre{position:relative;background:var(--code-bg);border:1px solid var(--line);border-radius:12px;
  padding:16px 18px;overflow-x:auto;margin:1.1em 0}
pre code{background:none;border:0;padding:0;font-size:13.6px;line-height:1.62;white-space:pre}
.copy{position:absolute;top:8px;right:8px;font:600 11px/1 var(--sans);color:var(--muted);
  background:var(--panel);border:1px solid var(--line);border-radius:7px;padding:5px 8px;cursor:pointer;
  opacity:0;transition:opacity .15s}
pre:hover .copy{opacity:1}
.copy:hover{color:var(--accent);border-color:var(--accent)}

.table-scroll{overflow-x:auto;margin:1.3em 0;border:1px solid var(--line);border-radius:12px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:14.6px}
th,td{padding:9px 13px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th{background:var(--accent-soft);font-weight:650;font-size:13px;letter-spacing:.02em;
  position:sticky;top:0;backdrop-filter:blur(4px)}
tr:last-child td{border-bottom:0}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--panel) 60%,var(--bg))}
tbody tr:hover{background:var(--accent-soft)}

.tools{position:fixed;right:22px;bottom:22px;display:flex;flex-direction:column;gap:8px;z-index:40}
.tools button{width:42px;height:42px;border-radius:12px;border:1px solid var(--line);background:var(--panel);
  color:var(--ink);cursor:pointer;font-size:16px;box-shadow:0 4px 14px rgba(0,0,0,.10)}
.tools button:hover{color:var(--accent);border-color:var(--accent)}
@media (max-width:1000px){
  .wrap{display:block}
  .sidebar{position:static;width:auto;height:auto;border-right:0;border-bottom:1px solid var(--line)}
  .sidebar nav{max-height:40vh;overflow:auto}
  main{padding:28px 20px 100px}
}
@media print{
  .sidebar,.tools,#progress,.copy{display:none!important}
  body{background:#fff;color:#000;font-size:11pt}
  main{padding:0;max-width:none}
  h2{break-after:avoid} pre,table,blockquote{break-inside:avoid}
  a{color:#000;text-decoration:none}
}
"""

CHAT_CSS = """
/* ---- ask-about-this ---- */
#chat-btn{position:fixed;right:20px;bottom:112px;width:44px;height:44px;border-radius:50%;
  border:1px solid var(--line);background:var(--panel);color:var(--accent);cursor:pointer;font-size:17px;
  box-shadow:0 6px 18px rgba(0,0,0,.12);z-index:45;display:grid;place-items:center}
#chat-btn:hover{border-color:var(--accent)}
#sel-chip{position:absolute;z-index:46;transform:translate(-50%,-100%);background:var(--ink);color:var(--bg);
  font:600 12px/1 var(--sans);padding:7px 11px;border-radius:999px;cursor:pointer;white-space:nowrap;
  box-shadow:0 6px 18px rgba(0,0,0,.25);display:none}
#sel-chip:hover{background:var(--accent);color:#fff}
#chat-panel{position:fixed;right:20px;bottom:164px;width:min(420px,calc(100vw - 40px));max-height:min(70vh,620px);
  background:var(--panel);border:1px solid var(--line);border-radius:14px;z-index:47;display:none;
  flex-direction:column;box-shadow:0 18px 50px rgba(0,0,0,.18);overflow:hidden}
#chat-panel.open{display:flex}
#chat-head{display:flex;align-items:center;gap:8px;padding:11px 13px;border-bottom:1px solid var(--line);
  font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700}
#chat-head .sp{flex:1}
#chat-head button{background:none;border:0;color:var(--muted);cursor:pointer;font-size:15px;padding:2px 4px}
#chat-head button:hover{color:var(--accent)}
#chat-quote{display:none;margin:10px 13px 0;padding:8px 10px;border-left:2px solid var(--accent);
  background:var(--accent-soft);color:var(--muted);font-size:12.5px;border-radius:0 8px 8px 0;
  max-height:84px;overflow:auto;white-space:pre-wrap}
#chat-log{flex:1;overflow-y:auto;padding:12px 13px;display:flex;flex-direction:column;gap:10px;font-size:13.6px;line-height:1.55}
.msg{max-width:100%}
.msg.user{align-self:flex-end;background:var(--accent-soft);color:var(--ink);padding:7px 11px;border-radius:11px 11px 2px 11px;
  max-width:86%;white-space:pre-wrap}
.msg.bot{color:var(--ink)}
.msg.bot p{margin:.3em 0}
.msg.bot ul{margin:.3em 0;padding-left:1.15em}
.msg.bot code{font-size:.9em}
.msg.bot pre{background:var(--code-bg);border-radius:8px;padding:9px 11px;overflow-x:auto;font-size:12px;margin:.4em 0}
.msg.err{color:#b3261e;font-size:12.5px}
.msg .cursor:after{content:"▍";color:var(--accent);animation:blink 1s steps(2) infinite}
@keyframes blink{50%{opacity:0}}
#chat-form{display:flex;gap:8px;padding:10px 13px;border-top:1px solid var(--line)}
#chat-input{flex:1;resize:none;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--ink);
  font:inherit;font-size:13.5px;padding:8px 10px;max-height:110px;min-height:38px}
#chat-input:focus{outline:2px solid var(--accent);outline-offset:0}
#chat-send{border:1px solid var(--accent);background:var(--accent);color:#fff;border-radius:9px;
  width:38px;cursor:pointer;font-size:15px}
#chat-send:disabled{opacity:.45;cursor:default}
#chat-foot{font-size:11px;color:var(--muted);padding:0 13px 9px}
@media (max-width:640px){
  #chat-panel{right:8px;left:8px;width:auto;bottom:150px;max-height:66vh}
  #chat-btn{bottom:104px;right:16px}
}
@media print{#chat-btn,#chat-panel,#sel-chip{display:none!important}}
"""

CHAT_JS = r"""
(function(){
  var API="/api/chat";
  var panel=document.getElementById("chat-panel"),
      btn=document.getElementById("chat-btn"),
      chip=document.getElementById("sel-chip"),
      quote=document.getElementById("chat-quote"),
      log=document.getElementById("chat-log"),
      input=document.getElementById("chat-input"),
      send=document.getElementById("chat-send"),
      form=document.getElementById("chat-form");

  if(!panel) return;
  var pendingSelection="", busy=false, lastSelection="";

  function esc(s){return s.replace(/[&<>]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;"}[c];});}

  // minimal markdown: fenced code, inline code, bold, bullets, numbered lists
  function md(src){
    var parts=src.split(/```/), out="";
    for(var i=0;i<parts.length;i++){
      if(i%2){ out+="<pre><code>"+esc(parts[i].replace(/^\w*\n/,""))+"</code></pre>"; continue; }
      var t=esc(parts[i]);
      t=t.replace(/`([^`\n]+)`/g,"<code>$1</code>").replace(/\*\*([^*]+)\*\*/g,"<b>$1</b>");
      var lines=t.split(/\n/), html="", inUl=false, inOl=false;
      for(var j=0;j<lines.length;j++){
        var line=lines[j];
        if(/^\s*[-*]\s+/.test(line)){
          if(inOl){html+="</ol>";inOl=false;}
          if(!inUl){html+="<ul>";inUl=true;}
          html+="<li>"+line.replace(/^\s*[-*]\s+/,"")+"</li>"; continue;
        }
        if(/^\s*\d+[.)]\s+/.test(line)){
          if(inUl){html+="</ul>";inUl=false;}
          if(!inOl){html+="<ol>";inOl=true;}
          html+="<li>"+line.replace(/^\s*\d+[.)]\s+/,"")+"</li>"; continue;
        }
        if(inUl){html+="</ul>";inUl=false;}
        if(inOl){html+="</ol>";inOl=false;}
        if(line.trim()==="") continue;
        html+="<p>"+line+"</p>";
      }
      if(inUl)html+="</ul>";
      if(inOl)html+="</ol>";
      out+=html;
    }
    return out;
  }

  function outline(){
    return [].slice.call(document.querySelectorAll("main h2, main h3")).slice(0,40)
      .map(function(h){return (h.tagName==="H3"?"  - ":"- ")+h.textContent.replace(/#$/,"").trim();}).join("\n");
  }

  function sectionFor(node){
    var el = node && (node.nodeType===1?node:node.parentElement);
    if(!el || !el.closest) return "";
    el = el.closest("main") ? el : null;
    if(!el) return "";
    var heads=[].slice.call(document.querySelectorAll("main h2, main h3"));
    var cur=null, idx=-1;
    for(var i=0;i<heads.length;i++){
      if(heads[i].compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING) { cur=heads[i]; idx=i; }
    }
    if(!cur) return "";
    var stop = heads[idx+1] || null, txt=[], n=cur;
    while((n=n.nextSibling) && n!==stop){ if(n.textContent) txt.push(n.textContent); }
    return (cur.textContent+"\n"+txt.join("\n")).replace(/\s+\n/g,"\n").slice(0,3000);
  }

  function placeChip(x,y){
    chip.style.left=x+"px"; chip.style.top=(y+window.scrollY-8)+"px"; chip.style.display="block";
  }
  function hideChip(){ chip.style.display="none"; }

  document.addEventListener("mouseup",function(e){
    setTimeout(function(){
      var s=window.getSelection(), text=s?s.toString().trim():"";
      if(!text || text.length<3 || !s.anchorNode || !(s.anchorNode.parentElement||s.anchorNode).closest("main")){hideChip();return;}
      lastSelection=text;
      var r=s.getRangeAt(0).getBoundingClientRect();
      placeChip(r.left+r.width/2, Math.max(r.top,8));
    },10);
  });
  document.addEventListener("mousedown",function(e){ if(e.target!==chip) hideChip(); });

  chip.addEventListener("mousedown",function(e){ e.preventDefault(); });
  chip.addEventListener("click",function(e){
    e.stopPropagation();
    pendingSelection=lastSelection; hideChip(); open(pendingSelection);
  });

  function open(sel){
    panel.classList.add("open");
    if(sel){ quote.style.display="block"; quote.textContent=sel; pendingSelection=sel; }
    else { quote.style.display="none"; quote.textContent=""; pendingSelection=""; }
    setTimeout(function(){input.focus();},60);
  }
  function close(){ panel.classList.remove("open"); }

  btn.addEventListener("click",function(){ panel.classList.contains("open")?close():open(lastSelection||""); });
  document.getElementById("chat-close").addEventListener("click",close);
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") close(); });

  function addMsg(cls,html){
    var d=document.createElement("div"); d.className="msg "+cls; d.innerHTML=html; log.appendChild(d);
    log.scrollTop=log.scrollHeight; return d;
  }

  async function ask(q){
    if(busy||!q.trim()) return;
    busy=true; send.disabled=true;
    addMsg("user",esc(q));
    var bot=addMsg("bot",'<span class="cursor"></span>');
    var acc="";
    var sid=sessionStorage.getItem("mn-sid");
    if(!sid){ sid=(crypto.randomUUID?crypto.randomUUID():String(Date.now())+Math.random().toString(16).slice(2)); sessionStorage.setItem("mn-sid",sid); }
    var payload={q:q, sid:sid, sel:pendingSelection||"", page:document.querySelector("h1")?document.querySelector("h1").textContent.trim():document.title,
                 section:sectionFor(window.getSelection()&&window.getSelection().anchorNode?"":document.querySelector("main h2"))||"",
                 outline:outline()};
    // section: prefer the one containing the selection, else the first heading on screen
    try{
      var sel=window.getSelection();
      if(pendingSelection && sel && sel.anchorNode){ payload.section=sectionFor(sel.anchorNode); }
      if(!payload.section){
        var vis=[].slice.call(document.querySelectorAll("main h2, main h3")).filter(function(h){
          var r=h.getBoundingClientRect(); return r.top>-80 && r.top<window.innerHeight*0.6; }).pop();
        if(vis) payload.section=sectionFor(vis);
      }
    }catch(_){}

    try{
      var res=await fetch(API,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(payload)});
      if(!res.ok){
        var j=await res.json().catch(function(){return{};});
        throw new Error(j.error||("HTTP "+res.status));
      }
      var reader=res.body.getReader(), dec=new TextDecoder(), buf="";
      for(;;){
        var r=await reader.read(); if(r.done) break;
        buf+=dec.decode(r.value,{stream:true});
        var lines=buf.split("\n"); buf=lines.pop()||"";
        for(var i=0;i<lines.length;i++){
          var l=lines[i].trim(); if(l.indexOf("data:")!==0) continue;
          var d=l.slice(5).trim(); if(d==="[DONE]") continue;
          try{ var o=JSON.parse(d); if(o.d){acc+=o.d; bot.innerHTML=md(acc)+'<span class="cursor"></span>'; log.scrollTop=log.scrollHeight;} if(o.error) throw new Error(o.error);}catch(_){}
        }
      }
      bot.innerHTML=md(acc||"_no answer_");
    }catch(err){
      bot.className="msg err";
      bot.textContent = String(err.message).indexOf("Failed to fetch")>-1 || String(err.message).indexOf("HTTP 5")>-1
        ? "Assistant unavailable — it only works on the deployed site (needs the /api/chat function)."
        : "Error: "+err.message;
    }finally{
      busy=false; send.disabled=false; input.value=""; input.focus();
      pendingSelection=""; quote.style.display="none";
    }
  }

  form.addEventListener("submit",function(e){ e.preventDefault(); ask(input.value); });
  input.addEventListener("keydown",function(e){
    if(e.key==="Enter"&&!e.shiftKey){ e.preventDefault(); ask(input.value); }
  });
  input.addEventListener("input",function(){ input.style.height="auto"; input.style.height=Math.min(input.scrollHeight,110)+"px"; });
})();
"""

JS = """
(function(){
  var root=document.documentElement, key='minotes-theme';
  var saved=localStorage.getItem(key);
  var prefers=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
  root.setAttribute('data-theme', saved || prefers);

  var btn=document.getElementById('theme');
  function sync(){ if(btn) btn.textContent = root.getAttribute('data-theme')==='dark' ? '\\u2600' : '\\u263E'; }
  sync();
  if(btn) btn.addEventListener('click',function(){
    var next = root.getAttribute('data-theme')==='dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next); localStorage.setItem(key,next); sync();
  });

  var bar=document.getElementById('progress');
  if(bar) addEventListener('scroll',function(){
    var h=document.documentElement.scrollHeight-innerHeight;
    bar.style.width=(h>0?(scrollY/h*100):0)+'%';
  },{passive:true});

  document.querySelectorAll('pre').forEach(function(pre){
    var b=document.createElement('button');
    b.className='copy'; b.textContent='copy';
    b.addEventListener('click',function(){
      var t=pre.querySelector('code'); var txt=t?t.innerText:pre.innerText;
      navigator.clipboard.writeText(txt).then(function(){
        b.textContent='copied'; setTimeout(function(){b.textContent='copy';},1200);
      });
    });
    pre.appendChild(b);
  });

  document.querySelectorAll('main table').forEach(function(t){
    if(t.parentElement.classList.contains('table-scroll')) return;
    var w=document.createElement('div'); w.className='table-scroll';
    t.parentNode.insertBefore(w,t); w.appendChild(t);
  });

  var links=[].slice.call(document.querySelectorAll('.sidebar a[href^="#"]'));
  var map={}; links.forEach(function(a){ map[a.getAttribute('href').slice(1)]=a; });
  var heads=[].slice.call(document.querySelectorAll('main h2[id], main h3[id]'));
  if('IntersectionObserver' in window && heads.length){
    var obs=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(!e.isIntersecting) return;
        links.forEach(function(a){a.classList.remove('active');});
        var a=map[e.target.id]; if(a){a.classList.add('active');}
      });
    },{rootMargin:'-10% 0px -75% 0px'});
    heads.forEach(function(h){obs.observe(h);});
  }

  var top=document.getElementById('top');
  if(top) top.addEventListener('click',function(){ scrollTo({top:0,behavior:'smooth'}); });
})();
"""

MERMAID_SCRIPTS = """<script src="../assets/mermaid.min.js"></script>
<script>
(function(){
  var nodes=[].slice.call(document.querySelectorAll('.mermaid'));
  if(!nodes.length) return;
  nodes.forEach(function(n){ n.dataset.src=n.textContent; });
  function theme(){ return document.documentElement.getAttribute('data-theme')==='dark'?'dark':'default'; }
  function run(){
    mermaid.initialize({startOnLoad:false, theme:theme(), securityLevel:'loose',
      flowchart:{htmlLabels:true, curve:'basis', nodeSpacing:38, rankSpacing:52, padding:12},
      themeVariables:{fontFamily:'Inter,system-ui,sans-serif', fontSize:'15px'}});
    nodes.forEach(function(n){ n.removeAttribute('data-processed'); n.innerHTML=n.dataset.src; });
    mermaid.run({nodes:nodes, suppressErrors:true});
  }
  run();
  new MutationObserver(function(m){
    if(m.some(function(x){return x.attributeName==='data-theme';})) run();
  }).observe(document.documentElement,{attributes:true});
})();
</script>"""

PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}} · {{SUBJECT}}</title>
<style>{{CSS}}</style>
</head>
<body>
<div id="progress"></div>
<div class="wrap">
  <aside class="sidebar">
    <a class="home" href="index.html">← {{SUBJECT}}</a>
    {{PRACTICE_LINK}}
    <h1>{{LABEL}}</h1>
    <p class="sub">{{SUB}}</p>
    <nav class="toc">{{TOC}}</nav>
  </aside>
  <main>
    <div class="doc-head">
      <div class="kicker">{{CODE}} · {{SUBJECT}}</div>
      <div class="meta">{{SUB}} · rendered from {{SRC}}</div>
    </div>
    {{BODY}}
  </main>
</div>
<button id="chat-btn" title="Ask about this page (select text first)">✳</button>
<div id="sel-chip">Ask about this</div>
<div id="chat-panel" role="dialog" aria-label="Ask about this page">
  <div id="chat-head"><span>Ask this page</span><span class="sp"></span><button id="chat-close" title="Close">✕</button></div>
  <div id="chat-quote"></div>
  <div id="chat-log"></div>
  <form id="chat-form" autocomplete="off">
    <textarea id="chat-input" rows="1" placeholder="Ask about the selection or the section…"></textarea>
    <button id="chat-send" title="Send">↑</button>
  </form>
  <div id="chat-foot">Select text → “Ask about this”. Enter sends, Shift+Enter newline.</div>
</div>
<div class="tools">
  <button id="theme" title="Toggle light / dark">☾</button>
  <button id="top" title="Back to top">↑</button>
</div>
<script>{{JS}}</script>
{{MERMAID}}
</body>
</html>
"""

SHELL_CSS = """
body{background:var(--bg)}
.shell{max-width:1080px;margin:0 auto;padding:0 28px}
.topbar{padding:26px 0 0;display:flex;justify-content:space-between;align-items:center;gap:16px}
.topbar .brand{font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:700}
.topbar a{font-size:13px;color:var(--muted);text-decoration:none}
.topbar a:hover{color:var(--accent)}
.hero{padding:34px 0 6px}
.hero .kicker{font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700}
.hero h1{font-size:2.4rem;margin:.2em 0 .25em;letter-spacing:-.02em}
.hero p{color:var(--muted);max-width:64ch;margin:0}
.searchbox{margin:24px 0 6px;display:flex;align-items:center;gap:12px}
.searchbox label{font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);
  font-weight:700;white-space:nowrap}
.searchbox input{flex:1;padding:13px 16px;border-radius:12px;border:1px solid var(--line);
  background:var(--panel);color:var(--ink);font:inherit;font-size:15px}
.searchbox input:focus{outline:2px solid var(--accent);outline-offset:1px}
.count{font-size:13px;color:var(--muted);white-space:nowrap;min-width:150px;text-align:right}
section.group{margin:38px 0 0}
section.group>h2{font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);
  opacity:.62;border:0;margin:0 0 14px;padding:0;font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:16px}
.card{position:relative;display:flex;flex-direction:column;text-decoration:none;color:inherit;
  background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:20px 20px 16px;
  transition:transform .15s,border-color .15s,box-shadow .15s}
.card:hover{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 12px 30px rgba(0,0,0,.09)}
.card .tag{font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);font-weight:700}
.card h3{font-size:1.14rem;margin:.5em 0 .35em;border:0;padding:0;line-height:1.3}
.card .blurb{margin:0;color:var(--muted);font-size:14px}
.card .q{margin-top:auto;padding-top:14px;font-size:12.5px;color:var(--muted);font-family:var(--mono)}
.card .go{position:absolute;top:18px;right:18px;color:var(--accent);opacity:0;transition:opacity .15s}
.card:hover .go{opacity:1}
.card.hero-card{grid-column:1/-1;background:linear-gradient(120deg,var(--accent-soft),var(--panel) 62%);
  border-color:color-mix(in srgb,var(--accent) 30%,var(--line));padding:24px 26px}
.card.hero-card h3{font-size:1.45rem;margin-top:.3em}
.card.hero-card .go{opacity:.9}
.hint{max-width:1080px;margin:44px auto 70px;padding:0 28px;font-size:13px;color:var(--muted)}
.tools button{box-shadow:0 4px 14px rgba(0,0,0,.10)}
"""

SUBJECT_PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{SUBJECT}} · minotes</title>
<style>{{CSS}}</style>
</head>
<body>
<div class="shell">
  <div class="topbar"><div class="brand">{{CODE}} · {{SUBJECT}}</div><a href="../index.html">minotes ↗</a></div>
  <div class="hero">
    <div class="kicker">{{TAGLINE}}</div>
    <h1>{{SUBJECT}}</h1>
    <p>{{BLURB}}</p>
  </div>
  <div class="searchbox">
    <label for="q">Filter</label>
    <input id="q" type="search" placeholder="laravel · box model · arrays · session · tracker">
    <span class="count" id="count"></span>
  </div>
</div>
<div class="shell">
{{CARDS}}
</div>
<p class="hint">Inside any document: <strong>☾</strong> switches light/dark, <strong>↑</strong> jumps back to the top, every code block has a copy button, and Ctrl+P prints cleanly without the sidebar.</p>
<div class="tools"><button id="theme" title="Toggle light / dark">☾</button></div>
<script>{{JS}}</script>
<script>
(function(){
  var input=document.getElementById('q'), count=document.getElementById('count');
  var cards=[].slice.call(document.querySelectorAll('.card'));
  function apply(){
    var v=input.value.toLowerCase().trim(), shown=0;
    cards.forEach(function(c){
      var hay=(c.textContent+' '+(c.dataset.tags||'')).toLowerCase();
      var hit = !v || hay.indexOf(v) > -1;
      c.style.display = hit ? '' : 'none'; if(hit) shown++;
    });
    document.querySelectorAll('section.group').forEach(function(g){
      var any=[].slice.call(g.querySelectorAll('.card')).some(function(c){return c.style.display!=='none';});
      g.style.display = any ? '' : 'none';
    });
    count.textContent = shown + ' of ' + cards.length + ' documents';
  }
  input.addEventListener('input', apply); apply();
})();
</script>
</body>
</html>
"""

HUB_PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>minotes</title>
<style>{{CSS}}</style>
</head>
<body>
<div class="shell">
  <div class="topbar"><div class="brand">minotes</div><a href="https://github.com/sebastian-abraham/minotes">source ↗</a></div>
  <div class="hero">
    <div class="kicker">{{KICKER}}</div>
    <h1>Notes</h1>
    <p>Lecture notes, exam kits and trackers, rendered from Markdown. Everything here is static — one folder per subject, one page per document.</p>
  </div>
</div>
<div class="shell">
{{CARDS}}
</div>
<p class="hint">Add a subject by dropping Markdown into <code>sources/&lt;subject&gt;/</code> and running <code>tools/build.py</code>.</p>
<div class="tools"><button id="theme" title="Toggle light / dark">☾</button></div>
<script>{{JS}}</script>
{{MERMAID}}
</body>
</html>
"""

DOC_CARD = """<a class="card{{CLASS}}" href="{{FILE}}" data-tags="{{TAGS}}">
  <span class="go">→</span>
  <div class="tag">{{LABEL}}</div>
  <h3>{{TITLE}}</h3>
  <p class="blurb">{{BLURB}}</p>
  <div class="q">{{SUB}}</div>
</a>"""

SUBJECT_CARD = """<a class="card" href="{{FILE}}" data-tags="{{TAGS}}">
  <span class="go">→</span>
  <div class="tag">{{CODE}}</div>
  <h3>{{TITLE}}</h3>
  <p class="blurb">{{BLURB}}</p>
  <div class="q">{{META}}</div>
</a>"""

FENCE = re.compile(r"(?ms)^(```|~~~)[ \t]*([\w+#-]*)[^\n]*\n(.*?)^\1[ \t]*$")
CODE_SPAN = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
PH_OPEN, PH_CLOSE = "\ue000", "\ue001"


def protect(md_text):
    """Render fenced blocks and inline code spans as placeholders before
    Markdown runs.

    Two reasons: a paragraph starting with a backticked tag ("`<table>` ...")
    is read by Markdown as a raw HTML block and swallows the rest of the file;
    and escaping '<' globally would double-escape code spans.
    """
    store = []

    def keep(rendered):
        store.append(rendered)
        return f"{PH_OPEN}{len(store) - 1}{PH_CLOSE}"

    def fence(m):
        lang, body = m.group(2), m.group(3)
        if lang == "mermaid":
            return keep(f'<div class="mermaid">{html_mod.escape(body)}</div>')
        cls = f' class="language-{html_mod.escape(lang)}"' if lang else ""
        return keep(f"<pre><code{cls}>{html_mod.escape(body)}</code></pre>")

    md_text = FENCE.sub(fence, md_text)
    md_text = CODE_SPAN.sub(lambda m: keep(f"<code>{html_mod.escape(m.group(2))}</code>"), md_text)
    # A converted-deck line like "#header { height: 60px; }" is CSS, not a heading.
    md_text = re.sub(r"^(#{1,6})(?=[^ #])", lambda m: "\\" + m.group(1), md_text, flags=re.M)
    return md_text.replace("<", "&lt;"), store


def restore(text, store):
    return re.sub(f"{PH_OPEN}(\\d+){PH_CLOSE}", lambda m: store[int(m.group(1))], text)


def render(md_text):
    md = markdown.Markdown(
        extensions=["tables", "def_list", "footnotes", "sane_lists", "toc"],
        extension_configs={"toc": {"toc_depth": "2-3", "slugify": slugify_unicode}},
    )
    protected, store = protect(md_text)
    body = md.convert(protected)
    return restore(body, store), restore(md.toc or "", store)


def first_h1(md_text, fallback):
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def build_doc(subject, src_name, label, sub, slug):
    src = os.path.join(SOURCES, subject["slug"], src_name)
    if not os.path.exists(src):
        print(f"  ! missing source: {src_name}")
        return None
    md_text = open(src, encoding="utf-8").read()
    body, toc = render(md_text)
    title = first_h1(md_text, slug)

    # drop in-page links whose anchor no longer exists (converted docs carry
    # anchors from their original HTML); the link text stays as plain text.
    def _dead_anchor(m):
        target = m.group(1)
        return m.group(2) if f'id="{target}"' not in body else m.group(0)
    body = re.sub(r'<a href="#([^"]+)"[^>]*>(.*?)</a>', _dead_anchor, body, flags=re.S)

    body = re.sub(
        r'(<h([23]) id="([^"]+)">)(.*?)(</h\2>)',
        lambda m: f'{m.group(1)}{m.group(4)}<a class="anchor" href="#{m.group(3)}">#</a>{m.group(5)}',
        body, flags=re.S,
    )

    page = (PAGE
            .replace("{{TITLE}}", html_mod.escape(strip_tags(title)))
            .replace("{{LABEL}}", html_mod.escape(label))
            .replace("{{SUB}}", html_mod.escape(sub))
            .replace("{{SRC}}", html_mod.escape(src_name))
            .replace("{{CODE}}", html_mod.escape(subject["code"]))
            .replace("{{SUBJECT}}", html_mod.escape(subject["title"]))
            .replace("{{PRACTICE_LINK}}", '<a class="home" href="practice.html">Practice drills</a>' if subject.get("drills") else "")
            .replace("{{TOC}}", toc or "")
            .replace("{{BODY}}", body)
            .replace("{{CSS}}", CSS + CHAT_CSS)
            .replace("{{MERMAID}}", MERMAID_SCRIPTS if 'class="mermaid"' in body else "")
            .replace("{{JS}}", JS + CHAT_JS))
    out = os.path.join(ROOT, subject["slug"], f"{slug}.html")
    write(out, page)
    print(f"  {subject['slug']}/{slug + '.html':24s} {os.path.getsize(out) // 1024:5d} KB")
    return title


def build_subject(subject):
    print(f"\n[{subject['title']}]")
    cards, rendered = {}, {}
    for src_name, label, sub, blurb, pretty, group, slug in subject["docs"]:
        title = build_doc(subject, src_name, label, sub, slug)
        if title is None:
            continue
        rendered[slug] = title
        card = (DOC_CARD
                .replace("{{CLASS}}", " hero-card" if group == "start" else "")
                .replace("{{FILE}}", f"{slug}.html")
                .replace("{{LABEL}}", html_mod.escape(label))
                .replace("{{TITLE}}", html_mod.escape(pretty))
                .replace("{{BLURB}}", html_mod.escape(blurb))
                .replace("{{SUB}}", html_mod.escape(sub))
                .replace("{{TAGS}}", html_mod.escape(f"{label} {pretty} {blurb} {src_name}")))
        cards.setdefault(group, []).append(card)

    if subject.get("drills"):
      cards.setdefault("practice", []).append(
        DOC_CARD
        .replace("{{CLASS}}", " hero-card")
        .replace("{{FILE}}", "practice.html")
        .replace("{{LABEL}}", "Practice")
        .replace("{{TITLE}}", "Syntax drills — 10 combined tasks")
        .replace("{{BLURB}}", "Two per module: fill the blanks, or write the whole thing and have the tutor grade it.")
        .replace("{{SUB}}", "fill · output · write · checked in the browser")
        .replace("{{TAGS}}", "practice drills coding syntax fill output write"))

    drill_list = {"ehs": ehs_drill_data.EHS_DRILLS, "ise": ise_drill_data.ISE_DRILLS}.get(subject.get("drills"), drill_data.DRILLS)
    page = practice_page.build(drill_list, subject["title"], CSS + SHELL_CSS, JS)
    write(os.path.join(ROOT, subject["slug"], "practice.html"), page)
    print(f"  {subject['slug']}/practice.html      {os.path.getsize(os.path.join(ROOT, subject['slug'], 'practice.html')) // 1024:5d} KB  ({len(drill_list)} drills)")

    blocks = []
    for key, heading in GROUPS:
        if key not in cards:
            continue
        if key == "start":
            blocks.append('<section class="group">' + "".join(cards[key]) + "</section>")
        else:
            blocks.append(f'<section class="group"><h2>{heading}</h2><div class="grid">'
                          + "".join(cards[key]) + "</div></section>")

    page = (SUBJECT_PAGE
            .replace("{{SUBJECT}}", html_mod.escape(subject["title"]))
            .replace("{{CODE}}", html_mod.escape(subject["code"]))
            .replace("{{TAGLINE}}", html_mod.escape(subject["tagline"]))
            .replace("{{BLURB}}", html_mod.escape(subject["blurb"]))
            .replace("{{CARDS}}", "\n".join(blocks))
            .replace("{{CSS}}", CSS + SHELL_CSS)
            .replace("{{MERMAID}}", "")
            .replace("{{JS}}", JS))
    path = os.path.join(ROOT, subject["slug"], "index.html")
    write(path, page)
    print(f"  {subject['slug']}/index.html      {os.path.getsize(path) // 1024:5d} KB  ({len(rendered)} documents)")


def build_hub():
    cards = []
    for subject in SUBJECTS:
        cards.append(SUBJECT_CARD
                     .replace("{{FILE}}", f"{subject['slug']}/index.html")
                     .replace("{{CODE}}", html_mod.escape(subject["code"]))
                     .replace("{{TITLE}}", html_mod.escape(subject["title"]))
                     .replace("{{BLURB}}", html_mod.escape(subject["blurb"]))
                     .replace("{{META}}", f"{subject['tagline']} · {len(subject['docs'])} documents")
                     .replace("{{TAGS}}", html_mod.escape(subject["title"] + " " + subject["code"])))
    if len(cards) == 1:
        blocks = '<section class="group"><div class="grid">' + cards[0] + "</div></section>"
    else:
        blocks = ('<section class="group"><h2>Subjects</h2><div class="grid">'
                  + "".join(cards) + "</div></section>")
    page = (HUB_PAGE
            .replace("{{KICKER}}", "markdown → html · static")
            .replace("{{CARDS}}", blocks)
            .replace("{{CSS}}", CSS + SHELL_CSS)
            .replace("{{MERMAID}}", "")
            .replace("{{JS}}", JS))
    write(os.path.join(ROOT, "index.html"), page)
    print(f"\n  index.html                  hub, {len(SUBJECTS)} subject(s)")


def main(argv):
    only = [a for a in argv if not a.startswith("-")]
    subjects = [s for s in SUBJECTS if not only or s["slug"] in only]
    print("Building site from:", SOURCES, "| subjects:", ", ".join(s["slug"] for s in subjects))
    for subject in subjects:
        build_subject(subject)
    build_hub()
    print("\nDone. Open", os.path.join(ROOT, "index.html"))


if __name__ == "__main__":
    main(sys.argv[1:])
