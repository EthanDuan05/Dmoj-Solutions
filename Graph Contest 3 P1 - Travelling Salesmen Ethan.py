N, M = map(int, input().split())

def bfs(graph, Source):
    visited = [False] * len(graph)
    level = [-1]*len(graph)
    queue = []
    for i in Source:
        queue.append(i)
        visited[i] = True
        level[i] = 0

    while len(queue) > 0:
        s = queue.pop(0)
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                level[i] = level[s] + 1
    return max(level)

Graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)
    Graph[b].append(a)

source = []
K = int(input())
for _ in range(K):
    sou = int(input())
    sou -= 1
    source.append(sou)

print(bfs(Graph, source))