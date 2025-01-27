N = int(input())

line = list(map(int, input().split()))

ans = sum(line)

if ans < 200:
    print(200 - ans)
elif ans == 200:
    print(0)
else:
    print('Over maximum capacity!')