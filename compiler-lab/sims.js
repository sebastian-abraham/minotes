/* Compiler Lab — algorithm simulators.
   Each sim is a PURE function: input string -> array of frames.
   frame = { note: "what just happened, in words",
             state: "HTML of the machine state",
             code:  ["anchor substring", ...]   // lines to highlight in the C pane
           }
   The anchors are substrings of the real source files, resolved to line numbers
   by the page (see anchors map emitted next to the code).                          */

var esc = function (s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
};

function kv(label, value) {
  return '<div class="kv"><span class="k">' + esc(label) + '</span><span class="v">' +
         esc(value) + "</span></div>";
}

function box(title, body) {
  return '<div class="sbox"><div class="sbox-t">' + esc(title) + "</div>" +
         '<div class="sbox-b">' + body + "</div></div>";
}

function stackHtml(arr, empty) {
  if (!arr.length) return '<span class="dim">' + esc(empty || "empty") + "</span>";
  return arr.map(function (x, i) {
    return '<span class="cell' + (i === arr.length - 1 ? " top" : "") + '">' + esc(x) + "</span>";
  }).join("");
}

function setHtml(arr) {
  if (!arr.length) return '<span class="dim">∅</span>';
  return "{" + arr.map(function (x) { return "q" + x; }).join(" ") + "}";
}

function table(head, rows) {
  var h = "<table class='stbl'><tr>" + head.map(function (x) {
    return "<th>" + esc(x) + "</th>";
  }).join("") + "</tr>";
  rows.forEach(function (r) {
    h += "<tr>" + r.map(function (c) {
      return "<td" + (c && c.cell ? ' class="hi"' : "") + ">" + (c && c.v !== undefined ? c.v : c) + "</td>";
    }).join("") + "</tr>";
  });
  return h + "</table>";
}

var SIMS = {};

/* ---------------------------------------------------------------- 1. scanner */
SIMS.scan = function (src) {
  var KW = ["int", "float", "char", "if", "else", "while", "for", "return", "void",
            "break", "continue", "double", "main"];
  var f = [], i = 0, out = [];
  f.push({ note: "fgetc() reads one character at a time. Blanks, tabs and newlines are skipped " +
                 "before anything else is classified.",
           state: kv("characters read", 0) + box("tokens so far", '<span class="dim">none</span>'),
           code: ["while ((ch = fgetc(fp)) != EOF)", "ch == ' ' || ch == '\\t' || ch == '\\n'"] });

  while (i < src.length) {
    var ch = src[i];
    if (ch === " " || ch === "\t" || ch === "\n") { i++; continue; }

    if (ch === "/" && src[i + 1] === "/") {
      var j = i; while (j < src.length && src[j] !== "\n") j++;
      f.push({ note: "Two characters '/' '/' — that is a comment. Skip to the newline. The lookahead " +
                     "character was read with a second fgetc, so it is already consumed.",
               state: kv("skipped", src.slice(i, j)), code: ["if (next == '/')"] });
      i = j; continue;
    }
    if (ch === "/" && src[i + 1] === "*") {
      var k = i + 2; while (k < src.length - 1 && !(src[k] === "*" && src[k + 1] === "/")) k++;
      f.push({ note: "Multi-line comment: scan forward until the pair '*' '/' appears, tracking the " +
                     "previous character (prev).",
               state: kv("skipped", src.slice(i, k + 2)), code: ["prev == '*' && ch == '/'"] });
      i = k + 2; continue;
    }

    var tok, kind;
    if (/[A-Za-z_]/.test(ch)) {
      var s = i; while (i < src.length && /[A-Za-z0-9_]/.test(src[i])) i++;
      tok = src.slice(s, i); kind = KW.indexOf(tok) >= 0 ? "Keyword" : "Identifier";
      out.push(kind + " : " + tok);
      f.push({ note: (kind === "Keyword" ? "The buffer matches an entry of the keyword array, so " +
                     "isKeyword() returned 1." : "The buffer is not in the keyword list, so it is an " +
                     "Identifier.") + " The character that ended the token was PUSHED BACK with ungetc.",
               state: kv("buffered", tok) + box("tokens so far", "<pre>" + esc(out.join("\n")) + "</pre>"),
               code: kind === "Keyword"
                 ? ["if (isalpha(ch) || ch == '_')", "ungetc(ch, fp)", "if (isKeyword(buffer))"]
                 : ["if (isalpha(ch) || ch == '_')", "ungetc(ch, fp)", "if (isKeyword(buffer))"] });
    } else if (/[0-9]/.test(ch)) {
      var d = i; while (i < src.length && /[0-9]/.test(src[i])) i++;
      tok = src.slice(d, i); kind = "Number";
      out.push(kind + " : " + tok);
      f.push({ note: "Digits are collected while isdigit() holds; the terminator is pushed back too.",
               state: kv("buffered", tok) + box("tokens so far", "<pre>" + esc(out.join("\n")) + "</pre>"),
               code: ["else if (isdigit(ch))", "ungetc(ch, fp)"] });
    } else if ("+-*=<>!%".indexOf(ch) >= 0) {
      i++; kind = "Operator"; out.push(kind + " : " + ch);
      f.push({ note: "One character, and it is in the operator set — strchr() found it. No lookahead needed.",
               state: kv("char", ch) + box("tokens so far", "<pre>" + esc(out.join("\n")) + "</pre>"),
               code: ['strchr("+-*=<>!%", ch)'] });
    } else if ("(){}[];,.".indexOf(ch) >= 0) {
      i++; kind = "Symbol"; out.push(kind + " : " + ch);
      f.push({ note: "In the symbol set — printed and dropped.",
               state: kv("char", ch) + box("tokens so far", "<pre>" + esc(out.join("\n")) + "</pre>"),
               code: ['strchr("(){}[];,.", ch)'] });
    } else {
      i++;
      f.push({ note: "None of the four tests matched: this character is silently ignored by this " +
                     "scanner — a real limitation, not a feature.",
               state: kv("char", ch), code: ["else if (strchr"] });
    }
  }
  f.push({ note: "EOF: the loop ends, fclose(fp) runs. " + out.length + " tokens classified.",
           state: box("all tokens", "<pre>" + esc(out.join("\n")) + "</pre>"),
           code: ["fclose(fp)"] });
  return f;
};

