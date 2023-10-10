quantity_of_oranges = int(input())
all_juice = list(map(int, input().split(' ')))
a = sum(all_juice)
print(a / quantity_of_oranges)