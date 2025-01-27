import sys
import math

N = int(input())

X, Y, Z = map(int, input().split())
a, b, c = map(int, input().split())

volume_package = X*Y*Z
volume_truck = a*b*c
Debug = False

T = math.floor(volume_truck / volume_package)
if T == 0:
    print('SCAMMED')
    sys.exit(0)

if N // T != 0:
    if N % T == 0:
        print(N / T)
    else:
        print(round(N / T))
else:
    print(N // T + 1)

if Debug:
    print(T)
    print(N / T)
