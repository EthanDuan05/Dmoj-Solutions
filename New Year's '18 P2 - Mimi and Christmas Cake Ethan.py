import sys
input = sys.stdin.readline

import math

N = int(input())
L = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if L[i] == 1:
        continue
    else:
        sqrt_n = math.sqrt(L[i])
        flag = True
        for f in range(2, int(sqrt_n)+1):
            if L[i] % f == 0:
                flag = False
                break

        if flag:
            cnt += 1

print(cnt)


