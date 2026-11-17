# GROUP C — Parsing (Exp 8–10)

Same layout: **why it exists → input/output → logic → edge cases → built-ins → deep
pseudocode → record version → verified output.**

## Read this first: where these three sit

Group A turned characters into **tokens**. Group B made the *token recogniser* runnable. But
neither says anything about **structure** — whether `a + b *` is a legal *sentence* of the
language. That is **syntax analysis (parsing)**, and it needs one new idea: a **grammar**.

The three experiments are the three standard approaches to the same question:

| Exp | Approach | Direction | Builds the stack… | Real-world descendant |
|---|---|---|---|---|
| 8 | FIRST / FOLLOW | — | *the table the parser reads* | feeds LL(1) table-driven parsing |
| 9 | Recursive descent | **top-down** | …implicitly, via C recursion | hand-written parsers in real compilers |
| 10 | Shift-reduce | **bottom-up** | …explicitly, an array | **LR / LALR — which is what YACC (Exp 4) actually is** |

Exp 8 is pure theory applied to a grammar: it computes the two sets a parser needs to *decide*.
Exp 9 and 10 are two implementations that make the decision. If you can say **"8 computes the
information, 9 and 10 use it from opposite directions"**, this group is organised.

---

## Exp 8 — FIRST and FOLLOW of a grammar  ·  `fnf.c`

### 1. Why this exists
To parse `E → T E'` a machine must answer one question at each step: **given the token I'm
looking at right now, which rule do I apply?** There is no way to decide that from the rule text
alone. So the answer is precomputed into a table, and the table is filled from two sets:

- **FIRST(α)** — *which terminals can appear as the first symbol of something derived from α?*
- **FOLLOW(A)** — *which terminals can appear immediately after A?*

Concretely: rule `A → α` goes into table cell `[A, t]` for every `t ∈ FIRST(α)`. And if α can
vanish into nothing (ε), then the decision must instead be made by what can *follow* A — so the
rule also goes into cell `[A, t]` for every `t ∈ FOLLOW(A)`. **If you understand that one
paragraph, you know why these sets exist and you will not forget the definitions.**

### 2. Input → target output
**Input:** the number of productions `n`, then `n` productions typed as **strings** in the form
`LHS=RHS`, using **`#` to mean ε** (you cannot type ε on a keyboard):

```
4
S=AB
A=a
B=bC
C=c
```

**Target output:** FIRST and FOLLOW for every non-terminal that appears on a left-hand side.
```
FIRST sets:
FIRST(S) = { a }     FIRST(A) = { a }     FIRST(B) = { b }     FIRST(C) = { c }

FOLLOW sets:
FOLLOW(S) = { $ }    FOLLOW(A) = { b }    FOLLOW(B) = { $ }    FOLLOW(C) = { $ }
```
`$` is the end-of-input marker. It is in FOLLOW(S) because S is the start symbol.

### 3. The logic
**FIRST — the rules.** For a symbol X:
1. X is a **terminal** → `FIRST(X) = { X }`. (A terminal begins with itself.) Done.
2. X is a **non-terminal** → for each production `X → Y1 Y2 ... Yk`:
   - add `FIRST(Y1) − {ε}` to `FIRST(X)`
   - if Y1 can derive ε, then Y2 might be the first symbol → add `FIRST(Y2) − {ε}`, and so on
   - if **every** Y1…Yk can derive ε, then X itself can be ε → add **ε** to FIRST(X)

The word **"− {ε}"** keeps coming up. It means: *a non-terminal's nullability is not a first
symbol*. ε is a real result, but it is pulled out and handled separately at each level. Only the
top-level symbol can actually report ε.

**FOLLOW — the rules.** For a non-terminal A:
1. If A is the **start symbol** → add `$` to FOLLOW(A).
2. For every production `B → α A β` — that is, every place A appears on a right-hand side:
   - add `FIRST(β) − {ε}` to FOLLOW(A) — *whatever can come after A in this rule*
   - if β can derive ε (or β is empty — A is **last** in the rule), then nothing follows A *within
     this rule*, so whatever can follow **B** can also follow A → add `FOLLOW(B)` to FOLLOW(A)

