for _ in range(5):
    standard = int(input())
    name = ''
    weight = -10000
    current_difference = 10000

    for _ in range(4):
        n, w = input().split()
        w = int(w)

        difference = 0
        if w > standard:
            difference = w - standard
        elif w < standard:
            difference = standard - w
        else:
            difference = 0

        if difference < current_difference:
            current_difference = difference
            weight = w
            name = n

        elif difference == current_difference:
            if w > weight:
                current_difference = difference
                weight = w
                name = n


    print(name)