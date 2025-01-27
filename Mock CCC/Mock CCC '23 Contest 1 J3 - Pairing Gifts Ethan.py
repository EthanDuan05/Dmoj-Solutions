import sys
input = sys.stdin.readline


N, K, M = map(int, input().split())
line_a = list(map(int, input().split()))
line_b = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for s in range(N):
        if line_a[i] + line_b[s] == M and abs((i+1)-(s+1)) >= K:
            cnt += 1

print(cnt)