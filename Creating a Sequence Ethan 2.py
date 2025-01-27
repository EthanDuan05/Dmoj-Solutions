N, K = map(int, input().split())

L = []
cnt = 0
while N > 1:
    N -= 1
    cnt += 1
    L.append(0)

L.append(K)
print(' '.join(map(str, L)))

