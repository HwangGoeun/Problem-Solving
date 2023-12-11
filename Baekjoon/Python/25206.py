def compare(grade):
    if grade == 'A+':
        return 4.5
    elif grade == 'A0':
        return 4.0
    elif grade == 'B+':
        return 3.5
    elif grade == 'B0':
        return 3.0
    elif grade == 'C+':
        return 2.5
    elif grade == 'C0':
        return 2.0
    elif grade == 'D+':
        return 1.5
    elif grade == 'D0':
        return 1.0
    elif grade == 'F':
        return 0.0

# 학점 * 과목 평점
calSum = 0
# 학점의 합
sum = 0
for i in range(20):
    sub, score, grade = input().split()
    if grade != 'P':
        calSum += float(score) * compare(grade)
        sum += float(score)

print(calSum / sum)