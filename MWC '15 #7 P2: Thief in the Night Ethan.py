f, r = map(int, input().split())
PSA = []

for s in range(f):
    line = input().split()
    psa = [0] * (r + 1)
    for f in range(r):
        psa[f+1] = int(line[f]) + psa[f]
    PSA.append(psa)

Solution = []
q = int(input())
for s in range(q):
    a, b, c = map(int, input().split())
    K = PSA[c-1]
    solution = K[b] - K[a-1]
    Solution.append(solution)

for s in Solution:
    print(s)