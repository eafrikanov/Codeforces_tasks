mas = []
for i in range(5):
    mas.append(list(map(int, input().split())))

row = 0
column = 0

for i in range(5):
    for j in range(5):
        if mas[i][j] == 1:
            row = i
            column = j


print(abs(row - 2) + abs(column - 2))
