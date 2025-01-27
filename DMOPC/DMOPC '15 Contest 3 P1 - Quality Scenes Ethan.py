a = int(input())
b = int(input())
c = int(input())
d = int(input())

L_1 = []
L_2 = []

for i in range(a+1, b):
    L_1.append(i)

for i in range(c+1, d):
    L_2.append(i)

if len(L_1) == 0 and len(L_2) == 0:
    if a == b == c == d:
        print('YES')
    elif c < b:
        print('YES')
    else:
        print('NO')
else:
    for i in L_1:
        if i in L_2:
            print('YES')
            break
    else:
        print('NO')