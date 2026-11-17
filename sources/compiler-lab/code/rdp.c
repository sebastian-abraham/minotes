/*
gcc rdp.c
./a.out

(i+i)*i

./a.out
i+*i
*/

#include <stdio.h>
#include <stdlib.h>

char input[100];
int pos = 0;

void E();
void Eprime();
void T();
void Tprime();
void F();

void error() {
    printf("Invalid string\n");
    exit(0);
}

void E() {
    T();
    Eprime();
}

void Eprime() {
    if (input[pos] == '+') {
        pos++;
        T();
        Eprime();
    }
}

void T() {
    F();
    Tprime();
}

void Tprime() {
    if (input[pos] == '*') {
        pos++;
        F();
        Tprime();
    }
}

void F() {
    if (input[pos] == 'i') {
        pos++;
    }
    else if (input[pos] == '(') {
        pos++;
        E();

        if (input[pos] == ')')
            pos++;
        else
            error();
    }
    else {
        error();
    }
}

int main() {
    printf("Enter the input string: ");
    scanf("%s", input);

    E();

    if (input[pos] == '\0')
        printf("String is accepted\n");
    else
        printf("String is rejected\n");

    return 0;
}
