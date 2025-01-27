import sys
import math

N, a, R = map(int, input().split())

if a > R:
    print(0)
    sys.exit(0)

ans = math.floor(R / a)

if ans == 0:
    print(0)
    sys.exit(0)

if ans > N:
    print(N)
else:
    print(ans)