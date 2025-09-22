sides = list(map(int, input().split()))
max_v = max(sides)
others = sum(sides) - max_v

if others > max_v:
    print(sum(sides))
else:
    print(others * 2 - 1)