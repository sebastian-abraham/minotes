# Compiler Design Lab — Exam Drill Pack

**Exam shape (from Haze):** write the **algorithm on paper** → get machine access → **write + run the code**
→ **viva**. Same 11 experiments as the record (`README.md`).

**How to use this file.** Nothing below is new material — the teaching docs are
`ALGORITHMS.md` + `study/GROUP_*.md`. This file is the *practice*: closed-book tasks, then the
answers behind the barrier at the foot. Work a whole set first, then scroll.

Rule: **write your attempt before looking.** A set is 4 tasks. Grade line by line against the
checklist in each answer block.

---

## 0. Exam-day command sheet — verified on this machine (17 Nov 2026)

`flex`, `bison`, `gcc` all present. `yacc` *is* `bison 3.8.2`; `lex` *is* `flex`.

```
Exp 1   gcc lex_a.c                                     ./a.out      (needs input.c in the same folder)
Exp 2   lex lexer.l ; gcc lex.yy.c -lfl ;               ./a.out
Exp 3   lex lex_count.l ; gcc lex.yy.c -lfl ;           ./a.out      (end input with Ctrl+D)
Exp 4   yacc -d yacc_id.y ; lex lex_id.l ; gcc y.tab.c lex.yy.c -lfl ; ./a.out   ← order matters
Exp 5   gcc e_closure.c ;      ./a.out
Exp 6   gcc e-nfa_nfa.c ;      ./a.out
Exp 7   gcc nfa_dfa.c ;        ./a.out
Exp 8   gcc fnf.c ;            ./a.out
Exp 9   gcc rdp.c ;            ./a.out
Exp 10  gcc srp.c ;            ./a.out
Exp 11  gcc intermediate.c ;   ./a.out
```

**Two traps, both hit for real this session:**

1. **`-ll` fails on this machine** — `ld: cannot find -ll`. The lex library here is `libfl`, so
   the flag is **`-lfl`**. The textbook/record says `-ll`; on the college machine either may work.
   *Say this in the viva:* "`-ll` is the System V lex library name; flex installs `libfl`, so the
   link flag is `-lfl`."
2. **`yacc -d` must run before `lex`** — the `.l` file does `#include "y.tab.h"`, which `yacc -d`
   generates. Regenerate it first or the compile dies on a missing header. If `lex.yy.c` was
   generated into another directory, add **`-I.`** to gcc so `y.tab.h` is found.

`./verify_all.sh` in the project rebuilds and runs all 11 with their header sample inputs, so you
can diff your output against a known-good run in one command.

---

## 1. Priority order — if you only get to some

| Tier | Experiments | Why |
|---|---|---|
| **Must** | 4 (lex+yacc), 10 (shift-reduce), 8 (FIRST/FOLLOW) | Each is a full-credit question on its own; 4 is the only two-tool chain |
| **Must** | 11 (three-address code), 9 (recursive descent) | 20 lines of code each, easy to blank out under pressure |
| **Should** | 5, 7 (ε-closure, subset construction) | The formulas are the marks; trace by hand |
| **Should** | 2, 3 (lex rules) | Pure regex recall, no algorithm to forget |
| **Last** | 1 (hand-written scanner), 6 (ε-NFA→NFA) | Longest programs, least likely to be the assigned one |

---

## 2. Drill log — fill this in, it's what tells you you're ready

| Set | Date | Score | Corrections to remember |
|---|---|---|---|
| 1 — algorithm recall | | /4 | |
| 2 — code from blank | | /4 | |
| 3 — viva bank | | /20 | |
| 1 — retry | | /4 | |

---

# SET 1 — Algorithm recall (closed book, 6 minutes each)

Write the **mid-level record version**: name the real structures and the real loop/condition, one
short "why" where a step is a trick. Not "declare int i", not "process the input".

**1.1** Write the algorithm for **ε-closure of all states of an NFA** (Exp 5), including the
recursive helper.

**1.2** Write the algorithm for **NFA → DFA conversion by subset construction** (Exp 7).

**1.3** Write the algorithm for **FIRST and FOLLOW** (Exp 8) — both procedures and the main driver.

**1.4** Write the algorithm for **shift-reduce parsing** (Exp 10), including the termination
condition.

*(Set 2 and Set 3 are below the barrier.)*

# SET 2 — Code from a blank file (machine phase)

