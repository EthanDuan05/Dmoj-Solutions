n = int(input())
line = input()

L = []
for i in range(1, n+1):
    L.append(i)

print(' '.join(map(str, L)))