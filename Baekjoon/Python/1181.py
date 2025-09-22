words = []
for i in range(int(input())):
    word = input()
    if not word in words:
        words.append(word)

print("\n".join(sorted(sorted(words), key=len)))