mode = input()
line1 = list(map(float, input().split()))
line2 = list(map(float, input().split()))

if mode == 'Multiply':
    ans = []
    for i in range(len(line1)):
        a = line1[i] * line2[i]
        a = '%.7f'%a
        ans.append(a)
    print(' '.join(map(str, ans)))

elif mode == 'Screen':
    ans = []
    for i in range(len(line1)):
        a = 1-(1-line1[i])*(1-line2[i])
        a = '%.7f' % a
        ans.append(a)
    print(' '.join(map(str, ans)))

elif mode == 'Overlay':
    ans = []
    for i in range(len(line1)):
        if line2[i] <= 0.5:
            a = 2*line1[i]*line2[i]
            a = '%.7f'%a
            ans.append(a)
        else:
            a = 1 - 2 * (1 - line1[i]) * (1 - line2[i])
            a = '%.7f'%a
            ans.append(a)
    print(' '.join(map(str, ans)))