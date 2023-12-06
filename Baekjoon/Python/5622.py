dial = input()
time = 0
for i in range(len(dial)):
    cal = ord(dial[i]) / 3
    if ord(dial[i]) <= 82:
        if round(cal, 1) - int(cal) == 0.6:
            time += (round(cal, 0)-1) % 7 + 3
        else:
            time += round(cal, 0) % 7 + 2
    elif ord(dial[i]) == 83:
        time += 8
    elif ord(dial[i]) <= 89:
        time += int(cal) - 19
    else:
        time += 10

print(str(int(time)))