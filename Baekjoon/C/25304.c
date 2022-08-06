#include <stdio.h>

int main() {
	// x = total cost, n = number of items purchased, a = cost of item, b = number of items
	int x, n, a, b, sum = 0;
	scanf("%d", &x);
	scanf("%d", &n);
	
	int i;
	for (i = 0; i < n; i++) {
		scanf("%d %d", &a, &b);	
		sum += a * b;
	}
	
	if (sum == x) {
		printf("Yes");
	}
	else {
		printf("No");
	}
	
	return 0;
}