That second bullet is the recursion in FOLLOW, and **the recursion is the whole difficulty of
this experiment.** FOLLOW(A) needs FOLLOW(B), which may need FOLLOW of something else.

**Why FIRST can be solved by recursion but FOLLOW looks like it needs a loop.** Because A
appearing at the *end* of a rule hands the question to FOLLOW(LHS). Writing FOLLOW as a
function that calls itself on the LHS is how this program avoids implementing a
"repeat until nothing changes" fixed-point loop.

**How this maps onto the C.** Everything in the program is bookkeeping around those rules:

| Grammar concept | In the code |
|---|---|
| a production string `S=AB` | `prod[i][0]` = LHS (`S`), `prod[i][1]` = `=`, `prod[i][2]` onwards = RHS (`A`,`B`) |
| ε | the character `'#'` |
| a non-terminal | any **uppercase** character (`isupper`) — lowercase = terminal |
| a set | a **string of characters**, e.g. `"ab"`, terminated by `'\0'` |
| adding to a set without duplicates | the `add()` helper |
| ε survives in a set temporarily | `FIRST` collects `'#'` into a `temp` buffer and checks for it with a flag |

### 4. Edge cases — **verified by running, and two are real bugs**
| Edge case | What happens | Verdict |
|---|---|---|
| an explicit ε production `A=#` | `if (prod[i][2] == '#') add(result, '#')` catches it → `FIRST(A) = { # }` | correct ✔ |
| **every RHS symbol nullable** — `S=AB`, `A=#`, `B=#` | theory says FIRST(S) should be `{#}`. **The program prints `FIRST(S) = { }` (empty).** | **BUG** — the code only adds `#` for an *explicit* `#` production; when the loop walks past the end of a fully-nullable RHS it just falls out without adding ε. **Know this — it is the single most interesting thing about this program, and a great "limitation" answer** |
| a nullable symbol in the middle — `S=AB`, `A=a`, `B=#` | the `!epsilon` check makes the loop advance past a nullable symbol, so FOLLOW(A) picks up `$` from FOLLOW(S) | correct ✔ (verified `FOLLOW(A) = { $ }`) |
| **two productions with the same LHS** — `S=AB` and `S=a` | `main` loops over *productions*, not non-terminals, so it prints `FIRST(S)` **twice** | **cosmetic bug** — verified. The set is right, it is just printed once per production |
| a non-terminal on **no** right-hand side — `A=a` where A never appears in any RHS | FOLLOW(A) stays empty (no `$`, because A is not the start symbol) | correct — an unreachable non-terminal has no follow set ✔ |
| **left recursion** in FOLLOW (A appears in a rule for A) | `FOLLOW(A)` would recurse into itself forever | guarded by `if (prod[i][0] != c)` before the recursive `FOLLOW(prod[i][0], ...)` call — **that guard is not optional** |
| ε inside FOLLOW | ε must never be in a FOLLOW set | the `epsilon` flag is checked and `'#'` is skipped before `add()` is called |
| a **lowercase non-terminal** | `isupper` fails → treated as a terminal | a real limitation of the representation; grammar symbols must be uppercase |
| a production longer than 19 chars, or more than 10 productions | `prod[10][20]` | overflow, **not guarded** |
| a set longer than 19 chars | `char temp[20]` | overflow, not guarded |

### 5. Built-ins used (and why)
| Item | What it does | Why it's used |
|---|---|---|
| `isupper(c)` | true if `c` is an uppercase letter | the whole "terminal vs non-terminal" decision, in one call — uppercase is the convention |
| `add(set, c)` (**own**) | scans the set string for `c`; appends only if absent; keeps `'\0'` at the end | C has no set type. It also handles the `'\0'` bookkeeping, so every caller gets a valid string |
| a set as a **char string** | `"abc"` = the set {a,b,c} | printable direct with `printf(" %c", temp[j])`, and membership is a simple scan |
| `char temp[20] = "";` | a fresh empty set per computation | avoids stale data between calls |
| the `epsilon` flag | remembers "I saw a `#` that I did NOT add to the result" | because ε must be *removed* from FIRST at each level, but must be *noticed* to decide whether to continue |
| `scanf("%s", prod[i])` | reads one production string | the `LHS=RHS` string encoding keeps input trivial to type |
| `printf` in a loop to end-of-`'\0'` | prints the set | the set is already a string |
| `<string.h>` | **included but not actually used** | a harmless leftover — worth knowing so you don't claim `strcpy` is doing work |

