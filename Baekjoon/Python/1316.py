sum = int(input())
num = sum
new_list = []

# 입력한 숫자만큼 입력받기
for i in range(num):
    # 문자열 입력 받으면 리스트로 변환
    word = list(input())

    new_list.append(word[0])
    for i in range(1, len(word)):        
        if word[j] == word[j-1]:
            

print(sum)