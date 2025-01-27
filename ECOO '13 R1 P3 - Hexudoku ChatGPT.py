Order = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

L = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def create_quadrants(a, b, MAP):
    Quadrants = [[] for _ in range(16)]
    for i in range(a, b):
        for j in range(16):
            s = MAP[i][j]
            if s in Order.keys():
                quadrant_index = (i // 4) * 4 + (j // 4)
                Quadrants[quadrant_index].append(s)
    for i in range(16):
        Quadrants[i] = sorted(Quadrants[i], key=lambda x: Order[x])
    return Quadrants

def find_row_values(ind, MAP):
    row = MAP[ind]
    row = list(row)
    row = [x for x in row if x != '-']
    row = sorted(row, key=lambda x: Order[x])
    u_i = 0
    while True:
        if L[u_i] not in row:
            break
        u_i += 1
    return L[u_i], u_i

def find_col_values(ind, MAP):
    col = []
    for one in MAP:
        col.append(one[ind])
    col = [x for x in col if x != '-']
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

def check_row(i, num, MAP):
    if num in MAP[i]:
        return False
    return True

def check_col(i, num, MAP):
    for q in MAP:
        if num == q[i]:
            return False
    return True

def main(a, b, MAP):
    cnt = 0
    Quadrants = create_quadrants(a, b, MAP)
    for i in range(a, b):
        for j in range(16):
            s = MAP[i][j]
            if s == '-':
                for ans in L:
                    quadrant_index = (i // 4) * 4 + (j // 4)
                    if (
                        check_quadrants(Quadrants[quadrant_index], ans) and
                        check_row(i, ans, MAP) and
                        check_col(j, ans, MAP)
                    ):
                        MAP[i][j] = ans
                        cnt += 1
                        Quadrants[quadrant_index].append(ans)
                        Quadrants[quadrant_index] = sorted(Quadrants[quadrant_index], key=lambda x: Order[x])
                        break
    return cnt

for _ in range(10):
    sample_input = []
    for i in range(16):
        line = input()
        sample_input.append(line)

    MAP = [list(line) for line in sample_input]

    # Process the input data
    n1 = 0
    n2 = 16
    ans = main(n1, n2, MAP)


    # for row in MAP:
        # print(''.join(row))
    print(ans)
