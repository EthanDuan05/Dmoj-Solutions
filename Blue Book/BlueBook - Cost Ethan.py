import math
N = int(input())

for _ in range(N):
    mass = int(input())
    if 0 <= mass <= 30:
        print(38)
    elif 30 < mass <= 50:
        print(55)
    elif 50 < mass <= 100:
        print(73)
    elif mass > 100:
        more = mass - 100
        add = more % 50
        if add == 0:
            print(73 + 24*(more // 50))
        else:
            print(73 + 24*(more // 50 + 1))