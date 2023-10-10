word = input().lower()
n = 0
various_symbols = 0
for i in range(len(word)):
    if word[n] not in word[:n]:
        n += 1
        various_symbols += 1
    else:
        n += 1

if various_symbols % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
