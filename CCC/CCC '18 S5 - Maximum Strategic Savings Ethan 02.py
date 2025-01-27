import sys
input = sys.stdin.readline

N, M, P, Q = map(int, input().split())

Graph = []
Parent = [i for i in range(M)]
Rank = [0 for _ in range(M)]
Total = 0
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


for _ in range(P):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Graph.append([c, a, b])
    Graph.append([c, b, a])
    Total += c * N

if Debug: print(Graph)
if Debug: print(Total)

ans_1, Min_Flights = MST(M)
ans_1 = ans_1

Graph = []
Parent = [i for i in range(N)]
Rank = [0 for _ in range(N)]

for _ in range(Q):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    Graph.append([z, x, y])
    Graph.append([z, y, x])
    Total += z * M

ans_2, Min_Portals = MST(N)
ans_2 = ans_2

if Debug: print(ans_1, ans_2)

if N == 1:
    print(Total - ans_1)
    sys.exit(0)

if Min_Portals[-1] <= Min_Flights[0]:
    New_Cost = ans_1 + ans_2*M
    print(Total - New_Cost)
    sys.exit(0)

if Min_Flights[-1] <= Min_Portals[0]:
    New_Cost = ans_2 + ans_1*N
    print(Total - New_Cost)
    sys.exit(0)

i, j = 0, 0
New_Cost = ans_1 + ans_2

while i < len(Min_Flights) and j < len(Min_Portals):
    if Min_Flights[i] < Min_Portals[j]:
        New_Cost += Min_Flights[i]*(N-j-1)
        i += 1
    else:
        New_Cost += Min_Portals[j]*(M-i-1)
        j += 1

    if Debug: print(New_Cost)

if Debug: print(Min_Flights)
if Debug: print(Min_Portals)


print(Total - New_Cost)