T = 5
row = 10
col = 10

def bfs(graph, fires, visited, level, trees):
    queue = []
    MAX_level = 0
    Tr = 0

    for r, c in fires:
        visited[r][c] = True
        level[r][c] = 0
        queue.append((r, c))

    direction = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
    while len(queue) > 0:
        row_, col_ = queue.pop(0)
        for d_r, d_c in direction.values():
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            if graph[current_r][current_c] == '.': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
            MAX_level = max(level[current_r][current_c], MAX_level)
            Tr += 1
            if Tr == trees:
                return MAX_level

    return -1

for _ in range(T):
    Graph = [['*' for c in range(col + 2)] for r in range(row + 2)]
    Visited = [[False for c in range(col + 2)] for r in range(row + 2)]
    Level = [[-1 for c in range(col + 2)] for r in range(row + 2)]
    F_cor = []
    Trees = 0

    for s in range(1, row+1):
        line = list(input())
        for i in range(col):
            if line[i] == 'F':
                r = s
                c = i + 1
                F_cor.append((r, c))
            elif line[i] == 'T':
                Trees += 1

        Graph[s] = ['*'] + line + ['*']

    L = bfs(Graph, F_cor, Visited, Level, Trees)

    print(L)

    Damn = input()