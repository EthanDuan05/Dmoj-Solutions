import math

N = int(input())
L = []

for _ in range(N):
    num = int(input())
    L.append(num)

L.sort()

if N % 2 == 0:
    i = N // 2
    print(math.ceil((L[i-1] + L[i]) / 2))
else:
    i = N // 2
    print(round(L[i]))