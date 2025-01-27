N = int(input())
L = []
L2 = []

for _ in range(N):
    S = input()
    L.append(S)

for i in range(N):
    if 'yubo' in L[i]:
        if L[i] not in L2:
            L2.append(L[i])
        if i - 1 >= 0:
            if L[i - 1] not in L2:
                L2.append(L[i - 1])

        if i + 1 < N:
            if L[i + 1] not in L2:
                L2.append(L[i + 1])

L2.sort()

for i in L2:
    print(i)