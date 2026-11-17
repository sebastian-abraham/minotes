"""Content for the Compiler Lab pages: per-experiment algorithm steps, each tied to
the exact source lines that implement it (anchors = unique substrings, resolved to
line numbers at build time), plus curveballs and viva answers.

Anchors MUST be literal substrings of sources/compiler-lab/code/<file>.
The build fails loudly if an anchor does not resolve, so the map can never drift
away from the compiled code.
"""

EXPS = [
    # ------------------------------------------------------------------ Exp 1
    {
        "id": "exp1", "n": "1", "title": "Lexical analyser, hand-written",
        "files": ["lex_a.c", "input.c"], "sim": "scan",
        "simhint": "Paste any C snippet; the scanner classifies it token by token.",
        "simdefault": "int main(){\n  int a = 10;\n  float b = 20;\n  if (a < b) { a = a + 1; }\n  return 0;\n}",
        "story": "The compiler's first job is to stop seeing text and start seeing <b>words</b>. "
                 "This program reads a file character by character and prints what each chunk is: "
                 "keyword, identifier, number, operator, or symbol. Each chunk is a <b>token</b>.",
        "steps": [
            ("Open the file and read <b>one character at a time</b> — the whole program is one loop over fgetc().",
             ["FILE *fp = fopen(\"input.c\", \"r\");", "while ((ch = fgetc(fp)) != EOF)"]),
            ("Skip blanks, tabs and newlines before classifying anything.",
             ["ch == ' ' || ch == '\\t' || ch == '\\n'"]),
            ("A '/' is ambiguous — it may be a comment or an operator, so <b>read one character past it</b>.",
             ["if (ch == '/') {", "char next = fgetc(fp);"]),
            ("'//' swallows the rest of the line; '/*' swallows until the pair '*' '/' — tracked with a "
             "<b>prev</b> variable, because one character alone cannot tell you the pair just closed.",
             ["if (next == '/')", "if (prev == '*' && ch == '/')"]),
            ("A bare '/' IS an operator — and the character you read to check must be <b>pushed back</b> "
             "with ungetc(), or the next token loses its first character.",
             ["printf(\"Operator : /\\n\");", "ungetc(next, fp);"]),
            ("A letter or '_' starts a word: copy it and every following letter/digit/'_' into a buffer.",
             ["if (isalpha(ch) || ch == '_') {"]),
            ("Close the buffer with '\\0' and push the terminating character back, so it is read again as "
             "the start of the next token.",
             ["buffer[i] = '\\0';", "ungetc(ch, fp);"]),
            ("Compare the buffer against the keyword array: match → <b>Keyword</b>, no match → <b>Identifier</b>. "
             "Same shape, fixed list — that is the only difference between the two.",
             ["if (isKeyword(buffer))"]),
            ("A digit starts a number and only digits continue it — same push-back discipline.",
             ["else if (isdigit(ch)) {"]),
            ("Operators and symbols are single characters in a fixed set, so strchr() decides them.",
             ["strchr(\"+-*=<>!%\", ch)", "strchr(\"(){}[];,.\", ch)"]),
            ("At EOF the file is closed and the program ends.",
             ["fclose(fp);"]),
        ],
        "curve": [
            ("They ask for <b>more keywords</b>", "Only the keywords[] array changes. The scanner logic is untouched — "
             "this is the cheapest possible modification, and a common one."),
            ("They ask it to read <b>stdin instead of input.c</b>", "Drop fopen/fclose and use getchar() in place of "
             "fgetc(fp); ungetc's second argument becomes stdin. The loop condition becomes "
             "while ((ch = getchar()) != EOF)."),
            ("They ask for <b>two-character operators</b> (<=, >=, ==)", "This design cannot do it in one pass: it "
             "classifies a single character. You must copy the '/' trick — read the next character after '<'/'='/'>' "
             "and decide, pushing back when it is not the second half."),
            ("They ask to <b>count</b> tokens instead of printing", "Add an int per class and ++ in each branch; the "
             "printing lines are the only ones that change."),
        ],
        "viva": [
            ("Why read a character past the end of a token?", "To know the token ended. That character belongs to the "
             "next token, so ungetc() pushes it back — otherwise every following token loses its first character."),
            ("How does it tell a keyword from an identifier?", "isKeyword() strcmp's the buffer against the array. "
             "Both are the same shape; only the fixed list separates them."),
            ("Why is the multiline comment loop tricky?", "It needs TWO characters to decide ('*' then '/'), so it "
             "keeps the previous one in prev. A single getc cannot see a pair."),
            ("What happens to a character in no set, like '@'?", "It is silently ignored — the four if/else-if "
             "branches have no final else. That is a real limitation to state honestly."),
        ],
    },
    # ------------------------------------------------------------------ Exp 2
    {
        "id": "exp2", "n": "2", "title": "Lexical analyser with LEX",
        "files": ["lexer.l"], "sim": "lex",
        "simhint": "Type C code; each token shows which rule won and why.",
        "simdefault": "int a = a+b*2;",
        "story": "Exp 1 was hand-written. Here LEX <b>writes the scanner for you</b>: you list pattern → action "
                 "pairs, and it generates lex.yy.c containing yylex(). LEX builds one big DFA from all the "
                 "patterns, which is why matching order has rules.",
        "steps": [
            ("<b>Definitions section</b> (%{ … %}): headers and any globals the actions need.",
             ["%{"]),
            ("<b>Rules section</b> (after %%): one pattern → action pair per token class. This is the entire "
             "program logic.",
             ["\"int\"|\"float\"|\"char\""]),
            ("Keywords first: quoted strings, alternated with |. Each prints the matched text yytext.",
             ["{ printf(\"Keyword : %s\\n\", yytext); }"]),
            ("Numbers: [0-9]+ means 'one or more digits'. The + is why 42 is one token and not two.",
             ["[0-9]+    { printf(\"Number"]),
            ("Identifiers: a letter or underscore, then any number of letters/digits/underscores. "
             "Written as [a-zA-Z_][a-zA-Z0-9_]* — two character classes, not one.",
             ["[a-zA-Z_][a-zA-Z0-9_]*    { printf(\"Identifier"]),
            ("Operators, longest strings first inside the alternation (== before =) — reflex, not required, "
             "but it keeps the intent obvious.",
             ["\"==\"|\"!=\"|\"<=\""]),
            ("Special symbols: the bracket/brace/semicolon/comma set.",
             ["\"[\"|\"]\"|\"(\"|\")\""]),
            ("Whitespace matches and does <b>nothing</b> — an empty action (just a semicolon). Consuming it is "
             "the point.",
             ["[ \\t\\n]+    ;"]),
            ("A final '.' catches anything unmatched, so no character is silently lost (Exp 1's weakness).",
             [".    { printf(\"Unknown"]),
            ("<b>User code section</b>: yywrap() returning 1 means 'no more input files', and main() just calls "
             "yylex() once — it loops internally until EOF.",
             ["int yywrap()", "yylex();"]),
        ],
        "curve": [
            ("They ask to <b>add comments</b>", "Two rules, both written BEFORE the operator rule: "
             "\\/\\/.* ; and \\/\\*([^*]|\\*+[^*/])*\\*+\\/ ;. Longest-match makes /* win over the '/' operator, and "
             "the earlier-rule rule settles ties."),
            ("They ask to <b>count</b> keywords", "int k=0; in the definitions section, k++ inside the keyword "
             "action, print in main. Only the action changes."),
            ("They ask for <b>one output per line</b> instead of per token", "You cannot — LEX calls your action per "
             "match. Buffer the text and print at EOF, or write a rule that matches a whole line (.*\\n) and "
             "re-tokenise inside it."),
            ("They ask what happens to '123abc'", "Longest match: the identifier rule would need a letter first, so "
             "[0-9]+ takes 123, then [a-zA-Z_][a-zA-Z0-9_]* takes abc — two tokens, not one error. LEX has no "
             "concept of 'invalid token', only 'unmatched'."),
        ],
        "viva": [
            ("Longest match vs first rule — which wins?", "Length first: the longest match at the current position "
             "wins. Only when two rules match the SAME length does the earlier rule win."),
            ("What are yytext and yyleng?", "yytext is the matched text as a string, yyleng its length. No copying "
             "needed, which is why counting is characters += yyleng."),
            ("Why is main() inside the third section?", "YACC also generates a main() (Exp 4). Standalone LEX needs "
             "its own driver, so it goes after the second %% and calls yylex()."),
            ("What does yywrap() do?", "Called at end of input; returning 1 tells the scanner there are no further "
             "files, so yylex() returns 0."),
        ],
    },
    # ------------------------------------------------------------------ Exp 3
    {
        "id": "exp3", "n": "3", "title": "Count lines, words, characters with LEX",
        "files": ["lex_count.l"], "sim": "count",
        "simhint": "Type text; watch the three counters move rule by rule (Ctrl+D is the real program's EOF).",
        "simdefault": "hello world\nthis is lex\n",
        "story": "Same tool, different job: instead of <b>labelling</b> tokens it <b>counts</b> them. It proves a "
                 "lex action can do anything C can — including keeping state.",
        "steps": [
            ("The three counters are <b>globals</b> in the definitions section, so every action can update them.",
             ["int lines = 0;", "int words = 0;", "int characters = 0;"]),
            ("Newline rule: one line, one character. The pattern is the escape \\n.",
             ["\\n              { lines++; characters++; }"]),
            ("Blanks and tabs: [ \\t]+ matches a RUN, so characters must add yyleng — not 1.",
             ["[ \\t]+          { characters += yyleng; }"]),
            ("Word rule: a run of letters/digits is one word, and its length is again added with yyleng.",
             ["[a-zA-Z0-9]+    { words++; characters += yyleng; }"]),
            ("Catch-all '.' takes any single other character (punctuation) — it counts one character.",
             [".               { characters++; }"]),
            ("main() prints the prompt, calls yylex() (which loops to EOF), then prints the three counters.",
             ["printf(\"\\nNumber of lines", "printf(\"Number of words", "printf(\"Number of characters"]),
        ],
        "curve": [
            ("They ask to count <b>sentences</b>", "Add a rule [.!?] with sentences++ and characters += yyleng. The "
             "structure of the program does not change at all — that is the lesson."),
            ("They ask what happens without the '.' rule", "Characters in no rule are skipped silently, so the "
             "character count is WRONG while lines and words stay right. The catch-all is what makes the count "
             "conservation property hold."),
            ("They ask for words <b>excluding digits</b>", "Change [a-zA-Z0-9]+ to [a-zA-Z]+, and note digits then "
             "fall to the '.' rule and count as characters only. Say that consequence out loud."),
            ("They ask why characters is updated in every rule", "Because every matched rule consumes characters. Any "
             "rule that forgets to account for its own match breaks the invariant 'sum of consumed = total'."),
        ],
        "viva": [
            ("How do you end input in this program?", "Ctrl+D (not Enter). yylex() returns on EOF, then main() prints."),
            ("What is special about the whitespace rule here vs Exp 2?", "Exp 2's whitespace action is empty; here it "
             "must add yyleng to characters. Same pattern, different action — the action is where the experiment "
             "lives."),
            ("Why is [ \\t]+ one rule and not two?", "[ \\t]+ is a run: a tab-indented line is one match. Splitting it "
             "would still count the same characters, but yyleng makes the run cheaper."),
        ],
    },
    # ------------------------------------------------------------------ Exp 4
    {
        "id": "exp4", "n": "4", "title": "Identifier validator: LEX + YACC",
        "files": ["lex_id.l", "yacc_id.y"], "sim": "yacc",
        "simhint": "Type an identifier; watch LEX feed tokens and YACC decide.",
        "simdefault": "abc123",
        "story": "LEX knows nothing about <b>order</b>. It can say 'this is a letter', not 'a letter must come "
                 "first'. YACC supplies the grammar, LEX supplies the tokens — together they decide legality.",
        "steps": [
            ("LEX includes the header yacc -d generated, so token NAMES exist in both halves with identical numbers.",
             ["#include \"y.tab.h\""]),
            ("Only four rules. A letter returns LETTER, a digit returns DIGIT — LEX does not decide anything, it "
             "just reports what it saw.",
             ["[a-zA-Z]    { return LETTER; }", "[0-9]       { return DIGIT; }"]),
            ("Newline is passed through explicitly, and every other character is returned as itself. Those are the "
             "characters the grammar has no rule for — YACC will reject them.",
             ["\\n          { return '\\n'; }", ".           { return yytext[0]; }"]),
            ("YACC declares the two token names it expects from LEX.",
             ["%token LETTER DIGIT"]),
            ("The start rule demands identifier followed by the newline; only then does the action print Valid.",
             ["identifier '\\n'   { printf(\"Valid Identifier\\n\"); }"]),
            ("The grammar rule is <b>left-recursive</b>: identifier can be a LETTER, or an identifier followed by "
             "one more LETTER/DIGIT. Left recursion is what LALR wants, and note the base case is LETTER only.",
             ["      LETTER", "| identifier LETTER", "| identifier DIGIT"]),
            ("main() calls yyparse(), which drives yylex() until the start symbol is complete or an error occurs.",
             ["yyparse();"]),
            ("yyerror() is called by YACC when no rule can consume the next token — that is the invalid path.",
             ["printf(\"Invalid Identifier\\n\");"]),
        ],
        "curve": [
            ("They allow an identifier to <b>start with underscore</b>", "Change ONLY the .l: [a-zA-Z_] returns "
             "LETTER. The grammar is untouched, because '_' is just another letter to it. The .y file is where you "
             "say WHY nothing changes."),
            ("They ask for <b>float validation</b> (digits '.' digits)", "That is a grammar change: add a rule like "
             "number : DIGIT | number DIGIT | number '.' DIGIT …, and add a token for '.'. Same left-recursive "
             "shape — this is the modification most likely to appear, so be able to sketch it."),
            ("They ask why 123abc fails but abc123 passes", "The only way to START a derivation is LETTER. 123 starts "
             "with DIGIT, so no derivation exists; after a first letter, DIGIT and LETTER are both fine."),
            ("They ask for a longer identifier limit", "YACC has no length limit; the constraint, if any, is a C array "
             "or a length counter in a lex action. Nothing in the grammar changes."),
        ],
        "viva": [
            ("Which tool decides, LEX or YACC?", "LEX reports tokens; YACC decides. LEX's [a-zA-Z] rule cannot know "
             "position — the grammar is what encodes 'letter first'."),
            ("What does yacc -d add?", "It writes y.tab.h containing the token numbers, which the .l file includes. "
             "Without it the two halves disagree and nothing compiles."),
            ("Why left recursion and not right?", "LALR parsers consume input bottom-up with a bounded stack; left "
             "recursion folds each new symbol into the existing identifier. Right recursion would grow the stack for "
             "the length of the name."),
            ("What is yyerror's role?", "YACC calls it when the next token fits no rule. Here it prints Invalid "
             "Identifier; a real compiler would also report the line number."),
        ],
    },
    # ------------------------------------------------------------------ Exp 5
    {
        "id": "exp5", "n": "5", "title": "ε-closure of every state",
        "files": ["e_closure.c"], "sim": "eclosure",
        "simhint": "First line = number of states n, then n lines of n 0/1 values.",
        "simdefault": "4\n0 1 0 0\n0 0 1 0\n0 0 0 1\n0 0 0 0",
        "story": "An NFA may have <b>ε-transitions</b>: moves that consume no input, like a free teleport. The "
                 "ε-closure of a state is the state itself plus everything reachable by ε-moves only. Experiments 6 "
                 "and 7 both need this set.",
        "steps": [
            ("State lives in two global matrices: epsilon (the input) and closure (what we compute). "
             "closure[s][t] = 1 means 't is in the ε-closure of s'.",
             ["int epsilon[20][20];", "int closure[20][20];"]),
            ("The recursive helper takes <b>two</b> states: state = whose closure (fixed), current = where the walk "
             "is now (changes).",
             ["void findClosure(int state, int current){"]),
            ("Mark the current state as belonging to the closure. This happens BEFORE looking for moves — that is "
             "what makes it terminate.",
             ["closure[state][current] = 1;"]),
            ("Scan all states for an ε-move out of current <b>that we have not already marked</b>. The second half "
             "of that condition is the cycle guard.",
             ["epsilon[current][i] == 1 && closure[state][i] == 0"]),
            ("Recurse on each unvisited ε-reachable state. The closure matrix doubles as the visited set — no "
             "separate array is needed.",
             ["findClosure(state, i);"]),
            ("main reads n, then the full n×n matrix row by row.",
             ["scanf(\"%d\", &n);", "scanf(\"%d\", &epsilon[i][j]);"]),
            ("Every state is seeded with itself: findClosure(s, s) for s = 0 … n-1.",
             ["findClosure(i, i);"]),
            ("Print by scanning each closure row for 1s — the order of printing is q0 first, and the set order is "
             "ascending, which matters if you compare against the sample.",
             ["printf(\"E-closure(q%d) = { \", i);"]),
        ],
        "curve": [
            ("They ask for the closure of <b>one state only</b>", "One call: findClosure(k, k), then print row k. The "
             "driver loop is the only change."),
            ("They give the automaton as an <b>edge list</b> instead of a matrix", "Read pairs (from, to) into the "
             "same matrix; everything downstream is identical. Say that the representation is not the algorithm."),
            ("They ask for <b>transitive closure</b> of a general relation", "Same recursion with ε replaced by the "
             "relation — this IS Warshall's algorithm in recursive clothing, and saying that out loud is worth marks."),
            ("They ask what breaks on an ε-cycle", "Nothing — that is exactly what the closure[state][i]==0 test "
             "prevents. Remove it and you get infinite recursion, i.e. a stack overflow."),
        ],
        "viva": [
            ("Why does the helper need two parameters?", "One says whose closure is being computed and never changes; "
             "the other is the state we have reached. Conflating them loses the origin."),
            ("Where is the visited check?", "In the if condition: closure[state][i] == 0. Marking before recursing is "
             "what makes it a visited set."),
            ("What does ε-closure(q0) mean in words?", "Every state the machine could be in without consuming any "
             "input, starting from q0. It is where 'free moves' are resolved."),
            ("Which later experiment consumes this result?", "Exp 6 takes it as input and Exp 7 needs it whenever the "
             "NFA has ε-moves. The pipeline is 5 → 6 → 7."),
        ],
    },
    # ------------------------------------------------------------------ Exp 6
    {
        "id": "exp6", "n": "6", "title": "ε-NFA → NFA (remove ε-moves)",
        "files": ["e-nfa_nfa.c"], "sim": "enfa",
        "simhint": "Program's own input format: n, m, symbols, then closures, then transitions.",
        "simdefault": "3 2\na b\n3\n0 1 2\n2\n1 2\n1\n2\n1 1\n1 0\n1 2\n0\n0\n1 2",
        "story": "ε-moves are convenient to draw and annoying to run. This experiment rewrites the transition table "
                 "so every move reads a real symbol, while accepting exactly the same language.",
        "steps": [
            ("addState() appends a state to a set only if it is not already there. Every set in this program is kept "
             "duplicate-free by that one function.",
             ["void addState(int arr[], int *count, int state) {"]),
            ("Read n, m and the m alphabet symbols.",
             ["scanf(\" %c\", &symbols[i]);"]),
            ("Read the ε-closure of every state as input. This program does NOT compute it — Exp 5 does. Say that "
             "link out loud.",
             ["scanf(\"%d\", &ecount[i]);"]),
            ("Read the transitions: for each state and symbol, a count followed by that many destinations.",
             ["scanf(\"%d\", &trans[i][j][0]);"]),
            ("The core loop — for each state i and each symbol j, build one result set.",
             ["int result[MAX], rcount = 0;"]),
            ("Step 1 of the formula: iterate over ε-closure(i). You may teleport freely <b>before</b> reading.",
             ["for (k = 0; k < ecount[i]; k++) {"]),
            ("Step 2: from each of those states, read the symbol and take its destinations.",
             ["int tcount = trans[state][j][0];"]),
            ("Step 3: from each destination, add its whole ε-closure — teleport freely <b>after</b> reading. addState "
             "keeps the union duplicate-free.",
             ["for (int y = 0; y < ecount[next]; y++)", "addState(result, &rcount, eclose[next][y]);"]),
            ("Print δ'(qi, a) = the accumulated set. Three nested loops, one formula.",
             ["printf(\"d'(q%d,%c) = { \", i, symbols[j]);"]),
        ],
        "curve": [
            ("They ask you to <b>compute</b> the closure instead of taking it as input", "Call Exp 5's findClosure() "
             "before the main loop and fill eclose from the closure matrix. Nothing else changes — that is why the "
             "two experiments are neighbours."),
            ("They ask for <b>one symbol only</b>", "Fix j to that symbol's index; the outer loop over j disappears."),
            ("They ask what the formula is, verbatim", "δ'(q,a) = ε-closure( ∪ over p ∈ ε-closure(q) of δ(p,a) ). "
             "In words: teleport free, read the symbol, teleport free."),
            ("They ask why δ' may include MORE states than δ", "Because both free-teleport passes add states that the "
             "original move never named. That is the price of removing ε: the sets get fatter, the language does not "
             "change."),
        ],
        "viva": [
            ("Why remove ε-moves at all?", "A machine cannot 'choose' to teleport — an implementation needs a concrete "
             "next state for every (state, symbol). Removing ε makes it runnable, and Exp 7 then makes it deterministic."),
            ("What does addState protect against?", "Duplicates. Two different paths can reach the same state, and a set "
             "with repeats would print wrongly and break set comparison later."),
            ("Is the result an NFA or a DFA?", "Still an NFA — a symbol may lead to several states. Determinism is Exp "
             "7's job."),
            ("What is the input order here?", "n, m, the m symbols, then per state: count + closure states, then per "
             "state × symbol: count + destinations. Reading the header comment is the fastest way to get it right."),
        ],
    },
    # ------------------------------------------------------------------ Exp 7
    {
        "id": "exp7", "n": "7", "title": "NFA → DFA (subset construction)",
        "files": ["nfa_dfa.c"], "sim": "subset",
        "simhint": "Program's input format: n, m, symbols, then per state × symbol: count + destinations.",
        "simdefault": "3 2\na b\n1 0\n1 1\n1 0\n2 1 2\n1 2\n0",
        "story": "A computer cannot be in three states at once. Subset construction fixes that by declaring every "
                 "<b>set of NFA states</b> to be a single state of a new deterministic machine. Where the NFA "
                 "branches, the DFA tracks the whole branch.",
        "steps": [
            ("Three set helpers do the real work: contains(), sortSet(), sameSet() — and findDFAState() uses them to "
             "ask 'have I seen this set before?'.",
             ["int contains(int set[], int count, int state)", "int sameSet(int a[], int acount, int b[], int bcount)"]),
            ("sortSet() exists for one reason: {q1,q2} and {q2,q1} must compare equal, or the DFA grows duplicate "
             "states and never terminates.",
             ["void sortSet(int set[], int count)"]),
            ("The DFA starts as ONE state: {q0}. totalDFA counts how many exist.",
             ["dfaStates[0][0] = 0;", "totalDFA = 1;"]),
            ("The worklist loop: while there is an unprocessed DFA state. New sets are APPENDED during the loop, so "
             "they are processed in the same pass — a queue, for free.",
             ["while (current < totalDFA){"]),
            ("For the current DFA state, union the NFA moves from <b>every</b> NFA state in the set.",
             ["for (int i = 0; i < dfaCount[current]; i++){"]),
            ("Duplicates are filtered as they are added, then the set is sorted so it has one canonical form.",
             ["if (!contains(newSet, newCount, nextState)){", "sortSet(newSet, newCount);"]),
            ("Look the set up: if it already exists, reuse its index; if not, it becomes a new DFA state and is "
             "appended to the list.",
             ["int stateIndex = findDFAState(newSet, newCount);", "if (stateIndex == -1){", "totalDFA++;"]),
            ("Record the transition and move to the next symbol.",
             ["dfa[current][j] = stateIndex;"]),
            ("After all states are processed, print the table with each state labelled by its set, e.g. {q1,q2}.",
             ["printf(\"\\nEquivalent DFA Transition Table:\\n\\n\");"]),
        ],
        "curve": [
            ("They add <b>final states</b>", "A DFA state is final if its set CONTAINS any NFA final state. One extra "
             "loop when printing — the construction itself is unchanged."),
            ("They use a <b>3-symbol alphabet</b>", "Only m and the read loop change. Say explicitly that the "
             "algorithm is alphabet-agnostic."),
            ("They ask what happens if you skip sortSet()", "Set identity is order-dependent, so {q1,q2} and {q2,q1} "
             "count as two states, the table grows without bound, and the program loops or overflows. That is the bug "
             "the sort prevents."),
            ("They ask how many DFA states at most", "Up to 2^n subsets of an n-state NFA — in practice far fewer, "
             "because only reachable subsets appear."),
        ],
        "viva": [
            ("What is a DFA state here?", "A set of NFA states — 'the NFA could be in any of these'. That is the entire "
             "idea of subset construction."),
            ("Why does the worklist loop terminate?", "Each iteration either processes a state already in the list or "
             "appends a genuinely new subset. There are finitely many subsets, so it must end."),
            ("Where would ε-closure fit in?", "If the NFA has ε-moves, each computed set must be ε-closed before being "
             "stored (and the start state is ε-closure(q0)). This program's input has none, so it is absent."),
            ("What does sameSet compare?", "Sizes first, then membership of every element of a in b — an order-"
             "independent equality, which is why sorting is not strictly required but is still good hygiene."),
        ],
    },
    # ------------------------------------------------------------------ Exp 8
    {
        "id": "exp8", "n": "8", "title": "FIRST and FOLLOW",
        "files": ["fnf.c"], "sim": "fnf",
        "simhint": "Productions as S=AB, one per token or line; use # for ε.",
        "simdefault": "S=AB A=a B=bC C=c",
        "story": "To parse, a machine must answer at every step: <b>given the token I am looking at, which rule do I "
                 "apply?</b> That decision is precomputed into a table, and the table is filled from these two sets.",
        "steps": [
            ("Sets are plain C strings, and add() appends a character only when it is not already present. That single "
             "function is the whole set implementation — dedupe included.",
             ["void add(char set[], char c) {"]),
            ("FIRST of a terminal is itself — the base case. isupper() is how the program tells a non-terminal from a "
             "terminal.",
             ["if (!isupper(c)) {"]),
            ("FIRST of a non-terminal: scan every production whose left-hand side is c.",
             ["if (prod[i][0] == c) {"]),
            ("An explicit ε-production (#) puts ε in FIRST directly.",
             ["if (prod[i][2] == '#') {"]),
            ("Otherwise walk the right-hand side, taking FIRST of each symbol in turn.",
             ["FIRST(prod[i][j], temp);"]),
            ("Add everything except ε, and STOP as soon as a symbol cannot vanish. Only a nullable symbol lets you "
             "move to the next one — that is the rule people forget.",
             ["if (!epsilon)", "break;"]),
            ("FOLLOW of the start symbol always contains $. Here the start symbol is simply prod[0][0] — the "
             "left-hand side of the first production.",
             ["if (c == prod[0][0])"]),
            ("FOLLOW scan: find c anywhere in a right-hand side (starting at index 2, since index 1 is '=').",
             ["for (j = 2; prod[i][j] != '\\0'; j++) {"]),
            ("If something follows c, add FIRST of it minus ε; if nothing does — or it can vanish — copy FOLLOW of the "
             "left-hand side. That recursion is the theory's step 2(b), not a shortcut.",
             ["FOLLOW(prod[i][0], temp2);", "FOLLOW(prod[i][0], temp);"]),
            ("main() reads n productions, then computes and prints FIRST for each left-hand side, then FOLLOW.",
             ["printf(\"\\nFIRST sets:\\n\");", "printf(\"\\nFOLLOW sets:\\n\");"]),
        ],
        "curve": [
            ("A grammar with an <b>ε production</b>", "Write it as A=# . FIRST(A) gets #, and every FIRST of a "
             "non-terminal that references A must then continue past it — the !epsilon check is what handles that."),
            ("They ask for the <b>LL(1) table</b> from these sets", "Rule A → α goes into [A, t] for t ∈ FIRST(α); if α "
             "is nullable, also into [A, t] for t ∈ FOLLOW(A). Two loops over the productions you already have."),
            ("A grammar where a non-terminal never appears on any right-hand side", "FOLLOW is {$} if it is the start "
             "symbol, otherwise EMPTY — worth saying, examiners like that edge."),
            ("They change the input format", "This program is positional: prod[i][0] is the LHS and the RHS starts at "
             "index 2 because index 1 is '='. Change the format and those two offsets everywhere are what must change "
             "— good answer to 'what if the format were A->a'?"),
        ],
        "viva": [
            ("FIRST vs FOLLOW in one line each", "FIRST(X): terminals that can BEGIN a string derived from X. "
             "FOLLOW(A): terminals that can appear immediately AFTER A (plus $ if A can end the input)."),
            ("Why does '#' stand for ε?", "Epsilon cannot be typed conveniently, so the program uses a character that "
             "is not a grammar symbol."),
            ("Why does add() matter so much?", "Every set is a raw char string; without dedupe, FIRST and FOLLOW "
             "print with repeats and any downstream table lookup is wrong."),
            ("When do you stop scanning a right-hand side?", "As soon as a symbol's FIRST does not contain ε — nothing "
             "past it can be first."),
        ],
    },
    # ------------------------------------------------------------------ Exp 9
    {
        "id": "exp9", "n": "9", "title": "Recursive descent parser",
        "files": ["rdp.c"], "sim": "rdp",
        "simhint": "i = operand, brackets allowed. Try (i+i)*i, then i+*i.",
        "simdefault": "(i+i)*i",
        "story": "The simplest way to build a parser: <b>one C function per grammar non-terminal</b>. To parse E you "
                 "call E(); it calls T(), which calls F(). Each function eats the symbol it expects. If everything is "
                 "eaten and we stand on end-of-string, the input was valid.",
        "steps": [
            ("A shared index pos into the input string. It only ever moves forward — one symbol per match. That "
             "shared cursor is what makes separate functions cooperate.",
             ["char input[100];", "int pos = 0;"]),
            ("E → T E': call the two functions for its right-hand side, in order. Nothing else.",
             ["void E() {"]),
            ("E' → + T E' | ε: test for '+'. If present, consume it (pos++) and recurse; if absent, return. "
             "<b>The absent match IS the ε-production</b> — there is no if(ε) anywhere.",
             ["void Eprime() {", "if (input[pos] == '+') {"]),
            ("T → F T': same pattern one level down.",
             ["void T() {"]),
            ("T' → * F T' | ε: identical shape, testing '*'. Because T' lives inside T, every '*' is finished before "
             "the enclosing '+' is touched — <b>that nesting is where precedence comes from</b>.",
             ["void Tprime() {", "if (input[pos] == '*') {"]),
            ("F → i | ( E ): the only function that consumes a token or brackets. An operand is one character here.",
             ["if (input[pos] == 'i') {"]),
            ("On '(' it recurses into E for the whole bracketed expression, then REQUIRES ')'. A missing bracket is an "
             "immediate error, not a misplaced symbol.",
             ["else if (input[pos] == '(') {", "if (input[pos] == ')')"]),
            ("error() prints and calls exit(0) — the parse does not unwind, it terminates. Worth knowing for the viva: "
             "exit(0) is a success status, which is arguably a bug.",
             ["void error() {", "exit(0);"]),
            ("Accept test: after E(), pos must have reached the end of the string.",
             ["if (input[pos] == '\\0')"]),
        ],
        "curve": [
            ("They add '-' and '/'", "Extend the two tests: if (input[pos]=='+' || input[pos]=='-') and the same for "
             "'*' || '/'. Nothing else changes — that is the payoff of one-function-per-non-terminal."),
            ("They want multi-digit numbers", "F must collect a run of digits: while (isdigit(input[pos])) pos++. The "
             "structure is unchanged; only F's 'i' case grows."),
            ("They ask for a grammar with left recursion (E → E + T)", "It CANNOT be written this way — the first call "
             "to E() would call E() again forever. That is precisely why the grammar is rewritten to E → T E'. Saying "
             "this is a strong viva answer."),
            ("They ask what error recovery exists", "None. error() exits. A real parser would report the position and "
             "skip to a synchronising token."),
        ],
        "viva": [
            ("Where is the ε-production in the code?", "In the missing else: Eprime() tests for '+' and otherwise falls "
             "off the end. Returning without consuming anything is the ε-derivation."),
            ("Why does * bind tighter than +?", "Because * is matched deeper in the call chain (inside T, which is "
             "inside E). Deeper nesting is completed first."),
            ("What makes this left-to-right?", "The single shared pos. Each call resumes exactly where the previous one "
             "stopped."),
            ("Why is one function per non-terminal enough?", "The grammar is LL(1)-ish here: at every point one token "
             "of lookahead (input[pos]) decides which alternative to take. No backtracking is needed."),
        ],
    },
    # ------------------------------------------------------------------ Exp 10
    {
        "id": "exp10", "n": "10", "title": "Shift-reduce parser",
        "files": ["srp.c"], "sim": "srp",
        "simhint": "Grammar E→E+E | E*E | i. Try i+i*i, then i*i+i.",
        "simdefault": "i+i*i",
        "story": "The opposite direction to Exp 9. Instead of predicting from the top, build the parse from the "
                 "<b>bottom up</b>: push input symbols (<b>shift</b>), and whenever the top of the stack looks like a "
                 "rule's right-hand side, replace it by the left-hand side (<b>reduce</b>).",
        "steps": [
            ("A character stack and a top index; top = -1 means empty. The stack is the parser's entire memory.",
             ["char stack[50], input[50];", "int top = -1;"]),
            ("reduce() tries three right-hand sides, in this order: 'i' first, then E+E, then E*E. That order is the "
             "program's entire grammar.",
             ["void reduce() {", "if (top >= 0 && stack[top] == 'i') {"]),
            ("E → E+E: the top three symbols must be E, '+', E, and the reduction pops two and pushes one.",
             ["stack[top - 1] == '+'"]),
            ("E → E*E: same, looking for '*'.",
             ["stack[top - 1] == '*'"]),
            ("main() walks the input; each character is pushed (SHIFT).",
             ["stack[++top] = input[i];"]),
            ("After every push, stack[top+1] is set to '\\0' so the stack can be printed as a string in the trace. "
             "That single write is why the output looks like a stack.",
             ["stack[top + 1] = '\\0';"]),
            ("<b>reduce() is called once per shift</b> and performs AT MOST ONE reduction (if/else-if, no loop). That "
             "is why i+i*i reduces i, then E*E, then E+E — and not the other way round.",
             ["reduce();"]),
            ("After the input ends, reduce again while top > 0, breaking when a call changes nothing. The oldtop == "
             "top comparison is the only termination guard.",
             ["int oldtop = top;", "if (oldtop == top)"]),
            ("Accept means the stack is exactly one symbol and it is E.",
             ["if (top == 0 && stack[0] == 'E')"]),
        ],
        "curve": [
            ("They add brackets: E → (E)", "One more else-if in reduce(): if the top three are '(', E, ')' then replace "
             "by E. Same pattern of three-symbol lookback — be able to write it."),
            ("They want multi-character operands (id, num)", "This design breaks: the stack holds single characters. You "
             "would need a stack of strings and a comparison against whole right-hand sides — say that honestly."),
            ("They ask about the ambiguous grammar", "E→E+E|E*E|i is ambiguous. This parser gets i+i*i right by accident "
             "of reduction order, not by principle. A real LR parser uses a table with precedence; that is what YACC "
             "(Exp 4) is."),
            ("They ask why the trace is not the textbook one", "Because reduce() does one reduction per call and main() "
             "calls it once per shift. A textbook parser reduces in a loop until no rule applies; this one defers, which "
             "changes the visible order of reductions but not the final result."),
        ],
        "viva": [
            ("Shift vs reduce in one line each", "Shift: push the next input symbol. Reduce: replace a right-hand side "
             "on top of the stack with its left-hand side."),
            ("How does it terminate?", "Two loops: one over input, then while (top > 0) with an oldtop == top break when "
             "no reduction applies."),
            ("How is this related to YACC?", "YACC is an LR parser: same shift/reduce operations, but the decision comes "
             "from a generated table instead of hard-coded ifs. Exp 4 and Exp 10 are the same idea at two levels."),
            ("Why does the stack need the '\\0' write?", "So the trace can printf(\"%s\", stack). C strings need a "
             "terminator, and the array is being used as both stack and string."),
        ],
    },
    # ------------------------------------------------------------------ Exp 11
    {
        "id": "exp11", "n": "11", "title": "Three-address intermediate code",
        "files": ["intermediate.c"], "sim": "tac",
        "simhint": "Infix with single-letter operands, + - * /. Try a+b*c, then a-b-c.",
        "simdefault": "a+b*c",
        "story": "Turn infix like a+b*c into tiny instructions with at most one operator each, storing partial results "
                 "in compiler-made temporaries t1, t2. That is <b>three-address code</b> — what a real compiler hands "
                 "to the next phase.",
        "steps": [
            ("Globals: the expression string, and a counter for temporaries starting at 1.",
             ["char expr[50];", "int temp = 1;"]),
            ("generate() is the only place that prints — it takes the operator and the two operands and emits one "
             "instruction. Keeping it in one function is why the output format is consistent.",
             ["void generate(char op, char a[], char b[], char result[]) {"]),
            ("precedence() is the whole decision table: * / = 2, + - = 1, anything else 0.",
             ["int precedence(char op) {", "if (op == '*' || op == '/')"]),
            ("Two stacks: operand stack (strings, holding values AND temporaries) and operator stack (characters).",
             ["char operands[50][10];", "char operators[50];"]),
            ("Operands are pushed as one-character strings (isalnum).",
             ["if (isalnum(expr[i])) {"]),
            ("For an operator, reduce while the stacked operator has precedence >= the incoming one. The >= (not >) is "
             "what makes a-b-c parse as (a-b)-c.",
             ["precedence(operators[opTop]) >= precedence(expr[i])"]),
            ("Pop twice: b FIRST, then a. The second pop is the LEFT operand — get this backwards and the code still "
             "runs, but every instruction has its operands swapped.",
             ["strcpy(b, operands[top--]);", "strcpy(a, operands[top--]);"]),
            ("Name the temporary t<counter> with sprintf, print the instruction, push the temporary back as a value, "
             "then bump the counter and drop the operator.",
             ["sprintf(result, \"t%d\", temp);", "strcpy(operands[++top], result);", "temp++;"]),
            ("Push the incoming operator — it now waits for its right operand.",
             ["operators[++opTop] = expr[i];"]),
            ("When the input runs out, drain the operator stack the same way until it is empty.",
             ["while (opTop >= 0) {"]),
        ],
        "curve": [
            ("They add <b>parentheses</b>", "Add a '(' case that pushes without reducing, and a ')' case that reduces "
             "until '(' is popped and discarded. That is the standard extension — say it in those two steps."),
            ("They add <b>^ right-associative</b>", "Give ^ precedence 3, and use > instead of >= when the incoming "
             "operator is ^. Right-associativity IS the > comparison."),
            ("They want unary minus", "Hardest of the four: there is no operand on the left of the stack to pop. You "
             "need a special case that emits t = 0 - a, or a marker operand. Naming the problem earns the marks."),
            ("They change the expression to have multi-letter operands", "isalnum handles one character. You would "
             "collect runs of letters/digits into the operand string — the stacks already hold strings, so nothing "
             "else changes."),
        ],
        "viva": [
            ("Why two stacks?", "The operand stack holds partial results waiting for their operator; the operator stack "
             "holds operators waiting for their right operand."),
            ("Why >= and not >?", ">= reduces equal precedence immediately, giving left-to-right associativity: "
             "a-b-c → (a-b)-c, which is what C does."),
            ("What is a temporary and why invent one?", "A compiler-generated variable holding a partial result, so each "
             "instruction has at most one operator. Real backends map temporaries to registers."),
            ("How do you get a full expression's code, not just one step?", "Steps 2 and 3 of the algorithm run as a "
             "loop: every reduction emits one instruction, and the number of instructions equals the number of "
             "operators in the expression."),
        ],
    },
]

# Per-experiment build command, shown as a copyable block on the page.
BUILD = {
    "exp1": "gcc lex_a.c && ./a.out          # reads input.c from the same folder",
    "exp2": "lex lexer.l && gcc lex.yy.c -lfl && ./a.out",
    "exp3": "lex lex_count.l && gcc lex.yy.c -lfl && ./a.out     # Ctrl+D at the end",
    "exp4": "yacc -d yacc_id.y && lex lex_id.l && gcc y.tab.c lex.yy.c -lfl && ./a.out",
    "exp5": "gcc e_closure.c && ./a.out",
    "exp6": "gcc e-nfa_nfa.c && ./a.out",
    "exp7": "gcc nfa_dfa.c && ./a.out",
    "exp8": "gcc fnf.c && ./a.out",
    "exp9": "gcc rdp.c && ./a.out",
    "exp10": "gcc srp.c && ./a.out",
    "exp11": "gcc intermediate.c && ./a.out",
}
