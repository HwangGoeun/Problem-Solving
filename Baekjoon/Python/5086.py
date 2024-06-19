while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    state = "neither"
    if b % a == 0:
        state = "factor"
    if a % b == 0:
        state = "multiple"

    print(state)