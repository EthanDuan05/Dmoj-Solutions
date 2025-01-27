import sys
input = sys.stdin.readline

m, c, i, q = map(int, input().split())

cnt = 0
amount = 0
last = c
current = 0

while amount <= q:
    for _ in range(m):
        amount += last
        cnt += 1
    last += i

print(cnt-1)