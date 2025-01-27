N = int(input())

cnt = 0
K = int(input())
for _ in range(K):
    ships = int(input())
    if ships == 1:
        cnt += 0.5
    elif ships == 2:
        cnt += 1
    else:
        cnt += 5

if cnt <= N:
    print('Continue')
else:
    print('Return')