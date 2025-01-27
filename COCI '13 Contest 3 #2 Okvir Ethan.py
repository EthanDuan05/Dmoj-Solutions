M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

Graph = [[] for _ in range(U + M + D)]

first = '#'
for i in range(U + M + D):
    ans = []
    for j in range(L + N + R):
        if i == 0:
            if first == '#':
                ans.append(first)
                first = '.'
            else:
                ans.append(first)
                first = '#'
        else:
            if Graph[i-1][j] == '#':
                ans.append('.')
            else:
                ans.append('#')

    Graph[i] = ans

for s in range(M):
    line = input()
    for k in range(N):
        Graph[U + s][L + k] = line[k]

for i in Graph:
    print(''.join(i))