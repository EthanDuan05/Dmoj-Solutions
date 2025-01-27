N = int(input())
L = [0, 0, 1, 0, 0]

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    L[a], L[b] = L[b], L[a]

print(L.index(1)+1)
