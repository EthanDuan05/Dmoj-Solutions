N, T = map(int, input().split())

cnt = 0
for _ in range(N):
    o, d = map(int, input().split())
    price = o - o * (d / 100)
    if price <= T:
        cnt += 1
print(cnt)
