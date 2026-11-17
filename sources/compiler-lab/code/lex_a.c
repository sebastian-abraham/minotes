/*
gcc lex_a.c
./a.out
*/

#include <stdio.h>
#include <ctype.h>
#include <string.h>

char *keywords[] = {
    "int", "float", "char", "if", "else", "while", "for",
    "return", "void", "break", "continue", "double","main"
};

int isKeyword(char *str) {
    int n = sizeof(keywords) / sizeof(keywords[0]);
    for (int i = 0; i < n; i++) {
        if (strcmp(str, keywords[i]) == 0)
            return 1;
    }
    return 0;
}

int main() {
    FILE *fp = fopen("input.c", "r");

    char ch, buffer[100];
    int i;

    while ((ch = fgetc(fp)) != EOF) {

        if (ch == ' ' || ch == '\t' || ch == '\n')
            continue;

        if (ch == '/') {
            char next = fgetc(fp);

            if (next == '/') {
                while ((ch = fgetc(fp)) != '\n' && ch != EOF);
                continue;
            }

            else if (next == '*') {
                char prev = 0;
                while ((ch = fgetc(fp)) != EOF) {
                    if (prev == '*' && ch == '/')
                        break;
                    prev = ch;
                }
                continue;
            }

            else {
                printf("Operator : /\n");
                ungetc(next, fp);
                continue;
            }
        }

        if (isalpha(ch) || ch == '_') {
            i = 0;
            buffer[i++] = ch;

            while ((ch = fgetc(fp)) != EOF &&
                   (isalnum(ch) || ch == '_')) {
                buffer[i++] = ch;
            }

            buffer[i] = '\0';

            if (ch != EOF)
                ungetc(ch, fp);

            if (isKeyword(buffer))
                printf("Keyword    : %s\n", buffer);
            else
                printf("Identifier : %s\n", buffer);
        }

        else if (isdigit(ch)) {
            i = 0;
            buffer[i++] = ch;

            while ((ch = fgetc(fp)) != EOF && isdigit(ch)) {
                buffer[i++] = ch;
            }

            buffer[i] = '\0';

            if (ch != EOF)
                ungetc(ch, fp);

            printf("Number     : %s\n", buffer);
        }

        else if (strchr("+-*=<>!%", ch)) {
            printf("Operator   : %c\n", ch);
        }

        else if (strchr("(){}[];,.", ch)) {
            printf("Symbol     : %c\n", ch);
        }
    }

    fclose(fp);
    return 0;
}
