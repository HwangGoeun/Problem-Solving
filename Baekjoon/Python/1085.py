x, y, w, h = map(int, input().split())

nums = []
nums.append(abs(x))
nums.append(abs(x - w))
nums.append(abs(y))
nums.append(abs(y - h))

print(min(nums))