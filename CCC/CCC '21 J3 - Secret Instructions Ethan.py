P = ''
L = []
while True:
    line = input()
    sum = int(line[0]) + int(line[1])

    if line == '99999':
        break

    else:
        if sum == 0:
            D = P
        elif sum % 2 == 0:
            P = 'right'
        elif sum % 2 == 1:
            P = 'left'

    D = P
    L.append(P + ' ' + line[2:])

for i in L:
    print(i)