### 6. Algorithm — deep pseudocode
```
globals: prod[10][20]      # prod[i] = "LHS=RHS"
         n                 # number of productions

add(set, c):                                   # set-insert with dedupe
    for i = 0 to set[i] != '\0':
        if set[i] == c: return                 # already there
    set[i] = c;  set[i+1] = '\0'               # append and re-terminate

FIRST(c, result):                              # result is built up in place
    if not isupper(c):                         # c is a TERMINAL
        add(result, c)
        return

    for i = 0 to n-1:                          # for each production of c
        if prod[i][0] == c:
            if prod[i][2] == '#':              # explicit X → ε
                add(result, '#')
            else:
                j = 2
                while prod[i][j] != '\0':      # walk the RHS Y1, Y2, ...
                    temp[20] = ""
                    FIRST(prod[i][j], temp)    # recursive call per symbol

                    epsilon = 0
                    for k = 0 to temp[k] != '\0':
                        if temp[k] == '#': epsilon = 1     # don't add ε ...
                        else:              add(result, temp[k])   # ... but add the rest

                    if not epsilon: break      # Y_j cannot vanish → stop walking the RHS
                    j++                        # Y_j IS nullable → look at Y_{j+1}
                    # NOTE: if the whole RHS is nullable, nothing adds '#' here  ← the bug

FOLLOW(c, result):
    if c == prod[0][0]:                        # c is the start symbol
        add(result, '$')

    for i = 0 to n-1:                          # scan EVERY production
        for j = 2 to prod[i][j] != '\0':       # every RHS position
            if prod[i][j] == c:                # found c on a right-hand side
                if prod[i][j+1] != '\0':       # something follows c in this rule
                    next = prod[i][j+1]
                    temp[20] = ""
                    FIRST(next, temp)

                    epsilon = 0
                    for k = 0 to temp[k] != '\0':
                        if temp[k] == '#': epsilon = 1
                        else:              add(result, temp[k])

                    if epsilon:                            # next is nullable → c ends the rule
                        if prod[i][0] != c:                # guard: no self-recursion
                            temp2[20] = ""
                            FOLLOW(prod[i][0], temp2)      # hand over to FOLLOW(LHS)
                            for k: add(result, temp2[k])
                else:                                      # c is the LAST symbol of the rule
                    if prod[i][0] != c:
                        temp[20] = ""
                        FOLLOW(prod[i][0], temp)           # hand over to FOLLOW(LHS)
                        for k: add(result, temp[k])

main:
    read n;  read the n production strings
    print "FIRST sets:"
    for i = 0 to n-1:
        temp[0] = '\0';  FIRST(prod[i][0], temp)
        print "FIRST(" + prod[i][0] + ") = { ... }"
    print "FOLLOW sets:"
    for i = 0 to n-1:
        temp[0] = '\0';  FOLLOW(prod[i][0], temp)
        print "FOLLOW(" + prod[i][0] + ") = { ... }"
```

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Find the FIRST and FOLLOW sets of a grammar

FIRST(X):
1. If X is a terminal, FIRST(X) = { X } and return.
2. If X is a non-terminal, for each production X → Y1 Y2 ... Yk:
   a. Add FIRST(Y1) − {ε} to FIRST(X).
   b. If Y1 derives ε, add FIRST(Y2) − {ε}, and continue for Y3, ...
   c. If every one of Y1 ... Yk derives ε, add ε to FIRST(X).

FOLLOW(A):
1. If A is the start symbol, add $ to FOLLOW(A).
2. For each production B → α A β:
   a. Add FIRST(β) − {ε} to FOLLOW(A).
   b. If β derives ε (or β is empty), add FOLLOW(B) to FOLLOW(A).

