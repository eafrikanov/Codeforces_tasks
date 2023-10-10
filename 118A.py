word = str(input())
all_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
n = 0
for i in range(len(word)):
    if i in all_gls:
        word.replace(word[n], '')
        n += 1
print(word)
