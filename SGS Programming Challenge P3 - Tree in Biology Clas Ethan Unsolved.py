N = int(input())
line1 = input().split()
U = []
V = []
for i in range(N-1):
    u, v = input().split()
    U.append(int(u))
    V.append(int(v))

M = int(input())
L = []
for k in range(M):
    line2 = input().split()
    if len(line2) > 1:
        for c in line2:
            L.append(c)

print(line1)
print(U)
print(V)
print(L)