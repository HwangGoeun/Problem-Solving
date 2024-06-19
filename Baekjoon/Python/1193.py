X = int(input())
i = 1
while X > 0:
    X -= i
    i += 1
i -= 1
if i % 2 == 0:
    print("%d/%d" % (i + X, abs(X) + 1))
else:
    print("%d/%d" % (abs(X) + 1, i + X))