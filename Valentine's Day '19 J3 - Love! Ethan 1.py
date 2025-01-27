line = list(input())
line.reverse()
L = ['e', 'v', 'o', 'l']

current = ''

debug = True

cnt_e = 0
cnt_v = 0
cnt_o = 0
cnt_l = 0

for i in line:
    print(current)
    if i == 'e':
        if current != ('v' and 'o' and 'l'):
            cnt_e += 1
            current = 'e'

    elif i == 'v':
        if current == ('e' or 'v'):
            cnt_v += 1
            current = 'v'

    elif i == 'o':
        if current == ('v' or 'o'):
            cnt_o += 1
            current = 'o'

    elif i == 'l':
        if current == ('o' or 'l'):
            cnt_l += 1
            current = 'l'

if debug:
    print(cnt_e)
    print(cnt_v)
    print(cnt_o)
    print(cnt_l)

print(cnt_e*cnt_v*cnt_o*cnt_l)