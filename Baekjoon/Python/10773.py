stack = []

def push(num):
    global stack
    stack.append(num)

def pop():
    global stack
    stack.pop()

for i in range(int(input())):
    n = int(input())
    if n != 0:
        push(n)
    else:
        pop()

print(sum(stack))