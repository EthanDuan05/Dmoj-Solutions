import sys
input = sys.stdin.readline
M, N = map(int, input().split())

# create the initial query
initial = []
for i in range(M):
    initial.append([0]*N)

while True:
    r, c, x = map(int, input().split())
    if not (r == 0 and c == 0 and x == 0):
        initial[r-1][c-1] += x
    else:
        break

# find the opposite color
for i in range(len(initial)):
    if i % 2 == 0:
        for m in range(len(initial[i])):
            if m % 2 == 0:
                initial[i][m] *= -1
    else:
        for m in range(len(initial[i])):
            if m % 2 != 0:
                initial[i][m] *= -1

# create psa
psa = [[0 for i in range(N+1)] for j in range(M+1)]
for r in range(1, M+1):
    for c in range(1, N+1):
        psa[r][c] = psa[r-1][c] + psa[r][c-1] - psa[r-1][c-1] + initial[r-1][c-1]

ans = []
while True:
    r_1, c_1, r_2, c_2 = map(int, input().split())
    if not (r_1 == 0 and c_1 == 0 and r_2 == 0 and c_2 == 0):
        value = psa[r_2][c_2] - psa[r_1-1][c_2] - psa[r_2][c_1-1] + psa[r_1-1][c_1-1]
        if (r_1 + c_1) % 2 == 0:
            ans.append(-value)
        else:
            ans.append(value)
    else:
        break

for i in ans:
    print(i)