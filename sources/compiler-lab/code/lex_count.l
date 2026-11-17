/*
lex lex_count.l
gcc lex.yy.c
./a.out
hello world
this is lex

ctrl + d
*/

%{
#include <stdio.h>

int lines = 0;
int words = 0;
int characters = 0;
%}

%%

\n              { lines++; characters++; }

[ \t]+          { characters += yyleng; }

[a-zA-Z0-9]+    { words++; characters += yyleng; }

.               { characters++; }

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the text:\n");
    yylex();

    printf("\nNumber of lines      : %d\n", lines);
    printf("Number of words      : %d\n", words);
    printf("Number of characters : %d\n", characters);

    return 0;
}
