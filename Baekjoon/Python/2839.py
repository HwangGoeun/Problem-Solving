n = int(input())
sugar = 0

while True: 
    if n >= 5:
        sugar += n // 5
        n = n % 5
    else :
        if n >= 3:
            sugar += n // 3
            n = n % 3
        else :
            sugar += n - 3
            break

print(sugar)