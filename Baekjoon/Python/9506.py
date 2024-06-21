while True:
    n = int(input())
    if n == -1:
        break

    i = 1
    sum = 0
    nums = []
    while i < n:
        if n % i == 0:
            nums.append(i)
            sum += i
        i += 1
    if sum == n:
        print("%d = " % n, end = "")
        for i in nums:
            if i != nums[-1]:
                print("%d + " % i, end = "")
            else:
                print(i)
    else:
        print("%d is NOT perfect." % n)