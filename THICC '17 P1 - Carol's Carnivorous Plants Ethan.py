N , M = map(int, input().split())
L = list(map(int, input().split()))
L.sort(reverse=True)

K = [0 for _ in range(M)]

Total = 0
cnt = 0

ind = 0
while L:
    C = L.pop(0)
    if cnt < M:
        Total += C**K[ind]
        K[ind] += 1

    else:
        Total += C**K[ind]
        K[ind] += 1

    if ind + 1 >= M:
        ind = 0
    else:
        ind += 1

    cnt += 1

print(Total % 1000000007)
