#include <stdio.h>
#include <string.h>

#define MAX_LENGTH	10			        // 999 * 999 * 999 = 997002999

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	int sum = a * b * c;
	
	char str[MAX_LENGTH];
	
	sprintf(str, "%d", sum);
	
	int i, j;
	int cnt[10] = {0};
	for (i = 0; i < strlen(str); i++) {
		for (j = 0; j < 10; j++) {
			int ctoi = str[i] - '0';	// convert character to int
			if (ctoi == j) {
				++cnt[j];
				break;
			}
		}
	}
	
	// output number counts
	for (i = 0; i < 10; i++) {
		printf("%d\n", cnt[i]);
	}
	
	return 0;
}
