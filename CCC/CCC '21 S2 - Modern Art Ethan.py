import sys
input = sys.stdin.readline

row = int(input())
colum = int(input())

area = []
for i in range(row):
    area.append([0] * colum)

K = int(input())
for _ in range(K):
    order, inde = input().split()
    inde = int(inde)
    if order == 'R':
        for m in range(len(area[inde - 1])):
            area[inde - 1][m] += 1

    elif order == 'C':
        for s in area:
            s[inde - 1] += 1

ANS = 0
for s in area:
    for k in s:
        if k % 2 != 0:
            ANS += 1
print(ANS)