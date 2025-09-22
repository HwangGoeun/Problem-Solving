while True:
    text = input()
    compare = ""

    if text == ".":
        break

    for i in text:
        if i == "(" or i == ")" or i ==  "[" or i == "]":
            compare += i
    
    for j in range(len(compare) // 2):     
        for jj in range(len(compare)):
            if compare[jj:jj+2] == "()" or compare[jj:jj+2] == "[]":
                compare = compare[0:jj] + compare[jj+2:]
                break
    
    print("no" if compare else "yes")