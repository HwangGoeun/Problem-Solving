#include <stdio.h>

#define MAX_LENGTH	1000

int main() {
	int c;								// the number of test cases
	scanf("%d", &c);
	
	int i, j;
	int score[MAX_LENGTH];
	for (i = 0; i < c; i++) {	
		int n;							// the number of people in the cases.
		scanf("%d", &n);
		
		double sum = 0;
		for (j = 0; j < n; j++) {
			scanf("%d", &score[j]);		// input scores
			sum += (double)score[j];
		}
		double avg = sum / (double)n;
		
		// calculate percentage of studnets whose grade is above average
		int cnt = 0;
		for (j = 0; j < n; j++) {
			if (score[j] > avg) {
				++cnt;
			}
		}
		printf("%.3lf%%\n", (double)cnt / (double)n * (double)100);
	}
	
	return 0;
}
