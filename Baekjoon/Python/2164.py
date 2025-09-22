import queue

cards = queue.Queue()
for i in range(1, int(input()) + 1):
    cards.put(i)

while cards.qsize() > 1:
    cards.get()
    cards.put(cards.get())

print(cards.queue[0])