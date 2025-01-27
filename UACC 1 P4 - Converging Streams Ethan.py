N, M = map(int, input().split())
Graph = [[] for _ in range(N)]

in_degrees = [0 for _ in range(N)]
for _ in range(M):
    u, v, flow = map(int, input().split())
    u -= 1
    v -= 1
    Graph[u].append([v, flow])
    in_degrees[v] += 1

Pollution = list(map(int, input().split()))

def toposort(graph):
    Q = []
    Seq = []
    sub = [(0, 0) for _ in range(N)]
    Mul = [0]*N

    for m in range(N):
        if in_degrees[m] == 0:
            Q.append(m)
            vol = 1
            pol = 0 + Pollution[m]
            sub[m] = (vol, pol)
            Mul[m] = vol*pol

    while Q:
        k = Q.pop()
        Seq.append(k)
        v_vol, v_pol = sub[k]
        for v, flow in graph[k]:
            in_degrees[v] -= 1
            c_vol, c_pol = sub[v]
            sub[v] = (c_vol + v_vol*flow/100, c_pol)
            Mul[v] += (v_vol * flow / 100) * v_pol

            if in_degrees[v] == 0:
                Q.append(v)
                c_vol, c_pol = sub[v]
                c_pol = Mul[v] / c_vol + Pollution[v]
                sub[v] = (c_vol, c_pol)

    return sub

SUB = toposort(Graph)
for a, b in SUB:
    print(b)