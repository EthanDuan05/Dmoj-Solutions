line = input()
line = line.replace(' ', "*")
line += '*'

L = []
word = ''
for i in line:
    if i != '*':
        word += i
    elif i == '*':
        L.append(word)
        word = ''

for i in range(len(L)):
    pre = L[0]
    back = L[1]
    if len(pre) == 3 and len(back) == 7:
        if pre == '416' or pre == '647' or pre == '437':
            if pre == '416':
                print('valuable')
            else:
                print('valueless')
        else:
            print('invalid')
    elif len(pre) != 3 or len(back) != 7:
        print('invalid')
    break