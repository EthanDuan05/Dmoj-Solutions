t = input()
s = input()
line = []

for i in range(len(s)):
    line.append(s[i:]+s[:i])

y = False
for string in line:
    if string in t:
        y = True
        break

if y == False:
    print('no')
elif y == True:
    print('yes')