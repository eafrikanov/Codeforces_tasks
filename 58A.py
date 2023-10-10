word = 'gf'
word += 'a'
print(word)
check_word = str
for letter in range(len(word)):
    if letter == 'h':
        if 'h' not in check_word:
            check_word += 'h'
