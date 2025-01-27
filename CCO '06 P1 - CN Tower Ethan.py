import math

N = int(input())
L = []

for _ in range(N):
    place, degree = input().split()
    degree = float(degree)
    L.append(degree)

L.sort()
GAP = []

for i in range(N-1):
    gap = L[i+1] - L[i]
    GAP.append(gap)

GAP.append(L[0] - (L[-1] - 360))

print(math.ceil(4320*(360-max(GAP))/360))