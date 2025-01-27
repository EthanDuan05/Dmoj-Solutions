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


N = 4
graph = [[] for i in range(N)]
graph[0].append(1)
graph[0].append(2)
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(3)

bfs(graph, 0)