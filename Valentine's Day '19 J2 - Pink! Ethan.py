T = int(input())

cnt = 0
for _ in range(T):
    r, g, b = map(int, input().split())
    if 240 <= r <= 255 and 0 <= g <= 200 and 95 <= b <= 220:
        cnt += 1

print(cnt)