n, k = map(int, input().split())
std = sorted(list(map(int, input().split())), reverse=True)
print(std[k-1])