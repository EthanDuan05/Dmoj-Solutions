N = int(input())
symbol = {'(': ')'}

for _ in range(N):
    ans = True
    line = list(input())
    symbol_line = []
    for i in line:
        if i in symbol.keys():
            symbol_line.append(i)
        elif i in symbol.values():
            if len(symbol_line) == 0:
                ans = False
                break
            left = symbol_line.pop()
            if i == symbol[left]:
                continue
            else:
                ans = False
                break
    if ans and len(symbol_line) == 0:
        print('YES')
    else:
        print('NO')


