/*
gcc e_closure.c
./a.out

4
0 1 0 0
0 0 1 0
0 0 0 1
0 0 0 0
*/

#include <stdio.h>

int n;
int epsilon[20][20];
int closure[20][20];

void findClosure(int state, int current){
    int i;

    closure[state][current] = 1;

    for (i = 0; i < n; i++){
        if (epsilon[current][i] == 1 && closure[state][i] == 0){
            findClosure(state, i);
        }
    }
}

int main(){
    int i, j;

    printf("Enter the number of states: ");
    scanf("%d", &n);

    printf("Enter the epsilon transition matrix:\n");
    printf("(Enter 1 if epsilon transition exists, otherwise 0)\n");

    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            scanf("%d", &epsilon[i][j]);
        }
    }

    for (i = 0; i < n; i++){
        findClosure(i, i);
    }

    printf("\nEpsilon Closure of all states:\n");

    for (i = 0; i < n; i++){
        printf("E-closure(q%d) = { ", i);

        for (j = 0; j < n; j++){
            if (closure[i][j] == 1){
                printf("q%d ", j);
            }
        }

        printf("}\n");
    }

    return 0;
}

