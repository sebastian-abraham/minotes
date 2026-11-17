# Compiler Design Lab — Study Set (11 experiments)

**Files in this folder**

| File | Covers |
|---|---|
| `ALGORITHMS.md` (this file) | the map, the study route, verified sample runs, compile commands |
| `study/GROUP_A_lexical_analysis.md` | Exp 1–4 — characters → tokens (hand-written, LEX, count, YACC) |
| `study/GROUP_B_automata.md` | Exp 5–7 — ε-closure → ε-NFA→NFA → NFA→DFA |
| `study/GROUP_C_parsing.md` | Exp 8–10 — FIRST/FOLLOW, recursive descent, shift-reduce |
| `study/GROUP_D_code_generation.md` | Exp 11 — infix → three-address code |

The code for every experiment is in the repo root (`~/projects/mainproject/`), and every
algorithm in these files was **checked by actually compiling and running the program** — the
"Verified output" section of each experiment is real captured output, not a description.

---

## 1. The map — learn this first

Every experiment is one phase of a compiler, or one of the machines behind a phase.

```
source.c ──► LEXICAL ANALYSIS ──► tokens ──► SYNTAX ANALYSIS ──► parse tree ──► INTERMEDIATE CODE
              Exp 1, 2, 3                      Exp 4, 8, 9, 10                    Exp 11
              (Group A)                        (Group C)                          (Group D)

THE MACHINES BEHIND IT (Group B):
Exp 5 ε-closure ──► Exp 6 ε-NFA → NFA ──► Exp 7 NFA → DFA
"compute the free jumps"  "delete them"   "make it deterministic — a computer can't guess"
```

**The dependency chain to memorise:** Group B is a pipeline, not three topics. Exp 6 consumes
Exp 5's output as its **input**; Exp 7 consumes the ε-free machine. **5 feeds 6; 5 and 6 feed 7.**

**Why Group B exists at all:** LEX (Exp 2) has to turn regular expressions into executable code.
The classic method builds an **ε-NFA** (ε-moves are the glue between sub-automata). But ε-moves
are painful to *run*, and an NFA is worse — a computer cannot be in several states at once, or
guess a branch. So: compute the ε-closures, absorb the ε-moves into real moves, then make it
deterministic. **Group A needs Group B to actually work** — that is the connection.

## 2. Where each experiment sits, and why it exists

| # | Experiment | The problem it was written to solve |
|---|---|---|
| 1 | Lexical analyser, hand-written | a parser wants *words*, not characters — and you should see what LEX automates |
| 2 | Lexical analyser with **LEX** | hand-writing a scanner doesn't scale; get the generator to build the DFA |
| 3 | LEX counter | proves a LEX action is *arbitrary C* — so a scanner can measure, not just label |
| 4 | **YACC** identifier check | LEX can't judge *order*; structure needs a grammar and a parser |
| 5 | ε-closure | ε-moves are free jumps — you must know where they can take you |
| 6 | ε-NFA → NFA | absorb the free jumps into the symbol moves so the machine is easy to run |
| 7 | NFA → DFA | a computer cannot be in two states or guess — so make each *set* of states one state |
| 8 | FIRST / FOLLOW | a parser must decide *which rule* from the next token — precompute it into a table |
| 9 | Recursive descent | top-down parsing: one function per non-terminal |
| 10 | Shift-reduce | bottom-up parsing — the hand-written miniature of what **YACC itself** does (LALR) |
| 11 | Intermediate code | the parse tree must become machine-ish: one operator per instruction |

## 3. Study route for tonight

Do it in this order — it follows how the ideas actually depend on each other, so nothing is
memorised blind:

1. **Group A** first. Exp 1 → 2 is "here's the job, here's the tool that does it". Exp 4 is the
   pivot of the whole course: **LEX classifies characters, YACC judges their order.**
2. **Group B** second, and read the group preamble before Exp 5. The three experiments are a
   chain; once you see "5 feeds 6, 6 feeds 7" they stop being three separate panic topics.
3. **Group C** third. Exp 8 is the *information* (FIRST/FOLLOW), Exp 9 and 10 are two *users* of
   that information from opposite directions. Say that sentence and this group is done.
4. **Group D** last — it's one experiment and the output is two lines you can memorise.

For each experiment, the fast path through the file is:
**§3 The logic** (read properly — this is the understanding) → **§6 deep pseudocode** →
**§7 record version** (what you write) → **§4 edge cases** (this is where extra marks hide).

## 4. Verified sample runs — type these in and check

Every value below is real captured output. Use it as rehearsal: if your output differs, the input
has a typo.

