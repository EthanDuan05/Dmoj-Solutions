U = int(input())
M = int(input())
K = int(input())

total = 0
cnt = 0
while cnt < K:
    if U > M:
        total += U
        cnt += 1
    elif M > U:
        total += M
        cnt += 1
    else:
        total += U
        cnt += 1
print(total)