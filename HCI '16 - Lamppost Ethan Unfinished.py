N, C = map(int, input().split())
MAP = [[]for j in range(N+1)]
All = [[]for s in range(N+1)]

for _ in range(C):
    c1, c2 = map(int, input().split())
    MAP[c1].append(c2)
    MAP[c2].append(c1)

for i in range(N+1):
    All[i].append(len(MAP[i]))

max_n = max(All)

for k in range(N, -1, -1):
    if All[k] == max_n:
        print(k)
        break