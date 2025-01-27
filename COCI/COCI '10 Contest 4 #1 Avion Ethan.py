L = []
for i in range(5):
    line = input()
    L.append(line)

ans = []
for s in range(5):
    if 'FBI' in L[s]:
        ans.append(s+1)

P = ''
if len(ans) > 0:
    for i in range(len(ans)):
        r = len(ans) - 1
        if i < r:
            P += str(ans[i]) + ' '
        else:
            P += str(ans[i])
    print(P)
elif len(ans) == 0:
    print('HE GOT AWAY!')