ans = []
for _ in range(5):
    graph = []
    for _ in range(3):
        line = list(input())
        graph.append(line)

    winner = ' '

    for i in range(3):
        if graph[0][i] == graph[1][i] == graph[2][i]:
            winner = graph[0][i]
            break
        elif graph[i][0] == graph[i][1] == graph[i][2]:
            winner = graph[i][0]
            break

    if graph[0][0] == graph[1][1] == graph[2][2]:
        winner = graph[0][0]

    elif graph[0][2] == graph[1][1] == graph[2][0]:
        winner = graph[0][2]

    ans.append(winner)

for i in ans:
    if i != ('.' and ' '):
        print(i)
    else:
        print('.')