a = [[0 for i in range(9)] for j in range(9)]
max = 0
row = 1
col = 1

for i in range(9):
    a[i] = list(map(int, input().split()))
    for j in range(9):
        if a[i][j] > max:
            max = a[i][j]
            row = i + 1
            col = j + 1

print(max)
print(row, col)