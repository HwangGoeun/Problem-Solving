n = int(input())
sum = 2
if n >= 1:
    i = n-1
    while i >= 0:
        sum += 2 ** i
        i -= 1
print(sum * sum)