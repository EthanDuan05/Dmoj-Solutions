standard = [1, 1, 2, 2, 2, 8]
compare = [0]*6

ans = []
line = list(map(int, input().split()))
for i in range(6):
    compare[i] += line[i]

for i in range(6):
    if compare[i] == standard[i]:
        ans.append(0)
    elif compare[i] < standard[i]:
        ans.append(standard[i]-compare[i])
    else:
        ans.append(standard[i]-compare[i])

ANS = ''
for i in range(6):
    if i < 5:
        ANS += str(ans[i]) + ' '
    else:
        ANS += str(ans[i])
print(ANS)