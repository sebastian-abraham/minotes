# GROUP D — Intermediate Code Generation (Exp 11)

Same layout: **why it exists → input/output → logic → edge cases → built-ins → deep
pseudocode → record version → verified output.**

## Where this sits

You have now, across the course, gone:

```
characters ──(Group A)──► tokens ──(Group C)──► a parse tree ──(THIS experiment)──► instructions
```

After parsing, a compiler holds a **parse tree**. The next phase must turn that tree into
something closer to a machine. You cannot jump straight to assembly — you need a
**machine-independent middle form** first, so that the optimisation passes and the final
target-specific code generator have something clean to work on. That middle form is
**intermediate code**, and the specific flavour here is **three-address code**.

## Exp 11 — Generation of three-address code from an infix expression  ·  `intermediate.c`

### 1. Why this exists
**Three-address code** means every instruction has **at most one operator** and **at most three
addresses**:

```
result = operand1 operator operand2
```

So `a + b * c` cannot stay as one line — the multiplication must be done first, its answer stored
somewhere, and then the addition uses that answer. The "somewhere" is a **temporary**, and the
compiler invents them: `t1`, `t2`, …

**Where the algorithm comes from.** If you built the parse tree for `a+b*c` it would be
`(+ a (* b c))`. A **post-order walk** of that tree emits exactly:

```
t1 = b * c      ← visit the * subtree first (deeper = higher precedence)
t2 = a + t1     ← then the +
```

The post-order walk is the *concept*. But building a tree and walking it is a lot of code. The
**two-stack method** achieves the same emission **in a single left-to-right pass**, using a
stack of pending operators and a precedence rule to decide *when* to emit — the operator is
emitted as soon as something of higher-or-equal precedence is waiting behind it. So:

> **the two-stack method is a post-order tree walk done inline, with the tree implicit in the
> stacks.**

That sentence is the "how did we arrive here", and it is the answer to any "why does this work?"
question about this program.

### 2. Input → target output
**Input:** an infix expression typed as one string, e.g. `a+b*c`. Intended alphabet:
**single-character** operands and the operators `+ - * /`.

**Target output:** one line of three-address code per operation, in execution order.
```
Enter expression: a+b*c

Intermediate Code:
t1 = b * c
t2 = a + t1
```
Note `t2` uses `t1` — **the temporaries are the data-flow between instructions.** That is exactly
what makes this "code" rather than just "text": there is a producer and a consumer.

### 3. The logic
Two stacks and one comparison:

- **operand stack** — holds *names* of values (originally the input letters, later the `tN`)
- **operator stack** — holds operators that have been seen but **cannot be emitted yet**, because
  their right-hand operand has not arrived

The scan, one character at a time:

1. **Operand** (letter/digit) → push it on the operand stack. Nothing else; a lone value needs no
   instruction.
2. **Operator** → you cannot emit it yet (its right operand is still ahead of you). But before
   pushing it, check: *is an operator already waiting whose precedence is ≥ mine?* If yes, that
   waiting operator is **done** — everything it needed is now on the stack — so **emit it**, then
   push the new one.
   - the `while` (not `if`) matters: you may have to emit **several** before pushing one.
   - **`>=` and not `>` is a deliberate choice**: it makes operators of *equal* precedence emit
     left-to-right, which is what gives correct **left associativity**. `a-b-c` must be
     `(a-b)-c`, and `>=` is what enforces it.
3. **After the scan**, the operator stack may still hold operators (the lowest-precedence ones).
   Drain it with the same step.

**The emit step, in detail** — because the two pops are where people lose marks:
```
b = pop(operands)        ← the TOP of the stack
a = pop(operands)        ← the SECOND value down
result = "t" + (temp++)
emit:  result = a <op> b
push(operands, result)   ← the temporary becomes an operand for the next operation
```
**`b` is popped first and `a` second.** The stack gives you the *last-pushed* first, and the
last-pushed value is the **right** operand. Swapping these produces `t1 = c * b` — textually
almost identical, semantically wrong. Know which pop is which.

Also note *where* the result goes: it is pushed **back onto the operand stack**, so the temporaries
become operands of later instructions. That single line is why `t2 = a + t1` can reference `t1`.

