import sys
input = sys.stdin.readline

D, M = map(int, input().split())
L1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']

L2 = ['   ' for _ in range(7)]
L3 = ['   ' for _ in range(7)]
L4 = ['   ' for _ in range(7)]
L5 = ['   ' for _ in range(7)]
L6 = ['   ' for _ in range(7)]
L7 = ['   ' for _ in range(7)]

L2[D-1] = '  1'

print(' '.join(L1))

first = 1
M -= 1
ind = D-1

def ind_plus(n):
    if n + 1 > 6:
        return 0
    else:
        return n + 1

def construct(num):
    if num >= 10:
        return ' ' + str(num)
    else:
        return ' ' + ' ' + str(num)
cnt = D
debug = False

while M > 0:
    M -= 1
    first += 1
    ind = ind_plus(ind)
    cnt += 1

    if cnt >= 36 < 43:
        L7[ind] = construct(first)

    elif cnt >= 29 < 36:
        L6[ind] = construct(first)

    elif cnt >= 22 < 29:
        L5[ind] = construct(first)

    elif cnt >= 15 < 22:
        L4[ind] = construct(first)

    elif cnt > 7 < 15:
        L3[ind] = construct(first)

    elif cnt <= 7:
        L2[ind] = construct(first)

    if debug:
        print('-------------------')
        print(' '.join(L1))
        print(' '.join(L2))
        print(' '.join(L3))
        print(' '.join(L4))
        print(' '.join(L5))
        print(' '.join(L6))
        print('-------------------')
        print(cnt)

        if first == 13:
            print(cnt, '!!!')



print(' '.join(L2))
print(' '.join(L3))
print(' '.join(L4))
print(' '.join(L5))

if cnt >= 29 < 36:
    while L6[-1] == '   ':
        L6.pop(-1)
    print(' '.join(L6))

if cnt >= 36:
    while L7[-1] == '   ':
        L7.pop(-1)
    print(' '.join(L7))