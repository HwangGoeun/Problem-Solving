import math

n, b = input().split()
n = list(reversed(list(n)))
b = int(b)
sum = 0

for i in range(len(n)):
    if ord(n[i]) >= 65:
        sum += (ord(n[i]) - 55) * math.pow(b, i)
    else:
        sum += int(n[i]) * math.pow(b, i)

print(int(sum))