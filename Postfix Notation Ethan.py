L = list(input())
precedence = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '^': 3}


def applytoken(a, b, ops):
    if ops == '+':
        return int(a) + int(b)
    elif ops == '-':
        return int(a) - int(b)
    elif ops == '/':
        return int(a) / int(b)
    elif ops == '*':
        return int(a) * int(b)
    elif ops == '%':
        return int(a) % int(b)


ANS = []


def evaluate(line):
    values = []
    operator = []
    M = 0

    while M < len(line):
        if line[M].isdigit():
            val = 0
            while M < len(line) and line[M].isdigit():
                val = (val * 10) + int(line[M])
                M += 1
            values.append(val)

        elif line[M] in precedence:
            while len(operator) != 0 and precedence.get(operator[operator[-1]]) >= precedence.get(line[line[M]]):
                val_2 = int(values.pop())
                val_1 = int(values.pop())
                op = operator.pop()
                values.append(applytoken(val_1, val_2, op))
            operator.append(line[M])
        M += 1

    while len(operator) != 0:
        val1 = values.pop()
        val2 = values.pop()
        opss = operator.pop()

        values.append(applytoken(val1, val2, opss))

    return values[-1]


print(evaluate(L))
