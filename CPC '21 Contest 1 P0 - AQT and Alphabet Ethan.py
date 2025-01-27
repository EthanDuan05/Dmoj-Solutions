Alphabets = ['a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p',
             'q', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

line = input()
for i in Alphabets:
    if i in line:
        continue
    elif i not in line:
        print(i)
        break
