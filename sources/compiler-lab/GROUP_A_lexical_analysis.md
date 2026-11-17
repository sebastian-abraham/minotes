# GROUP A — Lexical Analysis (Exp 1–4)

Each experiment below is laid out the same way, and in the order knowledge actually arrived:

1. **Why this exists** — what problem forced this program to be written
2. **Input → target output** — what goes in, what must come out
3. **The logic** — how we get from the one to the other
4. **Edge cases** — what can go wrong, and how the code accounts for it
5. **Built-ins used** — what each function does *and why this one*
6. **Algorithm — deep pseudocode** — with the code nuances baked in
7. **Algorithm — record version** — the mid-level one to actually write in your lab record

---

## Exp 1 — Lexical Analyser, hand-written  ·  `input.c`, `lex_a.c`

### 1. Why this exists
A parser wants to reason about `int`, `a`, `+`, `10`, `;`. It does **not** want to reason about
the 13 individual characters `i`,`n`,`t`,` `,`a`,` `,`+`,` `,`1`,`0`,`;` — that would be
absurd. So something must sit in front of the parser and convert *characters* into *words*.
That something is the **lexical analyser (scanner)**, and this is the first experiment because
it is the first phase of a compiler.

This version is hand-written **on purpose**: writing it by hand shows you exactly what LEX
automates in Exp 2 (the pattern matching and the "longest match" rule you're about to see).

### 2. Input → target output
**Input:** an actual C source file named `input.c`, read from disk (not typed). The program
opens it by name, so it must be in the same folder.

`input.c` contains: a `//` comment, a `/* */` comment, declarations, `if`, operators, numbers.

**Target output:** a list of every token classified into one of five categories:
```
Keyword    : int
Identifier : a
Operator   : =
Number     : 10
Symbol     : ;
```
Exactly five labels: `Keyword`, `Identifier`, `Number`, `Operator`, `Symbol`.

### 3. The logic
The core loop reads **one character at a time** and asks "what did I just start?"

- whitespace → nothing, skip
- `/` → **ambiguous!** It could be division, `//` comment, or `/*` comment. You cannot decide from one character — you must peek at the next.
- letter or `_` → you've started an identifier or keyword. You don't know where it ends, so keep reading while the characters are still letters/digits/`_`.
- digit → started a number, keep reading while digits.
- operator char → one-character token, done
- symbol char → one-character token, done

Two ideas do all the work here, and both are what the examiner is probing for:

**(a) The greedy read.** For multi-character tokens you read *until the character no longer fits*, which means you have consumed **one character too many** — the character that told you the token ended.

**(b) The push-back.** That extra character is not yours to swallow; it belongs to the next token. So you give it back with `ungetc()`. This is called **lookahead with one-character pushback**, and every real scanner does it.

**(c) Keyword vs identifier.** They have the *same shape* — `int` and `a` both look like "letter then letters". The only difference is that `int` appears in a fixed list. So you classify by shape first, then check the list.
*Why check the list rather than handle keywords as their own pattern?* Because if you wrote a rule for `int` specifically, `intx` would still match the identifier rule — but you'd need one rule per keyword. Shape-first is what LEX also does (see Exp 2's tie-break).

### 4. Edge cases
| Edge case | What would break | How the code handles it |
|---|---|---|
| `//` comment | the `/` would be reported as an operator, and the comment text would be tokenised as code | read lookahead; if it's `/`, loop until `\n` — **emits nothing** |
| `/* ... */` spanning lines | same, plus you must find the *closing* pair | track the previous character; stop when `prev=='*' && ch=='/'` |
| plain division `a / b` | the lookahead character (`b` or space) got consumed and is now lost | `ungetc(next, fp)` pushes it back before reporting `/` |
| last token at end of file | after reading `abc`, `fgetc` returns `EOF` — which is `-1`, not a character | the read loops test `!= EOF` so they stop cleanly, and the `if (ch != EOF)` guard prevents pushing `EOF` back |
| the lookahead at EOF | `ungetc(EOF, fp)` would be a bug | guarded by `if (ch != EOF) ungetc(ch, fp);` |
| **`input.c` missing** | `fopen` returns `NULL` → the very first `fgetc` **segfaults** | **NOT handled** in `lex_a.c` — there is no `if (fp == NULL)` check. Know this: it is a real hole (the sibling program `token.c` *does* check). Worth mentioning as "the version in the record omits this check" |
| `char ch` holding `EOF` | `fgetc` returns `int`; `EOF` is `-1`. Storing in a plain `char` can, on platforms where `char` is unsigned, make the `!= EOF` test **never true → infinite loop** | `lex_a.c` declares `char ch`. It happens to work here, but the *correct* declaration is `int ch`. Excellent "why" answer if asked |
| token longer than the buffer | `char buffer[100]` has no bounds check → overflow | not guarded; note it |

