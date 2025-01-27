import sys
input = sys.stdin.readline

n, q, h = map(int, input().split())

height = [0]*n
yeild = [0]*n

psa_h = [0]*(n+1)
psa_y = [0]*(n+1)

for i in range(n):
    he, b = map(int, input().split())
    height[i] += he
    yeild[i] += b

for m in range(n):
    if height[m] > h:
        height[m] = 0
        yeild[m] = 0

for a in range(n):
    psa_y[a+1] = psa_y[a]+yeild[a]

cnt = 0
for p in range(q):
    l, s = map(int, input().split())
    ans = psa_y[s] - psa_y[l - 1]
    if ans > cnt:
        cnt = ans

print(cnt)