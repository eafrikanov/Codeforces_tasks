pay_for_1banana, dollars, number_of_bananas = map(int, input().split())
i = 1
pay_for_all_bananas = 0

b = []
for i in range(number_of_bananas):
    i += 1
    pay_for_all_bananas = i * pay_for_1banana
    b.append(pay_for_all_bananas)

pay_for_all_bananas = sum(b)

if pay_for_all_bananas <= dollars:
    print('0')
else:
    print(pay_for_all_bananas - dollars)
