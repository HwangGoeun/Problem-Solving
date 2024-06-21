cors = []
for i in range(3):
    a, b = map(int, input().split())
    cors.append(a)
    cors.append(b)

check1 = []
for i in range(3):
    index = i * 2
    if not cors[index] in check1:
        check1.append(cors[index])
    else:
        check1.remove(cors[index])

check2 = []
for i in range(1, 6, 2):
    if not cors[i] in check2:
        check2.append(cors[i])
    else:
        check2.remove(cors[i])

print(check1[0], check2[0])
