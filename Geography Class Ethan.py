import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    used = []
    sum = 1
    if N > 1:
        sum += N**2
    for i in range(2, int(math.sqrt(N))):
        if N % i == 0:
            K = N//i
            sum += i**2

            if K * K != N:
                sum += K**2

    print(sum)

print(2**17)