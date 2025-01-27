D = []
P = []

flag = True
while flag:
    direction = input()
    place = input()
    if place != 'SCHOOL':
        D.append(direction)
        P.append(place)
    else:
        D.append(direction)
        P.append(place)
        break

D.reverse()
P.reverse()

for i in range(len(P)):
    if P[i] == 'SCHOOL':
        if D[i] == 'R':
            print('Turn LEFT onto', P[i + 1], 'street.')
        elif D[i] == 'L':
            print('Turn RIGHT onto', P[i + 1], 'street.')

    elif P[i] != 'SCHOOL':
        if i+1 < len(D):
            if D[i] == 'R':
                print('Turn LEFT onto', P[i + 1], 'street.')
            elif D[i] == 'L':
                print('Turn RIGHT onto', P[i + 1], 'street.')
        elif i+1 == len(D):
            if D[i] == 'R':
                print('Turn LEFT into your HOME.')
            elif D[i] == 'L':
                print('Turn RIGHT into your HOME.')
