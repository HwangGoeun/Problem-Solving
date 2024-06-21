N = int(input())
factors = list()

i = 2
while i <= N:
    if N % i == 0:
        factors.append(i)
        N /= i
    else:
        i += 1

for i in factors:
    print(i)