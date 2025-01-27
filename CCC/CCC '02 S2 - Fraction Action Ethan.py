num = int(input())
dem = int(input())
a = num//dem
f = num % dem
S = 0

A = a
S = S

if a == 0 and f != 0:
    for i in range(1, dem):
        if f % i == 0 and dem % i == 0:
            if i == 1:
                w = f // i
                c = dem // i
                S = (str(w) + '/' + str(c))

            if i != 1:
                w = f // i
                c = dem // i
                S = (str(w) + '/' + str(c))
    print(S)

if a == 0 and f == 0:
    print(a)


if a != 0:
    if f == 0:
        print(a)

    elif f != 0:
        for i in range(1, dem):
            if f % i == 0 and dem % i == 0:
                if i != 1:
                    w = f//i
                    c = dem//i
                    S = (str(w) + '/' + str(c))

                elif i == 1:
                    w = f
                    c = dem
                    S = (str(w) + '/' + str(c))
        print(A, S)