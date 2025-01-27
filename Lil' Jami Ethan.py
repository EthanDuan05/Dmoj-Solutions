import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cup = [0]*n
psa = [0]*(n+1)

for i in range(k):
    stone = int(input())
    cup[stone] += 1

for s in range(n):
    psa[s+1] = psa[s] + cup[s]

M = []
q = int(input())
for m in range(q):
    a, b = map(int, input().split())
    a += 1
    b += 1
    ans = psa[b] - psa[a - 1]
    M.append(ans)

for i in M:
    print(i)