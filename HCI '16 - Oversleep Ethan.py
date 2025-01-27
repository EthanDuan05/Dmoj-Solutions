R, C = map(int, input().split())

Graph = [['X' for _ in range(C + 2)] for _ in range(R + 2)]

def bfs(graph, r, c, x, y):
    visited = [[False for _ in range(C + 2)] for _ in range(R + 2)]
    level = [[-1 for _ in range(C + 2)] for _ in range(R + 2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == 'X': continue
        for d in direction.keys():
            d_r, d_c = direction[d]
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == 'X': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
            if current_r == r and current_c == c:
                return level[r][c]

    return level[r][c]

Start = [0, 0]
End = [0, 0]

for i in range(1, R+1):
    line = list(input())
    Graph[i] = ['X'] + line + ['X']

    if 's' in line:
        Start[0] = i
        Start[1] = Graph[i].index('s')

    if 'e' in line:
        End[0] = i

        End[1] = Graph[i].index('e')

if bfs(Graph, End[0], End[1], Start[0], Start[1]) != -1:
    print(bfs(Graph, End[0], End[1], Start[0], Start[1]) - 1)
else:
    print(-1)


