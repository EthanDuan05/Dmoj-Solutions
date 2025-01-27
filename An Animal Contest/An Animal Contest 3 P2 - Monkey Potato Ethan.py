k, d = map(int, input().split())

line = list(map(int, input().split()))
line.sort()

if k <= 0 or d <= 0:
    print(-1)
elif max(line) == 0:
    print(-1)
else:
    a = line[0]
    if a == 0:
        if k <= 2:
            print(str(line[1])*k)
        else:
            print(str(line[1]) + '0'*(k-2) + str(line[1]))
    elif a > 0:
        print(str(a)*k)
