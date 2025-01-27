def bfs(graph, r, c, x, y):
    visited = [[False for j in range(colum + 2)] for i in range(row + 2)]
    level = [[-1 for j in range(colum + 2)] for i in range(row + 2)]
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == 'X': continue
        for d_r, d_c in direction:
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


def find_starting(character):
    for i in range(row+2):
        if character in Graph[i]:
            return i, Graph[i].index(character)


T = int(input())
for _ in range(T):
    colum, row = map(int, input().split())
    Graph = [['X' for j in range(colum + 2)] for i in range(row + 2)]

    for s in range(1, row+1):
        line = list(input())
        Graph[s] = Graph[s][:1] + line + Graph[s][-1:]

    c_x, c_y = find_starting('C')[0], find_starting('C')[1]
    w_x, w_y = find_starting('W')[0], find_starting('W')[1]

    ans = (bfs(Graph, w_x, w_y, c_x, c_y))

    if ans >= 60 or ans == -1:
        print('#notworth')
    else:
        print(ans)

