distance = int(input())
my_house = 0
steps = 0
while distance != 0:
    if distance >= 5:
        distance -= 5
        steps += 1
    if 5 > distance == 4:
        distance -= 4
        steps += 1
    if 5 > distance == 3:
        distance -= 3
        steps += 1
    if 5 > distance == 2:
        distance -= 2
        steps += 1
    if 5 > distance == 1:
        distance -= 1
        steps += 1


print(steps)
