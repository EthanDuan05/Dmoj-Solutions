import sys

N = int(input())
P = int(input())
Code = input()

Dic = {}
S = int(input())

if N == 0 or P == 0 or S == 0:
    print('None of the readers are perfectly efficient.')
    sys.exit(0)

for _ in range(S):
    Name, d_p, c_code = input().split()
    d_p = int(d_p)
    if c_code == Code:
        need = round(50 / d_p)
        if need <= N:
            Dic[Name] = d_p

MIN = min(Dic.values())
CNT = list(Dic.values()).count(MIN)

if len(Dic) == 0:
    print('None of the readers are perfectly efficient.')
elif CNT == 1:
    for i in Dic:
        if Dic[i] == MIN:
            print('The most efficient reader is ' + i + '.')
            print('This reader is perfectly efficient.')
if CNT > 1:
    NAME = []
    for i in Dic:
        if Dic[i] == MIN:
            NAME.append(i)

    ANS = ','.join(NAME)
    print('The most efficient readers are ' + ANS + '.')
    print('These readers are perfectly efficient.')