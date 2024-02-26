import math

for i in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(1)
    else:
        print(int(math.factorial(b) / (math.factorial(b-a)*math.factorial(a))))