/* ------------------------------------------------------------ 2/3. lex rules */
SIMS.lex = function (src) {
  var rules = [
    { re: /^(int|float|char|double|void|if|else|while|for|return|break|continue|main)\b/,
      label: "Keyword", code: '"int"|"float"|"char"' },
    { re: /^[0-9]+/, label: "Number", code: "[0-9]+" },
    { re: /^[a-zA-Z_][a-zA-Z0-9_]*/, label: "Identifier", code: "[a-zA-Z_][a-zA-Z0-9_]*" },
    { re: /^(==|!=|<=|>=|=|<|>|\+|-|\*|\/)/, label: "Operator", code: '"=="|"!="' },
    { re: /^[\[\](){};,]/, label: "Special Symbol", code: '"["|"]"|"("' },
    { re: /^[ \t\n]+/, label: "skip", code: "[ \\t\\n]+" },
    { re: /^[^]/, label: "Unknown", code: ".    { printf" }
  ];
  var f = [], i = 0, out = [];
  f.push({ note: "flex builds ONE DFA from all seven rules. At each position it tries every rule and " +
                 "keeps the LONGEST match; on a tie the rule written first wins.",
           state: box("rules, in order", "<pre>1 keyword\n2 number\n3 identifier\n4 operator\n" +
                      "5 special symbol\n6 whitespace (no action)\n7 anything else</pre>"),
           code: ['"int"|"float"|"char"'] });
  while (i < src.length) {
    var best = null;
    for (var r = 0; r < rules.length; r++) {
      var m = src.slice(i).match(rules[r].re);
      if (m && (!best || m[0].length > best.len)) best = { len: m[0].length, text: m[0], rule: r };
    }
    if (!best) break;
    var tok = best.text, rule = rules[best.rule];
    i += best.len;
    var why = rule.label === "skip"
      ? "Whitespace matched rule 6, whose action is empty — consumed but nothing printed."
      : rule.label + " — longest match at this position, so this rule's action runs. yytext = '" +
        tok + "', yyleng = " + tok.length + ".";
    if (rule.label !== "skip") out.push(rule.label + " : " + tok);
    f.push({ note: why, state: kv("matched", tok) + kv("rule", (best.rule + 1) + " of 7") +
              box("output", "<pre>" + esc(out.join("\n")) + "</pre>"),
             code: [rule.code] });
  }
  f.push({ note: "End of input: yylex() calls yywrap(); returning 1 means 'no more files', so scanning stops.",
           state: box("output", "<pre>" + esc(out.join("\n") || "(nothing)") + "</pre>"),
           code: ["int yywrap()"] });
  return f;
};

