line = map(int, input())
L = []
for i in line:
    if i == 0:
        L.append(10)
    else:
        L.append(i)

flag = True
for i in range(5):
    if abs(int(L[i+1]) - int(L[i])) == 1:
        continue
    else:
        flag = False
        break

if flag:
    print('VALID')
else:
    print('INVALID')