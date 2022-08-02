#include <stdio.h>

// find highest score
double max = 0;
void MAX(double sc) {
	if(max < sc) {
		max = sc;
	}
}

int main() {
	int n;
	scanf("%d", &n);
	double score[n];
	
	// input scores
	int i;
	for(i = 0; i < n; i++) {
		scanf("%lf", &score[i]);
		MAX(score[i]);
	}
	
	// calculate sum
	double sum = 0;
	for(i = 0; i < n; i++) {
		score[i] = score[i]/max*100;
		sum += score[i];
	}
	double avg = sum / (double)n;
	printf("%lf", avg);
	
	return 0;
}