SIMS.count = function (src) {
  var lines = 0, words = 0, chars = 0, f = [], i = 0, out = [];
  f.push({ note: "Three counters live in the definitions section as globals, so every rule's action can " +
                 "change them. yyleng is the length of the text the rule just matched.",
           state: kv("lines", 0) + kv("words", 0) + kv("chars", 0),
           code: ["int lines = 0;", "int words = 0;", "int characters = 0;"] });
  var rules = [
    { re: /^\n/, name: "newline", fn: function (t) { lines++; chars++; }, code: "\\n              { lines++; characters++; }" },
    { re: /^[ \t]+/, name: "blanks/tabs", fn: function (t) { chars += t.length; }, code: "[ \\t]+          { characters += yyleng; }" },
    { re: /^[a-zA-Z0-9]+/, name: "word", fn: function (t) { words++; chars += t.length; }, code: "[a-zA-Z0-9]+    { words++; characters += yyleng; }" },
    { re: /^[^]/, name: "other char", fn: function (t) { chars++; }, code: ".               { characters++; }" }
  ];
  while (i < src.length) {
    var hit = null;
    for (var r = 0; r < rules.length; r++) {
      var m = src.slice(i).match(rules[r].re);
      if (m) { hit = { m: m, r: rules[r] }; break; }
    }
    if (!hit) break;
    hit.r.fn(hit.m[0]);
    i += hit.m[0].length;
    out.push(hit.r.name + " '" + hit.m[0].replace(/\n/g, "\\n") + "'  →  lines=" + lines +
             " words=" + words + " chars=" + chars);
    f.push({ note: "Rule matched: " + hit.r.name + ". It updates only what it consumed — that is why " +
                   "characters is touched by EVERY rule.",
             state: kv("lines", lines) + kv("words", words) + kv("characters", chars),
             code: [hit.r.code] });
  }
  f.push({ note: "Ctrl+D sends end-of-file; yylex() returns and main() prints the three counters.",
           state: kv("lines", lines) + kv("words", words) + kv("characters", chars),
           code: ['printf("\\nNumber of lines'] });
  return f;
};

/* ---------------------------------------------------------------- 4. yacc id */
SIMS.yacc = function (src) {
  var f = [], stack = [], i = 0;
  f.push({ note: "yyparse() is a state machine built from the grammar. LEX returns one token at a time; " +
                 "yacc shifts it and, when the top of its stack matches a rule's right-hand side, reduces.",
           state: box("stack", '<span class="dim">empty</span>') +
                  kv("grammar", "identifier : LETTER | identifier LETTER | identifier DIGIT"),
           code: ["%token LETTER DIGIT"] });
  while (i < src.length && src[i] !== "\n") {
    var ch = src[i];
    var isLetter = /[A-Za-z]/.test(ch), isDigit = /[0-9]/.test(ch);
    if (!isLetter && !isDigit) {
      f.push({ note: "Character '" + ch + "' is returned as itself by the lex rule '.', and no grammar rule " +
                     "accepts it → syntax error → yyerror() prints Invalid Identifier.",
               state: kv("rejected at", "'" + ch + "'"), code: ["yyerror"] });
      return f;
    }
    if (isDigit && stack.length === 0) {
      f.push({ note: "'" + ch + "' is a DIGIT, but the only rule that can START an identifier is " +
                     "identifier : LETTER. No derivation exists → yyerror(). This is exactly why 123abc fails.",
               state: kv("token", "DIGIT") + kv("stack", "empty") + kv("verdict", "Invalid Identifier"),
               code: ["      LETTER", "yyerror"] });
      return f;
    }
    var tok = isLetter ? "LETTER" : "DIGIT";
    stack.push("id");
    i++;
    f.push({ note: "LEX returned " + tok + " for '" + ch + "'. yacc pushes it, then immediately reduces " +
                   "to identifier — 'an identifier followed by one more " +
                   (isLetter ? "letter" : "digit") + " is still an identifier'. That is the LEFT RECURSION.",
             state: kv("token", tok) + kv("stack", "identifier") ,
             code: isLetter ? ["| identifier LETTER"] : ["| identifier DIGIT"] });
  }
  if (stack.length === 0) {
    f.push({ note: "Empty input: nothing to derive from, so the start rule cannot match.",
             state: kv("verdict", "Invalid Identifier"), code: ["yyerror"] });
    return f;
  }
  f.push({ note: "The lexer returns '\\n' for the newline, and the start rule is identifier '\\n' — so the " +
                 "reduction succeeds and the action prints Valid Identifier.",
           state: kv("stack", "id '\\n' → start") + kv("verdict", "Valid Identifier"),
           code: ["identifier '\\n'   { printf"] });
  return f;
};