### 5. Built-ins used (and why this one)
| Function | What it does | Why it's used here |
|---|---|---|
| `fopen("input.c","r")` | opens a file, returns a `FILE *` | we need to read a file, not stdin |
| `fgetc(fp)` | reads **one** character, returns `int`, or `EOF` at end | the whole scanner is character-driven |
| `ungetc(c, fp)` | **pushes one character back** into the stream | undoes the lookahead read — without this the scanner cannot correct itself |
| `fclose(fp)` | closes the file, releases the handle | clean shutdown |
| `isalpha(c)` | true if `c` is a letter | decides "identifier might be starting" |
| `isdigit(c)` | true if `c` is `0`–`9` | decides "number is starting" / "number continues" |
| `isalnum(c)` | letter **or** digit | decides "identifier continues" (`abc123` is one token) |
| `strchr(set, c)` | returns non-NULL if `c` is inside the string `set` | used as a **membership test against a character set** — `strchr("+-*=<>!%", ch)` reads as "is this an operator?" Much shorter than a `switch` with 8 cases |
| `strcmp(a, b)` | returns `0` when the two strings are equal | comparing a token against each keyword |
| `sizeof(keywords)/sizeof(keywords[0])` | total bytes ÷ one element = array length | so the keyword loop doesn't hardcode a count |
| `printf` | formatted output | printing each token's class and text |

### 6. Algorithm — deep pseudocode
```
isKeyword(word):
    for each k in keywords:            # keywords[] = {int, float, char, if, else, while,
        if strcmp(word, k) == 0:       #                for, return, void, break, continue,
            return 1                   #                double, main}
    return 0

main:
    fp = fopen("input.c", "r")
    # (no NULL check here — a real gap; token.c has it)

    while (ch = fgetc(fp)) != EOF:                    # ch is declared char, not int (nuance)

        if ch is ' ' or '\t' or '\n':  continue       # whitespace produces no token

        if ch == '/':
            next = fgetc(fp)
            if next == '/':                           # single-line comment
                while (ch = fgetc(fp)) != '\n' and ch != EOF: pass
                continue                              # nothing emitted
            elif next == '*':                         # multi-line comment
                prev = 0
                while (ch = fgetc(fp)) != EOF:
                    if prev == '*' and ch == '/': break
                    prev = ch
                continue
            else:                                     # it really was division
                print "Operator : /"
                ungetc(next, fp)                      # give back the lookahead
                continue

        if isalpha(ch) or ch == '_':                  # start of identifier/keyword
            i = 0
            buffer[i++] = ch
            while (ch = fgetc(fp)) != EOF and (isalnum(ch) or ch == '_'):
                buffer[i++] = ch                      # greedy read — one char too far
            buffer[i] = '\0'
            if ch != EOF: ungetc(ch, fp)              # push the lookahead back
            if isKeyword(buffer): print "Keyword    : " + buffer
            else:                 print "Identifier : " + buffer

        elif isdigit(ch):                             # start of number
            i = 0
            buffer[i++] = ch
            while (ch = fgetc(fp)) != EOF and isdigit(ch):
                buffer[i++] = ch
            buffer[i] = '\0'
            if ch != EOF: ungetc(ch, fp)
            print "Number     : " + buffer

        elif strchr("+-*=<>!%", ch):  print "Operator   : " + ch
        elif strchr("(){}[];,." , ch): print "Symbol     : " + ch

    fclose(fp)
```
**The three lines that carry the whole experiment:** the greedy `while`, the `ungetc`, and the `isKeyword` test.

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Lexical Analysis (hand-written)
1. Start.
2. Open the source file input.c in read mode.
3. Read one character ch at a time until end of file:
   a. If ch is a blank, tab or newline — ignore it.
   b. If ch is '/', read the next character:
        - next is '/', skip until end of line (single-line comment);
        - next is '*', skip until the pair '*' '/' (multi-line comment);
        - otherwise push the lookahead back and report '/' as an operator.
   c. If ch is a letter or '_', collect it and every following letter/digit/'_' into a buffer.
      Compare the buffer with the keyword list — print "Keyword" if found, else "Identifier".
   d. If ch is a digit, collect it and every following digit and print "Number".
   e. If ch is one of + - * = < > ! % — print "Operator".
   f. If ch is one of ( ) { } [ ] ; , . — print "Symbol".
