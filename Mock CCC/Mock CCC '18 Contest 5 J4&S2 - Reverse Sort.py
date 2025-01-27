N = int(input())
line = list(map(int, input().split()))

cnt = 0
for i in range(N+1):
    for j in range(N-1):
        if line[j] < line[j+1]:
            line[j], line[j+1] = line[j+1], line[j]
            cnt += 1

print(cnt)