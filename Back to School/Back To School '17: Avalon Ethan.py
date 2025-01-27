P = 1

G = int(input())
for _ in range(G):
    evil, total = map(int, input().split())
    P_l = 1 - (evil / total)
    P *= P_l

decimal_point = len(str(P).split('.')[1])

if decimal_point == 1:
    if str(P).split('.')[1] == '0':
        print(round(P))
elif 1 < decimal_point <= 6:
    print(P)
else:
    print(round(P, 6))