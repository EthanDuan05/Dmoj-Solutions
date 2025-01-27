R = int(input())
C = int(input())

Graph = [['*' for _ in range(C+2)] for _ in range(R+2)]

for i in range(R):
    line = list(input().split())
    Graph[i+1] = ['*'] + line + ['*']

'''
for i in Graph:
    print(i)
'''

visited = [[False for _ in range(C + 2)] for _ in range(R + 2)]
level = [[-1 for _ in range(C + 2)] for _ in range(R + 2)]
level[R][C] = 0
visited[R][C] = True
Direct_Jump = R * C
queue = []

def bfs(graph, r, c, x, y):
    global Direct_Jump
    queue.append((x, y))
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        row_, col_ = queue.pop(0)
        for d in direction:
            dr, dc = d
            current_r = row_ + dr
            current_c = col_ + dc
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '*': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1

            if Direct_Jump == int(graph[current_r][current_c]):
                if current_r * current_c == Direct_Jump:
                    continue

                if current_r == 1 and current_c == 1:
                    return True

    return False

if bfs(Graph, 1, 1, R, C):
    print('yes')
else:
    print('no')

for i in level:
    print(i)

