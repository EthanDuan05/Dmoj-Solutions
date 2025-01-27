line = list(input())
K = int(input())

current_consecutive = 0

Flag = True
last = line[0]
for i in range(1, len(line)):
    if (line[i] and last) == 'S':
        if current_consecutive == 0:
            current_consecutive += 2
        else:
            current_consecutive += 1
        if current_consecutive >= K:
            Flag = False
            last = line[i]
            break
        else:
            last = line[i]
    else:
        if current_consecutive >= K:
            Flag = False
            last = line[i]
            break
        else:
            last = line[i]
            current_consecutive = 0

    if i == len(line)-1:
        if (line[i] and last) == 'S':
            if current_consecutive > 0:
                current_consecutive += 1
            else:
                current_consecutive += 2
            if current_consecutive >= K:
                Flag = False
                break

if current_consecutive >= K:
    Flag = False

if Flag:
    print('All good')
else:
    print('Spamming')
