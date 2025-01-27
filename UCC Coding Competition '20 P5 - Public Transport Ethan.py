L, S, E, N = map(int, input().split())

Map = [[] for _ in range(L)]

for _ in range(N):
    a, b = map(int, input().split())
    Map[a-1].append(b-1)

def bfs(graph, s):
    step = 0
    visited = [False] * len(graph)
    level = [-1]*len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    level[s] = 0
    while queue:
        s = queue.pop(0)
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                level[i] = level[s] + 1
                step += 1
    print(level[E-1])

bfs(Map, S-1)