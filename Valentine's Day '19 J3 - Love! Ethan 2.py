line = list(input())
line.reverse()

cnt_e, cnt_v, cnt_o, cnt_l = 0, 0, 0, 0

for cur in line:
    if cur == 'e':
        cnt_e += 1

    elif cur == 'v':
        cnt_v += cnt_e

    elif cur == 'o':
        cnt_o += cnt_v

    elif cur == 'l':
        cnt_l += cnt_o

print(cnt_l)