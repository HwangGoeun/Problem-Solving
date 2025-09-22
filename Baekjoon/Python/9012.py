check = []

for i in range(int(input())):
    ps = input()
    
    for j in range(len(ps) // 2):
        for jj in range(len(ps)):
            if ps[jj:jj+2] == "()":
                ps = ps[0:jj] + ps[jj+2:]
                break
    
    if ps:
        print("NO")
    else:
        print("YES")