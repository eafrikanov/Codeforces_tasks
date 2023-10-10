n, k = map(int, input().split())
spisok_nechet = []
spisok_chet = []
for i in range(n):
    if i % 2 == 0:
        spisok_nechet.append(i + 1)
    else:
        spisok_chet.append(i + 1)


all_spisok = spisok_nechet + spisok_chet
print(all_spisok[k - 1])

