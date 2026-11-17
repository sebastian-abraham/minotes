/*
lex lexer.l
gcc lex.yy.c
/a.out
int a = a+b*2;
*/

%{
#include <stdio.h>
%}

%%

"int"|"float"|"char"|"double"|"void"|"if"|"else"|"while"|"for"|"return"|"break"|"continue"|"main"    { printf("Keyword : %s\n", yytext); }

[0-9]+    { printf("Number : %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*    { printf("Identifier : %s\n", yytext); }

"=="|"!="|"<="|">="|"="|"<"|">"|"+"|"-"|"*"|"/"    { printf("Operator : %s\n", yytext); }

"["|"]"|"("|")"|"{"|"}"|";"|","    { printf("Special Symbol : %s\n", yytext); }

[ \t\n]+    ;

.    { printf("Unknown : %s\n", yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter a C program:\n");
    yylex();
    return 0;
}
