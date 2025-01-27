line1 = list(input())
line2 = list(input())
line3 = list(input())

D = {}

for i in range(len(line2)):
    a = line2[i]
    b = line1[i]
    if a not in D:
        D[a] = b
    else:
        continue

for i in D:
    line2.remove(i)
    line1.remove(D[i])

if (len(line1) == len(line2)) == 1:
    D[line2[0]] = line1[0]

ans = []
for i in line3:
    if i in D:
        ans.append(D[i])
    else:
        ans.append('.')

print(''.join(ans))