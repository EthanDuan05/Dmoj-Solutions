N = int(input())

line = list(map(int, input().split()))

line.sort()

ind = 0
if N % 2 == 0:
    ind = N // 2
else:
    ind = N // 2 + 1

L = line[ind:]

ans = []
for i in range(ind-1, -1, -1):
    ans.append(line[i])

    if L:
        h = L.pop(0)
        ans.append(h)
    else:
        continue

print(' '.join(map(str, ans)))
