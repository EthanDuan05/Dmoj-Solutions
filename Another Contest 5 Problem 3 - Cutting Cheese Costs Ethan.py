N, K = map(int, input().split())
DIC = []

for _ in range(N):
    P, D = map(int, input().split())
    DIC.append((P-D, P, D))

DIC.sort(reverse=True)

total = 0
for s, p, d in DIC:
    if K > 0:
        total += d
        K -= 1
    else:
        total += p

print(total)