| Exp | Build | Input | Expected output |
|---|---|---|---|
| 1 | `gcc lex_a.c` | `./a.out` with `input.c` present | one token per line: `Keyword int`, `Keyword main`, `Symbol (`, `Symbol )`, `Symbol {`, `Keyword int`, `Identifier a`, `Operator =`, `Number 10`, `Symbol ;`, `Keyword float`, `Identifier b`, `Operator =`, `Number 20`, `Symbol ;`, `Keyword if`, `Symbol (`, `Identifier a`, `Operator <`, `Identifier b`, `Symbol )`, `Symbol {`, `Identifier a`, `Operator =`, `Identifier a`, `Operator +`, `Number 1`, `Symbol ;`, `Symbol }`, `Keyword return`, `Number 0`, `Symbol ;`, `Symbol }` |
| 2 | `lex lexer.l` → `gcc lex.yy.c` | `int a = a+b*2;` | `Keyword : int`, `Identifier : a`, `Operator : =`, `Identifier : a`, `Operator : +`, `Identifier : b`, `Operator : *`, `Number : 2`, `Special Symbol : ;` |
| 3 | `lex lex_count.l` → `gcc lex.yy.c` | `Hello world`⏎`This is Lex`⏎ then **Ctrl+D** | `lines: 2`, `words: 5`, `characters: 24` |
| 4 | `yacc -d yacc_id.y` → `lex lex_id.l` → `gcc y.tab.c lex.yy.c -ll` | `abc123` then `123abc` | `Valid Identifier` then `Invalid Identifier` |
| 5 | `gcc e_closure.c` | `4` + `0 1 0 0 / 0 0 1 0 / 0 0 0 1 / 0 0 0 0` | `E-closure(q0) = { q0 q1 q2 q3 }`, `(q1) = { q1 q2 q3 }`, `(q2) = { q2 q3 }`, `(q3) = { q3 }` |
| 6 | `gcc e-nfa_nfa.c` | n=3, symbols `a b`, closures {0,1,2} {1,2} {2}, δ(q0,a)={1} δ(q0,b)={0} δ(q1,a)={2} δ(q1,b)={} δ(q2,a)={} δ(q2,b)={2} | `δ'(q0,a)={ q1 q2 }`, `δ'(q0,b)={ q0 q1 q2 }`, `δ'(q1,a)={ q2 }`, `δ'(q1,b)={ q2 }`, `δ'(q2,a)={ }`, `δ'(q2,b)={ q2 }` |
| 7 | `gcc nfa_dfa.c` | n=3, symbols `a b`, δ(q0,a)={0} δ(q0,b)={1} δ(q1,a)={0} δ(q1,b)={1,2} δ(q2,a)={2} δ(q2,b)={} | 4-row table: `{q0}→{q0},{q1}` · `{q1}→{q0},{q1,q2}` · `{q1,q2}→{q0,q2},{q1,q2}` · `{q0,q2}→{q0,q2},{q1}` |
| 8 | `gcc fnf.c` | `4` + `S=AB` `A=a` `B=bC` `C=c` | `FIRST(S)={a} FIRST(A)={a} FIRST(B)={b} FIRST(C)={c}` · `FOLLOW(S)={$} FOLLOW(A)={b} FOLLOW(B)={$} FOLLOW(C)={$}` |
| 9 | `gcc rdp.c` | `(i+i)*i` · `i+*i` · `(i)i` | `String is accepted` · `Invalid string` · `String is rejected` |
| 10 | `gcc srp.c` | `i+i*i` | Shift/Reduce trace (10 lines) then `String Accepted` |
| 11 | `gcc intermediate.c` | `a+b*c` | `t1 = b * c` / `t2 = a + t1` |

**Commands to have on the tip of your tongue:**
```
Exp 1     gcc lex_a.c                                    ./a.out
Exp 2     lex lexer.l        ; gcc lex.yy.c              ./a.out
Exp 3     lex lex_count.l    ; gcc lex.yy.c              ./a.out
Exp 4   yacc -d yacc_id.y    ; lex lex_id.l ; gcc y.tab.c lex.yy.c -lfl ; ./a.out   (-ll on System V lex)
Exp 5–11  gcc <file>.c                                   ./a.out
```
**Two flags people forget:** `-d` on yacc (writes `y.tab.h`, which the lexer `#include`s), and the
lex library. **Only Exp 4 needs the library flag** — and the name depends on the system:
`-ll` on the lab machine, **`-lfl` on a flex system** (verified: this machine needed `-lfl`).
Exp 2 and 3 build with a plain `gcc lex.yy.c` because `lexer.l` uses `%option noyywrap` and
`lex_count.l` defines its own `yywrap()`; `lex_id.l` does **neither**, which is exactly why
Exp 4 needs the flag. (What `yywrap()` does: LEX calls it at end-of-input; returning non-zero
means "no more files to read, stop scanning".)

