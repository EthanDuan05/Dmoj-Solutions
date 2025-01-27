SET = []

C = int(input())

ANS = []
for i in range(C):
    line = input()
    num = ''
    Object = ''

    if line != '4':
        line = line.split()
        num = line[0]
        Object = line[1]

    elif line == '4':
        num = '4'

    if num == '4':
        limit = len(SET)
        cnt = 0
        ans = ''
        while 'false' in SET:
            for K in SET:
                if K == 'false':
                    ans += str(K) + ' '
                    SET.remove(K)
        else:
            for K in SET:
                ans += str(K) + ' '
                SET.remove(K)
        M = len(ans)-1
        ANS.append(ans.strip(ans[M]))

    elif num == '1':
        if Object not in SET:
            SET.append(Object)
            ANS.append('true')
        else:
            ANS.append('false')
    elif num == '2':
        if Object in SET:
            SET.remove(Object)
            ANS.append('true')
        else:
            ANS.append('false')
    elif num == '3':
        if Object in SET:
            ind = SET.index(Object)
            ANS.append(ind)
        else:
            ANS.append(-1)

for i in ANS:
    print(i)