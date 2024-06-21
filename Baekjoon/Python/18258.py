import sys

queue = []
front = -1
rear = -1

def push(num):
    global queue, rear, front
    rear += 1
    if rear == 0:
        front += 1
    queue.append(num)

def pop():
    global queue, rear, front
    if rear >= front and (rear != -1):
        print(queue[front])
        front += 1
    else:
        print(-1)

def size():
    global queue, rear, front
    if rear >= front and (rear != -1):
        print(rear - front + 1)
    else:
        print(0)

def empty():
    global queue, rear, front
    if rear >= front and (rear != -1):
        print(0)
    else:
        print(1)

def front_func():
    global queue, rear, front
    if rear >= front and (rear != -1):
        print(queue[front])
    else:
        print(-1)

def back():
    global queue, rear, front
    if rear >= front and (rear != -1):
        print(queue[rear])
    else:
        print(-1)

N = int(input())
for i in range(N):
    req = sys.stdin.readline().split()

    if req[0] == "push":
        push(req[1])
    elif req[0] == "pop":
        pop()
    elif req[0] == "size":
        size()
    elif req[0] == "empty":
        empty()
    elif req[0] == "front":
        front_func()
    elif req[0] == "back":
        back()