import math

T = int(input())

for _ in range(T):
    N, B = map(int, input().split())
    Contestant = list(map(int, input().split()))

    cnt = 0
    for i in Contestant:
        if i > B:
            cnt += 1

    wins = 100*math.sqrt(N - cnt)
    ans = '%.2f'%wins

    print('Bob wins $'+str(ans)+' at IOI!')