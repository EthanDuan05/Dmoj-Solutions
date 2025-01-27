N, S = map(int, input().split())

PSA = [[0 for _ in range(N+1)] for _ in range(N+1)]
Grid = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(S):
    r, c = map(int, input().split())
    Grid[r][c] = 1

for j in range(1, N+1):
    for k in range(1, N+1):
        PSA[j][k] += PSA[j-1][k] + PSA[j][k-1] - PSA[j-1][k-1] + Grid[j][k]

cnt = 0
pairs = []
for i in range(1, N+1):
    for s in range(1, N+1):
        if i * s == S:
            cnt += 1
            pairs.append((i, s))

MAX_N = -1e9
for h, w in pairs:
    for a in range(1, N+1 - h + 1):
        for b in range(1, N+1 - w + 1):
            r, c = a + h - 1, b + w -1
            sub = PSA[r][c] + PSA[a-1][b-1] - PSA[a-1][c] - PSA[r][b-1]
            MAX_N = max(sub, MAX_N)

print(S - MAX_N)

