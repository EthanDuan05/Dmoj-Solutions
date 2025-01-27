N = int(input())
line = list(map(int, input().split()))

a = max(line)

GCM = 0
for i in range(1, a+1):
    flag = True
    for s in line:
        if s % i == 0:
            continue
        else:
            flag = False

    if i > GCM and flag:
        GCM = i

ans = []
for m in line:
    ans.append(m // GCM)

print(' '.join(map(str, ans)))
