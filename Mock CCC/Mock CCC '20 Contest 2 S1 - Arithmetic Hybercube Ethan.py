n = int(input())
line = map(int, input().split())
L = []
for i in line:
    L.append(i)
L.sort()
ans = ''
for i in range(n):
    if i < n-1:
        ans += str(L[i]) + ' '
    else:
        ans += str(L[i])
print(ans)