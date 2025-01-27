N = int(input())
L = []

for _ in range(N):
    word = input()
    L.append(word)

L.sort()

last = ''

for i in L:
    if last == '':
        print(i, end='')
    else:
        if i[0] == last[0]:
            print(', ' + i, end='')
        else:
            print('')
            print(i, end='')

    last = i