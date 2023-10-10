num_of_people = int(input())
people_ask = input().split(' ')
n = 0
for i in range(num_of_people):
    if people_ask[n] == 0:
        n += 1
        print("yes")
    else:
        print('HARD')
        break
