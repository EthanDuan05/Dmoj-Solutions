import math
x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())
D = int(input())
value_1 = math.sqrt((x_1 - x_3)**2 + (y_1 - y_3)**2)
value_2 = math.sqrt((x_2 - x_3)**2 + (y_2 - y_3)**2)

if D >= value_1 or D >= value_2:
    print('Yes')
else:
    print('No')