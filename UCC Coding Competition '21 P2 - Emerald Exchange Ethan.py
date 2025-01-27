N = int(input())
line = list(map(int, input().split()))
line.append(1)

L = []

current = 0
for i in range(N+1):
    if line[i] % 2 == 0:
        current += line[i]
    else:
        L.append(current)
        current = 0

print(max(L))