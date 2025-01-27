import sys
input = sys.stdin.readline
x, y, q = map(int, input().split())

line_1 = '9'*x
line_2 = '9'*y

ans = int(line_1) * int(line_2)
ans = str(ans)

for _ in range(q):
    ind = int(input())
    print(ans[ind - 1])