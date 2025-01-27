while True:
    N = input()

    if N[0] == 'X':
        break

    while True:
        fun = False

        ind = N.find('ANA')
        if ind != -1:
            N = N[0:ind] + 'A' + N[ind + 3:]
            fun = True

        else:
            ind = N.find('BAS')
            if ind != -1:
                N = N[0:ind] + 'A' + N[ind + 3:]
                fun = True

        if not fun:
            break

    if N != 'A':
        print('NO')
    else:
        print('YES')



