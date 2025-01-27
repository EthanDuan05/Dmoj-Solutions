T = int(input())

for _ in range(T):
    degree = int(input())
    if 0 <= degree <= 45:
        print('N')
    elif 45 < degree <= 135:
        print('E')
    elif 135 < degree <= 225:
        print('S')
    elif 225 < degree < 315:
        print('W')
    else:
        print('N')