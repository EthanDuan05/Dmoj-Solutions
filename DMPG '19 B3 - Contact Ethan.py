line = list(input())
line.append('R')
K = int(input())

stack = []
last = ''
cnt = 0

for i in line:
    if i == 'S':
        cnt += 1
    elif i != 'S':
        if last == 'S':
            stack.append(cnt)
            cnt = 0
    last = i

flag = True
for i in stack:
    if i >= K:
        flag = False

if flag:
    print('All good')
else:
    print('Spamming')