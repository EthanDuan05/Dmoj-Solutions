import math

L = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
     1024, 2048, 4096, 8192, 16384, 32768,
     65536, 131072, 262144, 524288, 1048576,
     2097152, 4194304, 8388608, 16777216, 33554432,
     67108864, 134217728, 268435456, 536870912, 1073741824,
     2147483648, 4294967296, 8589934592]


def log(x):
    if x == 0:
        return False
    elif x < 8589934592:
        return False
    elif x == 1:
        return True
    while x != 1:
        if x % 2 != 0:
            return False
        x = x // 2
    return True


ANS = []
n = int(input())
for i in range(n):
    x = int(input())
    if x <= 8589934592:
        if x in L:
            ANS.append('T')
        else:
            ANS.append('F')
    else:
        if log(x):
            ANS.append('T')
        else:
            ANS.append('F')

for i in ANS:
    print(i)