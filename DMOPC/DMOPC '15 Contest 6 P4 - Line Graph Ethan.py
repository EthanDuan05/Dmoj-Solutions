Graph = []

N, K = map(int, input().split())
WEIGHT = list(map(int, input().split()))

Total = 0
for i in range(N-1):
    Graph.append([WEIGHT[i], i, i+1])
    Graph.append([WEIGHT[i], i+1, i])
    Total += WEIGHT[i]*2

for i in range(N):
    if i + K <= N-1:
        Graph.append([0, i, i+K])
        Graph.append([0, i+K, i])


Parent = [i for i in range(N)]
Rank = [0 for _ in range(N)]
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
    Graph.sort()

    while e < node_count-1:
        cost, x, y = Graph[i]
        i += 1
        X = find(x)
        Y = find(y)

        if X != Y:
            e += 1
            Result += cost
            union(X, Y)
            selected.append(cost)

    return Result, selected


# print(Graph)

ans1, ans2 = MST(N)

print(ans1)