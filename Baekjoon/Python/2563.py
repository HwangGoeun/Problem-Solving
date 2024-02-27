paper = [[0 for _ in range(100)] for _ in range(100)]

for i in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            paper[j][i] = 1

sum_count = 0
for i in range(100):
    sum_count += paper[i].count(1)
print(sum_count)