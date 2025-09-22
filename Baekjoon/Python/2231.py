n = int(input())
sum = 0
i = 0
for i in range(1, 1000001):
    num = list(map(int, str(i)))
    sum = i
    for j in num:
        sum += j
    if sum == n:
        break
    if i == 1000000 and sum != n:
        i = 0
        break
print(i)