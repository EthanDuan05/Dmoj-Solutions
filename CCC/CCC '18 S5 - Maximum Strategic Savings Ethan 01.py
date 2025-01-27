import sys
input = sys.stdin.readline

N, M, P, Q = map(int, input().split())

Graph = []
Parent = [i for i in range(N * M)]
Rank = [0 for _ in range(N * M)]
Total = 0
Debug = False

for _ in range(P):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    for s in range(N):
        Graph.append([c, a + s * M, b + s * M])
        Graph.append([c, b + s * M, a + s * M])
        Total += c

for _ in range(Q):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    for k in range(M):
        Graph.append([z, k + x * M, k + y * M])
        Graph.append([z, k + y * M, k + x * M])
        Total += z


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


def MST():
    Result = 0
    i = 0
    e = 0
    Graph.sort()

    while e < N*M-1:
        cost, x, y = Graph[i]
        i += 1
        X = find(x)
        Y = find(y)

        if X != Y:
            e += 1
            Result += cost
            union(X, Y)

    return Result


if Debug:
    print(Graph)
    print(Total, 'Total')
    print(MST(), 'MST')

print(Total - MST())
