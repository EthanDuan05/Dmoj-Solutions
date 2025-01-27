n, t = map(int, input().split())

flag = True
for _ in range(n):
    num = int(input())
    if t - num < 0:
        flag = False
        break
    else:
        t -= num
        continue

if flag:
    print(t)
else:
    print('The budget will balance itself')