4. Close the file.
5. Stop.
Helper: isKeyword(word) — compares word with each keyword using strcmp.
```

### ▶ Verified output
`gcc lex_a.c && ./a.out` with `input.c` present — one token per line:
`Keyword int` → `Keyword main` → `Symbol (` → `Symbol )` → `Symbol {` → `Keyword int` → `Identifier a`
→ `Operator =` → `Number 10` → `Symbol ;` → `Keyword float` → `Identifier b` → `Operator =`
→ `Number 20` → `Symbol ;` → `Keyword if` → `Symbol (` → `Identifier a` → `Operator <`
→ `Identifier b` → `Symbol )` → `Symbol {` → `Identifier a` → `Operator =` → `Identifier a`
→ `Operator +` → `Number 1` → `Symbol ;` → `Symbol }` → `Keyword return` → `Number 0`
→ `Symbol ;` → `Symbol }`

---

## Exp 2 — Lexical Analyser using LEX  ·  `lexer.l`

### 1. Why this exists
Exp 1 works, but look at the cost: you hand-wrote the greedy reads, every `ungetc`, the keyword
comparison loop. Replace that file with a 30-rule grammar and the code becomes unmaintainable.

**LEX** is a *generator*: you declare the *patterns* (regular expressions) and the *actions*,
and LEX **builds a DFA from all the patterns at once** and emits the C code (`lex.yy.c`) that
runs it. This is the moment in the course where "regular expressions" stop being a topic and
become the actual tool used by the scanner.

### 2. Input → target output
**Input:** a C program typed at stdin (NOT a file this time — the generated scanner reads stdin).

**Target output:** the same classification job as Exp 1, but with these labels:
```
Keyword : int
Identifier : a
Operator : =
Number : 2
Special Symbol : ;
```
Note the labels differ from Exp 1 — `Special Symbol` (not `Symbol`) and no padding. In this
version whitespace is *deliberately* ignored by a rule with an empty action.

### 3. The logic
A `.l` file has **three sections**, separated by `%%`:

```
%{ definitions (C headers, globals) %}      ← %option noyywrap also lives here
%%
rules:   pattern    { action }              ← one per line
%%
user code:  main() { ... yylex(); ... }
```

The logic is: **for each pattern, say what to do when it matches.** Compare with Exp 1:

| Exp 1 (hand-written) | Exp 2 (LEX) |
|---|---|
| `if (isalpha(ch) \|\| ch=='_')` + greedy loop + `ungetc` | `[a-zA-Z_][a-zA-Z0-9_]*` |
| keyword `strcmp` loop | one rule listing the keywords, written **first** |
| `while(...) fgetc` | handled by the generated DFA |

The regular expressions, in words:
- `[a-zA-Z_][a-zA-Z0-9_]*` — a letter or `_`, then any number (**including zero**) of letters/digits/`_`. The `*` is what makes a single `a` valid.
- `[0-9]+` — one **or more** digits. `+` means at least one, so `0` alone is a number.
- `"int"` — the quotes mean *literal text*, not the pattern `i`,`n`,`t` as three separate class-memberships.

**The keyword-vs-identifier collision — and how LEX resolves it.** `int` matches *both* the
keyword rule and the identifier rule. Lex applies two rules, in this order:
1. **Longest match wins.** Whichever pattern consumes more characters wins.
2. **On a tie, the rule written first wins.**

Since `int` matches both with the *same length*, rule 2 decides it — and the keyword rule is
written above the identifier rule. **That ordering is not cosmetic; it is the mechanism.** Move
the identifier rule up and `int` prints as `Identifier`.

### 4. Edge cases
| Edge case | How it's handled |
|---|---|
| `int` matching two rules | longest-match, then **first-rule** tie-break; keyword rule sits above identifier rule |
| whitespace producing tokens | `[ \t\n]+  ;` — a rule with an **empty action** (just `;`) is the idiom for "match and discard" |
| a character matching *no* rule | the final catch-all `.  ;` swallows it silently — without this, unmatched input is echoed to stdout by default |
| end of input / wrap-up | `%option noyywrap` suppresses the need for a `yywrap()` function; otherwise LEX calls `yywrap()` at EOF |
| guesses that LEX cannot express | LEX patterns are **regular expressions only** — no nesting, no counting. `ab^n c^n` is impossible. This is *the* limitation that motivates parsing (Exp 8–10) |

### 5. Built-ins / LEX constructs used (and why)
| Item | What it is | Why |
|---|---|---|
| `yylex()` | the generated scanner function | you call it once; it loops internally, matching rule after rule, until EOF |
| `yytext` | the **text that matched** | that's the identifier/keyword/number you print |
| `yyleng` | length of `yytext` (`int`) | used in Exp 3 to count characters |
| `%option noyywrap` | tells the generated scanner not to call `yywrap()` | saves you writing a dummy function |
| `%%` | section separator | splits definitions / rules / user code |
| `%{ ... %}` | verbatim C to copy into the output | where headers and global variables go |
| the DFA inside `lex.yy.c` | generated automaton | this is the "hidden" Exp 5/7 machinery — LEX literally builds an automaton for you |
| `lex lexer.l` | the generator | translates patterns → `lex.yy.c` |
| `gcc lex.yy.c` | compiles the generated scanner | `lex.yy.c` is ordinary C |

### 6. Algorithm — deep pseudocode
```
lexer.l structure:

