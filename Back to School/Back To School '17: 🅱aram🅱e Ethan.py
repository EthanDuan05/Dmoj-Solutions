line = list(input())

capital = ['A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

ans = ''
for i in range(len(line)):
    if line[i][0] in capital and i != 0:
        ans += '.' + line[i]
    else:
        ans += line[i]

ans = list(ans)
for i in range(len(ans)):
    if ans[i] == ' ' and ans[i+1] == '.':
        ans[i], ans[i+1] = ans[i+1], ans[i]

ANS = ''
for i in ans:
    ANS += i
ANS += '.'
print(ANS)
