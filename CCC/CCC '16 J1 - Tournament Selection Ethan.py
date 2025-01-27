w = 0
l = 0
for i in range(6):
    m = input()
    if m == 'W':
        w += 1
    elif m == 'L':
        l += 1
if 5 <= w <= 6:
    print(1)
elif 3 <= w <= 4:
    print(2)
elif 1 <= w <= 2:
    print(3)
else:
    print(-1)