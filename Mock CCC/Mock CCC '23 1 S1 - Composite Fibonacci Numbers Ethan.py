T = int(input())

LIST_1 = [0, 1, 1, 2, 3, 5, 8]
LIST_2 = [13, 21, 34, 55, 89]
LIST_3 = [144, 233, 377, 610, 987]
LIST_4 = [1597, 2584, 4181, 6765]

for _ in range(T):
    num = int(input())
    new_num = list(str(num))
    if len(new_num) == 1:
        print('NO')
    elif len(new_num) == 2:
        # 1 1
        if (int(new_num[0]) and int(new_num[1])) in LIST_1:
            print('YES')
        # 11
        elif int((new_num[0] + new_num[1])) in LIST_2:
            print('YES')
        else:
            print('NO')
    elif len(new_num) == 3:
        # 1 1 1
        if (int(new_num[0]) and int(new_num[1]) and int(new_num[2])) in LIST_1:
            print('YES')
        # 11 1 and 1 11
        elif int(new_num[0] + new_num[1]) in LIST_2 and int(new_num[2]) in LIST_1:
            print('YES')
        elif int(new_num[0]) in LIST_1 and int(new_num[1] + new_num[2]) in LIST_2:
            print('YES')
        # 111
        elif int(new_num[0] + new_num[1] + new_num[2]) in LIST_3:
            print('YES')
        else:
            print('NO')
    elif len(new_num) == 4:
        # 1 1 1 1
        if (int(new_num[0]) and int(new_num[1]) and int(new_num[2]) and int(new_num[3])) in LIST_1:
            print('YES')
        # 1 111 and 111 1
        elif int(new_num[0]) in LIST_1 and int(new_num[1] + new_num[2] + new_num[3]) in LIST_3:
            print('YES')
        elif int(new_num[0] + new_num[1] + new_num[2]) in LIST_3 and int(new_num[3]) in LIST_1:
            print('YES')
        # 11 11
        elif int(new_num[0] + new_num[1]) and int(new_num[2] + new_num[3]) in LIST_2:
            print('YES')
        # 1111
        elif int(new_num[0] + new_num[1] + new_num[2] + new_num[3]) in LIST_4:
            print('YES')
        else:
            print('NO')
    elif len(new_num) == 5:
        # 1 1 1 1 1
        if (int(new_num[0]) and int(new_num[1]) and int(new_num[2]) and int(new_num[3]) and int(new_num[4])) in LIST_1:
            print('YES')
        # 1 1111 and 1111 1
        elif int(new_num[0]) in LIST_1 and int(new_num[1] + new_num[2] + new_num[3] + new_num[4]) in LIST_4:
            print('YES')
        elif int(new_num[0] + new_num[1] + new_num[2] + new_num[3]) in LIST_4 and int(new_num[4]) in LIST_1:
            print('YES')
        # 11 111 and 111 11
        elif int(new_num[0] + new_num[1]) in LIST_2 and int(new_num[2] + new_num[3] + new_num[4]) in LIST_3:
            print('YES')
        elif int(new_num[0] + new_num[1] + new_num[2]) in LIST_3 and int(new_num[3] + new_num[4]) in LIST_2:
            print('YES')
        else:
            print('NO')
