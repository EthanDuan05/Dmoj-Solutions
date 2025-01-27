T = int(input())
L = []

for i in range(T):
    n = int(input())
    line = input()
    L.append(line.split())


for k in L:
    cnt = 0
    for m in k:
        if m == '0':
            cnt += 1
    if cnt > 1:
        print('YES')
    elif cnt == 1:
        print('NO')
