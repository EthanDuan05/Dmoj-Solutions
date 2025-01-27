import sys
input = sys.stdin.readline
from collections import deque
# use deque (faster)

def path_finder(N, M, graph):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    blocked_set = set(graph)

    # Check if start or end positions are blocked
    if (1, 1) in blocked_set or (N, M) in blocked_set:
        return "NO"


    for r, c in graph:
        visited[r][c] = True

    queue = deque([(1, 1)])
    visited[1][1] = True

    while queue:
        x, y = queue.popleft()

        if x == N and y == M:
            return "YES"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= M and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return "NO"


N, M, K = map(int, input().split())
Graph = [tuple(map(int, input().split())) for _ in range(K)]
print(path_finder(N, M, Graph))
