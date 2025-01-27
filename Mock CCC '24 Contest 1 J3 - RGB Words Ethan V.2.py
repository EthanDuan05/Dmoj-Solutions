N = int(input())
Line = list(input())

F_R = False
F_G = False
F_B = False
cnt = 0
r1 = 0
r2 = 0

for i in Line:
    if i == 'R':
        if not F_R:
            F_R = True
            r1 = 1
        else:
            if F_G:
                r2 += 1
            else:
                r1 += 1

    if i == 'G':
        if F_R == True and F_G == False:
            F_G = True
        else:
            r1 = r2
            r2 = 0

    if i == 'B':
        if F_R and F_G:
            cnt += r1


print(cnt)