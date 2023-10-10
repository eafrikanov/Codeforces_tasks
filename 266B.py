quantity, time = map(int, input().split())
queue = (input())
ll = list(queue)
n = 0
for i in ll:
    if ll[n] == 'B' and ll[n+1] == 'G':
        time += 1
        n += 1
        ll[n], ll[n+1] = ll[n+1], ll[n]


print(queue)