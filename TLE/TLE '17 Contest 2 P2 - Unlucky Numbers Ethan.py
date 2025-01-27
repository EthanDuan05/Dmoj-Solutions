import sys
input = sys.stdin.readline

T = int(input())

K = list(map(int, input().split()))

N = int(input())

for _ in range(N):
    F = int(input())
    PSA = [0 for j in range(F)]

    for i in K:
        if i <= F:
            PSA[i-1] = 1

    # print(PSA)

    cnt = 0
    for i in PSA:
        if i != 0:
            cnt += 1

    print(F - cnt)
