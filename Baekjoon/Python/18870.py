n = int(input())
numbers = list(map(int, input().split()))
sets = list(set(numbers))

for i in range(n):
    count = 0
    for j in sets:
        if numbers[i] > j:
            count += 1
    print(count, end = " ")