/* ------------------------------------------------------------ 5. e-closure */
SIMS.eclosure = function (input) {
  var nums = input.trim().split(/\s+/).map(Number);
  var n = nums[0], m = [], f = [], i, j;
  if (!(n > 0 && n <= 20)) return [{ note: "Input must start with the number of states n (1–20).", state: "", code: [] }];
  for (i = 0; i < n; i++) { m.push(nums.slice(1 + i * n, 1 + (i + 1) * n)); }
  var closure = [], depth = 0, calls = 0;
  for (i = 0; i < n; i++) { closure.push(new Array(n).fill(0)); }

  function grid() {
    var head = [""], a, b; for (a = 0; a < n; a++) head.push("q" + a);
    var rows = [];
    for (a = 0; a < n; a++) {
      var r = ["<b>q" + a + "</b>"];
      for (b = 0; b < n; b++) r.push({ v: closure[a][b], cell: closure[a][b] === 1 });
      rows.push(r);
    }
    return table(head, rows);
  }

  function rec(state, current) {
    closure[state][current] = 1;
    calls++;
    f.push({ note: "findClosure(state=q" + state + ", current=q" + current + "): mark closure[q" +
                   state + "][q" + current + "] = 1 — q" + current + " is in the closure. Then look for " +
                   "ε-moves OUT of q" + current + ".",
             state: box("closure matrix", grid()) + kv("recursion depth", depth),
             code: ["closure[state][current] = 1;"] });
    for (var k = 0; k < n; k++) {
      if (m[current][k] === 1) {
        if (closure[state][k] === 0) {
          f.push({ note: "ε-move q" + current + " → q" + k + " exists and q" + k + " is not yet in this " +
                         "closure, so recurse. This is the free teleport.",
                   state: box("closure matrix", grid()) + kv("following", "ε: q" + current + " → q" + k),
                   code: ["epsilon[current][i] == 1 && closure[state][i] == 0", "findClosure(state, i);"] });
          depth++; rec(state, k); depth--;
        } else {
          f.push({ note: "ε-move q" + current + " → q" + k + " exists, but q" + k + " is ALREADY marked. " +
                         "Skipping it is what stops a cycle of ε-moves from recursing forever.",
                   state: box("closure matrix", grid()) + kv("skipped", "q" + k + " (visited)"),
                   code: ["closure[state][i] == 0"] });
        }
      }
    }
    f.push({ note: "All ε-moves out of q" + current + " examined; this call returns.",
             state: box("closure matrix", grid()), code: ["}", "}"] });
  }

  f.push({ note: "Read n and the n×n ε matrix. ε[i][j] = 1 means an ε-move from i to j.",
           state: box("ε matrix", (function () {
             var head = [""]; for (i = 0; i < n; i++) head.push("q" + i);
             var rows = [];
             for (i = 0; i < n; i++) {
               var r = ["<b>q" + i + "</b>"];
               for (j = 0; j < n; j++) r.push({ v: m[i][j], cell: m[i][j] === 1 });
               rows.push(r);
             }
             return table(head, rows);
           })()),
           code: ['scanf("%d", &n)'] });

  for (i = 0; i < n; i++) {
    f.push({ note: "main loops s = 0..n-1 and calls findClosure(s, s) — the state is always seeded with itself.",
             state: kv("computing closure of", "q" + i), code: ["findClosure(i, i);"] });
    rec(i, i);
  }
  var lines = [];
  for (i = 0; i < n; i++) {
    var set = []; for (j = 0; j < n; j++) if (closure[i][j]) set.push(j);
    lines.push("E-closure(q" + i + ") = { " + set.map(function (x) { return "q" + x; }).join(" ") + " }");
  }
  f.push({ note: "Print the 1-entries rowwise. " + calls + " calls to findClosure in total.",
           state: box("result", "<pre>" + esc(lines.join("\n")) + "</pre>"),
           code: ['printf("E-closure(q%d) = { "'] });
  return f;
};

/* ------------------------------------------------------------ 6. e-NFA -> NFA */
SIMS.enfa = function (input) {
  var t = input.trim().split(/\s+/).map(String), p = 0, f = [];
  function next() { return t[p++]; }
  var n = +next(), m = +next(), syms = [];
  if (!(n > 0 && m > 0)) return [{ note: "Input must be the program's own format: n, m, then m symbols.", state: "", code: [] }];
  for (var i = 0; i < m; i++) syms.push(next());
  var eclose = [], ecount = [];
  for (i = 0; i < n; i++) {
    ecount.push(+next()); var s = [];
    for (var j = 0; j < ecount[i]; j++) s.push(+next());
    eclose.push(s);
  }
  var trans = [];
  for (i = 0; i < n; i++) {
    trans.push([]);
    for (j = 0; j < m; j++) {
      var c = +next(), s2 = [];
      for (var k = 0; k < c; k++) s2.push(+next());
      trans[i].push(s2);
    }
  }
  f.push({ note: "The ε-closure of every state is GIVEN as input here — experiment 5 is what computes it. " +
                 "That pipeline (5 → 6 → 7) is what the examiner asks about.",
           state: box("ε-closures", "<pre>" + eclose.map(function (s, x) {
             return "E-closure(q" + x + ") = " + setHtml(s);
           }).join("\n") + "</pre>"),
           code: ["scanf(\"%d\", &ecount[i]);"] });

  for (i = 0; i < n; i++) {
    for (var a = 0; a < m; a++) {
      var result = [];
      f.push({ note: "δ'(q" + i + "," + syms[a] + "): start from ε-closure(q" + i + ") = " + setHtml(eclose[i]) +
                     " — you may teleport freely BEFORE reading the symbol.",
             state: kv("working result", setHtml(result)), code: ["for (k = 0; k < ecount[i]; k++)"] });
      eclose[i].forEach(function (st) {
        f.push({ note: "From q" + st + ", read '" + syms[a] + "' → δ(q" + st + "," + syms[a] + ") = " +
                       setHtml(trans[st][a]) + ".",
                 state: kv("state", "q" + st) + kv("on symbol", syms[a]) +
                        kv("destinations", "{" + trans[st][a].map(function (x) { return "q" + x; }).join(" ") + "}"),
                 code: ["int tcount = trans[state][j][0];"] });
        trans[st][a].forEach(function (nxt) {
          eclose[nxt].forEach(function (q) {
            if (result.indexOf(q) < 0) result.push(q);
          });
          f.push({ note: "After arriving at q" + nxt + ", teleport freely again: add ε-closure(q" + nxt + ") = " +
                         setHtml(eclose[nxt]) + ", skipping duplicates with addState().",
                   state: kv("result now", setHtml(result)),
                   code: ["for (int y = 0; y < ecount[next]; y++)", "addState(result, &rcount, eclose[next][y]);"] });
        });
      });
      f.push({ note: "δ'(q" + i + "," + syms[a] + ") = " + setHtml(result) +
                     ". That is the formula: ε-closure( ∪ over p ∈ ε-closure(q) of δ(p,a) ).",
             state: kv("δ'", setHtml(result)), code: ['printf("d\'(q%d,%c) = { "'] });
    }
  }
  return f;
};

