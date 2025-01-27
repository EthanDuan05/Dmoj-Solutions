import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    for i in range(1, int(1e9+1)):
        if i // A == B and (i % A == C % A):
            print(i)
            break