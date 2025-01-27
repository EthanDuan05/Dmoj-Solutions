N, G = map(int, input().split())
cnt = 0
for i in range(N):
    num = int(input())
    if num % G == 0:
        cnt += 1
print(cnt)