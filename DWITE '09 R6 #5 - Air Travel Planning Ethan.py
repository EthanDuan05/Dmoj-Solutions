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

for _ in range(5):
    N = int(input())

    cities = {}
    current_city = 0
    city_cnt = 0
    Command = []
    Graph = []
    Total = 0

    for _ in range(N):
        name1, name2, cost = input().split()
        cost = int(cost)
        if name1 not in cities:
            cities[name1] = current_city
            current_city += 1
            city_cnt += 1

        if name2 not in cities:
            cities[name2] = current_city
            current_city += 1
            city_cnt += 1

        Graph.append([cost, cities[name1], cities[name2]])
        Total += cost

    Parent = [i for i in range(city_cnt)]
    Rank = [0 for _ in range(city_cnt)]

    print(MST(city_cnt)[0])



