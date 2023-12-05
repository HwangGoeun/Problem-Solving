n, m = map(int, input().split())
baskets = list(range(0, n+1))

for b in range(m):
    i, j = map(int, input().split())
    new_list = baskets[i:j+1]
    new_list.reverse()

    index = 0
    for b in range(i, j+1):
        baskets[b] = new_list[index]
        index += 1

print(*baskets[1:])