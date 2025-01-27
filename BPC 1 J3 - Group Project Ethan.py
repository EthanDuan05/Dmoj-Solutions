import sys
input = sys.stdin.readline

N = int(input())
Line = list(map(int, input().split()))

Line.sort()

cnt = 0
for i in range(0, 2*N, 2):
    cnt += Line[i+1] - Line[i]

print(cnt)