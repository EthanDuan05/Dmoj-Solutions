t = int(input())
m = {'A': '2', 'B': '2', 'C': '2',
     'D': '3', 'E': '3', 'F': '3',
     'G': '4', 'H': '4', 'I': '4',
     'J': '5', 'K': '5', 'L': '5',
     'M': '6', 'N': '6', 'O': '6',
     'P': '7', 'Q': '7', 'R': '7',
     'S': '7', 'T': '8', 'U': '8',
     'V': '8', 'W': '9', 'X': '9',
     'Y': '9', 'Z': '9'}

LL = ''

for i in range(t):
    L = []
    line = input()
    cnt = 0
    for s in line:
        if s == '-':
            continue
        elif s in m:
            L.append(m[s])
        elif s not in m:
            L.append(s)

        cnt += 1

        if cnt == 10:
            break

    L.insert(3, '-')
    L.insert(7, '-')

    for w in range(12):
        LL += L[w]

LLL = []

for i in range(t):
    LLL.append(LL[i*12:i*12+12])

for i in LLL:
    print(i)