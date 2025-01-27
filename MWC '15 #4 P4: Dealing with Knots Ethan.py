N = int(input())

Graph = [[] for _ in range(N)]

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)

def bfs(graph, s, t):
    visited = [False] * len(graph)
    level = [-1]*len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    level[s] = 0
    while queue:
        k = queue.pop(0)
        for i in graph[k]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                level[i] = level[s] + 1
                if i == t:
                    return True
    return False

S, T = map(int, input().split())
S -= 1
T -= 1

if bfs(Graph, S, T):
    print('Tangled')
else:
    print('Not Tangled')