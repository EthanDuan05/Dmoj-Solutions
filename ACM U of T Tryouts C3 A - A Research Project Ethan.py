G = int(input())
m_min = [0]*G
m_max = [0]*G

for i in range(G):
    n = int(input())
    m = map(int, input().split())
    L = sorted(m)
    min = L[0]
    max = L[n-1]
    m_min[i] += min
    m_max[i] += max

for s in range(G):
    print(m_min[s], m_max[s])