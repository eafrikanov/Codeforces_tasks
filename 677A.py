quantity, height = map(int, input().split())
road_width = 0
n = 0
boy_height = input().split()
for i in range(quantity):
    if int(boy_height[n]) > height:
        n += 1
        road_width += 2
    else:
        road_width += 1
        n += 1
print(road_width)