### 4. Edge cases — **all verified by running**
| Edge case | What actually happens | Verdict |
|---|---|---|
| **multi-digit numbers** `12+3` | `isalnum` is tested **per character**, so `1` and `2` become two separate operands. Result: `t1 = 2 + 3` — the `1` sits unused at the bottom of the operand stack and is **silently dropped** | **real bug**; verified. The scanner never builds a multi-character number token |
| **parentheses** `(a+b)*c` | `(` and `)` are not `isalnum`, so they fall into the *operator* branch. Their `precedence()` is `0`, and the while condition is `precedence(top) >= precedence(current)` = `≥ 0` — which is **true for every operator**, so it pops everything, including past the bottom of the operand stack → `operands[-1]` → **segmentation fault** | **crash**; verified (`Segmentation fault (core dumped)`). Understanding *why* is worth more than the fact: a precedence of 0 makes the comparison always succeed |
| **a bare operand** `a` | no operator is ever pushed, so both while loops never run → **no output at all** | not a crash, but there is no instruction. Fine (a lone value needs no code) but note it |
| **left associativity** `a-b-c` | `t1 = a - b`, then `t2 = t1 - c` | correct ✔ — this is the `>=` at work |
| **chained operators** `a+b*c+d` | `t1 = b * c`, `t2 = a + t1`, `t3 = t2 + d` | correct ✔ — one temporary per operator |
| **unary minus** `-a` | treated as a binary operator with no left operand → pops an empty operand | unsupported; the program has no notion of arity |
| **an operator with no operands** `+` | pops an empty stack | unsupported; not guarded |
| division by zero | irrelevant | the program only *generates* code, it never evaluates — nothing is divided |
| **temporaries past `t9`** | `sprintf(result, "t%d", temp)` writing into `char[10]` | safe: `t100` is 4 characters |
| more than 50 operands/operators | `operands[50][10]`, `operators[50]` | overflow, **not guarded** |
| spaces in the input | `scanf("%s")` stops at the first space | spaces cannot appear — the expression must be one word |
| input with `%`, `^`, `&` | precedence 0 → same always-pop problem as brackets | unsupported; know the failure mode is *the same one as `)`* |

**The pattern to notice across those rows:** three separate edge cases (`)`, `(`, `%`) all fail
for the **same reason** — `precedence()` returns `0`, and `0` is ≥ `0`, so every pending operator
gets popped. One sentence explains three bugs.

### 5. Built-ins used (and why)
| Item | What it does | Why it's used here |
|---|---|---|
| `isalnum(c)` | true if letter or digit | the "is this an operand or an operator?" test. In an infix expression the two cases are exactly "(letter/digit) vs anything else" |
| `char operands[50][10]` | a stack of **strings**, not chars | later values are `"t10"` — two characters, more than a `char` can hold. This is why the stack is 2-D |
| `strcpy(b, operands[top--])` | copies one stack entry into a local buffer | the values are strings, so assignment means copy — and the `--` pops in the same expression |
| `strcpy(operands[++top], result)` | pushes the new temporary back | the result of one instruction becomes the operand of the next |
| `sprintf(result, "t%d", temp)` | formats `t1`, `t2`, … into a string | generates the compiler's temporary names. **`sprintf` returns the character count**, though here the return value is ignored |
| `precedence(op)` (**own**) | returns 2 for `* /`, 1 for `+ -`, 0 otherwise | encapsulates the one table the algorithm needs |
| `generate(op, a, b, result)` (**own**) | a **one-line wrapper around `printf`** | exists so the emission format lives in exactly one place — if the output format changes, one function changes. Worth pointing out: a tiny example of factoring out an output format |
| `printf("%s = %s %c %s\n", result, a, op, b)` | the instruction format | `%c` for the single-character operator, `%s` for the string operands |
| `scanf("%s", expr)` | reads the expression | one word, no spaces |