MAIN:
1. Read n, the number of productions; read the n productions (use # for ε).
2. For each left-hand-side non-terminal, compute and print its FIRST set.
3. For each left-hand-side non-terminal, compute and print its FOLLOW set.
4. Stop.
```

### ▶ Verified output
`4` / `S=AB` / `A=a` / `B=bC` / `C=c` →
`FIRST(S)={a} FIRST(A)={a} FIRST(B)={b} FIRST(C)={c}` ·
`FOLLOW(S)={$} FOLLOW(A)={b} FOLLOW(B)={$} FOLLOW(C)={$}`

Reasoning for FOLLOW(A)={b} and FOLLOW(B)={$}, to say out loud: *A is followed by B inside
`S→AB`, so FOLLOW(A) gets FIRST(B)={b}. B is last in `S→AB`, so FOLLOW(B) gets FOLLOW(S)={$}.
C is last in `B→bC`, so FOLLOW(C) gets FOLLOW(B)={$}.*

---

## Exp 9 — Recursive Descent Parser  ·  `rdp.c`

### 1. Why this exists
Exp 8 computed the information a parser needs. Now actually parse. There are two directions;
this is the **top-down** one, and it is the one you can genuinely write by hand in an exam:

> **Write one C function per grammar non-terminal.** To parse an `E`, call `E()`. Each function
> consumes the symbols it expects and calls the functions for the symbols on its right-hand side,
> in order.

The grammar encodes **precedence through layering** — this is the idea that makes it work:

```
E  → T E'          E' → + T E' | ε        E handles + (lowest precedence)
T  → F T'          T' → * F T' | ε        T handles *
F  → i | ( E )                            F handles brackets and operands
```

`*` is nested *deeper* (inside `T`) than `+`, so it binds tighter. Brackets sit deepest of all.

### 2. Input → target output
**Input:** a string over the alphabet `i`, `+`, `*`, `(`, `)` — where `i` stands for an operand.

**Target output:** one of **three** messages (and knowing *why there are three* is worth marks):
```
i+i*i   → String is accepted
(i)i    → String is rejected
i+*i    → Invalid string
```

### 3. The logic
There is a single global `pos` indexing the input. It **only ever moves forward**, one symbol per
consumed token. Every function sees the same `pos`, so each one knows exactly where the previous
one stopped — that shared cursor *is* the parser's state.

```
E():  T(); E'();
E'(): if input[pos]=='+' { pos++; T(); E'(); }
T():  F(); T'();
T'(): if input[pos]=='*' { pos++; F(); T'(); }
F():  if input[pos]=='i' { pos++; }
      else if input[pos]=='(' { pos++; E(); if input[pos]==')' pos++; else error(); }
      else error();
```

**The ε-production — the single most-asked point about this program.** `E' → + T E' | ε` has an
ε alternative, and the code writes **no `else` branch for it**:

```
void Eprime() {
    if (input[pos] == '+') { pos++; T(); Eprime(); }
}
```

If the lookahead is not `+`, the function **simply returns** — and *that return IS the ε
production*. There is no "consume nothing" operation to write, because consuming nothing is what
falling off the end of the function already does. If someone asks "where is ε handled?", the
answer is **"in the absence of a match — nowhere explicitly."**

**Why two different failure messages.** Two distinct failure modes:
- `error()` — a function matched a *prefix* and then hit something impossible (inside `F`). It
  prints **"Invalid string"** and calls `exit(0)` immediately, mid-parse.
- **"String is rejected"** — parsing *succeeded* (`E()` returned normally) but `pos` did not reach
  the end of the string: there is **leftover input** the grammar could not use.

So: *"Invalid string" = the sentence broke the grammar while being built. "String is rejected" =
the grammar built a prefix and then stopped early.*

### 4. Edge cases — **all verified by running**
| Input | Result | Why |
|---|---|---|
| `i` | **accepted** | `E→T→F` consumes `i`; `T'` sees EOF (not `*`) → returns (ε); `E'` sees EOF (not `+`) → returns (ε). `pos` at `'\0'` ✓ |
| `i*i` | **accepted** | exercises the `T'` loop |
| `(i+i)*i` | **accepted** | brackets recurse into `E` |
| `(i)i` | **rejected** (`String is rejected`) | `E` consumes `(i)`, then `E'` sees `i` — not `+` — so it returns as ε. Parsing ended, but input remains → leftover input |
| `(i` | **Invalid string** | `F` consumed `(`, `E` consumed `i`, then expects `)` but finds end-of-string → `error()` |
| `i+` | **Invalid string** | `E'` consumed `+`, calls `T`, which reaches `F` at end-of-string → neither `i` nor `(` → `error()` |
| *(empty input)* | **Invalid string** | `F` finds neither `i` nor `(` → `error()`. Note there is **no ε-production for `F`**, so an empty sentence is illegal |
| `i i` (space) | only `i` is parsed | `scanf("%s")` **stops at whitespace** — spaces are not part of the alphabet, so the space never reaches the parser |
| multi-character operand `ab` | not representable | operands are exactly the character `i`. A real parser would consume an *identifier token*; this toy grammar uses one char |
| `-` or `/` | Invalid string | the grammar only knows `+` and `*` |

