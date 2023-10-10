import math
n, m, a = map(int, input().split())

answer_n = math.ceil(n / a)
answer_m = math.ceil(m / a)
print(answer_n * answer_m)
