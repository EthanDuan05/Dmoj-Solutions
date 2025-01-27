import sys
input = sys.stdin.readline

T = int(input())
Line = list(map(int, input().strip().split()))
ANS = []

REGION = 0
for i in range(T):
    C_A = []
    for j in range(T):
        if j + i < T:
            Arr = Line[j:j+i+1]

            LEN = len(Arr)
            if LEN == 1:
                C_A.append(0)
            else:
                U_A = Arr
                Total = 0
                if LEN % 2 == 0:
                    while U_A:
                        a = U_A.pop(0)
                        b = U_A.pop(-1)
                        Total += abs(a-b)
                    C_A.append(Total)
                else:
                    while len(U_A) != 1:
                        a = U_A.pop(0)
                        b = U_A.pop(-1)
                        Total += abs(a - b)
                    C_A.append(Total)

    ANS.append(min(C_A))
    REGION += 1

print(' '.join(map(str, ANS)))