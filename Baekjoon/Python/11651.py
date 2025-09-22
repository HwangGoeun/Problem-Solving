cords = []

for i in range(int(input())):
    x, y = map(int, input().split())
    cords.append([y, x])

cords = sorted(cords)
for i in range(len(cords)):
    print(cords[i][1], cords[i][0])