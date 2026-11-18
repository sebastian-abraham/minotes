"""Viva / MCQ content for Compiler Lab — the whole-course revision sheet.

Kept deliberately short: one-line answers only, because this is read the night
before and skimmed in a queue. Every item is a fact that can be asked as an MCQ
or in one breath by an examiner.
"""

# Sections: (title, blurb, rows)  where rows are (question, answer).
# `table` sections carry headers + rows instead.
SECTIONS = [
    ("1. The compiler as a whole", "Know the phase order cold — it is the most-asked MCQ block.", [
        ("What is a compiler?",
         "A program that translates source code in a high-level language into an equivalent target program "
         "(machine code or assembly), reporting errors it finds on the way."),
        ("Compiler vs interpreter?",
         "A compiler translates the whole program first and produces an output file; an interpreter executes "
         "the source statement by statement and produces no output file."),
        ("What is a hybrid (Java-style) system?",
         "Compile to an intermediate bytecode, then interpret/JIT that bytecode on a virtual machine."),
        ("Name the six phases, in order.",
         "Lexical analysis → syntax analysis → semantic analysis → intermediate code generation → "
         "code optimisation → code generation."),
        ("Which two phases are not in the linear chain?",
         "Symbol-table management and error handling — they are used by every phase."),
        ("Which phases form the front end, which the back end?",
         "Front end: lexical, syntax, semantic, intermediate code (machine-independent). "
         "Back end: optimisation and code generation (machine-dependent)."),
        ("What is a pass?",
         "One complete traversal of the source (or intermediate form). A compiler can be one-pass or multi-pass."),
        ("What does each phase take in and put out?",
         "Lexical: characters → tokens. Syntax: tokens → parse tree. Semantic: parse tree → annotated tree. "
         "Intermediate: tree → three-address code. Optimisation: code → better code. Codegen: IR → assembly."),
        ("Where does the symbol table fit?",
         "Every phase stores or looks up identifiers in it. It records name, type, scope, size, and (later) address."),
        ("What are the four kinds of error a compiler reports?",
         "Lexical (illegal character), syntactic (unbalanced brackets), semantic (type mismatch, undeclared), "
         "and logical (compiles fine, wrong answer — the compiler cannot catch these)."),
        ("What is the usual error-recovery trick?",
         "Panic mode: skip input until a synchronising token (a semicolon or brace) and resume."),
    ]),

    ("2. Lexical analysis (scanner)", "", [
        ("Lexeme vs token vs pattern?",
         "Lexeme = the actual characters. Token = the class it belongs to, written <name, attribute>. "
         "Pattern = the rule describing lexemes of that token."),
        ("For `count = count + 1`, name lexemes and tokens.",
         "Lexemes: count, =, count, +, 1. Tokens: <id,1> <assign> <id,1> <plus> <num,1>."),
        ("Which formalism does a scanner use?",
         "Regular expressions, converted to an NFA, then a DFA — because a DFA needs no backtracking."),
        ("Why can a regular expression not check matching brackets?",
         "Balanced brackets are not a regular language — they need a stack, i.e. a context-free grammar."),
        ("What does LEX actually do?",
         "It is a lexical-analyser generator: it reads a .l file of pattern/action rules and writes lex.yy.c, "
         "a C program containing the scanner function yylex()."),
        ("What are yytext and yyleng?",
         "yytext is the matched text, yyleng its length — so no copying is needed to measure a token."),
        ("Longest match or first rule?",
         "Longest match wins; when two rules match the same length, the earlier rule wins."),
        ("What is yywrap() for?",
         "Called at end of input; returning 1 means 'no more files', so yylex() stops."),
        ("Two scanner terms examiners like.",
         "Lookahead (read one character past a token to find its end) and push-back (ungetc), so the "
         "lookahead character is not lost."),
    ]),

    ("3. Syntax analysis (parser) + YACC", "", [
        ("Which formalism does a parser use?",
         "Context-free grammars (BNF productions), because they can express nesting and recursion."),
        ("What does YACC actually do?",
         "It is a parser generator: it reads a .y file of grammar rules and actions and writes y.tab.c, "
         "containing an LALR(1) shift-reduce parser, yyparse()."),
        ("What does `yacc -d` add?",
         "It also writes y.tab.h — the token numbers — so the .l file can include them and both halves agree."),
        ("How do LEX and YACC cooperate?",
         "LEX returns one token at a time (return LETTER); YACC shifts it and decides, using the grammar, "
         "whether a rule's right-hand side is complete enough to reduce."),
        ("GNU names for lex and yacc?",
         "flex (fast lexical analyser) and bison."),
        ("Shift vs reduce?",
         "Shift = push the next input token. Reduce = replace a right-hand side on top of the stack by its "
         "left-hand side."),
        ("When is a grammar ambiguous?",
         "When one sentence has more than one parse tree (or more than one leftmost derivation). Classic case: "
         "the dangling else."),
        ("What are the two conflicts a generator reports?",
         "Shift/reduce (could push or reduce) and reduce/reduce (two rules both match). Fix by precedence, "
         "associativity, or rewriting the grammar."),
        ("Why does YACC prefer left recursion?",
         "It is LALR — bottom-up — so left recursion consumes input with a bounded stack; right recursion "
         "grows the stack for every symbol."),
        ("Name the four parsing strategies.",
         "Top-down: recursive descent, predictive/LL(1). Bottom-up: shift-reduce with a table — LR(0), "
         "SLR(1), LALR(1), canonical LR(1). YACC is LALR(1)."),
        ("LL vs LR in one line each?",
         "LL reads left-to-right and builds a leftmost derivation top-down (predictive). LR reads left-to-right "
         "and builds a rightmost derivation in reverse bottom-up (shift-reduce with a table)."),
        ("What does LL(1) mean?",
         "Left-to-right scan, leftmost derivation, one token of lookahead."),
        ("Can recursive descent handle `E → E + T`?",
         "No — the first call to E would call E again forever. Rewrite as `E → T E'` (remove left recursion) "
         "and left-factor common prefixes."),
        ("What are FIRST and FOLLOW used for?",
         "Filling the LL(1) table: rule A → α goes in [A, t] for t in FIRST(α); if α is nullable, also for "
         "t in FOLLOW(A)."),
        ("What is a handle?",
         "The substring of a right-sentential form that matches a rule's right-hand side — the thing LR "
         "parsers reduce next."),
        ("What is an LR item?",
         "A production with a dot marking how much has been seen, e.g. E → E · + T. Items build the "
         "LR state machine."),
    ]),

    ("4. Semantic analysis", "", [
        ("What does semantic analysis do?",
         "Type checking, scope/declaration checking, and annotating the parse tree — it catches things the "
         "grammar allows but the language forbids."),
        ("Give one thing only the semantic phase catches.",
         "`int x; x = \"hello\";` — syntactically perfect, semantically a type error."),
        ("What is an attribute grammar?",
         "A grammar with attributes (type, value, address) and rules for computing them — synthesised "
         "(bottom-up) or inherited (top-down)."),
        ("What is type coercion?",
         "An implicit conversion the compiler inserts, e.g. int → float in `x + 1.5`."),
    ]),

    ("5. Intermediate code + optimisation", "", [
        ("Why generate intermediate code at all?",
         "It separates the machine-independent front end from the machine-dependent back end, so n languages "
         "× m machines needs n + m translators instead of n × m."),
        ("What is three-address code?",
         "Instructions of the form `x = y op z` — at most one operator each, with compiler-made temporaries "
         "t1, t2, ..."),
        ("Quadruple vs triple vs indirect triple?",
         "Quadruple stores op, arg1, arg2, result as four fields. A triple stores op, arg1, arg2 and refers "
         "to results by position number. Indirect triples keep an array of pointers so instructions can be "
         "reordered without renumbering."),
        ("What is a DAG used for?",
         "Common-subexpression elimination: identical subexpressions become one node, so they are computed once."),
        ("Name four optimisations in one line.",
         "Constant folding (2*3 → 6), constant propagation, dead-code elimination, and loop-invariant code motion."),
        ("What is strength reduction?",
         "Replacing an expensive operation with a cheap one — `x*2` → `x+x`, or multiply → shift."),
        ("What is peephole optimisation?",
         "A local pass over a small window of instructions, removing redundant loads/stores and jumps to jumps."),
        ("Which end does optimisation belong to?",
         "The back end is machine-dependent, so target-specific optimisation lives there; most optimisation "
         "happens on the intermediate code."),
    ]),

    ("6. Code generation and runtime", "", [
        ("What does the code generator decide?",
         "Instruction selection, register allocation, and evaluation order — usually from the tree, left to right."),
        ("What is an activation record?",
         "The stack frame for one call: return value, actual parameters, control link, access link, saved "
         "machine state, locals, temporaries."),
        ("Where do locals, globals and malloc'd data live?",
         "Locals on the stack (in the activation record), globals in static storage, malloc/new on the heap."),
        ("Four things a symbol table can be built with?",
         "Linear list, sorted list, binary search tree, hash table (hash is the usual answer for speed)."),
        ("What is a compiler-compiler?",
         "A tool that generates part of a compiler from a specification — lex and yacc are the classic pair."),
        ("What is the compiler's cousin list?",
         "Preprocessor, assembler, linker, loader — the stages around the compiler itself."),
    ]),

    ("7. Automata, in the terms this lab uses", "", [
        ("NFA vs DFA?",
         "An NFA may have several moves for one symbol and ε-moves; a DFA has exactly one move per "
         "(state, symbol) and no ε-moves."),
        ("What is an ε-closure?",
         "The state itself plus every state reachable from it by ε-moves only — all the places you can be "
         "without consuming input."),
        ("Three standard conversions?",
         "Regex → NFA (Thompson's construction), NFA → DFA (subset construction), DFA → minimal DFA "
         "(state merging / Hopcroft)."),
        ("What is the subset construction's key idea?",
         "Each DFA state is a SET of NFA states — the set of places the NFA could be."),
        ("Why do scanners prefer DFAs?",
         "Deterministic: one move per symbol, so the scan is a single pass with no guessing or backtracking."),
        ("Which language class does a scanner recognise, and which does a parser recognise?",
         "Scanner: regular languages (type-3, DFA). Parser: context-free languages (type-2, pushdown automaton)."),
    ]),

    ("8. Rapid-fire MCQ facts", "One line each — these are the shapes MCQs come in.", [
        ("Output of the lexical analyser", "a stream of tokens"),
        ("Phase that uses regular expressions", "lexical analysis"),
        ("Phase that uses context-free grammar", "syntax analysis"),
        ("Phase that builds/uses the symbol table most", "all of them; semantic analysis most heavily"),
        ("Phase that does type checking", "semantic analysis"),
        ("Phase that produces the parse tree", "syntax analysis"),
        ("Phase that is machine-dependent", "code generation (and target-specific optimisation)"),
        ("Parse tree vs syntax tree", "parse tree keeps every grammar symbol; syntax tree drops punctuation "
                                      "and single-child chains"),
        ("Tool for the scanner", "lex / flex"),
        ("Tool for the parser", "yacc / bison"),
        ("Parser YACC generates", "LALR(1), bottom-up, shift-reduce"),
        ("Files generated", "lex.yy.c from lex; y.tab.c and y.tab.h from yacc -d"),
        ("Function names", "yylex() scans, yyparse() parses, yyerror() reports, yywrap() ends input"),
        ("Conflict that the dangling else creates", "shift/reduce"),
        ("Grammar type a programming language needs", "context-free (type 2)"),
        ("Automaton for a compiler's scanner", "DFA (finite automaton)"),
        ("Automaton for a compiler's parser", "pushdown automaton"),
        ("Commonest IR", "three-address code"),
        ("Quadruple holds", "operator, operand1, operand2, result"),
        ("Optimisation that removes repeated subexpressions", "common subexpression elimination (DAG)"),
        ("Optimisation that computes 2*3 at compile time", "constant folding"),
        ("Symbol table best implementation", "hash table"),
        ("Number of passes in most real compilers", "usually two or more (front end / back end)"),
        ("Compilation unit order in the lab", "yacc -d first, then lex, then gcc both .c files"),
        ("Library to link a lex scanner", "-lfl on flex, -ll on System V lex"),
    ]),
]

