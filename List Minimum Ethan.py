N = int(input())

L = []
for _ in range(N):
    num = int(input())
    L.append(num)

L.sort()
for i in L:
    print(i)