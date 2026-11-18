# How to run each program

Three kinds of program in this lab, and only the first kind is plain `gcc`.

| # | Program | Special command? | Compile | Run |
|---|---|---|---|---|
| 1 | `lex_a.c` | no — but it opens `input.c` itself | `gcc lex_a.c -o lex_a` | `./lex_a` |
| 2 | `lexer.l` | **yes — `lex` first** | `lex lexer.l` then `gcc lex.yy.c -lfl -o lexer` | `./lexer` |
| 3 | `lex_count.l` | **yes — `lex` first**, end with Ctrl+D | `lex lex_count.l` then `gcc lex.yy.c -lfl -o count` | `./count` |
| 4 | `lex_id.l` + `yacc_id.y` | **yes — `yacc -d` first, then `lex`, then one gcc** | `yacc -d yacc_id.y` · `lex lex_id.l` · `gcc y.tab.c lex.yy.c -lfl -o idcheck` | `./idcheck` |
| 5 | `e_closure.c` | no | `gcc e_closure.c -o eclosure` | `./eclosure` |
| 6 | `e-nfa_nfa.c` | no | `gcc e-nfa_nfa.c -o enfa` | `./enfa` |
| 7 | `nfa_dfa.c` | no | `gcc nfa_dfa.c -o nfadfa` | `./nfadfa` |
| 8 | `fnf.c` | no | `gcc fnf.c -o fnf` | `./fnf` |
| 9 | `rdp.c` | no | `gcc rdp.c -o rdp` | `./rdp` |
| 10 | `srp.c` | no | `gcc srp.c -o srp` | `./srp` |
| 11 | `intermediate.c` | no | `gcc intermediate.c -o tac` | `./tac` |

`-o name` just names the binary (`a.out` if you leave it out). Nothing else about plain C changes.

## The three shapes

**Plain C (1, 5–11)** — one `gcc`, then run it. The only thing that varies is that most of them are
**interactive**: they sit waiting for you to type input, so `./a.out` alone shows a prompt and nothing
else until you type.

**LEX alone (2, 3)** — two tools, in order:

```
lex lexer.l            # reads the .l RULES, writes lex.yy.c (a full C program)
gcc lex.yy.c -lfl      # compiles the generated C, linking the lex runtime
./a.out
```

You never compile `.l` directly — it is not C. `-lfl` is the lex runtime library: `yywrap()`, the
input buffer, `yytext`. **On a System V lex the same library is called `libl`, so the flag is `-ll`.**
If `-ll` says "cannot find -ll", use `-lfl`; if `-lfl` fails, use `-ll`. One of the two exists.

**LEX + YACC (4)** — three tools, and the **order is not optional**:

```
yacc -d yacc_id.y          # writes y.tab.c (the parser) AND y.tab.h (the token numbers)
lex lex_id.l               # lex.yy.c does #include "y.tab.h", so this must come AFTER yacc -d
gcc y.tab.c lex.yy.c -lfl  # both generated C files are compiled and linked together
./a.out
```

- `-d` is the flag that writes the header. Without it the lex file cannot compile at all.
- Only the lex side needs `-lfl`; `y.tab.c` is ordinary C.
- If lex wrote `lex.yy.c` into a different folder, add `-I.` to `gcc` so `y.tab.h` is still found:
  `gcc -I. y.tab.c ../build/lex.yy.c -lfl`.

## Input: what a run actually looks like

| # | Type this | Notes |
|---|---|---|
| 1 | *(nothing)* | reads `input.c` from the working folder |
| 2 | `int a = a+b*2;` | one line, then **Ctrl+D** |
| 3 | `hello world` ↵ `this is lex` | then **Ctrl+D** — Enter alone does not finish |
| 4 | `abc123` then `123abc` | two separate runs; second one must print Invalid |
| 5 | `4` ↵ then 4 rows of `0 1 0 0` | ε matrix, whitespace-separated |
| 6 | `3 2 a b` then the closures then transitions | strict order: n, m, symbols, per-state closure (count + states), per state×symbol (count + destinations) |
| 7 | `3 2 a b` then per state×symbol `count destinations…` | same shape as 6 but no closures |
| 8 | `4` then `S=AB` `A=a` `B=bC` `C=c` | `#` means ε |
| 9 | `(i+i)*i` | then `./a.out` again with `i+*i` to see rejection |
| 10 | `i+i*i` | grammar is `E → E+E | E*E | i` |
| 11 | `a+b*c` | single-character operands, operators `+ - * /` |

**Ctrl+D** (not Enter) is end-of-file: it is what makes `yylex()` stop and the program print its
result. On the lab machines the same key combination ends input everywhere.

## If the tools are named differently

`lex` and `yacc` are traditional names that map to the GNU tools:

| Traditional | GNU name | What it is |
|---|---|---|
| `lex` | `flex` | lexical analyser generator |
| `yacc` | `bison` | parser generator (LALR(1)) |

`yacc` on a modern Linux usually *is* bison in compatibility mode, so `yacc -d file.y` works and
still writes `y.tab.c` / `y.tab.h`. Check with `which lex flex yacc bison`.

## Shortcuts

On this machine, from the lab folder:

```
./run.sh 7        # compile + run experiment 7 with its sample input
./run.sh          # list all eleven
./verify_all.sh   # rebuild and run everything, so you can diff your output
```