# The phase pipeline, drawn in plain divs.
PHASES = ["Lexical analysis", "Syntax analysis", "Semantic analysis",
          "Intermediate code", "Optimisation", "Code generation"]
PHASE_IO = [("characters", "tokens"), ("tokens", "parse tree"), ("parse tree", "annotated tree"),
            ("annotated tree", "three-address code"), ("IR", "better IR"), ("IR", "assembly")]

# The last-10-minutes page: eight things that earn marks in almost any answer.
DEFENCE = [
    ("If asked to define a compiler",
     "A program that translates a whole high-level program into an equivalent target program and reports the "
     "errors it finds during translation."),
    ("If asked what lex does",
     "It generates a scanner: regular-expression rules in, lex.yy.c with yylex() out, longest match first."),
    ("If asked what yacc does",
     "It generates an LALR(1) parser: grammar rules in, y.tab.c with yyparse() out, plus y.tab.h with -d."),
    ("If asked why two tools",
     "Lexical rules are regular (a DFA suffices); grammatical rules are context-free (a stack is needed). "
     "One tool cannot do both well."),
    ("If asked why left recursion",
     "Bottom-up parsers consume input with a bounded stack, so left recursion is efficient; top-down parsers "
     "cannot use it at all."),
    ("If asked what optimisation is not",
     "Not speed of the compiler — it is making the generated program faster or smaller, without changing "
     "what it computes."),
    ("If asked about a bug in your own program",
     "Name the mechanism, not the symptom: 'precedence() returns 0 for an unknown operator, so the >= test is "
     "always true and the stack is popped past its bottom'."),
    ("If you do not know",
     "Say what the phase does and where the answer would come from — examiners reward the structure over a "
     "guessed keyword."),
]
