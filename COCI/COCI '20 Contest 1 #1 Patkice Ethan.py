r, c = map(int, input().split())

Graph = [['*' for _ in range(c+2)] for _ in range(r+2)]

Start = 0, 0
Target = 0, 0

Debug = True
# Debug = False

def bfs(graph, r_, c_, x, y, direction, level):
    visited = [[False for _ in range(c + 2)] for _ in range(r + 2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    while queue:
        row_, col_ = queue.pop(0)
        if graph[row_][col_] == '*': continue
        if graph[row_][col_] == '.': continue

        if (row_, col_) == Start:
            d_r, d_c = direction
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            if graph[current_r][current_c] == '.': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1

        elif (row_, col_) == Target:
            return True, level

        else:
            ways = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
            D = graph[row_][col_]
            if D in ways:
                d_r, d_c = ways[D]
            else:
                d_r, d_c = 0, 0
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            if graph[current_r][current_c] == '.': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
            if current_r == r_ and current_c == c_:
                return True

    return False

for i in range(1, r+1):
    line = list(input())
    Graph[i] = Graph[i][:1] + line + Graph[i][-1:]

    if 'o' in line:
        Start = i, line.index('o')+1

    if 'x' in line:
        Target = i, line.index('x')+1

D = {'east': (0, 1), 'north': (-1, 0), 'south': (1, 0), 'west': (0, -1)}

ANS = [[] for _ in range(4)]
D_d = ['E', 'N', 'S', 'W']

cnt = 0
for i in D:
    Level = [[-1 for _ in range(c + 2)] for _ in range(r + 2)]
    ans = bfs(Graph, Target[0], Target[1], Start[0], Start[1], D[i], Level)
    ANS[cnt].append(ans)
    ANS[cnt].append(Level[Target[0]][Target[1]])
    ANS[cnt].append(D_d[cnt])
    cnt += 1

MAX = 1e9
IND = 0
ANS_D = ''
Flag = False

for i in ANS:
    if i[0]:
        Flag = True
        if i[1] < MAX:
            MAX = i[1]
            ANS_D = [i[2]]

if Flag:
    print(':)')
    print(*ANS_D)
else:
    print(':(')