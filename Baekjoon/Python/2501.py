N, K = map(int, input().split())
count = 0
check = False
for i in range(1, N + 1):
    if N % i == 0:
        count += 1
    if count == K:
        check = True
        break
if check:
    print(i)
else:
    print(0)