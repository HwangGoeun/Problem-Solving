#include <stdio.h>
#include <string.h>

#define MAX_LENGTH	80

int main() {
	int n;
	scanf("%d", &n);
	char sc[MAX_LENGTH];
	
	int i, j;
	for(i = 0; i < n; i++) {
		scanf("%s", sc);	// input scores

		// calculate sum		
		int sum = 0, cnt = 0;
		for(j = 0; j < strlen(sc); j++) {
			if (sc[j] == 'O') {
				++cnt;
				sum += cnt;
			}
			else {
				cnt = 0;
			}
		}
		printf("%d\n", sum);
	}
}