%option noyywrap
%{
#include <stdio.h>
%}

%%
   <keyword set>        { printf("Keyword : %s\n", yytext); }
   [a-zA-Z_][a-zA-Z0-9_]*  { printf("Identifier : %s\n", yytext); }
   [0-9]+               { printf("Number : %s\n", yytext); }
   "+"|"-"|"*"|"/"|"="|"<"|">"   { printf("Operator : %s\n", yytext); }
   ";"|","|"("|")"|"{"|"}"       { printf("Special Symbol : %s\n", yytext); }
   [ \t\n]+             ;        # empty action = discard
   .                    ;        # catch-all = discard anything unmatched
%%

int main() {
    printf("Enter a C program:\n");
    yylex();                      # runs the whole scan
    return 0;
}

# build:  lex lexer.l  →  gcc lex.yy.c  →  ./a.out
```
Lex's internal algorithm, worth stating in words because it *is* Exp 7's algorithm:
*the patterns are combined into one NFA, converted to a DFA (Exp 6 + Exp 7), and the DFA is
simulated; the DFA simultaneously tracks the longest match found so far so that rule 1 is
enforced.*

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Lexical Analysis using LEX
1. Start.
2. In the definitions section declare the required headers and global variables.
3. In the rules section write a pattern–action pair for each token class:
   a. keywords — print "Keyword";
   b. [a-zA-Z_][a-zA-Z0-9_]* (identifier) — print "Identifier";
   c. [0-9]+ (number) — print "Number";
   d. operators + - * / = < > — print "Operator";
   e. special symbols ; , ( ) { } — print "Special Symbol";
   f. blanks, tabs and newlines — no action.
4. In the user-code section write main() which calls yylex().
5. Generate the scanner with lex and compile the generated lex.yy.c with gcc.
6. Run the program; yylex() applies the longest matching rule.
7. Stop.
```

