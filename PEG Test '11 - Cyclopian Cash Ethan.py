N = int(input())

L = []

for _ in range(N):
    L.append(int(input()))

L.sort()

if N % 2 == 0:
    ind_1 = N // 2
    ind_2 = ind_1-1
    M = (L[ind_1] + L[ind_2]) / 2
    print('%.1f'%M)
else:
    ind = N // 2
    print('%.1f'%L[ind])