Order = custom_order = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

L = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


Quadrants = [[] for _ in range(4)]

def creat_quadrants(a, b):
    for i in range(a, b):
        LINE = MAP[i]
        for ind in range(16):
            for s in LINE[ind]:
                if s in Order.keys():
                    if 0 <= ind <= 3:
                        Quadrants[0].append(s)
                    # change to 4 to 7
                    elif 4 <= ind <= 7:
                        Quadrants[1].append(s)

                    # change to 8 to 11
                    elif 8 <= ind <= 11:
                        Quadrants[2].append(s)

                    # change t0 12 to 15
                    elif 12 <= ind <= 15:
                        Quadrants[3].append(s)

    for i in Quadrants:
        i = sorted(i, key=lambda x: Order[x])

def find_rows(ind):
    row = MAP[ind]
    row = list(row)
    row = [x for x in row if x != '-']
    # delete later
    row = [x for x in row if x != ' ']
    row = sorted(row, key=lambda x: Order[x])
    u_i = 0
    while True:
        if L[u_i] not in row:
            break
        u_i += 1

    return L[u_i], u_i

def find_cols(ind):
    col = []
    for one in MAP:
        col.append(one[ind])

    col = [x for x in col if x != '-']
    # delete later
    col = [x for x in col if x != ' ']
    col = sorted(col, key=lambda x: Order[x])
    u_i = 0
    while True:
        if L[u_i] not in col:
            break
        u_i += 1

    return L[u_i], u_i

def check_quadrants(Sorted_L, ele):
    if ele in Sorted_L:
        return False

    return True

def row(i, num):
    if num in MAP[i]:
        return False
    return True

def col(i, num):
    for q in MAP:
        if num == q[i]:
            return False
    return True

def main(a, b):
    cnt = 0
    for i in range(a, b):
        # change to 16
        for j in range(16):
            s = MAP[i][j]
            if s == '-':
                row_min, u_i_row = find_rows(i)
                col_min, u_i_col = find_cols(j)
                ans = max(row_min, col_min)
                ans_ind = 0

                if ans == row_min:
                    ans_ind = u_i_row
                elif ans == col_min:
                    ans_ind = u_i_col

                # quad_check_ans = None
                # quad_check_row = None
                # quad_check_col = None
                Total = False
                Q1, Q2, Q3, Q4, = False, False, False, False
                # change to 0 to 3
                while not Total:
                    if 0 <= j <= 3:
                        quad_check_ans = check_quadrants(Quadrants[0], ans)
                        check_row = row(i, ans)
                        check_col = col(j, ans)
                        if quad_check_ans and check_row and check_col:
                            Q1 = True
                            Total = True

                    # change to 4 to 7
                    elif 4 <= j <= 7:
                        quad_check_ans = check_quadrants(Quadrants[1], ans)
                        check_row = row(i, ans)
                        check_col = col(j, ans)
                        if quad_check_ans and check_row and check_col:
                            Q2 = True
                            Total = True

                    # change to 8 to 11
                    elif 8 <= j <= 11:
                        quad_check_ans = check_quadrants(Quadrants[2], ans)
                        check_row = row(i, ans)
                        check_col = col(j, ans)
                        if quad_check_ans and check_row and check_col:
                            Q3 = True
                            Total = True

                    # change t0 12 to 15
                    elif 12 <= j <= 15:
                        quad_check_ans = check_quadrants(Quadrants[3], ans)
                        check_row = row(i, ans)
                        check_col = col(j, ans)
                        if quad_check_ans and check_row and check_col:
                            Q4 = True
                            Total = True

                    if not Total:
                        if ans_ind < 15:
                            ans_ind += 1

                        ans = L[ans_ind]

                    if Total:
                        MAP[i][j] = ans
                        cnt += 1
                        if Q1:
                            Quadrants[0].append(ans)
                            Quadrants[0] = sorted(Quadrants[0], key=lambda x: Order[x])
                        elif Q2:
                            Quadrants[1].append(ans)
                            Quadrants[1] = sorted(Quadrants[1], key=lambda x: Order[x])
                        elif Q3:
                            Quadrants[2].append(ans)
                            Quadrants[2] = sorted(Quadrants[2], key=lambda x: Order[x])
                        elif Q4:
                            Quadrants[3].append(ans)
                            Quadrants[3] = sorted(Quadrants[3], key=lambda x: Order[x])

                    if ans_ind == 15:
                        ans = L[ans_ind]
                        if 0 <= j <= 3:
                            quad_check_ans = check_quadrants(Quadrants[0], ans)
                            check_row = row(i, ans)
                            check_col = col(j, ans)
                            if quad_check_ans and check_row and check_col:
                                Q1 = True
                                Total = True

                        # change to 4 to 7
                        elif 4 <= j <= 7:
                            quad_check_ans = check_quadrants(Quadrants[1], ans)
                            check_row = row(i, ans)
                            check_col = col(j, ans)
                            if quad_check_ans and check_row and check_col:
                                Q2 = True
                                Total = True

                        # change to 8 to 11
                        elif 8 <= j <= 11:
                            quad_check_ans = check_quadrants(Quadrants[2], ans)
                            check_row = row(i, ans)
                            check_col = col(j, ans)
                            if quad_check_ans and check_row and check_col:
                                Q3 = True
                                Total = True

                        # change t0 12 to 15
                        elif 12 <= j <= 15:
                            quad_check_ans = check_quadrants(Quadrants[3], ans)
                            check_row = row(i, ans)
                            check_col = col(j, ans)
                            if quad_check_ans and check_row and check_col:
                                Q4 = True
                                Total = True

                        if not Total:
                            break
                        else:
                            MAP[i][j] = ans
                            cnt += 1

                        if Q1:
                            Quadrants[0].append(ans)
                            Quadrants[0] = sorted(Quadrants[0], key=lambda x: Order[x])
                        elif Q2:
                            Quadrants[1].append(ans)
                            Quadrants[1] = sorted(Quadrants[1], key=lambda x: Order[x])
                        elif Q3:
                            Quadrants[2].append(ans)
                            Quadrants[2] = sorted(Quadrants[2], key=lambda x: Order[x])
                        elif Q4:
                            Quadrants[3].append(ans)
                            Quadrants[3] = sorted(Quadrants[3], key=lambda x: Order[x])
                        break

    return cnt


for _ in range(10):
    MAP = []
    #change to 16
    for _ in range(16):
        line = list(input())
        if len(line) != 0:
            MAP.append(line)

    n1 = 0
    n2 = 4
    ans = 0
    while n2 <= 16:
        creat_quadrants(n1, n2)
        n = main(n1, n2)
        Quadrants = [[] for _ in range(4)]
        n1 += 4
        n2 += 4
        ans += n

    print(ans)
