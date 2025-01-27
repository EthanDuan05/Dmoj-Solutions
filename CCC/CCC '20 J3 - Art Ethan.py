N = int(input())  # number of the points
x_max = -1
x_min = 101
y_max = -1
y_min = 101
for i in range(N):
    x,y = input(). split(',')
    x = int(x)
    y = int(y)
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
print(str(x_min - 1) + ',' + str(y_min - 1))
print(str(x_max + 1) + ',' + str(y_max + 1))