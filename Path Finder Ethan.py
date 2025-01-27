import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
Graph = [['.' for _ in range(M+2)] for _ in range(N+2)]

for _ in range(K):
    r, c = map(int, input().split())
    Graph[r][c] = '#'

Graph[0] = ['#' for _ in range(M+2)]
Graph[N+2-1] = ['#' for _ in range(M+2)]

for i in range(1, N+2):
    Graph[i] = ['#'] + Graph[i][1:M+1] + ['#']

visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]

def bfs(graph, r, c, x, y):
    queue = []
    queue.append((x, y))
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    while queue:
        row_, col_ = queue.pop(0)
        for d_r, d_c in direction:
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '#': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            if current_r == r and current_c == c:
                return True

    return False

'''
for i in visited:
    print(i)
for i in level:
    print(i)
'''

if bfs(Graph, N, M, 1, 1):
    print('YES')
else:
    print('NO')