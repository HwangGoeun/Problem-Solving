nums = []
isosceles = False

for i in range(3):
    n = int(input())
    if n in nums:
        isosceles = True
    nums.append(n)

if nums[0] == 60 and nums[1] == 60 and nums[2] == 60:
    print("Equilateral")
elif sum(nums) == 180 and isosceles:
    print("Isosceles")
elif sum(nums) == 180 and not isosceles:
    print("Scalene")
else:
    print("Error")