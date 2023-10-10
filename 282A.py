n = int(input())
x = 0
for i in range(n):
    new_line = input()
    if '++' in new_line:
        x += 1
    if '--' in new_line:
        x -= 1

print(x)
