n, m = map(int, input().split())
cards = list(map(int, input().split()))
sum = 0
max = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if i == j or j == k or k == i:
                continue
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m:
                if max < sum:
                    max = sum

print(max)