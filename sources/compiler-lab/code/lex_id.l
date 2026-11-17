/*
yacc -d yacc_id.y
lex lex_id.l

gcc y.tab.c lex.yy.c -ll
./a.out

abc123
123abc
*/

%{
#include "y.tab.h"
%}

%%

[a-zA-Z]    { return LETTER; }
[0-9]       { return DIGIT; }
\n          { return '\n'; }
.           { return yytext[0]; }

%%
