T = int(input())

for _ in range(T):
    N = int(input())
    Mountain_cars = []
    Waiting_cars = []

    # create the list
    for _ in range(N):
        Mountain_cars.append(int(input()))

    while Mountain_cars[len(Mountain_cars)-1] != 1:
        Waiting_cars.append(Mountain_cars[len(Mountain_cars)-1])
        Mountain_cars.pop()

    need = 1

    ans = 'Y'
    while len(Mountain_cars) > 0 or len(Waiting_cars) > 0:
        if len(Mountain_cars) > 0 and len(Waiting_cars) > 0:
            if Mountain_cars[len(Mountain_cars)-1] == need:
                need += 1
                Mountain_cars.pop()
            elif Waiting_cars[len(Waiting_cars)-1] == need:
                need += 1
                Waiting_cars.pop()
            else:
                Waiting_cars.append(Mountain_cars[len(Mountain_cars)-1])
                Mountain_cars.pop()

        elif len(Mountain_cars) > 0:
            if Mountain_cars[len(Mountain_cars)-1] == need:
                need += 1
                Mountain_cars.pop()
            else:
                Waiting_cars.append(Mountain_cars[len(Mountain_cars)-1])
                Mountain_cars.pop()
        else:
            if Waiting_cars[len(Waiting_cars)-1] == need:
                need += 1
                Waiting_cars.pop()
            else:
                ans = 'N'
                break
    print(ans)