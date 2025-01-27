N = int(input())
COST = []
DAY = []

for _ in range(N):
    cost, day = map(int, input().split())
    COST.append(cost)
    DAY.append(day)

options =[]
option_d = max(DAY)

for i in range(len(DAY)):
    if DAY[i] == option_d:
        options.append(COST[i])

print(min(options), option_d)