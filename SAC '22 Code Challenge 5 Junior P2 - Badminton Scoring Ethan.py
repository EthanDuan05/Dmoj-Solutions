n = int(input())
cnt = 0
for i in range(n):
    m, o = map(int, input().split())
    if m > o:
        cnt += 1

print(cnt)