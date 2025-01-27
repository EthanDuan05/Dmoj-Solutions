import sys

S = input()
D = {}

for i in S:
    if i not in D:
        D[i] = 1
    else:
        D[i] += 1

K = list(map(int, D.values()))
K.sort(reverse=True)

if len(K) <= 1:
    print(0)
    sys.exit(0)

sum = K[0] + K[1]
total = len(S)

print(total - sum)
