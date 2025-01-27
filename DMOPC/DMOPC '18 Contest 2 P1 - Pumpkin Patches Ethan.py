max_x = 0
min_x = 0
max_y = 0
min_y = 0

P = int(input())
for _ in range(P):
    x, y = map(int, input().split())
    if x > max_x:
        max_x = x

    if x < min_x:
        min_x = x

    if y > max_y:
        max_y = y

    if y < min_y:
        min_y = y

length = max_x - min_x
width = max_y - min_y

print((length + width) * 2)