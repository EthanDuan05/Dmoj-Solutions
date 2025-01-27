K = int(input())

N = int(input())

L = []

for i in range(N-1):
    if K - i + 1 > 0:
        K -= i+1
        L.append(i+1)

L.append(K)

for i in L:
    print(i)