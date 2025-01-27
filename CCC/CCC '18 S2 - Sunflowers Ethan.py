N = int(input())

Graph = [[]for _ in range(N)]

for i in range(N):
    line = list(input().split())
    Graph[i] = line

print(Graph)