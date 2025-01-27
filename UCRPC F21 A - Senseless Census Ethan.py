N, M = map(int, input().split())

cnt = 0
for _ in range(N):
    line = input()
    for i in range(M):
        if line[i] == 't':
            cnt += 1

print(cnt)