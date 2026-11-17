/*
yacc -d yacc_id.y
lex lex_id.l

gcc y.tab.c lex.yy.c -ll
./a.out

abc123
123abc
*/

%{
#include <stdio.h>

int yylex(void);
int yyerror(char *s);
%}

%token LETTER DIGIT

%%

start:
      identifier '\n'   { printf("Valid Identifier\n"); }
    ;

identifier:
      LETTER
    | identifier LETTER
    | identifier DIGIT
    ;

%%

int main()
{
    printf("Enter an identifier: ");
    yyparse();
    return 0;
}

int yyerror(char *s)
{
    printf("Invalid Identifier\n");
    return 0;
}
