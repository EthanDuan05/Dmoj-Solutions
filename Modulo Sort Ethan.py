N = int(input())
K = int(input())
Array = (list(map(int, input().split())))

L = []
for i in range(N):
    elem = Array[i]
    L.append((elem % K, elem))

L.sort()
for i in L:
    print(i[1], end = ' ')