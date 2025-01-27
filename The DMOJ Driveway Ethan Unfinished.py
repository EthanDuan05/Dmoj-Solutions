t, m = map(int, input().split())

cars = []

for s in range(t):
    a, b = input().split(' ')
    if b == 'in':
        cars.append(a)
    elif b == 'out':
        if cars[len(cars)-1] == a:
            cars.pop(a)
            m -= 1
        elif cars[len(cars)-1] != a:
            if cars[0] == a:
                if m >= 1:
                    cars.remove(a)
                    m -= 1

for i in cars:
    print(i)