import sys
input = sys.stdin.readline

row = int(input())
colum = int(input())

area = []
for i in range(row):
    area.append([0] * colum)

# 0 is black, 1 is gold
K = int(input())
for _ in range(K):
    order, inde = input().split()
    inde = int(inde)
    if order == 'R':
        for m in range(len(area[inde - 1])):
            if area[inde - 1][m] == 0:
                area[inde - 1][m] = 1
            else:
                area[inde - 1][m] = 0

    elif order == 'C':
        for s in area:
            if s[inde - 1] == 0:
                s[inde - 1] = 1
            else:
                s[inde - 1] = 0

ANS = 0
for s in area:
    ans = s.count(1)
    ANS += ans
print(ANS)