n = int(input())
cnt = 0
L = []
for i in range(n):
    x, y = input().split(' ')
    x = int(x)
    y = str(y)
    cnt = cnt+1
    if cnt <= n:
        L.append(x*y)
print(*L, sep="\n")