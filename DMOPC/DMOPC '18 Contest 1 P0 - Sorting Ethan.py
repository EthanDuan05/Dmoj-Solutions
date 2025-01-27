a = int(input())
b = int(input())
c = int(input())

M = []
L = []
L.append(a)
L.append(b)
L.append(c)
M.append(a)
M.append(b)
M.append(c)

L.sort()

flag = True
for i in range(3):
    if L[i] == M[i]:
        continue
    else:
        flag = False
        break

if not flag:
    print('Try again!')
else:
    print('Good job!')
