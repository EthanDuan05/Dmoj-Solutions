n, t = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

for i in range(1, (1<<n)+1):
    amount = 0
    for k in range(n):
        mask = 1<<k
        if mask & i:
            amount += a[k]
    if amount == t:
        cnt += 1

print(cnt)