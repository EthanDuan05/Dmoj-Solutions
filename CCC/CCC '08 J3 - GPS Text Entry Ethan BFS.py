Map = [['*', '*', '*', '*', '*', '*', '*', '*'],
       ['*', 'A', 'B', 'C', 'D', 'E', 'F', '*'],
       ['*', 'G', 'H', 'I', 'J', 'K', 'L', '*'],
       ['*', 'M', 'N', 'O', 'P', 'Q', 'R', '*'],
       ['*', 'S', 'T', 'U', 'V', 'W', 'X', '*'],
       ['*', 'Y', 'Z', ' ', '-', '.', 'enter', '*'],
       ['*', '*', '*', '*', '*', '*', '*', '*']]

def bfs(graph, r, c, x, y):
    visited = [[False for j in range(8)] for i in range(7)]
    level = [[-1 for j in range(8)] for i in range(7)]
    level[x][y] = 0
    visited[x][y] = True
    queue = []
    queue.append((x, y))
    direction = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == '*': continue
        for d in direction.keys():
            d_r, d_c = direction[d]
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
            if current_r == r and current_c == c:
                return level[r][c]

    return level[x][y]

def index(I):
    for row in range(7):
        if I in Map[row]:
            y = Map[row].index(I)
            x = row
            return x, y


string = list(input())

x_cor = 1
y_cor = 1
total = 0
while string:
    i = string.pop(0)
    x1, y1 = index(i)
    total += bfs(Map, x1, y1, x_cor, y_cor)

    x_cor = x1
    y_cor = y1

total += bfs(Map, 5, 6, x_cor, y_cor)
print(total)
