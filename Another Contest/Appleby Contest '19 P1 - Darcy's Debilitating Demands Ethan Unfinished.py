import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())

    if (max(0, A+1) + max(0, B+1) + max(0, C+1)) < N:
        print(-1)
    else:
        a = 0