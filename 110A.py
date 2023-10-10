a = list(map(int, input()))

count_7 = a.count(7)
count_4 = a.count(4)
x = {4, 7}


if (count_4 + count_7) in x:
    print('YES')
else:
    print('NO')
