names = []
for i in range(int(input())):
    name, state = input().split()
    if state == "leave":
        names.remove(name)
    else:
        names.append(name)

names = sorted(names, reverse=True)
print("\n".join(names))