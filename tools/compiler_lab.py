"""compiler_lab.py — generates the two interactive Compiler Lab pages.

  compiler-lab/lab.html        algorithm step  <->  source line, + step-by-step trace player
  compiler-lab/playground.html write C in the browser and actually run it (Wandbox API)

Kept separate from build.py for the same reason practice.py is: these are apps, not
Markdown pages. Sources are read from sources/compiler-lab/code/ so the line map can
never drift from the code that was compiled.
"""

import html
import json
import os

import compiler_lab_data as data

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CODE_DIR = os.path.join(ROOT, "sources", "compiler-lab", "code")


def load_code():
    code = {}
    for name in sorted(os.listdir(CODE_DIR)):
        with open(os.path.join(CODE_DIR, name), encoding="utf-8") as fh:
            code[name] = fh.read()
    return code


def build_payload():
    """Resolve every anchor to real line numbers. Raises if an anchor is missing."""
    code = load_code()
    exps = []
    missing = []
    for e in data.EXPS:
        files = []
        line_of = {}
        for name in e["files"]:
            text = code[name]
            lines = text.split("\n")
            fl = []
            for i, ln in enumerate(lines, 1):
                fl.append(ln)
            files.append({"name": name, "lines": fl})
            for i, ln in enumerate(lines, 1):
                line_of.setdefault(ln, []).append(i)
        steps = []
        for text, anchors in e["steps"]:
            resolved = []
            for a in anchors:
                hit = None
                for name in e["files"]:
                    if a in code[name]:
                        hits = [i for i, ln in enumerate(code[name].split("\n"), 1) if a in ln]
                        hit = {"f": name, "l": hits}
                        break
                if hit is None:
                    missing.append((e["id"], a))
                else:
                    resolved.append(hit)
            steps.append({"t": text, "code": resolved})
        exps.append({
            "id": e["id"], "n": e["n"], "title": e["title"], "story": e["story"],
            "files": files, "steps": steps, "curve": e["curve"], "viva": e["viva"],
            "sim": e["sim"], "simhint": e["simhint"], "simdefault": e["simdefault"],
            "build": data.BUILD[e["id"]],
        })
    if missing:
        raise SystemExit("UNRESOLVED ANCHORS (fix in compiler_lab_data.py):\n" +
                         "\n".join(f"  {ei}: {a!r}" for ei, a in missing))
    return exps


