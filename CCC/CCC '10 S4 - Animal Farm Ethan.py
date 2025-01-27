import sys
input = sys.stdin.readline

N = int(input())

Map = dict()
Pen = dict()

Graph1 = []
Graph2 = []
Parent = [i for i in range(N)]
Rank = [0 for _ in range(N)]
Debug = False


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


def MST(node_count, graph):
    selected = []
    Result = 0
    graph.sort()

    for cost, x, y in graph:
        X = find(x)
        Y = find(y)

        if X != Y:
            Result += cost
            union(X, Y)
            selected.append(cost)

    return Result, selected

for i in range(N):
    D = list(map(int, input().split()))
    Edge = D.pop(0)
    Corner = D[:Edge]
    Weight = D[-Edge:]

    for s in range(Edge):
        if s+1 < Edge:
            corner1 = Corner[s]
            corner2 = Corner[s+1]
        else:
            corner1 = Corner[s]
            corner2 = Corner[0]

        if corner1 > corner2:
            corner1, corner2 = corner2, corner1

        if (corner1, corner2) not in Map:
            Map[(corner1, corner2)] = Weight[s]
            Pen[(corner1, corner2)] = [i]
        else:
            Pen[(corner1, corner2)].append(i)

outside = N
for key, pens in Pen.items():
    if len(pens) > 1:
        Graph1.append([Map[key], pens[0], pens[1]])
        Graph2.append([Map[key], pens[0], pens[1]])
    else:
        Graph2.append([Map[key], pens[0], outside])

if Debug:
    print(Graph1)
    print(Parent)
    print(Rank)

a = MST(N, Graph1)[0]

if Debug:
    print(Graph1)
    print(Parent)
    print(Rank)

Parent = [i for i in range(N+1)]
Rank = [0 for _ in range(N+1)]

if Debug:
    print(Graph2)
    print(Parent)
    print(Rank)

b = MST(N+1, Graph2)[0]

if Debug:
    print(Graph2)
    print(Parent)
    print(Rank)

print(min(a, b))