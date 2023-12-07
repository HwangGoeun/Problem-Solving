import collections

word = input().upper()
wordList = []
max_num = 0
max_char = ""

# 입력된 문자열 리스트로 생성
for i in range(len(word)):
    wordList.append(word[i])

# 최대 빈도 개수가 같은 문자를 찾기 위해 a~z 까지 개수 세기 (가장 마지막에 나오는 최대 빈도 문자 저장)
for i in range(65):
    if word.count(chr(65 + i)) >= max_num:
        max_num = word.count(chr(65 + i))
        max_char = chr(65 + i)

# 가장 첫번째 최대 빈도 문자 저장
wordList.sort()
common_char = collections.Counter(wordList).most_common(1)[0][0]

# 가장 많이 나온 문자의 빈도수와 가장 마지막에 나오는 최대 빈도 문자의 개수가 동일할 때
# 문자의 값이 다르면
if word.count(common_char) == max_num and common_char != max_char:
    print("?")
else:
    print(common_char)