# --------------------------------------------------------------------------- CSS
LAB_CSS = """
/* ---------- lab app ---------- */
body{padding-bottom:70px}
.lab{max-width:1500px;margin:0 auto;padding:22px 22px 50px;display:grid;
  grid-template-columns:236px minmax(0,1fr);gap:22px;align-items:start}
@media (max-width:980px){.lab{grid-template-columns:1fr;padding:16px}
  .rail{position:static!important;max-height:none!important;display:flex;overflow-x:auto;gap:6px}
  .rail .rl{white-space:nowrap;flex:0 0 auto}}
.rail{position:sticky;top:16px;max-height:calc(100vh - 32px);overflow:auto}
.rail h4{font:700 10.5px/1 var(--sans);letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);margin:0 0 8px}
.rl{display:flex;gap:8px;align-items:baseline;padding:6px 9px;border-radius:8px;cursor:pointer;
  font-size:13px;color:var(--muted);border:1px solid transparent;line-height:1.3}
.rl:hover{background:var(--accent-soft)}
.rl.on{background:var(--accent-soft);border-color:var(--accent);color:var(--ink)}
.rl b{font-family:var(--mono);font-size:11px;color:var(--accent);flex:0 0 20px}

.exp{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px 22px 22px}
.exp h2{margin:.1em 0 .5em;font-size:1.28rem;line-height:1.3}
.exp h2 span{color:var(--accent);font-family:var(--mono);font-size:1rem;margin-right:8px}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.chip{font-family:var(--mono);font-size:11px;color:var(--muted);border:1px solid var(--line);
  border-radius:6px;padding:2px 7px;background:var(--code-bg)}
.story{font-size:13.6px;line-height:1.62;color:var(--ink);margin:0 0 16px;
  border-left:2px solid var(--accent);padding-left:12px}

.map{display:grid;grid-template-columns:minmax(280px,.95fr) minmax(0,1.05fr);gap:16px;align-items:start}
@media (max-width:1180px){.map{grid-template-columns:1fr}}
.steps{display:flex;flex-direction:column;gap:4px}
.step{display:grid;grid-template-columns:20px 1fr;gap:9px;padding:7px 9px;border-radius:8px;
  cursor:pointer;border:1px solid transparent;font-size:13.1px;line-height:1.5}
.step:hover{background:var(--accent-soft)}
.step.on{background:var(--accent-soft);border-color:var(--accent)}
.step .num{font-family:var(--mono);font-size:10.5px;color:var(--accent);padding-top:3px}
.step code{font-size:11.5px}

.codepane{position:static;border:none;border-radius:0;background:var(--code-bg)}
#panes{position:sticky;top:16px;border:1px solid var(--line);border-radius:11px;
  background:var(--code-bg);overflow:auto;max-height:52vh}
#panes .codepane + .codepane{border-top:1px solid var(--line)}
.codepane .fname{font:700 10.5px/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);padding:9px 12px;border-bottom:1px solid var(--line);position:sticky;top:0;
  background:var(--code-bg);z-index:2}
.codepane table{border-collapse:collapse;width:100%;font-family:var(--mono);font-size:11.6px}
.codepane td{vertical-align:top;padding:0}
.codepane td.ln{width:38px;text-align:right;padding:0 8px 0 0;color:var(--muted);opacity:.55;
  user-select:none;border-right:1px solid var(--line)}
.codepane td.cd{padding:0 12px 0 10px;white-space:pre-wrap;word-break:break-word;color:var(--ink)}
.codepane tr.hl{background:color-mix(in srgb, var(--accent) 16%, transparent)}
.codepane tr.hl td.ln{opacity:1;color:var(--accent);font-weight:700}
.codepane tr.live{background:color-mix(in srgb, #ff9f0a 26%, transparent)}
.codepane tr{cursor:pointer}

.trace{margin-top:18px;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.trace .th{display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding:10px 12px;
  background:var(--accent-soft);border-bottom:1px solid var(--line)}
.trace .th b{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent)}
.trace .th .hint2{font-size:11.5px;color:var(--muted);flex:1}
.trace .tb{padding:12px}
.trace textarea{width:100%;min-height:60px;font-family:var(--mono);font-size:12px;
  background:var(--code-bg);color:var(--ink);border:1px solid var(--line);border-radius:8px;
  padding:9px 10px;resize:vertical}
.btn{font:600 12px/1 var(--sans);border:1px solid var(--line);background:var(--panel);
  color:var(--ink);border-radius:7px;padding:7px 11px;cursor:pointer}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.p{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.btnrow{display:flex;gap:7px;align-items:center;flex-wrap:wrap;margin-top:9px}
.note{margin-top:11px;font-size:13px;line-height:1.55;background:var(--accent-soft);
  border-left:2px solid var(--accent);border-radius:0 8px 8px 0;padding:9px 12px;min-height:20px}
.state{margin-top:10px;display:flex;gap:10px;flex-wrap:wrap}
.sbox{border:1px solid var(--line);border-radius:9px;background:var(--panel);min-width:120px}
.sbox-t{font:700 9.5px/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  padding:7px 9px;border-bottom:1px solid var(--line)}
.sbox-b{padding:8px 9px;font-family:var(--mono);font-size:11.5px;line-height:1.5;overflow:auto;max-width:420px}
.sbox-b pre{margin:0;font-size:11.5px}
.kv{display:flex;gap:8px;font-size:12px;padding:2px 0}
.kv .k{color:var(--muted);min-width:78px}
.kv .v{font-family:var(--mono);font-size:11.5px}
.cell{display:inline-block;border:1px solid var(--line);border-radius:5px;background:var(--code-bg);
  padding:1px 6px;margin:1px 2px;font-family:var(--mono);font-size:11px}
.cell.top{border-color:var(--accent);color:var(--accent);font-weight:700}
.dim{color:var(--muted);opacity:.7;font-size:11px}
.stbl{border-collapse:collapse;font-family:var(--mono);font-size:11px}
.stbl th,.stbl td{border:1px solid var(--line);padding:2px 6px;text-align:center}
.stbl th{color:var(--muted);font-weight:600;background:var(--code-bg)}
.stbl td.hi{background:color-mix(in srgb, var(--accent) 22%, transparent);font-weight:700}
.counter{font-family:var(--mono);font-size:11px;color:var(--muted)}
details{border-top:1px solid var(--line);margin-top:14px;padding-top:10px}
summary{cursor:pointer;font-size:12.5px;font-weight:600;color:var(--ink);letter-spacing:.01em}
summary::marker{color:var(--accent)}
.curve{margin-top:8px}
.cv{padding:8px 0;border-bottom:1px dashed var(--line);font-size:13px;line-height:1.55}
.cv:last-child{border-bottom:none}
.cv b{display:block;color:var(--accent);font-size:12px;margin-bottom:2px}
.qa{padding:8px 0;border-bottom:1px dashed var(--line);font-size:13px;line-height:1.55}
.qa:last-child{border-bottom:none}
.qa b{display:block;margin-bottom:3px}
.cmd{position:relative;margin:10px 0 0}
.cmd pre{margin:0;background:var(--code-bg);border:1px solid var(--line);border-radius:8px;
  padding:10px 12px;font-size:11.6px;overflow:auto}
.toplink{font-size:12.5px;color:var(--muted);text-decoration:none}
.toplink:hover{color:var(--accent)}
"""

