def toposort(graph, n):
    in_degrees = [0 for _ in range(n)]
    vertex_num = n
    for u in range(n):
        for v in graph[u]:
            in_degrees[int(v)] += 1
    Q = [s for s in range(n) if in_degrees[s] == 0]
    Seq = []
    while Q:
        k = Q.pop()
        Seq.append(k)
        for v in graph[k]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                Q.append(v)
    if len(Seq) == vertex_num:
        return True
    else:
        return False


N = int(input())
M = int(input())
Graph = [[] for _ in range(N)]

for _ in range(M):
    stu_1, stu_2 = map(int, input().split())
    Graph[stu_1-1].append(stu_2-1)

if toposort(Graph, N):
    print('Y')
else:
    print('N')