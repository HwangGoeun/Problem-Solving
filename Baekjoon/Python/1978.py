n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    j = 0
    for jj in range(2, i + 1):
        j = jj
        if i % jj == 0:
            break
    if i == j:
        count += 1
print(count)