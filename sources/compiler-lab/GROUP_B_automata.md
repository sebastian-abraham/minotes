# GROUP B — Finite Automata (Exp 5–7)

Same layout as Group A: **why it exists → input/output → logic → edge cases → built-ins →
deep pseudocode → record version → verified output.**

## Read this first: why these three exist, and why in this order

This chain is the part of the lab that people blank on, because the three experiments look
unrelated. They are not — they are one single pipeline, and knowing the pipeline is what makes
them stick.

**The story starts inside LEX.** LEX has to turn a set of regular expressions into executable
code. The classic method (Thompson's construction) builds an **ε-NFA**: to glue two
sub-automata together you invent a **free transition — a move that consumes no input**. That's
an **ε-transition**, and it makes *construction* easy.

But ε-transitions make *simulation* hard, and an NFA makes it harder still: at each step an NFA
may be in **several states at once**, and a real computer cannot "be in three states" or "guess
which branch to take". So three repairs are needed, in order:

```
ε-NFA  ──(Exp 5: compute ε-closures)──►  ε-NFA you understand
       ──(Exp 6: absorb ε into the symbol moves)──►  plain NFA, no ε
       ──(Exp 7: each SET of NFA states becomes ONE DFA state)──►  DFA  ← a computer can run this
```

**The dependency to memorise:** Exp 6 takes the ε-closures as **input** — i.e. Exp 5's output.
Exp 7 then consumes the ε-free machine. **5 feeds 6; 5 and 6 feed 7.** If you can say that
sentence, the group is organised in your head.

---

## Exp 5 — ε-closure of every state of an NFA  ·  `e_closure.c`

### 1. Why this exists
An ε-transition is a move that consumes **no input character** — a free jump. They exist
because building automata from regular expressions uses them as glue (Thompson's construction).

The problem: to *run* such a machine you must know "from state q, **without reading anything**,
where can I end up?" Answer: q itself, and then keep following ε-jumps as far as they go. That
set is the **ε-closure of q**, written **E-closure(q)** or **ε-closure(q)**.

This is the first repair in the chain, and it is needed *before* anything else can be done,
because Exp 6's formula is written entirely in terms of closures.

### 2. Input → target output
**Input:** `n` (number of states) followed by an **n × n matrix** of 0/1 where
`ε[i][j] = 1` means "there is an ε-transition from state i to state j".

Sample: `4` then
```
0 1 0 0      q0 --ε--> q1
0 0 1 0      q1 --ε--> q2
0 0 0 1      q2 --ε--> q3
0 0 0 0      q3 has no ε-moves
```

**Target output:** the closure of every state.
```
E-closure(q0) = { q0 q1 q2 q3 }
E-closure(q1) = { q1 q2 q3 }
E-closure(q2) = { q2 q3 }
E-closure(q3) = { q3 }
```
Read the first line as: *"starting at q0 and jumping only on ε, I can reach q0, q1, q2, q3."*
Note every closure **includes its own state** — that is by definition, not an accident.

### 3. The logic
Closure is naturally **recursive**: "the closure of q is q, plus the closure of every state
reachable from q by one ε-move."

```
closure(q) = { q } ∪ { closure(p) | there is an ε-transition q → p }
```

Three design decisions carry the whole program:

**(a) Where to store the answer.** Not as a list of sets, but as one **n × n boolean matrix**
`closure[state][j]`. `closure[s][j] = 1` means "j is in the closure of s". This makes printing
a trivial double loop and makes the "have I been here?" test a single array lookup.

**(b) The two parameters.** `findClosure(state, current)`:
- `state` = **whose closure we are computing** — fixed for the whole call, never changes
- `current` = **where the walk is right now** — this is what changes as we recurse

That separation is the whole trick. Without it you couldn't tell "who am I collecting for" from
"where am I standing".

**(c) Termination.** A cycle like `q1 --ε--> q2 --ε--> q1` would recurse forever. The code
uses **the answer matrix itself as the visited set**: it marks `closure[state][current] = 1`
*before* recursing, and only recurses `if closure[state][i] == 0`. So a state already in the
closure is never visited again → the walk terminates.

Notice this is *different* from the sibling program `nfa.c` in `~/output_recon/code/`, which
used a separate `visited[]` array and a `member[]` list. Both work; this version is leaner.
Know both, because an examiner may ask "how do you avoid the infinite loop?"

### 4. Edge cases
| Edge case | What would break | How the code accounts for it |
|---|---|---|
| **cycles of ε-moves** (q1→q2→q1) | infinite recursion → stack overflow | `closure[state][i] == 0` test: an already-marked state is never re-entered. This is *the* edge case of this experiment |
| a **self-loop** ε(q→q) | would recurse into itself forever | harmless: `closure[state][state]` is set to 1 *before* the loop, so the guard blocks the re-entry |
| a state with **no ε-moves** | closure would be empty | the function marks itself first, so `E-closure(q) = { q }` — never empty |
| ε reaching many states transitively | a non-recursive one-pass loop would miss them | recursion follows the chain all the way down |
| an ε-transition *into* an already-closed state | duplicate entries | the matrix stores a *flag*, so duplicates are structurally impossible — unlike a list where you'd need a `seen` check |
| **n > 20** | `epsilon[20][20]` overflows | **not guarded** — the arrays are statically sized. Worth one line in the record |
| reading the matrix | wrong count of values → wrong parse | `scanf` is called exactly `n × n` times in a nested loop: outer `i`, inner `j` |

### 5. Built-ins used (and why)
This program uses almost nothing — deliberately. Its whole content is the recursion, so the
"built-ins" section is about **recursion itself**.

| Item | What it does | Why it's used |
|---|---|---|
| `scanf("%d", &epsilon[i][j])` | reads one integer into a matrix cell | the machine is described as a matrix, so it is read as a matrix |
| `printf` inside a `for` over `j` | prints the states flagged 1 | the answer matrix is already the set — printing is a lookup, no searching |
| **recursion** `findClosure(state, i)` | the function calls itself on the next state | ε-closure is defined recursively; writing it as a loop would need an explicit stack |
| a `for` from 0 to n−1 scanning a row | "for every state reachable from `current`" | reading the matrix row *is* enumerating the outgoing ε-moves. No adjacency list needed |
| the matrix as a **visited mark** | doubles as the dedupe + termination mechanism | one array does two jobs — the elegant part of this program |

### 6. Algorithm — deep pseudocode
```
globals:  n
          epsilon[20][20]      # epsilon[i][j] = 1  ⟺  ε-transition i → j
          closure[20][20]      # closure[s][j]  = 1  ⟺  j ∈ E-closure(s)   (also the visited set)

findClosure(state, current):
    closure[state][current] = 1                 # mark FIRST — this is what stops the cycle
    for i = 0 to n-1:
        if epsilon[current][i] == 1 and closure[state][i] == 0:
            findClosure(state, i)               # recurse only into UNvisited states

main:
    read n
    for i = 0 to n-1:                           # read the n × n matrix
        for j = 0 to n-1:
            read epsilon[i][j]
    for i = 0 to n-1:
        findClosure(i, i)                       # closure of i, starting the walk AT i
    print "Epsilon Closure of all states:"
    for i = 0 to n-1:
        print "E-closure(q" + i + ") = {"
        for j = 0 to n-1:
            if closure[i][j] == 1:  print "q" + j
        print "}"
```
Trace `findClosure(0,0)` on the sample: marks `[0][0]`; sees ε(0,1)=1 and `[0][1]`=0 → recurse
`(0,1)`; marks `[0][1]`; sees ε(1,2)=1 → recurse `(0,2)`; marks `[0][2]`; ε(2,3)=1 → recurse
`(0,3)`; marks `[0][3]`; row 3 is all zeros → return. Result: `{q0,q1,q2,q3}`. ✔

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: ε-closure of every state of an NFA
1. Start.
2. Read n, the number of states.
3. Read the n × n epsilon transition matrix ε, where ε[i][j] = 1 means an ε-move from i to j.
4. Initialise the closure matrix to 0.
5. For each state s from 0 to n-1: call findClosure(s, s).
6. For each state s, print every j with closure[s][j] = 1 as E-closure(qs).
7. Stop.

Function findClosure(state, current):
   1. Mark closure[state][current] = 1.
   2. For every state i from 0 to n-1:
        if ε[current][i] = 1 and closure[state][i] = 0 → findClosure(state, i).
```

### ▶ Verified output
Input `4` + the matrix above → `E-closure(q0) = { q0 q1 q2 q3 }`,
`E-closure(q1) = { q1 q2 q3 }`, `E-closure(q2) = { q2 q3 }`, `E-closure(q3) = { q3 }`

---

## Exp 6 — Conversion of ε-NFA to NFA  ·  `e-nfa_nfa.c`

### 1. Why this exists
Exp 5 gave you the closures. Now use them to **delete the ε-transitions**.

Why delete them? Because a machine with ε-moves is awkward to simulate: at every step you'd
have to remember "also teleport wherever ε leads". It is cleaner to **absorb the teleports into
the symbol moves**, producing a machine where every transition reads a real character. The
language accepted is *exactly* the same — that's the point of the conversion.

### 2. Input → target output
**Input (interactive, in this exact order):**
1. number of states `n`
2. number of input symbols `m`
3. the `m` symbols (e.g. `a b`)
4. for each state: **how many states are in its E-closure**, then those states
   *(this is Exp 5's output, hand-fed in)*
5. for each state and each symbol: **how many destinations**, then the destination states

**Target output:** the new, ε-free transition for every (state, symbol) pair.
```
δ'(q0,a) = { q1 q2 }
δ'(q0,b) = { q0 q1 q2 }
δ'(q1,a) = { q2 }
δ'(q1,b) = { q2 }
δ'(q2,a) = { }
δ'(q2,b) = { q2 }
```

### 3. The logic
The whole experiment is **one formula**, written in terms of Exp 5's closure:

> **δ'(q, a) = ε-closure( ⋃ over p ∈ ε-closure(q) of δ(p, a) )**

In words, and this is how to remember it — **three moves in order:**
1. **Teleport free** — from q, go everywhere ε allows: that's `ε-closure(q)`.
2. **Read the symbol** — from each of those states, take the `a`-move: that's `δ(p, a)`.
3. **Teleport free again** — from every state you landed on, take its ε-closure.

The result is a set, so δ' is a *set-valued* transition — the machine is still an NFA, just one
with no ε-moves. (Removing ε does **not** make it deterministic. Determinism is Exp 7's job —
this is the single most common misconception here.)

**Why the nested loops map exactly onto the formula** — this correspondence is what makes the
code readable:
```
for p in ε-closure(q)          ← step 1 (teleport free)
    for q2 in δ(p, a)          ← step 2 (read the symbol)
        add ε-closure(q2)      ← step 3 (teleport free again)
```

### 4. Edge cases
| Edge case | How it's handled |
|---|---|
| **the result is empty** (no state in the closure has an `a`-move) | `rcount` stays 0 and the code prints `{ }` — an empty set. Verified: `δ'(q2,a) = { }`. This is *correct*, not a bug: it means "no move on a" |
| **the same state arriving from two different sources** | `addState()` checks the whole array before appending — a **linear-search dedupe**. Without it, `{ q1 q1 q2 }` would print. This is the whole job of the helper |
| a destination state's E-closure | step 3 must add *all* of `ε-closure(q2)`, not just `q2` itself — a very easy thing to get wrong |
| a state with **no transitions** on some symbol | `trans[state][j][0] == 0`, so the inner loop `for x = 1; x <= 0` never runs → contributes nothing |
| a state with **no ε-moves** | `ecount[i] == 1` (just itself), so the outer loop runs once with `p = i` — naturally correct |
| **n or m > 10** | `MAX = 10`, arrays are `[10][10][10]` → overflow, **not guarded** |
| **ordering of the output set** | the states print in **discovery order**, not sorted. (The sibling program `nfa_with_e.c` in `~/output_recon` *does* sort. Both are correct; know which you're presenting.) |
| closure not supplied (Exp 5 skipped) | the program **assumes** the closure is given as input. It cannot compute it — that's Exp 5's job |

### 5. Built-ins used (and why)
| Item | What it does | Why it's used here |
|---|---|---|
| `addState(arr, &count, state)` (**own helper**) | appends only if absent — linear scan then write | sets must not have duplicates; C has no set type, so you write the dedupe |
| the `&count` argument (pointer to `int`) | lets the helper **increase the caller's counter** | C passes by value; to let a function grow the caller's array-length you must pass the address |
| `scanf` in nested loops | fills the 3-D array `trans[state][symbol][k]` | δ is a 3-D relation: source, symbol, destination |
| `trans[i][j][0]` storing the **count** | index 0 of each row holds "how many destinations follow" | keeps the array rectangular and self-describing — you always know where the row ends |
| `printf` + a loop over `result[]` | prints the set | the set is a plain array plus its count |
| `ε-closure` reuse | conceptually the output of Exp 5 | this program *demonstrates the dependency*; say that in the record |

### 6. Algorithm — deep pseudocode
```
globals: n, m, symbols[10]
         trans[10][10][10]     # trans[state][symbolIdx][0] = count, [1..count] = destinations
         eclose[10][10]        # eclose[state][k] = k-th member of E-closure(state)
         ecount[10]            # ecount[state]   = size of E-closure(state)

addState(arr, *count, state):            # set-insert with dedupe
    for i = 0 to *count-1:
        if arr[i] == state: return       # already present → do nothing
    arr[*count] = state                  # else append
    (*count)++

main:
    read n;  read m;  read the m symbols
    for i = 0 to n-1:                    # step A: closures come IN as data (Exp 5's output)
        read ecount[i]
        for j = 0 to ecount[i]-1: read eclose[i][j]
    for i = 0 to n-1:                    # step B: the ε-NFA's transitions
        for j = 0 to m-1:
            read trans[i][j][0]                  # count of destinations
            for k = 1 to trans[i][j][0]: read trans[i][j][k]

    print "Equivalent NFA without epsilon transitions:"

    for i = 0 to n-1:                    # step C: apply δ'(q,a) = E( ⋃ E(δ(p,a)) )
        for j = 0 to m-1:
            result[MAX], rcount = 0

            for k = 0 to ecount[i]-1:                    # ← teleport free
                state = eclose[i][k]
                tcount = trans[state][j][0]
                for x = 1 to tcount:                     # ← read the symbol
                    next = trans[state][j][x]
                    for y = 0 to ecount[next]-1:         # ← teleport free again
                        addState(result, &rcount, eclose[next][y])

            print "d'(q" + i + "," + symbols[j] + ") = { "
            for k = 0 to rcount-1: print "q" + result[k]
            print "}"
```
Point at the three innermost loops and say *"teleport — read — teleport"*; that is the answer.

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Convert an ε-NFA into an equivalent NFA without ε-transitions
1. Start.
2. Read n (number of states), m (number of input symbols) and the m symbols.
3. Read the E-closure of each state: for each state, a count followed by the states in it.
4. Read the transitions: for each state and symbol, a count followed by the destination states.
5. For each state i and each input symbol a:
   a. Set result = empty.
   b. For each state p in E-closure(i):
        for each destination q in δ(p, a):
            add every state of E-closure(q) to result, skipping duplicates.
   c. Print δ'(qi, a) = result.
6. Stop.
```

### ▶ Verified output
With n=3, symbols `a b`, closures {0,1,2} {1,2} {2}, and the sample transitions →
`δ'(q0,a) = { q1 q2 }`, `δ'(q0,b) = { q0 q1 q2 }`, `δ'(q1,a) = { q2 }`, `δ'(q1,b) = { q2 }`,
`δ'(q2,a) = { }`, `δ'(q2,b) = { q2 }`

---

## Exp 7 — Conversion of NFA to DFA (subset construction)  ·  `nfa_dfa.c`

### 1. Why this exists
Exp 6 removed the ε-moves, but the machine is **still non-deterministic**: from `q1` on `b` it
may go to `q1` *or* `q2`. And here is the fundamental problem:

> **A computer cannot be in two states at once, and it cannot guess.**

So an NFA is **not directly runnable**. The repair is a change of viewpoint, and it is the single
best idea in this group:

> **If the machine might be in {q1, q2}, then let {q1, q2} itself BE one state of a new machine.**

Now there is nothing to guess: the machine is always in exactly one state — a *set* — and each
set has exactly one successor per symbol. That new machine is a **DFA**, and a DFA is what
LEX's generated scanner actually runs.

### 2. Input → target output
**Input:** `n`; `m`; the `m` symbols; then for every state and symbol, a count followed by the
destination states (a plain, ε-free NFA).

**Target output:** the DFA transition table, each state labelled by the set it stands for.
```
DFA State       a               b
{q0}            {q0}            {q1}
{q1}            {q0}            {q1,q2}
{q1,q2}         {q0,q2}         {q1,q2}
{q0,q2}         {q0,q2}         {q1}
```

### 3. The logic
The rules of the construction:
- The **start state is {q0}** — the set containing the NFA's start state.
- For a DFA state **S** and symbol **a**: *δ_DFA(S, a) = the union of δ(p, a) over every p in S.*
- If that union is a set you have **not seen before, it becomes a new DFA state** — append it and keep processing.

Read the table above as a story: start at `{q0}`; on `a` everything goes to `q0` → `{q0}`; on `b`
`q0` goes to `q1` → `{q1}`. From `{q1}` on `b` we get `q1` **and** `q2` → the brand-new state
`{q1,q2}`, which must then be processed in its own right. That is why the table has 4 rows from
a 3-state NFA.

**Set equality is the crux.** Two DFA states are the same state only if their sets contain
**exactly** the same members. `{q1,q2}` and `{q2,q1}` are the same set — but compared
element-by-element, position 0 differs. Hence the code **sorts each new set** before storing it
(step c below). Without that sort the DFA explodes into spurious duplicate states.

**The worklist loop.** The construction needs a queue of "sets discovered but not yet
processed". This program uses the **set list itself as that queue**:
`for (i = 0; i < nSets; i++)` — and `nSets` **grows while the loop runs**. New sets are appended
and therefore get processed in the same pass. That is a genuine subtlety; it is effectively a
BFS with `setList` as the queue.

**Three helpers do all the set work:**
- `sameSet(A, B)` — do two sets have identical members? (sizes must match, then member-by-member)
- `findSet(S)` — has this set already become a DFA state? → its index, or −1
- `addSet(S)` — return the existing index, or store S as a new DFA state and return the new index

### 4. Edge cases
| Edge case | What would break | How the code accounts for it |
|---|---|---|
| **the same set reached by two different paths** | a DFA with duplicated states — the classic failure | `findSet` searches all existing sets before `addSet` appends; identical sets collapse to one state |
| **member order differing** (`{q1,q2}` vs `{q2,q1}`) | `sameSet` compares positionally → they'd look different → duplicate states | each new set is **sorted ascending** (bubble sort of `tmp`) before being stored, so equal sets are byte-identical |
| **an empty set** (some state has no move on a symbol) | it is a legitimate DFA state — the **trap / dead state** | `addSet(tmp, 0)` is allowed: `sameSet` with two empty sets returns 1 (the comparison loop simply doesn't execute), so exactly **one** empty state is ever created, and it prints as `{}` |
| the DFA having **fewer** states than the NFA | expected | only reachable subsets appear — unreachable NFA states never generate a DFA state |
| the DFA having **more** states than the NFA | expected | the table above: 3 NFA states → 4 DFA states |
| infinite looping | appending sets forever | every new set is either already in the list (`findSet` ≠ −1) or genuinely new; the number of subsets of n states is finite (≤ 2ⁿ), so it terminates |
| **n, or the number of DFA states > 200** | `setList[200][10]` overflow | **not guarded**; the 200 is the stated subset cap |
| a state with **more than 10 destinations** | `trans[10][10][11]` — index 0 is the count, so only 10 fit | overflow, not guarded |
| declaring a variable **inside** a `for` body | illegal in C89 | `int q = trans[p][j][idx], seen = 0;` is C99 (a block-scope declaration). Fine with modern gcc, worth knowing the rule |

### 5. Built-ins used (and why)
| Item | What it does | Why it's used here |
|---|---|---|
| `sameSet`, `findSet`, `addSet` (**own**) | set equality, set lookup, set insertion | C has no sets; these three *are* the algorithm |
| `sprintf(out + k, "q%d", s[i])` | writes formatted text **at an offset**, returns how many chars it wrote | builds the label `{q0,q1}` piece by piece; the returned length advances `k` so the next piece appends after it. A neat use of sprintf's return value |
| the bubble sort (`for a`, `for b > a`, swap) | sorts the new set ascending | makes equal sets compare equal element-by-element |
| `trans[p][j][idx]` with `idx` from 1 | the destinations, skipping index 0 | index 0 is the count, not a state |
| `addSet(...)` returning an index | the DFA's transition becomes an **integer reference to a state** | tables are indexed by numbers; the sets are only for display |
| `%-16s` in `printf` | left-justified, padded to 16 columns | makes the DFA table line up |

### 6. Algorithm — deep pseudocode
```
globals: n, m, sym[10]
         trans[10][10][11]        # trans[state][sym][0] = count, [1..count] = destinations
         setList[200][10]         # setList[i] = the i-th DFA state, as a set of NFA states
         setSize[200]             # size of each set
         dfa[200][10]             # dfa[i][sym] = index of the next DFA state
         nSets = 0                # how many DFA states exist so far  (grows during the loop)

sameSet(A, na, B, nb):
    if na != nb: return 0
    for i = 0 to na-1: if A[i] != B[i]: return 0
    return 1

findSet(S, ns):                  # linear search over discovered DFA states
    for i = 0 to nSets-1:
        if sameSet(setList[i], setSize[i], S, ns): return i
    return -1                    # not seen before

addSet(S, ns):
    idx = findSet(S, ns)
    if idx != -1: return idx              # already a DFA state → reuse it
    copy S into setList[nSets]; setSize[nSets] = ns
    return nSets++                        # new DFA state → its index, list grows

main:
    read n; read m; read the m symbols
    for i = 0 to n-1: for j = 0 to m-1:
        read trans[i][j][0]                     # count
        for k = 1 to trans[i][j][0]: read trans[i][j][k]

    start[0] = 0;  addSet(start, 1)             # DFA start state = { q0 }

    for i = 0 to nSets-1:                       # NOTE: nSets grows inside the loop
        for j = 0 to m-1:
            tmp[MAX], cnt = 0
            for k = 0 to setSize[i]-1:          # every NFA state in this DFA state
                p = setList[i][k]
                for idx = 1 to trans[p][j][0]:  # union of δ(p, j)
                    q = trans[p][j][idx]
                    if q not already in tmp:  tmp[cnt++] = q     # dedupe
            sort tmp ascending (bubble)         # so equal sets compare equal
            dfa[i][j] = addSet(tmp, cnt)        # reuse or create the DFA state

    print the table: header row of symbols, then
        for each i: label(setList[i]) then for each j: label(setList[dfa[i][j]])
```
### 7. Algorithm — record version (mid-level)
```
ALGORITHM: NFA to DFA conversion (subset construction)
1. Start.
2. Read n, m and the input symbols.
3. Read the NFA transitions: for each state and symbol, a count followed by the destinations.
4. Create the first DFA state = { q0 } and add it to the set list.
5. For each DFA state i in the set list (the list grows as new sets are discovered):
     for each input symbol j:
       a. Set temp = empty.
       b. For each NFA state p in DFA state i: add every destination of δ(p, j) to temp,
          skipping duplicates.
       c. Sort temp so identical sets are always stored in the same order.
       d. dfa[i][j] = addSet(temp)   — reuse the index if temp already exists.
6. Print the DFA transition table, labelling each state by its set, e.g. {q0,q1}.
7. Stop.
```

### ▶ Verified output
n=3, symbols `a b`, transitions δ(q0,a)={0} δ(q0,b)={1} δ(q1,a)={0} δ(q1,b)={1,2} δ(q2,a)={2}
δ(q2,b)={} → the 4-row table shown in §2 above.

---

**Next group:** Group C (Exp 8–10) — where the tokens from Group A finally get *parsed*.
