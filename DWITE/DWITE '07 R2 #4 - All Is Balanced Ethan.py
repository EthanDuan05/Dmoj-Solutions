symbol = {'(': ')',
          '[': ']',
          '{': '}'}

for _ in range(5):
    line = list(input())
    stack = []
    state = True
    for i in line:
        if i in symbol.keys():
            stack.append(i)
        elif i in symbol.values():
            if len(stack) == 0:
                state = False
                break
            else:
                last = stack.pop(-1)
                if symbol[last] == i:
                    continue
                else:
                    state = False
                    break

    if len(stack) > 0:
        state = False

    if state:
        print('balanced')
    else:
        print('not balanced')
