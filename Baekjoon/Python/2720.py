T = int(input())
for i in range(T):
    C = int(input())
    print("%d" % (C // 25), end = " ")
    print("%d" % (C % 25 // 10), end = " ")
    print("%d" % (C % 25 % 10 // 5), end = " ")
    print("%d" % (C % 25 % 10 % 5 // 1))