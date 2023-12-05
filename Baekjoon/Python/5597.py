students = list(range(1, 31))

for i in range(len(students) - 2):
    number = int(input())
    if students.count(number):
        students.remove(number)

print(*students, sep='\n')