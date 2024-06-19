n = int(input())
i = 6
count = 1
while n > 1:
    n -= i
    i += 6
    count += 1
print(count)