N = int(input())
L = {}

for _ in range(N):
    Name = input()
    if Name not in L:
        L[Name] = 1
    else:
        L[Name] += 1

for _ in range(N-1):
    Name = input()
    L[Name] += 1

for i in L.keys():
    if L[i] % 2 != 0:
        print(i)
        break