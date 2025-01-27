N, T = map(int, input().split())

Graph = [[-1 for _ in range(N)] for _ in range(N)]

x, y = 0, 0
MAX_N = N*N
for i in range(T):
    Graph[x][y] = MAX_N
    x += 1
    y += 1
    MAX_N -= 1

for r in range(N):
    for c in range(N):
        if Graph[r][c] == -1:
            Graph[r][c] = MAX_N
            MAX_N -= 1

for i in Graph:
    print(' '.join(map(str, i)))