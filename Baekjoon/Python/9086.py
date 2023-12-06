T = int(input())
for i in range(T):
    word = input()
    if len(word) > 1:
        print(word[0]+word[-1])
    else:
        print(word[0]*2)