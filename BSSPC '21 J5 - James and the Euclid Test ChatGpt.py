import sys
from bisect import bisect_right

input = sys.stdin.readline

L = []
prime = [True for _ in range(int(300000 + 2))]

def sieve(N):
    p = 2
    while p * p <= N:
        if prime[p]:
            for i in range(p * p, N + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, N + 1):
        if prime[p]:
            L.append(p)

sieve(300000 + 1)
prefix_sums = [0] * (len(L) + 1)

# Precompute prefix sums
for i in range(1, len(L) + 1):
    prefix_sums[i] = prefix_sums[i - 1] + L[i - 1]

T = int(input())

for _ in range(T):
    x, k = map(int, input().split())

    if x in L:
        x_ind = L.index(x)
        total = prefix_sums[x_ind + k] - prefix_sums[x_ind]
        print(L[x_ind + k - 1], total)

    else:
        x_ind = bisect_right(L, x)
        total = prefix_sums[x_ind + k] - prefix_sums[x_ind]
        print(L[x_ind + k - 1], total)
