a = list(map(int, input()))

count_7 = a.count(7)
count_4 = a.count(4)
if (count_4 + count_7) == len(a):
    print('YES')
