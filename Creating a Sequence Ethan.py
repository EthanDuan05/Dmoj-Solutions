N, K = map(int, input().split())

L = []
cnt = 0
while N > 1:
    N -= 1
    cnt += 1
    L.append(1)

L.append(K-cnt)
print(' '.join(map(str, L)))