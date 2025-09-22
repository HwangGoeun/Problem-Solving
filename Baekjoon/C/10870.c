#include <stdio.h>
#include <stdlib.h>

int fib(int arr[], int n) {
    if (arr[n] != -1) {
        return arr[n];
    }
    else if (n == 0) {
        arr[n] = 0;
    }
    else if (n <= 2) {
        arr[n] = 1;
    } else {
        arr[n] = fib(arr, n - 1) + fib(arr, n - 2);
    }
    
    return arr[n];
}

int main() {
    int n;
    scanf("%d", &n);
    
    int * fibs = calloc(n + 1, sizeof(int));
    for (int i = 0; i <= n; i++) {
        fibs[i] = -1;
    }
    
    printf("%d", fib(fibs, n));

    return 0;
}