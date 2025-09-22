n = int(input())
sugar = 0

while n >= 3:
    if n % 5 == 0:
        sugar += n // 5
        n = n % 5
    if n % 3 == 0:
        sugar += n // 3
        n = n % 3
if n != 0:
    sugar = -1

print(sugar)