N = int(input())
Graph = []

for _ in range(N):
    line = list(input())
    for i in range(len(line)):
        if line[i] != '1' and line[i] != '0':
            line[i] = '0'
    Graph.append(line)

for i in Graph:
    print(''.join(i))