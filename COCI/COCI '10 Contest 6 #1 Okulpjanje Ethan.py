a, b = map(int, input().split())
line = input().split()

ANS = ''
for i in range(5):
    ans = int(line[i]) - (a*b)
    if i < 4:
        ANS += str(ans) + ' '
    else:
        ANS += str(ans)

print(ANS)