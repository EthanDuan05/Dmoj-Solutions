from queue import PriorityQueue


def toposort(graph, n):
    in_degrees = [0 for _ in range(n)]
    in_degrees_old = [0 for _ in range(n)]
    vertex_num = n
    for u in range(n):
        for v in graph[u]:
            in_degrees[int(v)] += 1
            in_degrees_old[int(v)] += 1

    Q = PriorityQueue()

    for s in range(n):
        if in_degrees[s] == 0:
            Q.put(s)

    Seq = []
    while not Q.empty():
        k = Q.get()
        Seq.append(k)
        for v in graph[k]:
            if in_degrees[v] == 0:
                Q.put(v)
            else:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    Q.put(v)
    if len(Seq) == vertex_num:
        return Seq
    else:
        return False


Graph = [[] for _ in range(7)]
Graph[0].append(6)
Graph[0].append(3)
Graph[1].append(0)
Graph[2].append(3)
Graph[2].append(4)

Flag = True
while Flag:
    instru_1 = int(input())
    instru_2 = int(input())

    if instru_1 == 0 and instru_2 == 0:
        Flag = False
    else:
        Graph[instru_1-1].append(instru_2-1)

if not toposort(Graph, 7):
    print('Cannot complete these tasks. Going to bed.')
else:
    ans = []
    for i in (toposort(Graph, 7)):
        ans.append(i + 1)

    print(' '.join(map(str, ans)))


