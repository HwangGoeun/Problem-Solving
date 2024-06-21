import sys

N = int(input())
xs = []
ys = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

if N != 1:
    print((max(xs) - min(xs)) * (max(ys) - min(ys)))
else:
    print(0)