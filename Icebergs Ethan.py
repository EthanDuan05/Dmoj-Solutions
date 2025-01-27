import sys
input = sys.stdin.readline

R, C = map(int, input().split())
L, W = map(int, input().split())

wall = '#'
Graph = [[wall for c in range(C+2)] for r in range(R+2)]

for r in range(1, R+1):
    line = list(input().strip())
    Graph[r] = [wall] + line + [wall]

def determine(x, y):
    for r in range(L):
        for c in range(W):
            if Graph[x+r][y+c] != '.':
                return False
    return True

start = [1, 1]
end = [R-L+1, C-W+1]

if not determine(1, 1):
    print(-1)
    sys.exit(0)

if L == R and C == W:
    print(0)
    sys.exit(0)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False for c in range(C + 2)] for r in range(R + 2)]
level = [[-1 for c in range(C + 2)] for r in range(R + 2)]
def bfs(sr, sc, tr, tc):
    queue = []
    queue.append((sr, sc))
    visited[sr][sc] = True

    while len(queue) > 0:
        r, c = queue.pop(0)
        for dr, dc in direction:
            ar, ac = r+dr, c+dc
            if Graph[ar][ac] == wall: continue
            if visited[ar][ac]: continue
            if determine(ar, ac):
                visited[ar][ac] = True
                level[ar][ac] = level[r][c] + 1
                queue.append((ar, ac))
                if ar == tr and ac == tc:
                    return level[ar][ac]

    return -1

ans = bfs(start[0], start[1], end[0], end[1])

if ans == -1:
    print(-1)
else:
    print(ans + 1)