N = int(input())

for _ in range(N):
    line1 = input()
    line2 = input()
    line3 = input()

    Flag1 = True
    # word 1
    pre_line1 = ''
    suf_line1 = ''
    if len(line1) >= N:
        pre_line1 = line1[0: N]
        suf_line1 = line1[-N:]
    else:
        pre_line1 = line1
        suf_line1 = line1

    if pre_line1 != line2[0:len(pre_line1)] and pre_line1!= line3[0:len(pre_line1)]:
        Flag1 = True
    else:
        Flag1 = False

    if suf_line1 != line2[-len(suf_line1):] and suf_line1 != line3[-len(suf_line1):]:
        Flag1 = True
    else:
        Flag1 = False

    Flag2 = True
    # word 2
    pre_line2 = ''
    suf_line2 = ''
    if len(line2) >= N:
        pre_line2 = line2[0: N]
        suf_line2 = line2[-N:]
    else:
        pre_line2 = line2
        suf_line2 = line2

    if pre_line2 != line1[0:len(pre_line2)] and pre_line2 != line3[0:len(pre_line2)]:
        Flag2 = True
    else:
        Flag2 = False

    if suf_line2 != line1[-len(suf_line2):] and suf_line2 != line3[-len(suf_line2):]:
        Flag2 = True
    else:
        Flag2 = False

    Flag3 = True
    # word 3
    pre_line3 = ''
    suf_line3 = ''
    if len(line3) >= N:
        pre_line3 = line3[0: N]
        suf_line3 = line3[-N:]
    else:
        pre_line3 = line3
        suf_line3 = line3

    if pre_line3 != line1[0:len(pre_line3)] and pre_line3 != line2[0:len(pre_line3)]:
        Flag3 = True
    else:
        Flag3 = False

    if suf_line3 != line1[-len(suf_line3):] and suf_line3 != line2[-len(suf_line3):]:
        Flag3 = True
    else:
        Flag3 = False

    if Flag1 and Flag2 and Flag3:
        print('Yes')
    else:
        print('No')

    print(Flag1, Flag2, Flag3)
