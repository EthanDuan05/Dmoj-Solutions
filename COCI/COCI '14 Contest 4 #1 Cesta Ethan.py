N = input()
L = []

for i in N:
    L.append(int(i))

L.sort()
L.reverse()

a = sum(L)
b = L[-1]

if a % 3 == 0 and b == 0:
    print(''.join(map(str, L)))
else:
    print(-1)