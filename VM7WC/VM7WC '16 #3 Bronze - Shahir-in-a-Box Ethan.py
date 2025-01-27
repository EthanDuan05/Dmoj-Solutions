N = int(input())

max_x = -1e9
max_y = -1e9

min_x = 1e9
min_y = 1e9

for _ in range(N):
    x, y = map(int, input().split())
    if x > max_x:
        max_x = x

    if x < min_x:
        min_x = x

    if y > max_y:
        max_y = y

    if y < min_y:
        min_y = y

x_d = max_x - min_x
y_d = max_y - min_y

print(x_d*y_d)