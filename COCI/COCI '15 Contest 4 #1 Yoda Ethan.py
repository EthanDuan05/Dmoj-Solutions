a = input()
b = input()

if len(a) != len(b):
    if len(a) > len(b):
        diff = len(a) - len(b)
        for _ in range(diff):
            b = '0' + b
    else:
        diff = len(b) - len(a)
        for _ in range(diff):
            a = '0' + a

ans_a = ''
ans_b = ''

for i in range(len(a)):
    if int(a[i]) > int(b[i]):
        ans_a += a[i]
    elif int(a[i]) < int(b[i]):
        ans_b += b[i]
    else:
        ans_a += a[i]
        ans_b += b[i]

if len(ans_a) == 0:
    print('YODA')
else:
    print(int(ans_a))

if len(ans_b) == 0:
    print('YODA')
else:
    print(int(ans_b))