### ▶ Verified output
Input `int a = a+b*2;` →
`Keyword : int` / `Identifier : a` / `Operator : =` / `Identifier : a` / `Operator : +` /
`Identifier : b` / `Operator : *` / `Number : 2` / `Special Symbol : ;`

---

## Exp 3 — Count lines, words and characters using LEX  ·  `lex_count.l`

### 1. Why this exists
Exp 2 used LEX to *label* tokens. This experiment proves the second half of the LEX claim: **an
action can be any C code, including updating counters.** So you can also use a scanner to
*measure* text. It also demonstrates that `yyleng` removes the need to count characters one at
a time — you get the length of every match for free.

### 2. Input → target output
**Input:** free text typed at stdin, ended with **Ctrl+D** (EOF).

**Target output:** three numbers.
```
Number of lines      : 2
Number of words      : 5
Number of characters : 24
```

### 3. The logic
Everything hinges on one rule: **every rule must account for the characters it consumed.**
Since LEX hands each match to exactly one rule, if each rule adds *its own* `yyleng` (or `1`),
the total is complete by construction — you never need to look at the input twice.

Why 24 for `Hello world\nThis is Lex\n`? `Hello world` = 11, newline = 1, `This is Lex` = 11,
newline = 1 → 24. The newline rule counts as *both* a line and a character; the whitespace rule
counts only characters; the word rule counts a word *and* its characters.

The word pattern `[a-zA-Z0-9]+` means a word is a run of alphanumerics. So `This` is one word,
`is` another, `Lex` another, `Hello` and `world` two — total 5.

### 4. Edge cases
| Edge case | How it's handled |
|---|---|
| end of input | **Ctrl+D** sends EOF; `yylex()` returns and `main` prints the totals. Typing Enter does *not* end it |
| punctuation like `Hello,` | `,` is not in the word class, so it matches the catch-all `.` rule → counted as a character, **not** as part of the word |
| a lone number `2026` | `[a-zA-Z0-9]+` — the word class includes digits, so it counts as **one word**. Know this if asked "how many words is `a1b2`?" → one |
| leading/multiple spaces | `[ \t]+` — the `+` matches a *run* of spaces as one match, and `yyleng` credits all of them at once |
| newlines inside words | impossible — `\n` is excluded from the class, so words never span lines |
| tabs | the whitespace class `[ \t]+` covers tabs, so tab-width never matters for counting |

### 5. Built-ins used (and why)
| Item | What / Why |
|---|---|
| `lines`, `words`, `characters` | **global** counters declared in the `%{ %}` block, so every rule's action can reach them |
| `yyleng` | number of characters in the current match. **Why:** the rules never see raw characters, so the match's length is the only way to know how many characters were consumed |
| `yylex()` | runs the scan to EOF |
| `\n` inside a pattern | a newline character in a regular expression — the line counter's trigger |
| `.` (dot) | matches **any single character** — the catch-all for punctuation and anything not covered above |

### 6. Algorithm — deep pseudocode
```
%{
#include <stdio.h>
int lines = 0, words = 0, characters = 0;
%}

%%
   \n             { lines++;  characters++; }                  # a line ends AND it is a char
   [ \t]+         { characters += yyleng;   }                  # a run of blanks, all counted
   [a-zA-Z0-9]+   { words++;  characters += yyleng; }           # a word; its letters count too
   .              { characters++;           }                  # anything else is one char
%%

int yywrap() { return 1; }        # 1 = "no more input, stop" (this file did not use noyywrap)

int main() {
    printf("Enter the text:\n");
    yylex();
    printf("\nNumber of lines      : %d\n", lines);
    printf("Number of words      : %d\n", words);
    printf("Number of characters : %d\n", characters);
    return 0;
}
```
The invariant to say out loud: **every input character is credited to exactly one rule, so the
character total is always right.**

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Count lines, words and characters using LEX
1. Start.
2. Declare global counters lines = 0, words = 0, characters = 0.
3. Write the rules:
   a. newline — lines++ and characters++;
   b. blanks and tabs — characters = characters + yyleng;
   c. a word (one or more letters/digits) — words++ and characters = characters + yyleng;
   d. any other single character — characters++.
