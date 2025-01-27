n = int(input())

ans = []
for _ in range(n):
    initial, min_l, max_l, final = map(int, input().split())
    L = []
    for i in range(min_l, max_l+1):
        L.append(i)
    if initial - final in L:
        ans.append('Yes')
    else:
        ans.append('No')

for i in ans:
    print(i)