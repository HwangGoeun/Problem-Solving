cords = []

for i in range(int(input())):
    cords.append(list(map(int, input().split())))

cords = sorted(cords)
for i in range(len(cords)):
    print(cords[i][0], cords[i][1])