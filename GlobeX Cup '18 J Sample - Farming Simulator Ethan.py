N, M = list(map(int, input().split()))
line = list(map(int, input().split()))

line.sort()
cnt = 0
while cnt < M:
    line.remove(line[0])
    cnt += 1

ans = sum(line)
print(ans)