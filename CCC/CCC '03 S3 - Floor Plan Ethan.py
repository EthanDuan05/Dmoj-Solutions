Flooring = int(input())
row = int(input())
colum = int(input())
Graph = [['I' for j in range(colum+2)] for i in range(row+2)]

for s in range(1, row+1):
    line = list(input())
    Graph[s] = Graph[s][:1] + line + Graph[s][-1:]

visited = [[False for j in range(colum+2)] for i in range(row+2)]
rooms = []


def bfs(graph, x, y):
    level = [[-1 for j in range(colum+2)] for i in range(row+2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    area = 0
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == 'I': continue
        for d_r, d_c in direction:
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == 'I': continue
            area += 1
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
    return area


for s in range(row+2):
    for k in range(colum+2):
        start_x = s
        start_y = k
        if Graph[start_x][start_y] == '.':
            ans = (bfs(Graph, start_x, start_y))
            if ans == 0:
                continue
            else:
                rooms.append(ans)

rooms.sort()
rooms.reverse()

cnt = 0
for i in rooms:
    if i <= Flooring:
        cnt += 1
        Flooring -= i
    else:
        break

left = Flooring

if cnt == 1:
    print(str(cnt) + ' ' + 'room,' + ' ' + str(left) + ' ' + 'square metre(s) left over')
else:
    print(str(cnt) + ' ' + 'rooms,' + ' ' + str(left) + ' ' + 'square metre(s) left over')
