ans = []

for _ in range(5):
    line = list(input())
    for i in range(5):
        ind = line.index('*')
        direction = input()
        if direction == 'R':
            if ind < len(line) - 1:
                line[ind], line[ind + 1] = line[ind + 1], line[ind]
            else:
                continue
        else:
            if ind >= 1:
                line[ind - 1], line[ind] = line[ind], line[ind - 1]
            else:
                continue

    ANS = ''
    for i in line:
        ANS += i
    ans.append(ANS)

for i in ans:
    print(i)