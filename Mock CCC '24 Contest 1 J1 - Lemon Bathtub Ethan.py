L = int(input())
K = int(input())

if L % K == 0:
    print(L // K)
else:
    print(L // K + 1)