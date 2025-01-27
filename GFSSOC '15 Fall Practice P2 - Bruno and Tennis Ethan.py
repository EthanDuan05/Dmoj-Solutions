import sys

N = int(input())

lob_flag = False
bruno_flag = False
last = ''
ind = 0

cnt = 0
for i in range(N):
    ind += 1
    Round = input()

    if Round == 'lob':
        lob_flag = True

    if ind % 2 != 0:
        last = Round
    else:
        if last == 'lob' and Round == 'lob':
            bruno_flag = True
        else:
            bruno_flag = False

if not lob_flag:
    print('Not enough information')
    sys.exit(0)

if lob_flag:
    if bruno_flag:
        print('Possible Bruno')
    else:
        print('BruNO')


