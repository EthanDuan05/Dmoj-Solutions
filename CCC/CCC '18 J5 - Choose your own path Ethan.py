N = int(input())

Graph = [[] for i in range(N+1)]

for i in range(1, N+1):
    line = list(map(int, input().split()))
    M = line.pop(0)
    if len(line) > 1:
        for s in range(M):
            Graph[i].append(line[s])
    else:
        Graph[i].append(M)


def bfs(graph, s):
    visited = [False] * len(graph)
    level = [-1]*len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    level[s] = 0
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                level[i] = level[s] + 1
    return level


print(Graph)
print(bfs(Graph, 1))