4. Write main(): print a prompt, call yylex(), then print the three counters.
5. Compile using lex and gcc, run, type the text and press Ctrl+D to signal end of input.
6. Stop.
```

### ▶ Verified output
Input `Hello world` ⏎ `This is Lex` ⏎ Ctrl+D → `2` lines, `5` words, `24` characters.

---

## Exp 4 — Valid identifier check using LEX + YACC  ·  `lex_id.l`, `yacc_id.y`

### 1. Why this exists
This is the pivotal step in the course. Exp 2 and 3 proved that LEX can recognise tokens —
and also proved what LEX **cannot** do:

> LEX can tell you `a` is a letter and `1` is a digit. It **cannot** tell you that `abc123` is a
> valid name while `123abc` is not.

Why not? Because "first character must be a letter" is a statement about the **order and
arrangement** of tokens, and LEX patterns are regular expressions, which cannot count or
remember position. **Structure is a different kind of question.** Answering it needs a
**grammar**, and a **parser** (YACC) to apply it.

So this experiment is the handover: **LEX chops characters into tokens → YACC judges their
sequence.** Two programs, each with one job.

### 2. Input → target output
**Input:** an identifier typed at stdin (`abc123`, `123abc`...).

**Target output:**
```
Enter an identifier: abc123
Valid Identifier
123abc
Invalid Identifier
```

### 3. The logic
Split the problem in two:

**Part 1 — `lex_id.l` (tokeniser).** Don't return "letter" as a *value*; return it as a
**token code**: `return LETTER;` and `return DIGIT;`. These are numbers that YACC understands.
The lexer deliberately does *no* judgement — a letter is a letter whether it's first or fifth.

**Part 2 — `yacc_id.y` (parser).** State the rule as a grammar:

```
start      : identifier '\n'
identifier : LETTER
           | identifier LETTER
           | identifier DIGIT
```

Read the third line as a recursive definition: *"an identifier followed by one more digit is
still an identifier."* Tracing `abc123`:

```
LETTER(a)  → identifier            (2nd rule)
           → identifier LETTER(b)  (3rd rule → "ab")
           → identifier LETTER(c)  (→ "abc")
           → identifier DIGIT(1)   (4th rule → "abc1")
           → identifier DIGIT(2)   (→ "abc12")
           → identifier DIGIT(3)   (→ "abc123")
