import sys
input = sys.stdin.readline
sentence = input()
M = [0] * (len(sentence))
PSA = [0] * (len(sentence) + 1)

ANS = []
q = int(input())
for m in range(q):
    a, b, letter = input().split()
    a = int(a)
    b = int(b)

    for i in range(len(sentence)):
        if sentence[i] == letter:
            M[i] += 1
        else:
            M[i] += 0

    for dd in range(len(sentence)):
        PSA[dd+1] = M[dd] + PSA[dd]

    ans = PSA[b] - PSA[a-1]
    ANS.append(ans)
    M = [0] * (len(sentence))
    PSA = [0] * (len(sentence) + 1)

for i in ANS:
    print(i)