/* ---------------------------------------------------------- 7. subset construction */
SIMS.subset = function (input) {
  var t = input.trim().split(/\s+/).map(String), p = 0, f = [];
  function next() { return t[p++]; }
  var n = +next(), m = +next(), syms = [];
  for (var i = 0; i < m; i++) syms.push(next());
  var nfa = [];
  for (i = 0; i < n; i++) {
    nfa.push([]);
    for (var j = 0; j < m; j++) {
      var c = +next(), s = [];
      for (var k = 0; k < c; k++) s.push(+next());
      nfa[i].push(s);
    }
  }
  var states = [[0]], dfa = {}, cur = 0;
  function key(s) { return s.join(","); }
  function label(s) { return "{" + s.map(function (x) { return "q" + x; }).join(",") + "}"; }
  function dfaTable(hiRow) {
    var head = ["DFA state"].concat(syms), rows = [];
    states.forEach(function (s, idx) {
      var r = [label(s)];
      for (var a = 0; a < m; a++) {
        var d = dfa[key(s) + "|" + a];
        r.push({ v: d === undefined ? "?" : label(states[d]), cell: hiRow === idx });
      }
      rows.push(r);
    });
    return table(head, rows);
  }
  f.push({ note: "Subset construction starts with ONE DFA state: {q0}. Every DFA state is a SET of NFA " +
                 "states — that is the whole idea.",
           state: box("DFA so far", dfaTable()), code: ["dfaStates[0][0] = 0;", "totalDFA = 1;"] });
  while (cur < states.length) {
    var s = states[cur];
    for (var a = 0; a < m; a++) {
      var set = [];
      f.push({ note: "Processing DFA state " + label(s) + " on '" + syms[a] + "': take the union of NFA " +
                     "moves from EVERY state in this set.",
             state: box("DFA so far", dfaTable(cur)) + kv("working set", "{ }"),
             code: ["while (current < totalDFA)", "for (int i = 0; i < dfaCount[current]; i++)"] });
      s.forEach(function (st) {
        nfa[st][a].forEach(function (nxt) { if (set.indexOf(nxt) < 0) set.push(nxt); });
      });
      var unsorted = set.slice();
      set.sort(function (x, y) { return x - y; });
      var existed = states.map(key).indexOf(key(set));
      var idx;
      if (existed >= 0) { idx = existed; }
      else { states.push(set); idx = states.length - 1; }
      dfa[key(s) + "|" + a] = idx;
      f.push({ note: "Union = {q" + unsorted.join(",q") + "}".replace("{q}", "{ }") +
                     (existed >= 0
                       ? " Sorted → " + label(set) + ", which ALREADY exists as DFA state " + idx + " — reused, not duplicated."
                       : " Sorted → " + label(set) + " is new, so it becomes DFA state " + idx +
                         " and is appended to the worklist (the loop will reach it)."),
             state: box("DFA so far", dfaTable(cur)) + kv("δ(" + label(s) + "," + syms[a] + ")", label(set)),
             code: existed >= 0
               ? ["int stateIndex = findDFAState(newSet, newCount);", "if (stateIndex == -1){"]
               : ["sortSet(newSet, newCount);", "totalDFA++;"] });
    }
    cur++;
    f.push({ note: "Row " + label(s) + " complete. Move to the next DFA state in the list (index " + cur +
                   " of " + states.length + ").",
             state: box("DFA", dfaTable()), code: ["current++;"] });
  }
  f.push({ note: "Every DFA state processed — " + states.length + " states, and no new sets appeared. " +
                 "The table is printed with each state labelled by its set.",
           state: box("final DFA", dfaTable()), code: ['printf("\\nEquivalent DFA Transition Table:\\n\\n");'] });
  return f;
};

