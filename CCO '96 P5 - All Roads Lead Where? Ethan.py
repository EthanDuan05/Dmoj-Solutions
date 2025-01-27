N, M = map(int, input().split())

Graph = [[] for _ in range(26)]
for _ in range(N):
    name_1, name_2 = input().split()
    n1 = ord(name_1[0]) - 65
    n2 = ord(name_2[0]) - 65
    Graph[n1].append(n2)
    Graph[n2].append(n1)


def bfs(graph, s, t):
    L = [-2] * len(graph)
    L[s] = -1
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                L[i] = v
                if i == t:
                    return L


for _ in range(M):
    find_1, find_2 = input().split()
    f1 = ord(find_1[0]) - 65
    f2 = ord(find_2[0]) - 65
    ans = (bfs(Graph, f1, f2))
    current_city = f2
    ANS = ''
    ANS += chr(f2 + 65)
    while True:
        if ans[current_city] >= -1:
            ANS += chr(ans[current_city] + 65)
            current_city = ans[current_city]
            if ans[current_city] == -1:
                break
    print(ANS[::-1])