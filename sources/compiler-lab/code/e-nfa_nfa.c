/*
gcc e-nfa_nfa.c
./a.out

3
2
a b

3
0 1 2

2 
1 2

1
2

1 1
1 0
1 2
0
0 
1 2
*/

#include <stdio.h>
#include <string.h>

#define MAX 10

int n, m;
char symbols[MAX];
int trans[MAX][MAX][MAX];  
int eclose[MAX][MAX];
int ecount[MAX];

void addState(int arr[], int *count, int state) {
    for (int i = 0; i < *count; i++)
        if (arr[i] == state)
            return;
    arr[(*count)++] = state;
}

int main() {
    int i, j, k;

    printf("Enter number of states: ");
    scanf("%d", &n);

    printf("Enter number of input symbols: ");
    scanf("%d", &m);

    printf("Enter input symbols: ");
    for (i = 0; i < m; i++)
        scanf(" %c", &symbols[i]);

    printf("\nEnter epsilon closure of each state:\n");
    for (i = 0; i < n; i++) {
        printf("Number of states in E-closure(q%d): ", i);
        scanf("%d", &ecount[i]);
        printf("States: ");
        for (j = 0; j < ecount[i]; j++)
            scanf("%d", &eclose[i][j]);
    }

    printf("\nEnter transitions (number of destinations followed by states):\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            printf("d(q%d,%c): ", i, symbols[j]);
            scanf("%d", &trans[i][j][0]);
            for (k = 1; k <= trans[i][j][0]; k++)
                scanf("%d", &trans[i][j][k]);
        }
    }

    printf("\nEquivalent NFA without epsilon transitions:\n");

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            int result[MAX], rcount = 0;

            for (k = 0; k < ecount[i]; k++) {
                int state = eclose[i][k];

                int tcount = trans[state][j][0];
                for (int x = 1; x <= tcount; x++) {
                    int next = trans[state][j][x];

                    for (int y = 0; y < ecount[next]; y++)
                        addState(result, &rcount, eclose[next][y]);
                }
            }

            printf("d'(q%d,%c) = { ", i, symbols[j]);
            for (k = 0; k < rcount; k++)
                printf("q%d ", result[k]);
            printf("}\n");
        }
    }

    return 0;
}





