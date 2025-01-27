line = input()
cnt = 0
for i in line:
    if i == ' ':
        continue
    else:
        cnt += 1

print(cnt)