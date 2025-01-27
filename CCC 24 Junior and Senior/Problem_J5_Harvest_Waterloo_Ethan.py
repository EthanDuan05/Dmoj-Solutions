row = int(input())
colum = int(input())
Graph = [['*' for j in range(colum + 2)] for i in range(row + 2)]

for s in range(1, row + 1):
    line = list(input())
    Graph[s] = Graph[s][:1] + line + Graph[s][-1:]

'''
for i in Graph:
    print(i)
'''

visited = [[False for j in range(colum+2)] for i in range(row+2)]
def bfs(graph, x, y):
    level = [[-1 for j in range(colum+2)] for i in range(row+2)]
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    goal = 0
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == '*': continue
        for d_r, d_c in direction:
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            if graph[current_r][current_c] == 'S':
                goal += 1
            elif graph[current_r][current_c] == 'M':
                goal += 5
            elif graph[current_r][current_c] == 'L':
                goal += 10

            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
    return goal

x = int(input())
y = int(input())
ans = bfs(Graph, x+2-1, y+2-1)
print(ans)
