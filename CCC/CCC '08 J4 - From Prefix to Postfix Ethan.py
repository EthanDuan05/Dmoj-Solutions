Operator = ['+', '-']

while True:
    N = input().split()

    if N[0] == '0':
        break

    N.reverse()
    S = []

    for i in N:
        if i not in Operator:
            S.append(i)
        else:
            result = S.pop(-1) + ' ' + S.pop(-1) + ' ' + i
            S.append(result)

    print(S[0])

