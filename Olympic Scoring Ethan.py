N, B, S, G = map(int, input().split())

curr = B*1 + S*3 + G*5
cnt = 0

diff = N - curr

n = diff // 5

cnt += n
curr += n*5

while curr <= N:
    curr += 5
    cnt += 1

if cnt < 0:
    print(0)
else:
    print(cnt)