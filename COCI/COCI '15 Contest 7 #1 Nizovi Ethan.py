S = input()

ind = -1
current_indent = 0

for i in S:
    ind += 1
    if i == '{':
        print('{')
        current_indent += 2

        if S[ind+1] != '}':
            print(current_indent * ' ', end= '')

    elif i == '}':
        current_indent -= 2

        if S[ind-1] == '{':
            print(' '*current_indent + '}', end='')
        else:
            print('\n' + ' '*current_indent + '}', end='')

    elif i == ',':
        print(',')
        print(current_indent * ' ', end='')

    else:
        print(i, end='')
print()