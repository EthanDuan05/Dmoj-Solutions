import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())
    N = a * b
    while True:
        if N % a == c % a:
            print(N)
            break
        else:
            N += 1