### 5. Built-ins used (and why)
| Item | What it does | Why it's used |
|---|---|---|
| shared global `pos` | the cursor into `input[]` | the only way mutual recursion can share state without threading a parameter through every call |
| `void` functions | the parsers return nothing | they communicate purely by **moving `pos` forward** — success is implicit, failure calls `error()` |
| forward declarations (`void E();` …) | declare the functions before defining them | `E` calls `Eprime` which calls `E` — mutual recursion needs prototypes |
| `scanf("%s", input)` | reads one whitespace-delimited word | the input is a single token string; no spaces in the language |
| `exit(0)` (in `error()`) | terminates the process immediately | aborts the parse the moment it becomes impossible. **Semantic nuance: `exit(0)` reports *success* to the OS, which is backwards for an error — `exit(1)` would be correct.** Good detail to mention |
| `<stdlib.h>` | included **only** for `exit` | that is the whole reason it is there |
| `printf("%s")` at the end | prints the verdict | `main` decides by testing `input[pos] == '\0'` |
| the check `input[pos] == '\0'` | "consumed everything?" | the C string terminator doubles as the end-of-input marker — so **`$` from Exp 8 is literally `'\0'` here** |

### 6. Algorithm — deep pseudocode
```
globals: input[100];  pos = 0

error():
    print "Invalid string"
    exit(0)                       # exit code 0 — semantically should be 1

E():                              # E → T E'
    T();  Eprime()

Eprime():                         # E' → + T E' | ε
    if input[pos] == '+':
        pos++
        T()
        Eprime()
    # no else → returning IS the ε-production

T():                              # T → F T'
    F();  Tprime()

Tprime():                         # T' → * F T' | ε
    if input[pos] == '*':
        pos++
        F()
        Tprime()

F():                              # F → i | ( E )
    if input[pos] == 'i':
        pos++
    elif input[pos] == '(':
        pos++
        E()
        if input[pos] == ')': pos++
        else: error()             # unclosed bracket → abort mid-parse
    else:
        error()                   # F has NO ε-production

main:
    read input
    E()                           # the whole parse
    if input[pos] == '\0':  print "String is accepted"
    else:                   print "String is rejected"
```
To trace by hand, keep a column for `input[pos]` and a column for `pos` after each call — the
recursion is shallow, so 5 lines of trace covers any exam string.

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Recursive descent parser for the grammar
           E → TE',  E' → +TE' | ε,  T → FT',  T' → *FT' | ε,  F → i | (E)

1. Start. Read the input string. Set pos = 0.
2. Call E().
3. If input[pos] is the end-of-string marker, print "String is accepted";
   otherwise print "String is rejected".
4. Stop.

E():    call T(); call E'().
E'():   if input[pos] = '+' → pos++; T(); E'().  (otherwise return — the ε-production)
T():    call F(); call T'().
T'():   if input[pos] = '*' → pos++; F(); T'().  (otherwise return — the ε-production)
F():    if input[pos] = 'i' → pos++;
        else if input[pos] = '(' → pos++; E(); if input[pos] = ')' pos++; else error();
        else error().
