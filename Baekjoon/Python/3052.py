num = 0
numbers = []

for i in range(10):
    num = int(input()) % 42
    if not numbers.count(num):
        numbers.append(num)

print(len(numbers))