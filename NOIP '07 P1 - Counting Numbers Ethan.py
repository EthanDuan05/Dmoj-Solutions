import sys
input = sys.stdin.readline

L = []
D = {}
N = int(input())
for _ in range(N):
    num = int(input())
    L.append(num)
    if num in D:
        D[num] += 1
    else:
        D[num] = 1

Now = sorted(set(L))
for i in Now:
    print(i, D[i])
