N = int(input())
L = []

nums_wa = 0

for _ in range(N):
    state = input()
    L.append(state)
    if state == 'WA':
        nums_wa += 1

limit_wa = (nums_wa*0.3)//1
accumulated_wa = 0
accumulated_ir = 0

ans = []
for i in L:
    if i == 'WA':
        if accumulated_wa < limit_wa:
            ans.append('AC')
            accumulated_wa += 1
        else:
            ans.append('WA')
    elif i == 'AC':
        ans.append('AC')
    elif i == 'TLE':
        ans.append('WA')
    elif i == 'IR':
        if accumulated_ir < 10:
            ans.append('AC')
            accumulated_ir += 1
        elif 10 <= accumulated_ir < 20:
            ans.append('WA')
            accumulated_ir += 1
        else:
            ans.append('IR')

for i in ans:
    print(i)