## 5. Verified edge cases — the "extra marks" list

These were all confirmed by running. Being able to state one of these for an experiment is what
separates a recited algorithm from an understood one.

| Exp | Edge case | Verified behaviour |
|---|---|---|
| 1 | no `if (fp == NULL)` check | `input.c` missing → **segfault**. Also `char ch` vs `int ch` for `EOF` (should be `int`) |
| 2 | `int` matches two rules | longest match, then **first rule** — which is why the keyword rule sits above the identifier rule |
| 3 | `Hello,` | the `,` matches the catch-all `.`, so it counts as a character but **not** as part of the word |
| 4 | `_ab` | **Invalid** — `[a-zA-Z]` does not include `_` (C itself allows it) |
| 5 | ε-cycle q1→q2→q1 | terminates: the answer matrix is marked **before** recursing, so it doubles as the visited set |
| 6 | no move on a symbol | prints `{ }` — correct, not a bug |
| 7 | an empty subset | becomes a genuine DFA state (the **trap state**), printed as `{}`; only one is ever created |
| 7 | `{q1,q2}` vs `{q2,q1}` | sets are **sorted** before storing, so equal sets compare equal; without the sort the DFA explodes |
| 8 | grammar `S=AB, A=#, B=#` | prints `FIRST(S) = { }` — **a real bug**: ε is only added for an explicit `#` production, never when the whole RHS is nullable |
| 8 | two productions for one LHS | `FIRST(S)` is printed **twice** (cosmetic) |
| 8 | A might be at the end of a rule | FOLLOW hands over to FOLLOW(LHS), guarded by `prod[i][0] != c` to stop self-recursion |
| 9 | `(i)i` | **rejected** — the parse succeeded but input was left over (this is the "String is rejected" path) |
| 9 | `(i`, `i+` | `Invalid string` — aborted mid-parse by `error()`. **Two failure paths, two messages** |
| 9 | empty input | Invalid — `F` has **no ε-production** |
| 10 | `i+` | rejected: the drain loop makes no progress and breaks out; `top != 0` |
| 10 | empty input | rejected via `top == -1` — watch the `-1` vs `0` distinction |
| 10 | `ii` | rejected: `EE` is not any right-hand side |
| 11 | `a` | **no output at all** — neither while loop runs |
| 11 | `(a+b)*c` | **segfault** — `precedence(')') == 0` and `0 >= 0` is true, so it pops past the bottom of the operand stack |
| 11 | `12+3` | `t1 = 2 + 3` — the `1` is **silently dropped**; operands are single characters |
| 11 | `a-b-c` | `t1 = a - b`, `t2 = t1 - c` — correct left associativity, from using `>=` |

## 6. The whole lab in eleven lines

| # | The one idea |
|---|---|
| 1 | Characters → tokens by hand; lookahead is **pushed back** with `ungetc` |
| 2 | LEX generates the scanner; **longest match wins, earlier rule wins ties** |
| 3 | Every rule counts its **own** characters (`yyleng`); Ctrl+D ends input |
| 4 | LEX makes tokens, **YACC checks their order**; the left-recursive rule forces "letter first" |
| 5 | E-closure = the state **+ everything reachable by ε**; the answer matrix is also the visited set |
| 6 | δ'(q,a) = **ε-closure( ∪ ε-closure(q) of δ(p,a) )** — *teleport, read, teleport* |
| 7 | **A SET of NFA states becomes ONE DFA state**; sort sets so equal sets compare equal |
| 8 | FIRST = what it can **begin** with; FOLLOW = what can come **after**; they fill the LL(1) table |
| 9 | One function per non-terminal; **falling out of the function IS the ε-production** |
| 10 | **Shift** = push, **reduce** = replace a RHS on top by its LHS; stop when a pass changes nothing |
| 11 | Two stacks + precedence → `t1 = b*c`, `t2 = a+t1` (a post-order tree walk, done inline) |

---

## Note on the repo state

The working-tree files in `~/projects/mainproject/` had all been **zeroed to 0 bytes** and
`refs/heads/main` was empty (that is the "branch appears to be broken" error). The content was
intact inside the git pack, so all 14 files were recovered into the working tree and the ref was
rebuilt — `git status` is clean apart from this study material. A second copy of the recovered
originals is kept in `recovered/`.
