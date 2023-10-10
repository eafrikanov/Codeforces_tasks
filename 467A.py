quantity_of_rooms = int(input())
quantity_of_rooms_where_can_lay = 0
for i in range(quantity_of_rooms):
    live, max_to_live = map(int, input().split())
    if live + 2 <= max_to_live:
        quantity_of_rooms_where_can_lay += 1

print(quantity_of_rooms_where_can_lay)
