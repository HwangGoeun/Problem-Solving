names = []
for i in range(int(input())):
    names.append(list(input().split()))

names = sorted(names, key = lambda x: int(x[0]))
for i in range(len(names)):
    print(names[i][0], names[i][1])