n, b = map(int, input().split())

remainder = n
sum_list = []

while remainder >= b:
    sum_list.append(remainder % b)
    remainder = remainder // b
sum_list.append(remainder)
print(sum_list)

sum = []
for i in range(len(sum_list)):
    num = sum_list[i]
    if num >= 10:
        sum.insert(0, chr(num + 55))
    else:
        sum.insert(0, str(num))

print(''.join(sum))
    
