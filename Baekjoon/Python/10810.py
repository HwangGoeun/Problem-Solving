n, m = map(int, input().split())

# 리스트 만들기
basket = []
for i in range(n+1):
    basket.append(0)

# 공 계산
for i in range(m):
    i, j, k = map(int, input().split())
    
    for b in range(i, j+1):
        basket[b] = k

print(*basket[1:])