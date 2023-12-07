sum = int(input())
num = sum
new_list = []

for i in range(num):
    word = list(input())

    new_list.append(word[0])
    for j in range(1, len(word)):

        # 이전 리스트 값과 비교했을 때 다르면
        if word[j] != word[j - 1]:

            # 기존 new_list에 있던 값인지 체크 - 없으면
            if new_list.count(word[j]):
                new_list.append(word[j])
            # 기존 new_list에 있으면 (그룹 단어가 아니면)
            else:
                sum -= 1
                break

print(sum)