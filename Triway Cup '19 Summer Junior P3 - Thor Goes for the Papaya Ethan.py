N = int(input())

L = []
for _ in range(N):
    num = int(input())
    L.append(num)

ANS = []
for i in range(N):
    if i + 1 < N:
        Letter = (L[i] * L[i+1]) % 26
        ANS.append(chr(65 + Letter))

print('Thanos is on Planet:', ''.join(ANS))