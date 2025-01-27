flag = True
A = []
while flag:
    direction = input()
    place = input()
    D = ''
    F_P = place
    F_D = ''

    if place == 'SCHOOL':
        if direction == 'R':
            F_D = 'LEFT'
        else:
            F_D = 'RIGHT'
        k = 'Turn', F_D, 'into your HOME.'
        A.append(k)
        flag = False

    else:
        if direction == 'R':
            F_D = 'LEFT'
        else:
            F_D = 'RIGHT'
        n = 'Turn', F_D, 'onto', F_P, 'street.'
        A.append(n)
for i in A:
    print(i)