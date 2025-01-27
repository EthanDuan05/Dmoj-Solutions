c, r = map(int, input().split())
ans = []
x_i, y_i = 0, 0
while True:
    a, b = map(int, input().split())
    if a != 0 or b != 0:
        if 0 <= x_i+a <= c and 0 <= y_i+b <= r:
            x_i += a
            y_i += b

        elif x_i+a > c and y_i+b > r:
            x_i = c
            y_i = r
        elif x_i+a > c and 0 <= y_i+b <= r:
            x_i = c
            y_i += b
        elif x_i+a > c and y_i + b < 0:
            x_i = c
            y_i = 0

        elif x_i + a < 0 and y_i + b > r:
            x_i = 0
            y_i = r
        elif 0 <= x_i+a <= c and y_i + b > r:
            x_i += a
            y_i = r

        elif x_i + a < 0 and y_i + b < 0:
            x_i = 0
            y_i = 0
        elif x_i + a < 0 and 0 <= y_i+b <= r:
            x_i = 0
            y_i += b
        elif x_i + a < 0 and y_i+b > r:
            x_i = 0
            y_i = r

        elif x_i + a < 0 and y_i + b < 0:
            x_i = 0
            y_i = 0
        elif 0 <= x_i+a <= c and y_i + b < 0:
            x_i += a
            y_i = 0
        elif x_i + a > c and y_i + b < 0:
            x_i = c
            y_i = 0
        ans.append(str(x_i)+' '+str(y_i))
    elif a == 0 and b == 0:
        break

for i in ans:
    print(i)