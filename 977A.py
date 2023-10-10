number, amount_of_subtraction = map(int, input().split())

for i in range(amount_of_subtraction):
    if number % 10 == 0:
        number /= 10
    else:
        number -= 1

print(int(number))