import sys
input = sys.stdin.readline

N, K = map(int, input().split())

STONE = list(map(int, input().split()))

Costs = [0 for _ in range(N+1)]

if K > N:
    K = N

for i in range(K):
    Costs[i+1] = abs(STONE[0] - STONE[i])

for i in range(K+1, N+1):
    ways = []
    for j in range(K):
        j += 1
        current_way = abs(STONE[i-1] - STONE[i-j-1])
        current_way += Costs[i-j]
        ways.append(current_way)

    Costs[i] = min(ways)

print(Costs[N])