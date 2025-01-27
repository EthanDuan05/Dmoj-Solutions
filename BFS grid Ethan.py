def bfs(graph, r, c, x, y):
    visited = [[False for _ in range(c + 2)] for _ in range(r + 2)]
    level = [[-1 for _ in range(c + 2)] for _ in range(r + 2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == '*': continue
        for d in direction.keys():
            if (d == 'north' or d == 'south') and graph[row_][col_] == '-':
                continue
            if (d == 'east' or d == 'west') and graph[row_][col_] == '|':
                continue
            d_r, d_c = direction[d]
            current_r = d_r + row_

            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = (level[row_][col_] + 1)
            if current_r == r and current_c == c:
                return level

    return level

T = int(input())

for _ in range(T):
    row = int(input())
    colum = int(input())
    Graph = [['*' for j in range(colum + 2)] for i in range(row + 2)]

    for s in range(1, row + 1):
        line = list(input())
        Graph[s] = Graph[s][:1] + line + Graph[s][-1:]

    L = (bfs(Graph, row, colum, 1, 1))
    if L[row][colum] != -1:
        print(L[row][colum] + 1)
    else:
        print(-1)
