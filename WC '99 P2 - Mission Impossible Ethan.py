while True:
    C, R = map(int, input().split())
    if R + C == -2:
        break

    wall = '0'

    Graph = [[wall for j in range(C+2)] for k in range(R+2)]

    for r in range(1, R+1):
        line = list(input().strip())
        Graph[r] = [wall] + line + [wall]

    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[False for c in range(C + 2)] for r in range(R + 2)]
    def bfs_grid(sr, sc):
        queue = []
        queue.append((sr, sc))
        visited[sr][sc] = True

        while len(queue) > 0:
            r, c = queue.pop(0)
            for dr, dc in direction:
                ar, ac = r+dr, c+dc
                if Graph[ar][ac] == wall: continue
                if visited[ar][ac]: continue
                visited[ar][ac] = True
                queue.append((ar, ac))

    cnt = 0
    for r in range(1, R+1):
        for c in range(1, C+1):
            if Graph[r][c] != wall and visited[r][c] == False:
                bfs_grid(r, c)
                cnt += 1

    print(cnt)
