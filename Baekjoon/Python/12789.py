n = int(input())
nums = list(map(int, input().split()))
others = []

i = 0
for _ in range(n):
    if nums[0] == i + 1:
        nums.remove(nums[0])
        i += 1
    elif others and others[-1] == i + 1:
        others.pop()
        i += 1
    else:
        others.append(nums[0])
        nums.remove(nums[0])

if (not others) or (others == sorted(others, reverse=True)):
    print("Nice")
else:
    print("Sad")