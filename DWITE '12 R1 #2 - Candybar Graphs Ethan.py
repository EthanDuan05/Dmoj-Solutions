import math

for _ in range(5):
    a, b = map(int, input().split())
    total = a + b
    percent = 100 * (a / total)
    # print(percent)
    percent = math.floor(percent/10)
    # print(percent)
    print('*'*percent + '.' * (10 - percent))