/* ------------------------------------------------------------- 8. FIRST/FOLLOW */
SIMS.fnf = function (input) {
  var prods = input.trim().split(/\s+/).filter(Boolean), f = [];
  var nonterms = [];
  prods.forEach(function (p) { if (nonterms.indexOf(p[0]) < 0) nonterms.push(p[0]); });
  var FIRSTS = {}, FOLLOWS = {};
  function add(set, c) { if (set.indexOf(c) < 0) set.push(c); }

  function first(c, seen) {
    seen = seen || [];
    if (!/[A-Z]/.test(c)) return [c];
    if (seen.indexOf(c) >= 0) return [];
    seen.push(c);
    var out = [];
    for (var i = 0; i < prods.length; i++) {
      if (prods[i][0] !== c) continue;
      var rhs = prods[i].slice(2);
      if (rhs === "#") { add(out, "#"); continue; }
      for (var j = 0; j < rhs.length; j++) {
        var sub = first(rhs[j], seen);
        sub.forEach(function (x) { if (x !== "#") add(out, x); });
        if (sub.indexOf("#") < 0) break;
        if (j === rhs.length - 1) add(out, "#");
      }
    }
    return out;
  }

  f.push({ note: "FIRST(X) asks: which terminals can BE the first symbol of something derived from X? " +
                 "A terminal answers for itself; a non-terminal asks its right-hand sides, in order, until " +
                 "one of them cannot vanish.",
           state: box("grammar", "<pre>" + esc(prods.join("\n")) + "</pre>"),
           code: ["void FIRST(char c, char result[])"] });

  nonterms.forEach(function (N) {
    var s = first(N, []);
    FIRSTS[N] = s;
    var related = prods.filter(function (p) { return p[0] === N; });
    f.push({ note: "FIRST(" + N + "): from rules " + related.map(function (p) { return p.replace("=", " → "); }).join(", ") +
                   " → { " + s.join(" ") + " }.",
             state: box("FIRST so far", "<pre>" + nonterms.map(function (x) {
               return "FIRST(" + x + ") = { " + (FIRSTS[x] || []).join(" ") + " }";
             }).join("\n") + "</pre>"),
             code: ["FIRST(prod[i][j], temp);", "if (!epsilon)", "add(result, '#');"] });
  });

  function follow(A) {
    var out = [];
    if (A === prods[0][0]) add(out, "$");
    for (var i = 0; i < prods.length; i++) {
      var rhs = prods[i].slice(2);
      for (var j = 0; j < rhs.length; j++) {
        if (rhs[j] !== A) continue;
        if (j + 1 < rhs.length) {
          var fx = first(rhs[j + 1], []);
          fx.forEach(function (x) { if (x !== "#") add(out, x); });
          if (fx.indexOf("#") >= 0) {
            if (prods[i][0] !== A) follow(prods[i][0]).forEach(function (x) { add(out, x); });
          }
        } else if (prods[i][0] !== A) {
          follow(prods[i][0]).forEach(function (x) { add(out, x); });
        }
      }
    }
    return out;
  }

  f.push({ note: "'#' in this program means ε — epsilon is painful to type. Now FOLLOW: what can appear " +
                 "immediately AFTER a non-terminal.",
           state: box("grammar", "<pre>" + esc(prods.join("\n")) + "</pre>"),
           code: ["void FOLLOW(char c, char result[])"] });

  nonterms.forEach(function (N) {
    var s = follow(N);
    FOLLOWS[N] = s;
    f.push({ note: "FOLLOW(" + N + ")" + (N === prods[0][0] ? " — it is the start symbol, so '$' is automatic" : "") +
                   " → { " + s.join(" ") + " }. Where the symbol sits at the END of a right-hand side, or the " +
                   "symbol after it can vanish, FOLLOW of the LEFT-HAND side is copied in.",
             state: box("FOLLOW so far", "<pre>" + nonterms.map(function (x) {
               return "FOLLOW(" + x + ") = { " + (FOLLOWS[x] || []).join(" ") + " }";
             }).join("\n") + "</pre>"),
             code: ["if (c == prod[0][0])", "FOLLOW(prod[i][0], temp2);"] });
  });

  f.push({ note: "These two sets fill the LL(1) table: rule A → α goes into cell [A, t] for every t in " +
                 "FIRST(α), and into [A, t] for every t in FOLLOW(A) when α can vanish. That single sentence " +
                 "is why the experiment exists.",
           state: box("FIRST", "<pre>" + nonterms.map(function (x) {
             return "FIRST(" + x + ") = { " + FIRSTS[x].join(" ") + " }";
           }).join("\n") + "</pre>") + box("FOLLOW", "<pre>" + nonterms.map(function (x) {
             return "FOLLOW(" + x + ") = { " + FOLLOWS[x].join(" ") + " }";
           }).join("\n") + "</pre>"),
           code: ['printf("\\nFIRST sets:\\n");'] });
  return f;
};

