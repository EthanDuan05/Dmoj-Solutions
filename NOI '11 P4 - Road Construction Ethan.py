N = int(input())

Cities = [[] for _ in range(N)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    Cities[a-1].append((b-1, c))
    Cities[b-1].append((a-1, c))

Parents = []
C_Represents = [1 for _ in range(N)]
Debug = False

def bfs(graph, s):
    visited = [False] * len(graph)
    level = [-1]*len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
    level[s] = 0
    while queue:
        s = queue.pop(0)
        for i, c in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                level[i] = level[s] + 1
                if len(Parents) < level[i]:
                    Parents.append([])
                Parents[level[i]-1].append((s, i, c))

    return level

bfs(Cities, 0)

if Debug:
    print(Parents)

Parents.reverse()

Total_Cost = 0
for i in Parents:
    for p, s, c in i:
        Total_Cost += c * abs(N - C_Represents[s]*2)
        C_Represents[p] += C_Represents[s]

if Debug:
    print(Parents)
    print(C_Represents)

print(Total_Cost)

