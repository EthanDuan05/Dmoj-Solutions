T = 5
row = 10
col = 10

def bfs(graph, r, c, x, y):
    visited = [[[False for _ in range(4)] for _ in range(col + 2)] for _ in range(row + 2)]
    level = [[-1 for _ in range(col + 2)] for _ in range(row + 2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
    while queue:
        row_, col_ = queue.pop(0)
        cnt = -1
        for d in direction.keys():
            cnt += 1
            d_r, d_c = direction[d]
            current_r = row_ + d_r
            current_c = col_ + d_c
            while True:
                # print(current_r, current_c, cnt)
                if visited[current_r][current_c][cnt]: break
                if graph[current_r][current_c] == '#': break
                if graph[current_r+d_r][current_c+d_c] == '#':
                    visited[current_r][current_c][cnt] = True
                    queue.append((current_r, current_c))
                    level[current_r][current_c] = level[row_][col_] + 1
                    if (current_r == r and current_c == c) and (Graph[current_r+d_r][current_c+d_c] == '#'):
                        return level[r][c]

                current_r += d_r
                current_c += d_c

    return level[r][c]

for _ in range(T):
    Graph = [['#' for _ in range(col + 2)] for _ in range(row + 2)]

    Start = [0, 0]
    Target = [0, 0]

    for r in range(1, row + 1):
        line = list(input())
        Graph[r] = ['#'] + line + ['#']

        if 'A' in line:
            Start[0] = r
            Start[1] = line.index('A') + 1

        if 'B' in line:
            Target[0] = r
            Target[1] = line.index('B') + 1

    print(bfs(Graph, Target[0], Target[1], Start[0], Start[1]))

    Damn = input()