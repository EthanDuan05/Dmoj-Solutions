import sys

N = int(input())
B = list(map(int, input().split()))

if N == 1:
    print(B[0])
    sys.exit(0)

ANS = []
previous_sum = 0
for i in range(N):
    if i+1 == 1:
        ANS.append(B[i])
        previous_sum += B[i]
    else:
        value = B[i]*(i+1)
        f_value = value - previous_sum
        ANS.append(f_value)
        previous_sum += f_value

print(' '.join(map(str, ANS)))
