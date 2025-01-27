import sys


def determine_a(S):
    if len(S) == 1:
        if S[0] == 'A':
            return True
        else:
            return False

    if len(S) > 2 and S[0] == 'A':
        S.pop(0)
        if S[0] == 'N' and determine_a(S[1:-1]):
            S.pop(0)
            return determine_a(S)
        else:
            return False

    elif len(S) > 2 and (S[0] == 'B' and S[-1] == 'S'):
        S.pop(0)
        S.pop(-1)
        return determine_a(S)

    return False

while True:
    Word = list(input())

    if Word[0] == 'X':
        break

    if determine_a(Word):
        print('YES')
    else:
        print('NO')
