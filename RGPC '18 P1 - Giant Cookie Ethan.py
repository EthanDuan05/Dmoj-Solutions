N, M = map(int, input().split())

if N % M == 0:
    print('yes', N // M)
else:
    for i in range(1, N+1):
        if i > M and N % i == 0:
            print('no', i - M)
            break