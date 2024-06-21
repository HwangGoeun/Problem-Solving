import sys

stack = []

def push(num):
    global stack, index
    stack.append(num)
    return stack

def pop():
    global stack
    if stack:
        print(stack.pop())
    else:
        print(-1)

def printLen():
    global stack
    print(len(stack))

def isEmpty():
    global stack
    if stack:
        print(0)
    else:
        print(1)

def printTop():
    global stack
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    req = list(map(int, sys.stdin.readline().split()))

    if req[0] == 1:
        stack = push(req[1])
    elif req[0] == 2:
        pop()
    elif req[0] == 3:
        printLen()
    elif req[0] == 4:
        isEmpty()
    elif req[0] == 5:
        printTop()