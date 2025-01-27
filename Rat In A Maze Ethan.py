N = int(input())

def bfs(graph, r, c, x, y):
    visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]
    level = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == 1: continue
        for d in direction.keys():
            d_r, d_c = direction[d]
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == 1: continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = (level[row_][col_] + 1)
            if current_r == r and current_c == c:
                return True

    return False

Graph = [[1 for _ in range(N+2)]for _ in range(N+2)]

for i in range(1, N+1):
    line = list(map(int, input().split()))
    Graph[i] = Graph[i][:1] + line + Graph[i][-1:]

if bfs(Graph, N, N, 1, 1):
    print('yes')
else:
    print('no')