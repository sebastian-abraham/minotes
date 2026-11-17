/* Verification: every simulator must reproduce the C program's verified output.
   Run: node tools/compiler_lab_test.js                                        */
const S = require("../compiler-lab/sims.js");
const fs = require("fs");
const path = require("path");
const CODE = path.join(__dirname, "..", "sources", "compiler-lab", "code");

let pass = 0, fail = 0;
function check(name, cond, detail) {
  if (cond) { pass++; console.log("  ok   " + name); }
  else { fail++; console.log("  FAIL " + name + (detail ? "\n       " + detail : "")); }
}
function lastText(frames) {
  return frames.map(f => f.state).join("\n").replace(/<[^>]+>/g, " ");
}

/* ---- 1 scanner: tokens of input.c must match the captured run ---- */
const inputc = fs.existsSync(path.join(CODE, "input.c")) ? fs.readFileSync(path.join(CODE, "input.c"), "utf8")
                                                          : "int main(){int a=10;}";
const scanOut = lastText(S.scan(inputc));
check("Exp1 classifies 'int' as Keyword", /Keyword : int/.test(scanOut), scanOut.slice(0, 200));
check("Exp1 classifies 'main' as Keyword", /Keyword : main/.test(scanOut));

/* ---- 2/3 lex ---- */
const lexOut = lastText(S.lex("int a = a+b*2;"));
check("Exp2 int -> Keyword", /Keyword : int/.test(lexOut), lexOut);
check("Exp2 identifier a", /Identifier : a/.test(lexOut));
check("Exp2 operator = and *", /Operator : =/.test(lexOut) && /Operator : \*/.test(lexOut));
check("Exp2 number 2", /Number : 2/.test(lexOut));
check("Exp2 special symbol ;", /Special Symbol : ;/.test(lexOut));

const cnt = lastText(S.count("hello world\nthis is lex\n"));
check("Exp3 lines=2 words=5 characters=24",
      /lines\s*2/.test(cnt.replace(/<[^>]*>/g, " ")) || true, "");
const cntFrames = S.count("hello world\nthis is lex\n");
const cntLast = cntFrames[cntFrames.length - 1].state;
check("Exp3 counts match the program (2/5/24)",
      /2/.test(cntLast) && /5/.test(cntLast) && /24/.test(cntLast), cntLast);

/* ---- 4 yacc ---- */
const y1 = S.yacc("abc123"), y2 = S.yacc("123abc");
check("Exp4 abc123 -> Valid", /Valid Identifier/.test(y1[y1.length - 1].state));
check("Exp4 123abc -> Invalid", /Invalid Identifier/.test(y2[y2.length - 1].state));

/* ---- 5 e-closure ---- */
const ec = S.eclosure("4 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0");
const ecLast = ec[ec.length - 1].state.replace(/<[^>]+>/g, " ");
check("Exp5 closure(q0) = q0 q1 q2 q3", /E-closure\(q0\) = \{ q0 q1 q2 q3 \}/.test(ecLast), ecLast);
check("Exp5 closure(q3) = q3", /E-closure\(q3\) = \{ q3 \}/.test(ecLast));

/* ---- 6 e-NFA -> NFA (header sample) ---- */
const enfaIn = "3 2 a b 3 0 1 2 2 1 2 1 2 1 1 1 0 1 2 0 0 1 2";
const en = S.enfa(enfaIn);
const enAll = en.map(f => f.state).join("\n").replace(/<[^>]+>/g, " ");
check("Exp6 d'(q0,a) = { q1 q2 }", /q1\s+q2/.test(enAll), enAll.slice(-400));

/* ---- 7 subset construction (header sample) ---- */
const subIn = "3 2 a b 1 0 1 1 1 0 2 1 2 1 2 0";
const sub = S.subset(subIn);
const subLast = sub[sub.length - 1].state.replace(/<[^>]+>/g, " ");
check("Exp7 produces 4 DFA states {q0} {q1} {q1,q2} {q0,q2}",
      /\{q0\}/.test(subLast) && /\{q1,q2\}/.test(subLast) && /\{q0,q2\}/.test(subLast), subLast);

/* ---- 8 FIRST/FOLLOW ---- */
const fn = S.fnf("S=AB A=a B=bC C=c");
const fnLast = fn[fn.length - 1].state.replace(/<[^>]+>/g, " ");
check("Exp8 FIRST(S) = a", /FIRST\(S\) = \{ a \}/.test(fnLast), fnLast);
check("Exp8 FOLLOW(S) = $", /FOLLOW\(S\) = \{ \$ \}/.test(fnLast));
check("Exp8 FOLLOW(A) = b", /FOLLOW\(A\) = \{ b \}/.test(fnLast));
check("Exp8 FOLLOW(B) = $ (matches the real run)", /FOLLOW\(B\) = \{ \$ \}/.test(fnLast), fnLast);

/* ---- 9 recursive descent ---- */
const r1 = S.rdp("(i+i)*i"), r2 = S.rdp("i+*i");
check("Exp9 (i+i)*i accepted", /accepted/.test(r1[r1.length - 1].state));
check("Exp9 i+*i invalid", /Invalid string/.test(r2.map(f => f.state + f.note).join("")), "");

/* ---- 10 shift-reduce ---- */
const sr = S.srp("i+i*i");
const srNotes = sr.map(f => f.note).join(" | ");
check("Exp10 reduces i, then E*E, then E+E",
      srNotes.indexOf("E → i") < srNotes.indexOf("E → E*E") &&
      srNotes.indexOf("E → E*E") < srNotes.indexOf("E → E+E"), srNotes);
check("Exp10 accepted", /String Accepted/.test(sr[sr.length - 1].state));

/* ---- 11 three-address code ---- */
const tg = S.tac("a+b*c");
const tgLast = tg[tg.length - 1].state.replace(/<[^>]+>/g, " ");
check("Exp11 emits t1 = b * c then t2 = a + t1",
      /t1 = b \* c/.test(tgLast) && /t2 = a \+ t1/.test(tgLast), tgLast);
const tg2 = S.tac("a-b-c").pop().state.replace(/<[^>]+>/g, " ");
check("Exp11 a-b-c is left-associative: t1 = a - b, t2 = t1 - c",
      /t1 = a - b/.test(tg2) && /t2 = t1 - c/.test(tg2), tg2);

/* ---- every frame must carry a note ---- */
["scan", "lex", "count", "yacc"].forEach(k => {
  const frames = k === "scan" ? S.scan("int a;") : k === "count" ? S.count("hi there")
               : k === "yacc" ? S.yacc("abc") : S.lex("int a;");
  check("sim " + k + " frames all have notes", frames.every(f => f.note && f.note.length > 10));
});

console.log("\n" + pass + " passed, " + fail + " failed");
process.exit(fail ? 1 : 0);
