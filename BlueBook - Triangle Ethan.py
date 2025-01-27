N = int(input())

L = [[1],
     [1, 1],
     [1, 2, 1]]

if N <= 3:
    for i in range(N):
        print(' '.join(map(str, L[i])))
else:
    for i in range(3, N+1):
        line = [1 for _ in range(i+1)]
        for j in range(1, i):
            line[j] = L[i-1][j-1] + L[i-1][j]

        L.append(line)

    for i in range(N):
        print(' '.join(map(str, L[i])))