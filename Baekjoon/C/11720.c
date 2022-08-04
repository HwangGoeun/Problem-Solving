#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	
	int i;
	int number[100] = {0}, sum = 0;
	for (i = 0; i < n; i++) {
		scanf("%1d", &number[i]);
		sum += number[i];
	}
	
	printf("%d", sum);
	
	return 0;
}
