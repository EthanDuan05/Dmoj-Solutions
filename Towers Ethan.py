N = int(input())
line = list(map(int, input().split()))

cnt = 0
for i in range(1, N-1):
    if line[i - 1] < line[i] < line[i + 1]:
        cnt += 1
print(cnt)