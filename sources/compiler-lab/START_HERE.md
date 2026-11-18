# Compiler Lab (20CSL401) — start here

**Exam:** tomorrow morning. Three phases, in this order:

1. **Algorithm on paper** — no code, no machine. This is the gate.
2. **Machine access** — you write the program and it must compile and run.
3. **Viva** — the examiner asks *why*, and pokes at edge cases.

**Eleven experiments.** Not "about eleven" — exactly eleven, and every one of them is on this site
with its real source.

## The one thing this site is built to do

Memorising the programs will not survive a modified question. So every experiment is here in three
forms:

- the **concept** (why the program exists at all),
- the **algorithm** in words, step by step,
- and — the important one — each algorithm step is **wired to the exact lines of C that implement
  it**. Click a step, the code lights up. Click a code line, the step lights up.

That mapping is the thing to internalise: when they change the question, you are not recalling a
program, you are moving *one step* and knowing *which lines move with it*. Every experiment also has
a **Curveballs** section listing exactly that — the four likely modifications and what changes.

## Where to work

| Page | What it's for |
|---|---|
| **Viva & MCQ** | the whole course in 85 one-line answers — phases, lex, yacc, parsing, IR — with quiz mode and a filter. Start here if the examiner asks theory |
| **Lab bench** | the 11 experiments: steps ↔ code, plus a **trace player** that runs the algorithm on your own input and lights the live line at every step |
| **Playground** | write a program in the browser and actually compile + run it (real gcc, remote sandbox); templates for all 11 |
| **Group kits** (A–D) | the long-form derivation: why it exists, the deep pseudocode, the mid-level record version, worked runs, edge cases |
| **Drill pack** | closed-book practice: 4 algorithm recalls, 4 code-from-blank tasks, 24 viva questions, answers behind a barrier |
| **ALGORITHMS.md** | the condensed one-page-per-experiment version — the last-10-minutes revision |

## Priority, if you only get through some

1. **Must** — Exp 4 (lex+yacc), Exp 10 (shift-reduce), Exp 8 (FIRST/FOLLOW): each is a full-credit
   question on its own.
2. **Must** — Exp 11 (three-address code), Exp 9 (recursive descent): about 20 lines each, and the
   easiest to blank out under pressure.
3. **Should** — Exp 5 and 7 (the automata formulas), Exp 2 and 3 (lex rules).
4. **Last** — Exp 1 and 6 (longest programs, least likely to be the assigned one).

## Two build traps, found by actually running all eleven

- **`-ll` fails on a flex system.** The lex runtime is `libfl` there, so the flag is **`-lfl`**.
  Textbooks say `-ll`; say "System V lex names it `-ll`, flex ships `-lfl`" in the viva.
- **`yacc -d` must run before `lex`**, because the `.l` file `#include`s the `y.tab.h` that yacc
  generates. If the generated `.c` lands in another folder, add `-I.` to gcc.

## Commands

```
Exp 1   gcc lex_a.c                                          ./a.out
Exp 2   lex lexer.l      ; gcc lex.yy.c -lfl                 ./a.out
Exp 3   lex lex_count.l  ; gcc lex.yy.c -lfl                 ./a.out   (Ctrl+D ends input)
Exp 4   yacc -d yacc_id.y ; lex lex_id.l ; gcc y.tab.c lex.yy.c -lfl ; ./a.out
Exp 5-11  gcc <file>.c                                       ./a.out
```

Local copies of every program live in `~/projects/mainproject/`, and `./verify_all.sh` there
rebuilds and runs all eleven so you can diff your own output against a known-good run.