PLAY_CSS = """
/* ---------- playground ---------- */
body{padding-bottom:60px}
.pg{max-width:1400px;margin:0 auto;padding:22px;display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;align-items:start}
@media (max-width:1000px){.pg{grid-template-columns:1fr}}
.pg .full{grid-column:1/-1}
.card3{background:var(--panel);border:1px solid var(--line);border-radius:13px;overflow:hidden}
.card3 .ch{display:flex;gap:9px;align-items:center;flex-wrap:wrap;padding:10px 12px;
  border-bottom:1px solid var(--line);background:var(--code-bg)}
.card3 .ch b{font:700 11px/1 var(--sans);letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.card3 .cb{padding:12px}
select,textarea,input{font-family:var(--mono);font-size:12.4px;background:var(--code-bg);
  color:var(--ink);border:1px solid var(--line);border-radius:7px;padding:8px 9px;width:100%}
#code{min-height:330px;line-height:1.55;white-space:pre;tab-size:4}
#stdin{min-height:52px}
#out{background:var(--code-bg);border:1px solid var(--line);border-radius:8px;padding:11px 12px;
  font-family:var(--mono);font-size:12.2px;line-height:1.5;white-space:pre-wrap;min-height:180px;
  max-height:46vh;overflow:auto}
.ok{color:#2ea043;font-weight:700}
.bad{color:#e5534b;font-weight:700}
.btn{font:600 12px/1 var(--sans);border:1px solid var(--line);background:var(--panel);color:var(--ink);
  border-radius:7px;padding:7px 12px;cursor:pointer}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.p{background:var(--accent);color:#fff;border-color:var(--accent)}
.btn:disabled{opacity:.5;cursor:not-allowed}
.row{display:flex;gap:7px;align-items:center;flex-wrap:wrap}
.hintline{font-size:12px;color:var(--muted);line-height:1.5;margin-top:8px}
"""

# --------------------------------------------------------------------------- lab page
LAB_PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lab bench — {{SUBJECT}}</title>
<style>{{CSS}}</style>
</head>
<body>
<div class="lab">
  <nav class="rail">
    <h4>11 experiments</h4>
    <div id="rail"></div>
    <h4 style="margin-top:16px">Elsewhere</h4>
    <div class="rl" onclick="location.href='playground.html'">⌨ Playground</div>
    <div class="rl" onclick="location.href='index.html'">← All documents</div>
  </nav>
  <main id="main"></main>
</div>
<script>var EXPS = {{DATA}};</script>
<script src="sims.js?v={{SIMSV}}"></script>
<script>{{JS}}</script>
</body>
</html>
"""

LAB_JS = r"""
var cur = 0, frames = [], fi = 0, timer = null;

function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}

function rail(){
  document.getElementById("rail").innerHTML = EXPS.map(function(e,i){
    return '<div class="rl'+(i===cur?" on":"")+'" data-i="'+i+'"><b>'+e.n+'</b><span>'+
      esc(e.title)+'</span></div>';
  }).join("");
  Array.prototype.forEach.call(document.querySelectorAll(".rl[data-i]"),function(el){
    el.onclick=function(){
      cur=+el.dataset.i;
      if(history.replaceState) history.replaceState(null,"","#"+EXPS[cur].id);
      render();window.scrollTo({top:0,behavior:"smooth"});};
  });
}

function codePane(e){
  var out = "";
  e.files.forEach(function(f){
    out += '<div class="codepane" data-file="'+esc(f.name)+'"><div class="fname">'+esc(f.name)+'</div>'+
      '<table><tbody>'+f.lines.map(function(ln,i){
        return '<tr data-line="'+(i+1)+'"><td class="ln">'+(i+1)+'</td><td class="cd">'+
               (esc(ln)||" ")+'</td></tr>';
      }).join("")+'</tbody></table></div>';
  });
  return out;
}

