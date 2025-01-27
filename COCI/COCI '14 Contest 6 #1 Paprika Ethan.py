N , X = map(int, input().split())
L = []

for _ in range(N):
    day, con = map(int, input().split())
    L.append([day, con])

for i in range(N-1):
    if L[i][1] == 1 and L[i+1][1] == 0:
        if L[i][0] > L[i+1][0]:
            L[i][0], L[i+1][0] = L[i+1][0], L[i][0]

    elif L[i][1] == 0 and L[i + 1][1] == 1:
        if L[i][0] < L[i+1][0]:
            L[i][0], L[i+1][0] = L[i+1][0], L[i][0]

cnt = 0
for i in L:
    if i[0] <= X and i[1] == 1:
        cnt += 1
    elif i[0] > X and i[1] == 0:
        cnt += 1

print(cnt)