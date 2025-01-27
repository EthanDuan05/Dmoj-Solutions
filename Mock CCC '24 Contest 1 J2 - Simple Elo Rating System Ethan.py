N, RA, RB, K = map(int, input().split())
WL = input()

def Calculate(a, b, score):
    diff = b - a
    diff /= 400
    result = 10**diff
    result += 1
    ans = 1 / result
    return a + (score - ans)*K

RESULT = []
for i in range(N):
    M = WL[i]
    a = 0
    b = 0
    if M == 'T':
        a = Calculate(RA, RB, 0.5)
        b = Calculate(RB, RA, 0.5)

    if M == 'L':
        a = Calculate(RA, RB, 0)
        b = Calculate(RB, RA, 1)

    if M == 'W':
        a = Calculate(RA, RB, 1)
        b = Calculate(RB, RA, 0)

    RA = a
    RB = b
    RESULT.append((round(a, 1), round(b, 1)))

for i in RESULT:
    print(i[0], i[1])