/* -------------------------------------------------------- 9. recursive descent */
SIMS.rdp = function (src) {
  var s = src.trim(), pos = 0, f = [], depth = 0;
  function ind() { return new Array(depth + 1).join("│  "); }
  function trace(msg, code) {
    f.push({ note: msg, state: kv("pos", pos) + kv("next char", pos < s.length ? "'" + s[pos] + "'" : "END") +
              box("call stack", "<pre>" + ind() + esc(s) + "\n" + ind() + new Array(pos + 1).join(" ") + "^\n" +
                   esc(traceLines[traceLines.length - 1] || "") + "</pre>"),
             code: code });
  }
  var traceLines = [];
  function error() {
    f.push({ note: "No rule applies here → error() prints \"Invalid string\" and calls exit(0). The parse " +
                   "stops immediately; nothing is thrown.",
             state: kv("failed at", "pos " + pos + " ('" + (s[pos] || "END") + "')") +
                    kv("verdict", "Invalid string"), code: ["void error()", "exit(0);"] });
    throw "stop";
  }
  function E() { traceLines.push(ind() + "E( )"); trace("E → T E': call T(), then E'.", ["void E() {"]); depth++; T(); Eprime(); depth--; }
  function Eprime() {
    traceLines.push(ind() + "E'( )");
    if (s[pos] === "+") {
      trace("input[pos] is '+', so the non-ε branch runs: consume it (pos++), then T() and E'() again. " +
            "This is left-to-right chaining of additions.",
            ["if (input[pos] == '+') {", "pos++;"]);
      pos++; depth++; T(); Eprime(); depth--;
    } else {
      trace("input[pos] is NOT '+'. The function returns without consuming anything — THE ABSENCE OF A " +
            "MATCH IS THE ε-PRODUCTION.", ["void Eprime() {"]);
    }
  }
  function T() { traceLines.push(ind() + "T( )"); trace("T → F T': brackets and operands first, then '*'s.", ["void T() {"]); depth++; F(); Tprime(); depth--; }
  function Tprime() {
    traceLines.push(ind() + "T'( )");
    if (s[pos] === "*") {
      trace("'*' found: consume it, then F() and T'(). Because T' sits INSIDE T, every '*' is finished " +
            "before the enclosing '+' can be — that is where precedence comes from.",
            ["if (input[pos] == '*') {"]);
      pos++; depth++; F(); Tprime(); depth--;
    } else {
      trace("Not '*': return. Again, the silent return IS the ε-production.",
            ["void Tprime() {"]);
    }
  }
  function F() {
    traceLines.push(ind() + "F( )");
    if (s[pos] === "i") {
      trace("F sees 'i' — an operand. Consume exactly one symbol and return.", ["if (input[pos] == 'i') {"]);
      pos++;
    } else if (s[pos] === "(") {
      trace("F sees '(' — recurse into E for the whole bracketed expression, then REQUIRE a closing ')'. " +
            "Missing ')' is an immediate error.", ["else if (input[pos] == '(') {"]);
      pos++; depth++; E(); depth--;
      if (s[pos] === ")") { trace("')' present, consume it, close the bracket.", ['if (input[pos] == \')\')']); pos++; }
      else error();
    } else error();
  }

  f.push({ note: "One function per non-terminal. E calls T, T calls F — the call stack is the parse tree. " +
                 "A single shared index pos always points at the next unconsumed symbol.",
           state: kv("input", s) + kv("pos", 0), code: ["void E()", "char input[100];", "int pos = 0;"] });
  try { E(); } catch (e) { return f; }
  if (pos === s.length) {
    f.push({ note: "Every symbol was consumed and pos sits on '\\0' — accepted.",
             state: kv("pos", pos) + kv("verdict", "String is accepted"), code: ["if (input[pos] == '\\0')"] });
  } else {
    f.push({ note: "Parsing finished but input remains ('" + s.slice(pos) + "') — the string is NOT a full " +
                   "derivation of E.",
             state: kv("leftover", s.slice(pos)) + kv("verdict", "String is rejected"),
             code: ['printf("String is rejected\\n");'] });
  }
  return f;
};

