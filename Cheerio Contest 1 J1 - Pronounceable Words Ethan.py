word = input()
vowels = 'aeiou'

previous = '*'
flag = True
for i in word:
    if previous == '*':
        previous = i
    else:
        if previous in vowels:
            if i in vowels:
                flag = False
            else:
                previous = i
        else:
            if i not in vowels:
                flag = False
            else:
                previous = i

if flag:
    print('YES')
else:
    print('NO')
