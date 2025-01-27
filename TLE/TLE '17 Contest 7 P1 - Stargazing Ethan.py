N = int(input())

Graph = []

initial_x = 0
initial_y = 0

Graph.append((initial_x, initial_y))

cnt = 1
for _ in range(N-1):
    p, x, y = map(int, input().split())
    current_x = Graph[p-1][0] + x
    current_y = Graph[p-1][1] + y

    if (current_x, current_y) not in Graph:
        Graph.append((current_x, current_y))
        cnt += 1
    else:
        Graph.append((current_x, current_y))
        continue

print(cnt)