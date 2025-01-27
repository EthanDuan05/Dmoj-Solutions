N = int(input())
STONE = list(map(int, input().split()))

Costs = [0 for _ in range(N+1)]

Costs[1] = 0
Costs[2] = abs(STONE[0] - STONE[1])

for i in range(3, N+1):
    way1 = abs(STONE[i-1] - STONE[i-2-1])
    way2 = abs(STONE[i-1] - STONE[i-1-1])
    way1 += Costs[i-2]
    way2 += Costs[i-1]
    Costs[i] = min(way1, way2)

print(Costs[N])