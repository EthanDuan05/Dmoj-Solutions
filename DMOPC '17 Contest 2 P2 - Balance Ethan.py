import sys

N = list(input())

S = []
chance = 0

for i in N:
    if i == '(':
        S.append(i)
    elif i == ')':
        if len(S) != 0:
            if S[-1] == '(':
                S.pop(-1)
        else:
            if chance == 0:
                chance += 1
                S.append('(')
            else:
                print('NO')
                sys.exit(0)

if chance == 0:
    if len(S) == 2:
        if S[0] == S[-1]:
            S.clear()

if len(S) == 0:
    print('YES')
else:
    print('NO')