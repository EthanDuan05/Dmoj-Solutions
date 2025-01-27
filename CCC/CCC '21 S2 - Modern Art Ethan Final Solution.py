row = int(input())
colum = int(input())

row_l = [0] * row
colum_l = [0] * colum

K = int(input())
for _ in range(K):
    order, ind = input().split()
    ind = int(ind)
    if order == 'R':
        row_l[ind - 1] += 1

    elif order == 'C':
        colum_l[ind - 1] += 1

ANS = 0
for s in range(row):
    for k in range(colum):
        if (row_l[s] + colum_l[k]) % 2 != 0:
            ANS += 1
print(ANS)