Start with `touch x.c`, no reference, 20 minutes each. Then compile and run against the header
sample input. Pass = your output matches the verified run in the answer block.

**2.1** `srp.c` — shift-reduce parser, grammar `E → E+E | E*E | i`, input `i+i*i`.
Expected end state: stack = single `E`, prints "String Accepted".

**2.2** `rdp.c` — recursive descent, grammar `E→TE'`, `E'→+TE'|ε`, `T→FT'`, `T'→*FT'|ε`,
`F→i|(E)`. Must accept `(i+i)*i` and reject `i+*i`.

**2.3** `intermediate.c` — three-address code from an infix expression; input `a+b*c` must print
`t1 = b * c` and `t2 = a + t1`.

**2.4** `lex_id.l` + `yacc_id.y` — identifier validator. `abc123` → Valid, `123abc` → Invalid.
Write out the exact 3-command build chain too.

# SET 3 — Viva bank (say the answer in one or two sentences)

3.1 Why does Exp 1 read one character *past* the end of a token?
3.2 In lex, `int` matches both a keyword rule and an identifier rule. Which wins, and why?
3.3 What does `yyleng` give you, and which experiment needs it?
3.4 Division of labour between lex and yacc, in one sentence.
3.5 What does `yacc -d` do that plain `yacc` doesn't?
3.6 What does `-ll` / `-lfl` link, and why is flex's name different?
3.7 Why must the identifier grammar be left-recursive?
3.8 In Exp 4, what exactly makes `123abc` fail — which grammar rule can never derive it?
3.9 Why is ε-closure recursive, and what stops it looping forever?
3.10 State the ε-NFA→NFA formula verbatim.
3.11 Why is the ε-closure *input* to Exp 6 rather than computed there?
3.12 What is a DFA state, in terms of NFA states?
3.13 Why does Exp 7 sort each set before storing it?
3.14 The loop in Exp 7 iterates over "each DFA state in the set list" while appending to that list.
Why doesn't it miss states?
3.15 FIRST vs FOLLOW — one line each.
3.16 Why does `#` mean ε in the FIRST/FOLLOW program?
3.17 In recursive descent, where is the ε-production? There is no `if (eps)` anywhere.
3.18 Why does `*` bind tighter than `+` in the recursive-descent parser?
3.19 Shift vs reduce — one line each.
3.20 In shift-reduce, why does the reduce loop compare `top` before and after a pass?
3.21 Why does Exp 11 pop the *second* operand as the left operand `a`?
3.22 Why `>=` and not `>` when comparing precedence in Exp 11?
3.23 Exp 10 accepts `i+i*i`. Which reduction order does it choose, and does that matter?
3.24 On a machine with no `flex` but with `lex`: does anything in your build change?

---
---
---

# ⛔ BARRIER — scroll only after you have written your own attempt

---
---
---

# ANSWERS — SET 1

## 1.1 ε-closure (Exp 5)

```
1. Read n, the number of states.
2. Read the n×n epsilon matrix ε, where ε[i][j]=1 means an ε-move i→j.
3. Initialise the closure matrix to 0.
4. For each state s = 0 .. n-1: call findClosure(s, s).
5. For each s, print every j with closure[s][j]=1 as E-closure(qs).
6. Stop.

findClosure(state, current):
1. Mark closure[state][current] = 1.
2. For each i = 0 .. n-1:
     if ε[current][i] = 1 AND closure[state][i] = 0:
         findClosure(state, i).
```

Two-parameter trick: `state` is *whose* closure we're computing (fixed); `current` is where the walk
is now (changes). The `closure[state][i] = 0` test is what stops a cycle of ε-moves recursing forever.

## 1.2 NFA → DFA (Exp 7)

```
1. Read n, m, the input symbols, and the NFA transition table
   (per state and symbol: a count followed by the destination states).
2. Create DFA state 0 = { q0 } and add it to the set list.
3. For each DFA state i in the set list (list grows while looping):
     for each input symbol j:
       a. temp = union of δ(p, j) over every NFA state p in DFA state i, duplicates removed.
       b. Sort temp, so identical sets are stored in the same order.
       c. dfa[i][j] = addSet(temp)   — reuse the existing index if this set is already a DFA state.
4. Print the DFA table, labelling each state by its set, e.g. {q1,q2}.
5. Stop.

sameSet(a,b) : are two sets identical?
findSet(s)   : index of this set if already a DFA state, else −1
addSet(s)    : findSet(s) if it exists, otherwise append it and return the new index
```