### 6. Algorithm — deep pseudocode
```
globals: expr[50];  temp = 1        # the temporary counter

precedence(op):
    if op is '*' or '/': return 2
    if op is '+' or '-': return 1
    return 0                        # ← this 0 is the source of the bracket bug

generate(op, a, b, result):
    print result + " = " + a + " " + op + " " + b

main:
    read expr
    operands[50][10];  top = -1          # operand stack, empty
    operators[50];     opTop = -1        # operator stack, empty

    for i = 0 to expr[i] != '\0':

        if isalnum(expr[i]):                       # --- operand ---
            push expr[i] onto operands          (top++)
            continue

        # --- operator ---
        while opTop >= 0 and
              precedence(operators[opTop]) >= precedence(expr[i]):   # >= enforces left-assoc

            b = pop(operands)               # TOP first  → the RIGHT operand
            a = pop(operands)               # next       → the LEFT operand
            result = "t" + temp
            generate(operators[opTop], a, b, result)
            push(operands, result)          # the temporary becomes an operand
            temp++
            opTop--                         # that operator is now consumed

        push expr[i] onto operators          (opTop++)

    # drain the operator stack with the same emission step
    while opTop >= 0:
        b = pop(operands);  a = pop(operands)
        result = "t" + temp
        generate(operators[opTop], a, b, result)
        push(operands, result)
        temp++
        opTop--
```

**Hand-trace `a+b*c`** — worth memorising, because the emitted output is only two lines and it is
the expected exam answer:

| Step | char | action | operand stack | operator stack | emitted |
|---|---|---|---|---|---|
| 1 | `a` | push operand | `a` | — | |
| 2 | `+` | opTop empty → push | `a` | `+` | |
| 3 | `b` | push operand | `a b` | `+` | |
| 4 | `*` | prec(`+`)=1 ≥ prec(`*`)=2? **no** → push | `a b` | `+ *` | |
| 5 | `c` | push operand | `a b c` | `+ *` | |
| 6 | end | drain: pop `*` | `a t1` | `+` | **t1 = b * c** |
| 7 | end | drain: pop `+` | `t2` | — | **t2 = a + t1** |

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Generation of three-address intermediate code from an infix expression
1. Start. Read the infix expression. Set the temporary counter t = 1.
2. For each character of the expression, left to right:
   a. If it is an operand (a letter or a digit):
        push it onto the operand stack.
   b. Otherwise it is an operator:
        i. While the operator stack is not empty AND
           precedence(top of operator stack) >= precedence(current operator):
              - pop two operands (b first, then a) from the operand stack;
              - emit the instruction  tN = a <op> b ;
              - push tN back onto the operand stack and increment N;
              - pop the operator stack.
        ii. Push the current operator onto the operator stack.
3. After the whole expression is scanned, repeat step 2(b)(i) until the operator stack is empty.
4. Stop.

precedence(op):  '*' or '/' → 2 ;  '+' or '-' → 1 ;  otherwise 0.
```

### ▶ Verified output
| Input | Output |
|---|---|
| `a+b*c` | `t1 = b * c` / `t2 = a + t1` |
| `a+b*c+d` | `t1 = b * c` / `t2 = a + t1` / `t3 = t2 + d` |
| `a-b-c` | `t1 = a - b` / `t2 = t1 - c`  ← left associativity, from `>=` |
| `a` | *(nothing emitted)* |
| `12+3` | `t1 = 2 + 3`  ← **the `1` is silently dropped** |
| `(a+b)*c` | **`Segmentation fault (core dumped)`** |

---

# Cross-group one-liners (the whole lab, smallest possible form)

| # | The one idea |
|---|---|
| 1 | Characters → tokens by hand; lookahead is **pushed back** with `ungetc` |
| 2 | LEX generates the scanner; **longest match wins, earlier rule wins ties** |
| 3 | Every rule counts its **own** characters (`yyleng`); Ctrl+D ends input |
| 4 | LEX makes tokens, **YACC checks their order**; the left-recursive rule forces "letter first" |
| 5 | E-closure = the state **+ everything reachable by ε**; the answer matrix doubles as the visited set |
| 6 | δ'(q,a) = **ε-closure( ∪ ε-closure(q) of δ(p,a) )** — *teleport, read, teleport* |
| 7 | **A SET of NFA states becomes ONE DFA state**; sort sets so equal sets compare equal |
| 8 | FIRST = what it can **begin** with; FOLLOW = what can come **after**; they fill the LL(1) table |
| 9 | One function per non-terminal; **falling out of the function IS the ε-production** |
| 10 | **Shift** = push, **reduce** = replace a RHS on top by its LHS; stop when a pass changes nothing |
| 11 | Two stacks + precedence → `t1 = b*c`, `t2 = a+t1` (a post-order tree walk, done inline) |
