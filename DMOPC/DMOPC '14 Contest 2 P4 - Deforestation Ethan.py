import sys
input = sys.stdin.readline

n = int(input())
tree_m = [0]*n
psa_m = [0]*(n+1)

for i in range(n):
    mass = int(input())
    tree_m[i] += mass

for i in range(n):
    psa_m[i+1] = psa_m[i] + tree_m[i]

q = int(input())

M = []
for i in range(q):
    a, b = map(int, input().split())
    ans = psa_m[b+1] - psa_m[a]
    M.append(ans)

for i in M:
    print(i)