## 1.3 FIRST / FOLLOW (Exp 8)

```
FIRST(X):
1. X terminal      → FIRST(X) = { X }; return.
2. X non-terminal  → for each production X → Y1 Y2 ... Yk:
     a. add FIRST(Y1) − {ε} to FIRST(X);
     b. if Y1 can derive ε, add FIRST(Y2) − {ε}, and continue for Y3 ...
     c. if every Yi can derive ε, add ε to FIRST(X).

FOLLOW(A):
1. If A is the start symbol, add $ to FOLLOW(A).
2. For each production B → α A β:
     a. add FIRST(β) − {ε} to FOLLOW(A);
     b. if β derives ε (or β is empty), add FOLLOW(B) to FOLLOW(A).

MAIN:
1. Read n and the n productions as strings (use # for ε).
2. For each non-terminal on a left-hand side, compute and print FIRST.
3. For each non-terminal, compute and print FOLLOW.
```

Implementation notes worth saying: a set is stored as a plain char string and `add()` appends only
if absent (that is the dedupe); FOLLOW recurses on the LHS of the current production in the
"β can vanish" case — that is step 2(b) of the theory, not an implementation shortcut.

## 1.4 Shift-reduce (Exp 10)

```
1. Read the input string. top = −1 (empty stack).
2. For each input character, left to right:
   a. SHIFT: push the character; print the stack.
   b. REDUCE repeatedly while the top of the stack matches a RHS:
        top = 'i'                → replace by 'E'      (E → i)
        top three = E '+' E      → replace by 'E'      (E → E+E)
        top three = E '*' E      → replace by 'E'      (E → E*E)
      Print every reduction.
3. After the input ends, keep reducing until a full pass performs no reduction
   (top unchanged before and after the pass).
4. If the stack holds exactly one symbol and it is 'E' → "String Accepted", else "String Rejected".
```

Detail for a mark: after every push/pop write `stack[top+1] = '\0'` so the stack can be printed as a
string in the trace.

# ANSWERS — SET 2

## 2.1 `srp.c` — verified run

Input `i+i*i` printed exactly:

```
Shift i   Stack: i
Reduce E -> i
Shift +   Stack: E+
Shift i   Stack: E+i
Reduce E -> i
Shift *   Stack: E+E*
Shift i   Stack: E+E*i
Reduce E -> i
Reduce E -> E*E
Reduce E -> E+E

String Accepted
```

Mark-bearing points: global `char stack[50], input[50]; int top = -1;` · a `reduce()` that tries the
three RHS matches in that order · the `top` before/after comparison that ends the second loop ·
`stack[top+1]='\0'` before every print · accept test = `top == 0 && stack[0] == 'E'`.

## 2.2 `rdp.c` — verified run

`(i+i)*i` → `String is accepted` · `i+*i` → `Invalid string`

Shape: `char input[100]; int pos = 0;` and five functions `E, Eprime, T, Tprime, F` plus `error()`
which prints "Invalid string" and `exit(0)`. Accept test in main: `input[pos] == '\0'` after `E()`.
`Eprime()` = `if (input[pos]=='+') { pos++; T(); Eprime(); }` and nothing else — **the absent
`else` is the ε-production.** `F()` = `'i'` → pos++ · `'('` → pos++, `E()`, expect `')'` → pos++ ·
anything else → `error()`.

## 2.3 `intermediate.c` — verified run

Input `a+b*c` printed exactly:

```
Intermediate Code:
t1 = b * c
t2 = a + t1
```

Shape: two char stacks (`operand[ ][ ]` of strings, `opstack[ ]`), `int temp = 1`, `precedence()`
returning 2 for `* /`, 1 for `+ -`, 0 otherwise; `generate()` printing `"%s = %s %c %s"`. Reduction
condition `while (top_op >= 0 && precedence(opstack[top_op]) >= precedence(ch))` — then pop `b`
first, `a` second, `sprintf(result,"t%d",temp++)`, push result.

## 2.4 Exp 4 — verified run + chain

`abc123` → `Valid Identifier` · `123abc` → `Invalid Identifier`

```
yacc -d yacc_id.y            # writes y.tab.c AND y.tab.h
lex lex_id.l                 # .l includes y.tab.h → must exist first
gcc y.tab.c lex.yy.c -lfl    # -ll on a System V lex; -lfl for flex
./a.out
```

