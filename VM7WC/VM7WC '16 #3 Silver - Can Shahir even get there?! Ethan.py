def bfs(graph, s, t):
    visited = [False] * len(graph)
    level = [-1] * len(graph)
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
                if i == t:
                    return True
    return False


N, M, A, B = map(int, input().split())
Graph = [[] for i in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    Graph[x-1].append(y-1)
    Graph[y-1].append(x-1)

for i in Graph:
    print(i)

if A == B:
    print('GO SHAHIR!')
elif bfs(Graph, A-1, B-1):
    print('GO SHAHIR!')
else:
    print('NO SHAHIR!')