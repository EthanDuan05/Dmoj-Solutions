N, K = map(int, input().split())

L = []
for _ in range(N):
    C = int(input())
    L.append(C)

L.sort(reverse=True)

Total = 0
for i in range(K):
    if L[i] >= 0:
        Total += L[i]

print(Total)