/* ------------------------------------------------------------ 10. shift-reduce */
SIMS.srp = function (src) {
  var s = src.trim(), stack = [], f = [];
  function show(extra) {
    return box("stack (bottom → top)", stackHtml(stack)) +
           kv("top index", stack.length - 1) + (extra ? kv("note", extra) : "");
  }
  function reduceOnce() {
    var n = stack.length;
    if (n >= 1 && stack[n - 1] === "i") {
      stack[n - 1] = "E";
      f.push({ note: "Top of stack is 'i' → reduce E → i.", state: show("reduced E → i"),
               code: ['stack[top] == \'i\''] });
      return true;
    }
    if (n >= 3 && stack[n - 3] === "E" && stack[n - 2] === "+" && stack[n - 1] === "E") {
      stack.length = n - 3; stack.push("E");
      f.push({ note: "Top three symbols are E + E → reduce E → E+E (and print it).",
               state: show("reduced E → E+E"), code: ["stack[top - 1] == '+'"] });
      return true;
    }
    if (n >= 3 && stack[n - 3] === "E" && stack[n - 2] === "*" && stack[n - 1] === "E") {
      stack.length = n - 3; stack.push("E");
      f.push({ note: "Top three are E * E → reduce E → E*E.",
               state: show("reduced E → E*E"), code: ["stack[top - 1] == '*'"] });
      return true;
    }
    return false;
  }
  f.push({ note: "Bottom-up: the parser pushes input symbols (SHIFT) and replaces right-hand sides on top of " +
                 "the stack with their left-hand side (REDUCE). Note reduce() performs AT MOST ONE reduction " +
                 "per call — main() calls it once after each shift. That single detail is what makes this " +
                 "trace come out in the order it does.",
           state: show(), code: ["char stack[50], input[50];"] });
  for (var i = 0; i < s.length; i++) {
    stack.push(s[i]);
    f.push({ note: "SHIFT '" + s[i] + "'. After every push the code writes stack[top+1]='\\0' so printf can " +
                   "print the stack as a string.",
             state: show(), code: ["stack[++top] = input[i];", "stack[top + 1] = '\\0';"] });
    reduceOnce();
  }
  f.push({ note: "Input exhausted. main() now keeps calling reduce() while top > 0, breaking as soon as a call " +
                 "leaves top unchanged — the oldtop == top test, the only thing stopping an infinite loop.",
           state: show(), code: ["while (top > 0)", "if (oldtop == top)"] });
  while (stack.length - 1 > 0) {
    var before = stack.length;
    reduceOnce();
    if (stack.length === before) break;
  }
  var ok = stack.length === 1 && stack[0] === "E";
  f.push({ note: ok ? "Exactly one symbol left on the stack and it is E → String Accepted."
                    : "The stack is not a single E → String Rejected.",
           state: show() + kv("verdict", ok ? "String Accepted" : "String Rejected"),
           code: ["if (top == 0 && stack[0] == 'E')"] });
  return f;
};

/* ------------------------------------------------- 11. three-address code */
SIMS.tac = function (src) {
  var e = src.trim().replace(/\s+/g, ""), operands = [], ops = [], temp = 1, out = [], f = [];
  function prec(c) { return (c === "*" || c === "/") ? 2 : (c === "+" || c === "-") ? 1 : 0; }
  function show(extra) {
    return box("operand stack", stackHtml(operands)) + box("operator stack", stackHtml(ops)) +
           box("emitted code", "<pre>" + esc(out.join("\n") || "(nothing yet)") + "</pre>") +
           kv("next temporary", "t" + temp) + (extra ? kv("note", extra) : "");
  }
  f.push({ note: "Two stacks instead of recursion: one holds values, one holds pending operators. Precedence " +
                 "* / = 2, + - = 1.",
           state: show(), code: ["int precedence(char op) {"] });
  for (var i = 0; i < e.length; i++) {
    var ch = e[i];
    if (/[a-zA-Z0-9]/.test(ch)) {
      operands.push(ch);
      f.push({ note: "'" + ch + "' is an operand (isalnum) — push it and wait for an operator.",
               state: show(), code: ["if (isalnum(expr[i])) {"] });
      continue;
    }
    while (ops.length && prec(ops[ops.length - 1]) >= prec(ch)) {
      var op = ops.pop(), b = operands.pop(), a = operands.pop();
      var t = "t" + temp;
      out.push(t + " = " + a + " " + op + " " + b);
      operands.push(t); temp++;
      f.push({ note: "precedence(top of operator stack) = " + prec(op) + " >= precedence('" + ch + "') = " +
                     prec(ch) + ", so reduce NOW: pop b='" + b + "' first, then a='" + a + "' (the second pop is " +
                     "the LEFT operand), emit " + t + " = " + a + " " + op + " " + b + ", push " + t + ".",
               state: show(), code: ["precedence(operators[opTop]) >= precedence(expr[i])",
                                     "strcpy(b, operands[top--]);", "strcpy(a, operands[top--]);"] });
    }
    ops.push(ch);
    f.push({ note: "Now push the incoming operator '" + ch + "' — it waits for its right operand.",
             state: show(), code: ["operators[++opTop] = expr[i];"] });
  }
  while (ops.length) {
    var op2 = ops.pop(), b2 = operands.pop(), a2 = operands.pop(), t2 = "t" + temp;
    out.push(t2 + " = " + a2 + " " + op2 + " " + b2);
    operands.push(t2); temp++;
    f.push({ note: "End of expression: drain the operator stack, one reduction per operator.",
             state: show(), code: ["while (opTop >= 0) {"] });
  }
  f.push({ note: "Result: " + out.length + " three-address instructions, each with at most ONE operator — " +
                 "that is what a machine can execute directly.",
           state: show(), code: ['printf("\\nIntermediate Code:\\n");'] });
  return f;
};

if (typeof module !== "undefined") module.exports = SIMS;