error(): print "Invalid string" and exit.
```

### ▶ Verified output
`i` → accepted · `i*i` → accepted · `(i+i)*i` → accepted · `(i)i` → **rejected** ·
`(i` → Invalid string · `i+` → Invalid string · empty → Invalid string

---

## Exp 10 — Shift-Reduce Parser  ·  `srp.c`

### 1. Why this exists
Exp 9 predicts from the top. This experiment parses from **the opposite end — bottom-up**:

> Push input symbols onto a **stack** (**shift**). Whenever the *top of the stack* looks like the
> right-hand side of a rule, replace it by the left-hand side (**reduce**). If you finish with a
> single `E` on the stack, the input parsed.

Why bother with the opposite direction? Because **this is what real parsers do** — including
**YACC from Exp 4**, which generates an **LALR** parser, a shift-reduce parser with a
precomputed table. So Exp 10 is the hand-written miniature of the machinery behind Exp 4. Saying
that link out loud is exactly the kind of connection that earns marks.

The grammar is deliberately tiny and **ambiguous**:
```
E → E + E | E * E | i
```

### 2. Input → target output
**Input:** a string over `i`, `+`, `*` (e.g. `i+i*i`).

**Target output:** a **trace** of the operations, then a verdict:
```
Shift i        Stack: i
Reduce E -> i
Shift +        Stack: E+
Shift i        Stack: E+i
Reduce E -> i
Shift *        Stack: E+E*
Shift i        Stack: E+E*i
Reduce E -> i
Reduce E -> E*E
Reduce E -> E+E
String Accepted
```
Note the trace prints the stack after every single operation — *"Shift i" then "Stack: i"*. That
is the thing the examiner wants to see: the stack contents at each step.

### 3. The logic
The two operations, and the order they are attempted:

1. **Shift** — push the next input character. This is unconditional; every character is pushed.
2. **Reduce** — check the top of the stack against the three right-hand sides, and collapse if it
   matches:
   - top is `i` → replace with `E` (`E → i`)
   - top three are `E + E` → replace with `E` (`E → E+E`)
   - top three are `E * E` → replace with `E` (`E → E*E`)

**Two structural details that the trace makes visible, and that you should be able to explain:**

**(a) `reduce()` applies at most ONE reduction per call.** The three cases are an `if / else-if /
else-if` chain, so a single call can never do two reductions. That is why the trace shows
`Reduce E -> i` immediately after each shift (the easy reduction happens first) and why
`E+E*E` sits on the stack until the **final drain loop** gets to it.

**(b) The final drain loop and its termination trick.** After the input is exhausted the stack may
still be reducible. So:

```
while (top > 0) {
    oldtop = top;
    reduce();
    if (oldtop == top) break;      // a full pass changed nothing → stop
}
```

**Comparing `top` before and after is the guard against an infinite loop.** Without it, an
unreducible stack would spin forever. Say this — "I remember whether the stack changed; if a pass
changes nothing, no further pass can help" — it is a genuinely reusable parsing insight.

**(c) Why the trace came out with correct precedence.** `i+i*i` reduced `E*E` **before** `E+E`.
That is not the program "knowing" that `*` binds tighter — the grammar is ambiguous and knows no
such thing. It happened because after the last shift the stack was `E+E*E`, and the chain
tests `E+E` **before** `E*E` but `E+E` requires the *middle* character to be `+`, which it is not
(`stack[top-1]` is `*`). So the `E*E` case fired first. **The stack shape decided it.**
An ambiguous grammar with a naive reducer gives the right answer here by luck of the layout —
worth saying, because it shows you understand *why* real parsers need a precedence table.

### 4. Edge cases — **all verified by running**
| Input | Result | Why |
|---|---|---|
| `i+i*i` | **Accepted** | the full trace above |
| `i*i+i` | **Accepted** | same mechanics, operators swapped |
| `i` | **Accepted** | shift `i` → reduce to `E`; the drain loop leaves `top == 0` and `stack[0] == 'E'` |
| `i+` | **Rejected** | after shifting, the stack is `E+`; the drain loop calls `reduce()`, nothing matches, `oldtop == top` → break; `top != 0` → rejected |
| `ii` | **Rejected** | stack becomes `EE`; `EE` is not any right-hand side, and `stack[top]` is `E` not `i`, so nothing reduces. Two symbols are left → rejected |
| `a` (an unknown symbol) | **Rejected** | `a` is shifted like any character, but no reduction ever involves `a` → the stack never collapses to `E` |
| *(empty input)* | **Rejected** | the input loop never runs, so `top == -1`; the drain loop's `while (top > 0)` never runs, and `top == 0` is false → rejected. Watch for this one: it is a `-1` vs `0` distinction |
| `i++i` | rejected | after the second `+` the stack is `E+E+`; `E+E` needs a **3-symbol** top window ending at `top`, so it cannot match while `+` sits on top |

### 5. Built-ins used (and why)
This program uses essentially **no library functions** — everything is the algorithm. That is
itself the point to make in the record.

| Item | What it does | Why |
|---|---|---|
| `stack[50]`, `input[50]`, `top = -1` | the parser's stack and cursor | `top = -1` means **empty** — the standard C stack idiom, and the reason `while (top >= 0)` tests work |
| the push idiom `stack[++top] = ch` | pre-increment then store | increments *then* uses the value, so the new element goes at the new top |
| the pop-and-collapse idiom `top -= 2; stack[top] = 'E';` | replace 3 stack cells by 1 | reducing `E+E` to `E` removes 2 cells: drop the top by 2, then overwrite |
| `stack[top + 1] = '\0';` | puts a terminator right after the top | **this is what makes the stack printable with `%s`**. Without it, `printf("Stack: %s")` would run past the top into stale characters. A tiny line, but it is the reason the trace output is correct |
| `oldtop == top` comparison | detects "no progress" | the termination guard |
| `printf("Shift %c\tStack: %s\n", ...)` | the trace line | `\t` aligns the columns |
| `<string.h>` | **included but unused** | leftover |
| `scanf("%s", input)` | reads the string | no spaces in the language |

### 6. Algorithm — deep pseudocode
```
globals: stack[50], input[50], top = -1

reduce():                               # ONE reduction at most per call (if/else-if chain)
    if top >= 0 and stack[top] == 'i':                          # E → i
        stack[top] = 'E'
        print "Reduce E -> i"

    elif top >= 2 and stack[top]   == 'E' and                    # E → E+E
                      stack[top-1] == '+' and
                      stack[top-2] == 'E':
        top -= 2                                                    # collapse 3 cells
        stack[top] = 'E'
        print "Reduce E -> E+E"

    elif top >= 2 and stack[top]   == 'E' and                    # E → E*E
                      stack[top-1] == '*' and
                      stack[top-2] == 'E':
        top -= 2
        stack[top] = 'E'
        print "Reduce E -> E*E"

main:
    read input
    print "Shift Reduce Steps:"

    for i = 0 to input[i] != '\0':              # process the whole input
        stack[++top] = input[i]                 # SHIFT
        stack[top + 1] = '\0'                   # keep it printable
        print "Shift " + input[i] + "\tStack: " + stack
        reduce()                                # try one reduction
        stack[top + 1] = '\0'

    while top > 0:                              # drain loop: keep reducing
        oldtop = top
        reduce()
        stack[top + 1] = '\0'
        if oldtop == top: break                 # no progress → stop (prevents an infinite loop)

    if top == 0 and stack[0] == 'E':  print "String Accepted"
    else:                             print "String Rejected"
```

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Shift-reduce parsing  (grammar  E → E+E | E*E | i)
1. Start. Read the input string. Set top = -1 (empty stack).
2. For each character of the input, left to right:
   a. SHIFT: push the character onto the stack.
   b. REDUCE: apply at most one reduction while the top of the stack matches a right-hand side:
        - top is 'i'          → replace by 'E'      (E → i)
        - top three are E + E → replace them by 'E'  (E → E+E)
        - top three are E * E → replace them by 'E'  (E → E*E)
      Print every shift and reduction performed.
3. After the input is exhausted, keep reducing until a full pass makes no reduction.
4. If the stack contains exactly one symbol and it is 'E' → print "String Accepted";
   otherwise → print "String Rejected".
5. Stop.
```

### ▶ Verified output
`i+i*i` → the trace in §2 → `String Accepted` · `i+` → Rejected · `ii` → Rejected ·
`a` → Rejected · `i` → Accepted

---

**Next group:** Group D (Exp 11) — turning a parsed expression into machine-ish code.
