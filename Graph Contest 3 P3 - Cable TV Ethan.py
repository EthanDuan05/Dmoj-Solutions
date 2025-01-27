N, M = map(int, input().split())

Map = []
Parent = [i for i in range(N)]
Rank = [0 for _ in range(M)]
Total = 0

def find(i):
    if Parent[i] != i:
        Parent[i] = find(Parent[i])
    return Parent[i]

def union(x, y):
    if Rank[x] < Rank[y]:
        Parent[x] = y
    elif Rank[x] > Rank[y]:
        Parent[y] = x
    else:
        Parent[y] = x
        Rank[x] += 1

def MST(node_count):
    selected = []
    Result = 0
    i = 0
    e = 0
    Map.sort()
    Dange = 0

    while e < node_count-1:
        cost, x, y = Map[i]
        i += 1
        X = find(x)
        Y = find(y)

        if X != Y:
            e += 1
            Result += cost[1]
            if cost[0] == 1:
                Dange += 1
            union(X, Y)
            selected.append(cost)

    return Result, Dange

for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    Map.append([(d, c), a, b])
    Map.append([(d, c), b, a])

ans_1, ans_2 = MST(N)

print(ans_2, ans_1)