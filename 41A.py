normal_word = input()
reversed_word = input()
a = ''.join(reversed(normal_word))
if a == reversed_word:
    print('YES')
else:
    print('NO')
