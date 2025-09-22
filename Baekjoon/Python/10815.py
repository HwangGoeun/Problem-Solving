n = int(input())
cards = list(map(int, input().split()))
m = int(input())
in_cards = list(map(int, input().split()))

for i in in_cards:
    if i in cards:
        print("1", end = " ")
    else:
        print("0", end = " ")