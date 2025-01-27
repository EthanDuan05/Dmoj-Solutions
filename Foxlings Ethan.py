import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
Relation = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Relation[a].append(b)
    Relation[b].append(a)

def bfs(s):
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        # print(level)
        s = queue.pop(0)
        for i in Relation[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(N):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)