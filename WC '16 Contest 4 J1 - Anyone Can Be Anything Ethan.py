N = int(input())
L1, L2 = map(int, input().split())
line = list(map(int, input().split()))

cnt = 0
for i in line:
    if i == 1:
        if L1 > 0:
            cnt += 1
            L1 -= 1
    elif i == 2:
        if L2 > 0:
            cnt += 1
            L2 -= 1

print(cnt)
