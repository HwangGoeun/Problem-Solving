numbers = []
chosen = []
for i in range(2):
    numbers.append(int(input()))
for i in range(numbers[0], numbers[1] + 1):
    j = 0
    for jj in range(2, i + 1):
        j = jj
        if i % jj == 0:
            break
    if i == j:
        chosen.append(i)
if chosen:
    print(sum(chosen))
    print(chosen[0])
else:
    print(-1)