N = int(input())
line = list(input().strip())

debug = True
state = True
last = ''
Occured = []
Group = []

for i in range(N):
    if i == 0:
        last = line[i]
        Group.append(line[i])
        continue
    else:
        if last == line[i]:
            Group.append(line[i])
            last = line[i]
        else:
            if len(Group) > 1:
                if line[i] not in Occured:
                    last = line[i]
                    Group = []
                    continue
                else:
                    state = False
                    break
            else:
                if debug: print(line[i], i, print(Group))
                state = False
                break

    # print(Group)

if state:
    print('Organized')
else:
    print('FIX YOUR BEADS!')