`lex_id.l` is 4 rules only (`[a-zA-Z]`→LETTER, `[0-9]`→DIGIT, `\n`→`'\n'`, `.`→ itself), no `main`.
`yacc_id.y` carries `%token LETTER DIGIT`, the left-recursive rule, `main()` calling `yyparse()`,
and `yyerror()` printing "Invalid Identifier".

# ANSWERS — SET 3 (viva)

**3.1** To detect where the token ends. That character belongs to the *next* token, so it is pushed
back with `ungetc()` — otherwise it is lost and the next token is misread.

**3.2** Both are possible, but lex applies **longest match first, then the earlier rule on a tie**.
Same length, so the keyword rule wins because it is written first.

**3.3** The length of the matched text (`yytext`). Exp 3 uses it to count characters without
looping: `characters += yyleng`.

**3.4** lex recognises tokens (regular expressions); yacc checks their *order* against a grammar
(context-free rules). lex feeds `yylex()`, yacc consumes it in `yyparse()`.

**3.5** It also writes the token-definition header `y.tab.h`, which the `.l` file includes so the two
halves agree on token numbers.

**3.6** The lex runtime library (`yywrap`, the input buffer). System V lex ships it as `libl` →
`-ll`; flex ships `libfl` → `-lfl`. On this machine only `libfl` exists.

**3.7** yacc is LALR — bottom-up — and left recursion lets it consume input with a bounded stack; it
also encodes "an identifier followed by one more letter is still an identifier" directly. Right
recursion would grow the stack for every symbol.

**3.8** `123abc` starts with `DIGIT`, and the rule `identifier : LETTER | identifier LETTER |
identifier DIGIT` can only *start* from `LETTER`. No derivation exists, so `yyerror()` fires.

**3.9** ε-closure = the state plus everything reachable by ε-moves, and ε-moves can chain, so it is
naturally recursive. The `closure[state][i] == 0` check visits each state once, so cycles terminate.

**3.10** δ'(q, a) = ε-closure( ∪ over p ∈ ε-closure(q) of δ(p, a) ) — teleport freely, read the
symbol, teleport freely again.

**3.11** Exp 5 computes it; Exp 6 takes it as input. That is the pipeline: 5 → 6 → 7.

**3.12** A **set of NFA states** — "the NFA could be in any of these right now". The subset
construction makes each such set one state of the deterministic machine.

**3.13** Without sorting, `{q1,q2}` and `{q2,q1}` are different arrays, `sameSet` says no, and the
DFA grows duplicate states forever.

**3.14** Sets are **appended** to the list and the loop index keeps advancing, so a set discovered at
index 3 is processed when the loop reaches index 3 in the same pass.

**3.15** FIRST(X): terminals that can begin a string derived from X. FOLLOW(A): terminals that can
appear immediately after A (plus `$` if A can end the input).

**3.16** ε is awkward to type on a terminal, so `#` stands in for it in the production strings.

**3.17** It is the **absence of a match**: `Eprime()` tests for `+`; if it isn't there, the function
returns without consuming anything. That silent return *is* the ε-production.

**3.18** Because `*` lives one level deeper — `F` is inside `T`, `T` is inside `E`. Deeper nesting is
applied first, so `*` binds tighter.

**3.19** Shift: move one input symbol onto the stack. Reduce: replace a RHS on top of the stack by
its LHS. Bottom-up, vs recursive descent's top-down.

**3.20** To detect "no progress". If a full pass leaves `top` unchanged, no rule applies and further
passes would loop forever.

**3.21** Operands come off a stack, so the **last** one pushed is the **right** operand. Popping
`b` first, then `a`, keeps `a op b` in source order — getting it backwards prints `t1 = c * b`.

**3.22** `>=` makes equal precedence reduce immediately, so operators of the same precedence
associate **left to right** — `a-b-c` becomes `(a-b)-c`, which is what C does.

**3.23** It reduces `i→E`, then `E*E→E`, then `E+E→E` — i.e. `i+(i*i)`, which matches precedence. The
grammar `E→E+E|E*E|i` is ambiguous, and this reduce-as-soon-as-possible order happens to pick the
precedence-correct parse for this input; it is not guaranteed in general.

**3.24** No. `lex` is the traditional name; on a flex machine it is the same tool (often a symlink or
wrapper). The generated file and the `-lfl` flag are what change, not your source.