function render(){
  rail();
  var e = EXPS[cur];
  var h = '<article class="exp">';
  h += '<h2><span>Exp '+e.n+'</span>'+esc(e.title)+'</h2>';
  h += '<div class="chips">'+e.files.map(function(f){return '<span class="chip">'+esc(f.name)+'</span>';}).join("")+
       '<a class="toplink" href="playground.html">run it in the playground →</a></div>';
  h += '<p class="story">'+e.story+'</p>';
  h += '<div class="map"><div class="steps" id="steps">';
  e.steps.forEach(function(s,i){
    h += '<div class="step" data-i="'+i+'"><div class="num">'+(i+1)+'</div><div>'+s.t+'</div></div>';
  });
  h += '</div><div id="panes">'+codePane(e)+'</div></div>';

  h += '<div class="trace"><div class="th"><b>Trace</b><span class="hint2">'+esc(e.simhint)+
       '</span><span class="counter" id="cnt"></span></div><div class="tb">'+
       '<textarea id="simin" spellcheck="false"></textarea>'+
       '<div class="btnrow"><button class="btn p" id="run">▶ Run trace</button>'+
       '<button class="btn" id="prev" disabled>← Prev</button>'+
       '<button class="btn" id="next" disabled>Next →</button>'+
       '<button class="btn" id="play" disabled>⏵ Auto</button>'+
       '<button class="btn" id="reset" disabled>⟲ Reset</button></div>'+
       '<div class="note" id="note">Press <b>Run trace</b> — every step lights the C lines that do it.</div>'+
       '<div class="state" id="state"></div></div></div>';

  h += '<div class="cmd"><pre>'+"$ "+esc(e.build)+'</pre></div>';

  h += '<details><summary>Curveballs — what changes if the question is modified</summary><div class="curve">'+
       e.curve.map(function(c){return '<div class="cv"><b>'+c[0]+'</b>'+c[1]+'</div>';}).join("")+
       '</div></details>';
  h += '<details><summary>Viva — '+e.viva.length+' questions with answers</summary>'+
       e.viva.map(function(q){return '<div class="qa"><b>'+q[0]+'</b>'+q[1]+'</div>';}).join("")+
       '</details>';
  h += '</article>';
  document.getElementById("main").innerHTML = h;

  document.getElementById("simin").value = e.simdefault;
  Array.prototype.forEach.call(document.querySelectorAll(".step"),function(el){
    el.onclick=function(){selectStep(+el.dataset.i);};
  });
  Array.prototype.forEach.call(document.querySelectorAll(".codepane tr"),function(tr){
    tr.onclick=function(){
      var ln = +tr.dataset.line, f = tr.closest(".codepane").dataset.file, hits = [];
      e.steps.forEach(function(s,i){
        s.code.forEach(function(c){ if(c.f===f && c.l.indexOf(ln)>=0) hits.push(i); });
      });
      if(hits.length) selectStep(hits[0]); else clearHL();
    };
  });
  document.getElementById("run").onclick = function(){ runSim(false); };
  document.getElementById("prev").onclick = function(){ step(-1); };
  document.getElementById("next").onclick = function(){ step(1); };
  document.getElementById("play").onclick = function(){ auto(); };
  document.getElementById("reset").onclick = function(){ runSim(false); };
  clearHL();
}

function clearHL(){
  Array.prototype.forEach.call(document.querySelectorAll(".codepane tr.hl, .codepane tr.live"),
    function(tr){tr.classList.remove("hl");tr.classList.remove("live");});
  Array.prototype.forEach.call(document.querySelectorAll(".step.on"),
    function(el){el.classList.remove("on");});
}

