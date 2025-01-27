Type = int(input())

N = int(input())
D = list(map(int, input().split()))
P = list(map(int, input().split()))

speed = 0
if Type == 2:
    D.sort()
    P.sort()
    while D:
        if D[-1] > P[-1]:
            a = D.pop(-1)
            b = P.pop(0)
            speed += max(a, b)

        elif D[-1] < P[-1]:
            a = D.pop(0)
            b = P.pop(-1)
            speed += max(a, b)

        else:
            if max(P[-1], D[0]) >= max(P[0], D[-1]):
                a = D.pop(0)
                b = P.pop(-1)
                speed += max(a, b)

elif Type == 1:
    D.sort()
    P.sort()
    while D:
        a = D.pop(0)
        b = P.pop(0)
        speed += max(a, b)

print(speed)
