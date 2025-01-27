line = input().split()
L = ''
for i in line:
    if i == '=':
        break
    elif i == 'P':
        L += '+'
    elif i == 'M':
        L += '-'
    else:
        L += i

print(eval(L))