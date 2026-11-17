/*
gcc fnf.c
./a.out
4
S=AB
A=a
B=bC
C=c
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

char prod[10][20];
int n;

void add(char set[], char c) {
    int i;

    for (i = 0; set[i] != '\0'; i++) {
        if (set[i] == c)
            return;
    }

    set[i] = c;
    set[i + 1] = '\0';
}

void FIRST(char c, char result[]) {
    int i, j;

    if (!isupper(c)) {
        add(result, c);
        return;
    }

    for (i = 0; i < n; i++) {
        if (prod[i][0] == c) {
            if (prod[i][2] == '#') {
                add(result, '#');
            } else {
                j = 2;

                while (prod[i][j] != '\0') {
                    char temp[20] = "";

                    FIRST(prod[i][j], temp);

                    int k;
                    int epsilon = 0;

                    for (k = 0; temp[k] != '\0'; k++) {
                        if (temp[k] == '#')
                            epsilon = 1;
                        else
                            add(result, temp[k]);
                    }

                    if (!epsilon)
                        break;

                    j++;
                }
            }
        }
    }
}

void FOLLOW(char c, char result[]) {
    int i, j, k;

    if (c == prod[0][0])
        add(result, '$');

    for (i = 0; i < n; i++) {
        for (j = 2; prod[i][j] != '\0'; j++) {
            if (prod[i][j] == c) {
                if (prod[i][j + 1] != '\0') {
                    char next = prod[i][j + 1];
                    char temp[20] = "";

                    FIRST(next, temp);

                    int epsilon = 0;

                    for (k = 0; temp[k] != '\0'; k++) {
                        if (temp[k] == '#')
                            epsilon = 1;
                        else
                            add(result, temp[k]);
                    }

                    if (epsilon) {
                        char temp2[20] = "";

                        if (prod[i][0] != c) {
                            FOLLOW(prod[i][0], temp2);

                            for (k = 0; temp2[k] != '\0'; k++)
                                add(result, temp2[k]);
                        }
                    }
                } else {
                    if (prod[i][0] != c) {
                        char temp[20] = "";

                        FOLLOW(prod[i][0], temp);

                        for (k = 0; temp[k] != '\0'; k++)
                            add(result, temp[k]);
                    }
                }
            }
        }
    }
}

int main() {
    int i, j;
    char temp[20];

    printf("Enter number of productions: ");
    scanf("%d", &n);

    printf("Enter productions (use # for epsilon):\n");

    for (i = 0; i < n; i++)
        scanf("%s", prod[i]);

    printf("\nFIRST sets:\n");

    for (i = 0; i < n; i++) {
        temp[0] = '\0';

        FIRST(prod[i][0], temp);

        printf("FIRST(%c) = {", prod[i][0]);

        for (j = 0; temp[j] != '\0'; j++)
            printf(" %c", temp[j]);

        printf(" }\n");
    }

    printf("\nFOLLOW sets:\n");

    for (i = 0; i < n; i++) {
        temp[0] = '\0';

        FOLLOW(prod[i][0], temp);

        printf("FOLLOW(%c) = {", prod[i][0]);

        for (j = 0; temp[j] != '\0'; j++)
            printf(" %c", temp[j]);

        printf(" }\n");
    }

    return 0;
}
