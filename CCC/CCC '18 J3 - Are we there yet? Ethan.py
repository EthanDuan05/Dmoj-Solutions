a, b, c, d = map(int, input().split())

M = []
for i in range(1, 6):
    if i == 1:
        L = 0, a, a + b, a + b + c, a + b + c + d, '*'
        for i in L:
            M.append(i)
    elif i == 2:
        L = a, 0, b, b + c, b + c + d, '*'
        for i in L:
            M.append(i)
    elif i == 3:
        L = a + b, b, 0, c, c + d, '*'
        for i in L:
            M.append(i)
    elif i == 4:
        L = a + b + c, b + c, c, 0, d, '*'
        for i in L:
            M.append(i)
    elif i == 5:
        L = a + b + c + d, b + c + d, c + d, d, 0
        for i in L:
            M.append(i)

P = ''
for s in M:
    if s != '*':
        P += str(s)+' '
    elif s == '*':
        P += '\n'
print(P)