V = 'aeiouy'

line = input()
cnt = 0

for i in line:
    if i in V:
        cnt += 1

if cnt >= 2:
    print('good')
else:
    print('bad')