import sys
input = sys.stdin.readline

n, q = map(int, input().split())
line = list(map(int, input().split()))
psa = [0]*(n+1)

for s in range(n):
    psa[s+1] = psa[s] + line[s]

M = []
for i in range(q):
    l, r = map(int, input().split())
    ans = psa[r] - psa[l-1]
    ans /= r-(l-1)
    M.append(ans)

for i in M:
    print(int(i))