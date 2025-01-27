import sys
input = sys.stdin.readline

N = int(input())

L = []
IND = N // 2 + 1

for _ in range(N):
    LIST = list(map(int, input().split()))
    LIST.sort()
    L.append(LIST[IND-1])

L.sort()
print(L[IND-1])
