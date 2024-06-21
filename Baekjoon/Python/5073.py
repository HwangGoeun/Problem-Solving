while True:
    sides = list(map(int, input().split()))
    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0:
        break

    if max(sides) >= sum(sides) - max(sides):
        print("Invalid")
    elif sides[0] == sides[1] and sides[1] == sides[2]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print("Isosceles")
    elif sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        print("Scalene")