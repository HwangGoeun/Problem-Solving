#include <stdio.h>

int fib_sum = 0;
int fibonacci_sum = 0;
int f[40] = {0};

int fib(int n) {
    if (n == 1 || n == 2) {
        fib_sum += 1;
        return 1;        
    }
        
    else {
        return fib(n-1) + fib(n-2);
    }
}

int fibonacci(int n) {
    for (int i = 2; i <= n - 1; i++) {
        f[i] = f[i - 1] + f[i - 2];
        fibonacci_sum += 1;
    }
    
    return f[n];
}

int main() {
    f[0] = 1;
    f[1] = 1;
    int n;
    scanf("%d", &n);
    
    fib(n);
    fibonacci(n);
    
    printf("%d\n%d", fib_sum, fibonacci_sum);
    
    return 0;
}