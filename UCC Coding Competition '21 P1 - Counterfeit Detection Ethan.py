line = input()

cnt = 0
for i in range(len(line)):
    if i < len(line) - 1:
        if line[i] == '2':
            if line[i+1] == '5':
                continue
            else:
                cnt += 1
    elif line[i] == '2':
        cnt += 1
print(cnt)