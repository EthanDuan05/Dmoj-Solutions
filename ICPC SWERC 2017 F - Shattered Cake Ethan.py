import sys
input = sys.stdin.readline

W = int(input())
N = int(input())

area = 0
for _ in range(N):
    w, l = map(int, input().split())
    area += w*l

print(area // W)