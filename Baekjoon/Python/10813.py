n, m = map(int, input().split())

basket = [0] * n
for b in range(n):
    basket[b] = b + 1

for b in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)