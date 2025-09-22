for i in range(int(input())):
    a, b = map(int, input().split())
    sum = 1
    common_list = [1, 1, 1]
    if a > b:
        a, b = b, a
    for num in range(1, a + 1):
        if a % num == 0 and b % num == 0:
            common_list = [num, a // num, b // num]
    for common in common_list:
        sum *= common
    print(sum)