function hl(anchors, cls){
  if(!anchors) return;
  anchors.forEach(function(c){
    var pane = document.querySelector('.codepane[data-file="'+c.f.replace(/"/g,'')+'"]');
    if(!pane) return;
    c.l.forEach(function(ln){
      var tr = pane.querySelector('tr[data-line="'+ln+'"]');
      if(tr){ tr.classList.add(cls||"hl"); }
    });
  });
}

function scrollToRow(tr){
  var panes = document.getElementById("panes");
  if(!tr || !panes) return;
  var top = tr.getBoundingClientRect().top - panes.getBoundingClientRect().top + panes.scrollTop;
  panes.scrollTop = Math.max(0, top - panes.clientHeight/3);
}

function selectStep(i){
  clearHL();
  var e = EXPS[cur], s = e.steps[i];
  var el = document.querySelector('.step[data-i="'+i+'"]');
  if(el){ el.classList.add("on"); }
  hl(s.code, "hl");
  var first = null;
  s.code.forEach(function(c){
    var pane = document.querySelector('.codepane[data-file="'+c.f.replace(/"/g,'')+'"]');
    if(pane && c.l.length){
      var tr = pane.querySelector('tr[data-line="'+c.l[0]+'"]');
      if(tr && !first) first = tr;
    }
  });
  scrollToRow(first);
  document.getElementById("note").innerHTML =
    "<b>Step "+(i+1)+":</b> "+e.steps[i].t+
    (s.code.length ? '<br><span class="counter">→ the highlighted lines in the right pane are exactly this step</span>' : "");
}

function runSim(keep){
  var e = EXPS[cur], input = document.getElementById("simin").value;
  clearHL();
  if(!SIMS[e.sim]){ document.getElementById("note").textContent = "No trace for this experiment."; return; }
  try { frames = SIMS[e.sim](input) || []; }
  catch(err){ frames = [{note:"Trace failed: "+err+"\\nCheck the input format.", state:"", code:[]}]; }
  fi = 0;
  document.getElementById("cnt").textContent = frames.length + " steps";
  ["prev","next","play","reset"].forEach(function(id){document.getElementById(id).disabled=false;});
  showFrame();
}

function liveHL(anchors){
  // Highlight, in the C pane, every line whose text contains one of the frame's
  // anchors. Done by text search rather than by line numbers so a frame can point
  // at code that no algorithm step owns.
  if(!anchors || !anchors.length) return;
  EXPS[cur].files.forEach(function(file){
    var pane = document.querySelector('.codepane[data-file="'+file.name+'"]');
    if(!pane) return;
    Array.prototype.forEach.call(pane.querySelectorAll("tr"), function(tr){
      var cd = tr.querySelector(".cd");
      if(!cd) return;
      var txt = cd.textContent;
      for(var i=0;i<anchors.length;i++){
        if(anchors[i] && txt.indexOf(anchors[i]) >= 0){ tr.classList.add("live"); return; }
      }
    });
  });
}

function showFrame(){
  if(!frames.length) return;
  var f = frames[fi];
  clearHL();
  document.getElementById("note").innerHTML = "<b>"+(fi+1)+"/"+frames.length+".</b> "+f.note;
  document.getElementById("state").innerHTML = f.state || "";
  document.getElementById("prev").disabled = fi===0;
  document.getElementById("next").disabled = fi===frames.length-1;
  if(f.code && f.code.length){
    liveHL(f.code);
    scrollToRow(document.querySelector(".codepane tr.live"));
  }
}

function step(d){
  fi = Math.max(0, Math.min(frames.length-1, fi+d));
  showFrame();
}

function auto(){
  if(timer){ clearInterval(timer); timer=null; document.getElementById("play").textContent="⏵ Auto"; return; }
  document.getElementById("play").textContent="⏸ Stop";
  timer = setInterval(function(){
    if(fi >= frames.length-1){ clearInterval(timer); timer=null;
      document.getElementById("play").textContent="⏵ Auto"; return; }
    step(1);
  }, 900);
}

document.addEventListener("keydown", function(ev){
  if(ev.target.tagName === "TEXTAREA") return;
  if(ev.key === "ArrowRight") step(1);
  if(ev.key === "ArrowLeft") step(-1);
});

function pickFromHash(){
  var m = /exp(\d+)/.exec(location.hash || "");
  if(!m) return;
  for(var i=0;i<EXPS.length;i++){ if(+EXPS[i].n === +m[1]){ cur = i; return; } }
}

pickFromHash();
render();
if(/[?&]run=1/.test(location.search)) runSim(false);
"""

# --------------------------------------------------------------------------- playground page
PLAY_PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Playground — {{SUBJECT}}</title>
<style>{{CSS}}</style>
</head>
<body>
<div class="pg">
  <div class="full row" style="justify-content:space-between">
    <div>
      <h1 style="font-size:1.3rem;margin:0 0 4px">Write it, run it</h1>
      <div class="hintline">C is compiled and executed on a remote sandbox (Wandbox) — nothing to install.
        LEX/YACC are not available there, so experiments 2–4 run locally with the command under the output.</div>
    </div>
    <div class="row">
      <a class="btn" href="lab.html">← Lab bench</a>
      <a class="btn" href="index.html">All documents</a>
    </div>
  </div>

  <div class="card3">
    <div class="ch"><b>source</b>
      <select id="tpl" style="width:auto;min-width:230px"></select>
      <span class="row" style="margin-left:auto">
        <button class="btn" id="clear">Blank file</button>
      </span>
    </div>
    <div class="cb"><textarea id="code" spellcheck="false"></textarea></div>
  </div>

  <div>
    <div class="card3">
      <div class="ch"><b>stdin</b><span class="hintline" style="margin:0">what scanf() will read</span></div>
      <div class="cb"><textarea id="stdin" spellcheck="false"></textarea>
        <div class="btnrow row" style="margin-top:9px">
          <button class="btn p" id="run">▶ Compile &amp; run</button>
          <button class="btn" id="local">Copy local command</button>
          <span id="status" class="hintline" style="margin:0"></span>
        </div>
      </div>
    </div>
    <div class="card3" style="margin-top:16px">
      <div class="ch"><b>output</b><span id="meta" class="hintline" style="margin:0"></span></div>
      <div class="cb"><div id="out">Run something. The exit status and any compiler diagnostics appear here.</div></div>
    </div>
  </div>
</div>
<script>var TPL = {{TPL}};</script>
<script>{{JS}}</script>
</body>
</html>
"""

PLAY_JS = r"""
var COMPILER = "gcc-13.2.0-c";   // if this ever 400s, fall back to "gcc-head"
var el = function(id){return document.getElementById(id);};

TPL.forEach(function(t,i){
  var o = document.createElement("option");
  o.value = i; o.textContent = "Exp " + t.n + " — " + t.title + " (" + t.file + ")";
  el("tpl").appendChild(o);
});

function loadTemplate(i){
  var t = TPL[i];
  el("code").value = t.code;
  el("stdin").value = t.stdin || "";
}
el("tpl").onchange = function(){ loadTemplate(+el("tpl").value); };
el("clear").onclick = function(){
  el("code").value = "/* Exp X — write it from memory, then run.\n   compile: gcc x.c   run: ./a.out */\n\n#include <stdio.h>\n\nint main() {\n    \n    return 0;\n}\n";
  el("stdin").value = "";
  el("out").textContent = "Blank file. Type your version and press Run.";
};
el("run").onclick = function(){ run(); };

function run(){
  var code = el("code").value, stdin = el("stdin").value;
  if(!code.trim()){ el("out").textContent = "Nothing to compile."; return; }
  el("out").textContent = "Compiling…";
  el("status").textContent = "";
  el("run").disabled = true;

  // The public sandbox occasionally refuses to spawn a container
  // ("OCI runtime error: crun: clone: Resource temporarily unavailable").
  // That is server-side capacity, not your code — so retry once on another compiler.
  var queue = ["gcc-13.2.0-c", "gcc-head"];

  function attempt(i){
    if(i >= queue.length){
      el("run").disabled = false;
      el("out").textContent = "The sandbox refused to run the program twice (server capacity, not your code).\n\n" +
        "Run it locally instead — copy the source into a file and:\n\n  " +
        (TPL[+el("tpl").value] || {cmd:"gcc prog.c -o prog && ./prog"}).cmd;
      return;
    }
    COMPILER = queue[i];
    el("meta").textContent = COMPILER;
    var body = JSON.stringify({
      compiler: COMPILER,
      code: code,
      stdin: stdin,
      "compiler-option-raw": "-w",
      save: false
    });
    fetch("https://wandbox.org/api/compile.json", {
      method: "POST",
      // text/plain keeps this a "simple" request, so no CORS preflight is needed
      headers: {"Content-Type": "text/plain;charset=UTF-8"},
      body: body
    }).then(function(r){ return r.json(); }).then(function(d){
      var bad = String(d.status) === "126" ||
                /OCI runtime error|Resource temporarily unavailable/i.test(d.program_error || "");
      if(bad && i + 1 < queue.length){ attempt(i + 1); return; }
      el("run").disabled = false;
      render(d);
    }).catch(function(e){
      el("run").disabled = false;
      el("out").textContent = "Network or sandbox error: " + e +
        "\n\nFall back to local: copy the source into a file and run the command from the Lab bench page.";
    });
  }
  attempt(0);
}

function render(d){
  el("run").disabled = false;
  var parts = [];
  var cerr = (d.compiler_error || "").trim();
  if(cerr){ parts.push("COMPILER ERROR\n" + cerr); }
  var cmsg = (d.compiler_message || "").trim();
  if(cmsg){ parts.push("compiler diagnostics\n" + cmsg); }
  var out = d.program_output || "";
  var perr = d.program_error || "";
  parts.push("stdout\n" + (out.length ? out : "(nothing)"));
  if(perr.trim()){ parts.push("stderr\n" + perr); }
  parts.push("exit status: " + d.status + (d.status === "0" ? "  (success)" : "  (non-zero)"));
  el("out").textContent = parts.join("\n\n" + new Array(58).join("-") + "\n\n");
  el("status").innerHTML = d.status === "0" ? '<span class="ok">ran</span>' : '<span class="bad">failed</span>';
}

el("local").onclick = function(){
  var t = TPL[+el("tpl").value] || {file:"prog.c"};
  var cmd = t.cmd || ("gcc " + t.file + " -o prog && ./prog");
  navigator.clipboard && navigator.clipboard.writeText(cmd);
  el("out").textContent = "Local command (copied):\n\n  " + cmd +
    "\n\nRun it from ~/projects/mainproject, or drop your file next to the others and use ./run.sh <n>.";
};

loadTemplate(0);
"""


def build_pages(subject_title, base_css):
    payload = build_payload()
    js_data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    sims_path = os.path.join(ROOT, "compiler-lab", "sims.js")
    stamp = "0"
    if os.path.exists(sims_path):
        import hashlib
        with open(sims_path, "rb") as fh:
            stamp = hashlib.sha256(fh.read()).hexdigest()[:8]

    lab = (LAB_PAGE
           .replace("{{SUBJECT}}", html.escape(subject_title))
           .replace("{{CSS}}", base_css + LAB_CSS)
           .replace("{{DATA}}", js_data)
           .replace("{{SIMSV}}", stamp)
           .replace("{{JS}}", LAB_JS))

    tpl = []
    code = load_code()
    for e in data.EXPS:
        main_file = e["files"][0]
        # the sample input for the playground is the same one the trace uses —
        # it is the program's own header sample, so nothing here is invented
        stdin = "" if e["id"] == "exp1" else e["simdefault"]
        tpl.append({"n": e["n"], "title": e["title"], "file": main_file,
                    "code": code[main_file], "stdin": stdin,
                    "cmd": data.BUILD[e["id"]]})
    tpl_data = json.dumps(tpl, ensure_ascii=False).replace("</", "<\\/")

    play = (PLAY_PAGE
            .replace("{{SUBJECT}}", html.escape(subject_title))
            .replace("{{CSS}}", base_css + PLAY_CSS)
            .replace("{{TPL}}", tpl_data)
            .replace("{{JS}}", PLAY_JS))
    return lab, play


# --------------------------------------------------------------------------- viva page
VIVA_CSS = """
body{padding-bottom:70px}
.vv{max-width:1000px;margin:0 auto;padding:24px 22px 60px}
.vv .head{border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:16px;
  display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.vv .head h1{font-size:1.45rem;margin:0}
.vv .head .sub{color:var(--muted);font-size:12.5px;flex:1}
.vv .head a{font-size:12.5px;color:var(--muted);text-decoration:none}
.vv .head a:hover{color:var(--accent)}
.pipe{display:flex;gap:6px;flex-wrap:wrap;align-items:stretch;margin:12px 0 6px}
.ph{flex:1 1 130px;min-width:120px;border:1px solid var(--line);border-radius:9px;
  background:var(--panel);padding:9px 10px}
.ph b{display:block;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.ph .io{font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-top:3px;line-height:1.4}
.ph .n{font-family:var(--mono);font-size:10px;color:var(--muted);opacity:.7}
.side{margin-top:8px;font-size:12px;color:var(--muted)}
.controls{position:sticky;top:0;z-index:5;background:var(--bg,#fff);padding:10px 0;margin:14px 0 6px;
  display:flex;gap:8px;align-items:center;flex-wrap:wrap;border-bottom:1px solid var(--line)}
.controls input{flex:1 1 220px;min-width:160px;font-family:var(--mono);font-size:12.5px;
  background:var(--code-bg);color:var(--ink);border:1px solid var(--line);border-radius:7px;padding:8px 10px}
.btn{font:600 12px/1 var(--sans);border:1px solid var(--line);background:var(--panel);color:var(--ink);
  border-radius:7px;padding:7px 11px;cursor:pointer}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.p{background:var(--accent);color:#fff;border-color:var(--accent)}
.cnt{font-family:var(--mono);font-size:11.5px;color:var(--muted)}
h2.s{font-size:1.02rem;margin:26px 0 4px;padding-top:8px;border-top:1px solid var(--line)}
h2.s:first-of-type{border-top:none}
.bl{font-size:12.5px;color:var(--muted);margin:0 0 10px}
.q{border:1px solid var(--line);border-radius:9px;margin:6px 0;background:var(--panel);cursor:pointer;
  overflow:hidden}
.q:hover{border-color:var(--accent)}
.q .qq{font-size:13.2px;font-weight:600;padding:9px 12px;line-height:1.4;display:flex;gap:8px}
.q .qq .m{color:var(--accent);flex:0 0 14px;font-family:var(--mono);font-size:11px}
.q .aa{font-size:13px;line-height:1.55;padding:0 12px 10px 34px;color:var(--ink)}
.quiz .aa{display:none}
.quiz .q.open .aa{display:block}
.q.open{background:var(--accent-soft)}
.def{border-left:2px solid var(--accent);padding:7px 0 7px 12px;margin:8px 0;font-size:13px;line-height:1.55}
.def b{display:block;color:var(--accent);font-size:12px;margin-bottom:2px}
.hide{display:none!important}
@media print{.controls{display:none}.quiz .aa{display:block!important}}
"""

VIVA_PAGE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Viva &amp; MCQ — {{SUBJECT}}</title>
<style>{{CSS}}</style>
</head>
<body>
<div class="vv">
  <div class="head">
    <h1>Viva &amp; MCQ notes</h1>
    <span class="sub">Whole course, one line per answer — not just the 11 experiments</span>
    <a href="lab.html">Lab bench</a>
    <a href="index.html">All documents</a>
  </div>

  <div class="pipe">{{PIPES}}</div>
  <div class="side">Every phase reads and writes the <b>symbol table</b>; every phase reports to the
    <b>error handler</b>. Front end = first four (machine-independent). Back end = last two.</div>

  <div class="controls">
    <input id="q" type="search" placeholder="filter — parse tree, yacc, epsilon, quadruple…">
    <button class="btn" id="quiz">Quiz mode: off</button>
    <button class="btn" id="all">Reveal all</button>
    <span class="cnt" id="cnt"></span>
  </div>

  <div id="body">{{BODY}}</div>
</div>
<script>{{JS}}</script>
</body>
</html>
"""

VIVA_JS = r"""
var quiz = false;
var body = document.getElementById('body');
var cards = [].slice.call(body.querySelectorAll('.q'));

function counts(){
  var shown = cards.filter(function(c){return c.offsetParent !== null;}).length;
  var open = cards.filter(function(c){return c.classList.contains('open');}).length;
  document.getElementById('cnt').textContent = shown + ' shown · ' + open + ' revealed';
}

cards.forEach(function(c){
  c.addEventListener('click', function(){
    c.classList.toggle('open');
    counts();
  });
});

document.getElementById('quiz').addEventListener('click', function(){
  quiz = !quiz;
  document.body.classList.toggle('quiz', quiz);
  this.textContent = 'Quiz mode: ' + (quiz ? 'on — click a card to reveal' : 'off');
  this.classList.toggle('p', quiz);
  if(quiz){ cards.forEach(function(c){c.classList.remove('open');}); }
  counts();
});

document.getElementById('all').addEventListener('click', function(){
  var anyClosed = cards.some(function(c){return !c.classList.contains('open');});
  cards.forEach(function(c){ c.classList.toggle('open', anyClosed); });
  document.body.classList.remove('quiz'); quiz = false;
  document.getElementById('quiz').textContent = 'Quiz mode: off';
  document.getElementById('quiz').classList.remove('p');
  counts();
});

document.getElementById('q').addEventListener('input', function(){
  var term = this.value.trim().toLowerCase();
  body.querySelectorAll('h2.s').forEach(function(h){
    var sec = h.nextElementSibling;           //  .bl  (may be empty)
    var list = [];
    var node = h.nextElementSibling;
    while(node && node.tagName !== 'H2'){ list.push(node); node = node.nextElementSibling; }
    var hits = 0;
    list.forEach(function(n){
      if(n.classList.contains('q')){
        var txt = n.textContent.toLowerCase();
        var show = !term || txt.indexOf(term) >= 0;
        n.classList.toggle('hide', !show);
        if(show) hits++;
      }
    });
    var hideSection = term && hits === 0;
    h.classList.toggle('hide', hideSection);
    list.forEach(function(n){ if(n.classList.contains('bl')) n.classList.toggle('hide', hideSection); });
  });
  counts();
});

counts();
"""


def build_viva(subject_title, base_css):
    import compiler_viva_data as vd
    pipes = []
    for i, (name, (inp, outp)) in enumerate(zip(vd.PHASES, vd.PHASE_IO), 1):
        pipes.append('<div class="ph"><span class="n">%d</span><b>%s</b>'
                     '<div class="io">%s → %s</div></div>' %
                     (i, html.escape(name), html.escape(inp), html.escape(outp)))

    parts = []
    for title, blurb, rows in vd.SECTIONS:
        parts.append('<h2 class="s">%s</h2>' % html.escape(title))
        parts.append('<p class="bl">%s</p>' % html.escape(blurb) if blurb else "")
        for q, a in rows:
            parts.append('<div class="q"><div class="qq"><span class="m">▸</span><span>%s</span></div>'
                         '<div class="aa">%s</div></div>' % (html.escape(q), html.escape(a)))

    parts.append('<h2 class="s">9. Say this if grilled</h2>')
    parts.append('<p class="bl">Eight sentences that fit almost any question — memorise the shape, '
                 'not the words.</p>')
    for q, a in vd.DEFENCE:
        parts.append('<div class="def"><b>%s</b>%s</div>' % (html.escape(q), html.escape(a)))

    return (VIVA_PAGE
            .replace("{{SUBJECT}}", html.escape(subject_title))
            .replace("{{CSS}}", base_css + VIVA_CSS)
            .replace("{{PIPES}}", "".join(pipes))
            .replace("{{BODY}}", "\n".join(parts))
            .replace("{{JS}}", VIVA_JS))
