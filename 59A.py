word = input()
n = 0
lower = 0
upper = 0
for i in range(len(word)):
    if word[n].isupper() == True:
        n += 1
        upper += 1
    else:
        n += 1
        lower += 1

if lower >= upper:
    print(word.lower())
else:
    print(word.upper())