then '\n' completes `start` → Valid
```

Now trace `123abc`: the **first** token is `DIGIT`. But every rule for `identifier` must
*start* from `LETTER` — the only base case is `identifier : LETTER`. There is no way to even
begin, so no derivation exists, `yyparse` fails, and YACC calls **`yyerror()`**.

**Why `identifier` appears on both sides of the rule** — this is **left recursion**. YACC
prefers it (LALR parsers handle left recursion in constant stack space), and every real grammar
for a list is written this way. It is also why the rule is *not* written
`identifier : LETTER identifier`, which would be right recursion and would build the string
backwards.

### 4. Edge cases
| Edge case | How it's handled |
|---|---|
| `abc123` | valid — letters then digits, both allowed *after* the first position |
| `123abc` | invalid — first token is `DIGIT`, and no rule starts with `DIGIT` |
| a single letter `a` | valid — the base rule `identifier : LETTER` covers the one-character case |
| uppercase `ABC` | valid — `[a-zA-Z]` covers both cases |
| empty input (just Enter) | the lexer returns `'\n'` immediately; `identifier` cannot derive the empty string, so → Invalid |
| underscore `_ab` | **invalid here** — `[a-zA-Z]` does not include `_` (C allows it; this grammar doesn't). Know the difference if asked |
| `abc def` (a space) | the lexer's catch-all returns the space as a character token, which no rule accepts → Invalid |
| the newline in `start : identifier '\n'` | **why is it there?** Without it, `yyparse` would not know when the identifier has ended; the `\n` is the signal "the name is complete" |
| missing `y.tab.h` | the lexer includes `"y.tab.h"` for `LETTER`/`DIGIT`. That file only exists if yacc was run with **`-d`** — hence the flag |
| linking failure | `-ll` links the lex library; on a **flex** system the library is `-lfl` (verified: this machine needed `-lfl`) |

### 5. Built-ins / tool constructs used (and why)
| Item | What / Why |
|---|---|
| `return LETTER;` (in lex) | hands a **token code** to the parser instead of printing. This is the interface between the two tools |
| `return yytext[0];` | returns the **actual character** as its own token code — for single characters like `\n` this is the convention (they need no `%token` declaration) |
| `%token LETTER DIGIT` (in yacc) | declares the names; yacc assigns them numbers and writes them into `y.tab.h` |
| `yyparse()` | the generated parser — you call it and it drives the whole parse |
| `yylex()` | called **by** `yyparse()` to fetch the next token (that's the handover) |
| `yyerror()` | yacc calls this when the sequence breaks the grammar — our "Invalid Identifier" |
| `|` (in the grammar) | "or" — alternatives for the same left-hand side |
| `yacc -d yacc_id.y` | generates `y.tab.c` **and** `y.tab.h` (the `-d` = definitions header) |
| `lex lex_id.l` | generates `lex.yy.c` |
| `gcc y.tab.c lex.yy.c -ll` | links the two generated files plus the lex library |

### 6. Algorithm — deep pseudocode
```
=========== lex_id.l — PART 1: characters → tokens ===========
%{
#include "y.tab.h"          # LETTER and DIGIT come from here (needs yacc -d)
%}
%%
   [a-zA-Z]   { return LETTER; }        # a letter → ITS CLASS, not its value
   [0-9]      { return DIGIT;  }
   \n         { return '\n';   }        # end-of-name signal
   .          { return yytext[0]; }     # anything else → itself
%%
   # no main() and no yywrap() here — yacc supplies main, and the tokens are enough

=========== yacc_id.y — PART 2: tokens → judgement ===========
%{
#include <stdio.h>
int yylex(void); int yyerror(char *s);
%}
%token LETTER DIGIT

%%
start      : identifier '\n'   { printf("Valid Identifier\n"); }
           ;
identifier : LETTER                       # base case: must START with a letter
           | identifier LETTER            # left recursion: keep letters coming
           | identifier DIGIT             # ...and digits after the first position
           ;
%%

int main() {
    printf("Enter an identifier: ");
    yyparse();                            # drives lex + the grammar
    return 0;
}
int yyerror(char *s) {
    printf("Invalid Identifier\n");
    return 0;
}

# build:  yacc -d yacc_id.y  →  lex lex_id.l  →  gcc y.tab.c lex.yy.c -ll  →  ./a.out
```
State the division of labour in one sentence: **LEX classifies each character into a token;
YACC accepts or rejects the resulting token *sequence* against the grammar.**

### 7. Algorithm — record version (mid-level)
```
ALGORITHM: Validate an identifier using LEX and YACC

Part 1 — lex_id.l (tokeniser)
1. Include y.tab.h so the token names LETTER and DIGIT are known.
2. Rules: [a-zA-Z] → return LETTER;  [0-9] → return DIGIT;  '\n' → return '\n';
   any other character → return that character.
   (no main() — yacc supplies it)

Part 2 — yacc_id.y (parser)
1. Declare the tokens with %token LETTER DIGIT.
2. Write the grammar:
     start      : identifier '\n'  { print "Valid Identifier" } ;
     identifier : LETTER | identifier LETTER | identifier DIGIT ;
3. main() prompts and calls yyparse().
4. yyerror() prints "Invalid Identifier".
5. Build: yacc -d yacc_id.y  →  lex lex_id.l  →  gcc y.tab.c lex.yy.c -ll  →  ./a.out.
6. Stop.
```

### ▶ Verified output
`abc123` → `Valid Identifier`  ·  `123abc` → `Invalid Identifier`

---

**Next group:** Group B (Exp 5–7) — the automata chain, where each experiment's output is the
next one's input.
