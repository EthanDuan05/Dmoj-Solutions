N = int(input())
line = input()
line += '*'

L = []
segment = ''
last = ''
for i in range(N+1):
    if i == 0:
        last = line[i]
        segment += last
    else:
        if line[i] == last:
            segment += line[i]
            last = line[i]
        else:
            L.append(segment)
            segment = line[i]
            last = line[i]

Flag = True
used = []
for i in L:
    if i[0] not in used:
        used.append(i[0])
        continue
    else:
        Flag = False
        print('FIX YOUR BEADS!')
        break

if Flag:
    print('Organized')