sum = int(input())
num = sum

# 입력한 숫자만큼 입력받기
for i in range(num):
    # 문자열 입력 받으면 리스트로 변환
    word = list(input())

    # 첫 글자 리스트에 집어넣기
    new_list = []
    new_list.append(word[0])

    # 그 다음 글자부터 리스트값 비교 시작
    for j in range(1, len(word)):        
        # 만약 이전값과 현재값이 다르다면
        if word[j] != word[j-1]:
            # new_list에 들어있는 값인지 확인 -> 아니면 -> 리스트에 값 추가
            if not word[j] in new_list:
                new_list.append(word[j])
            # 이미 들어있으면 sum -= 1 하고 반복문 탈출
            else:
                sum -= 1
                break

print(sum)