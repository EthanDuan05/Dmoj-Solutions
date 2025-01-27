def convert(s: str, numRows: int):
    if numRows == 1:
        return s

    S = s
    step = numRows
    ind = 0
    ans = [[] for _ in range(numRows)]
    state = None

    for i in S:
        ans[ind].append(i)
        if ind == 0:
            state = True
        elif ind == step - 1:
            state = False

        if state:
            ind += 1
        else:
            ind -= 1

    ANS = ''
    for s in ans:
        ANS += ''.join(s)
    return ANS

print(convert("AB", 1))