n, a, b = map(int, input().split())
list_a = [0]*n
list_b = [0]*n

for i in range(n):
    andrew, tommy = map(int, input().split())
    list_a[i] += andrew
    list_b[i] += tommy

cnt_a = 0
for i in list_a:
    if i < a:
        cnt_a += 1
    else:
        cnt_a += 2

cnt_b = 0
for i in list_b:
    if i < b:
        cnt_b += 1
    else:
        cnt_b += 2

if cnt_a < cnt_b:
    print('Andrew wins!')
elif cnt_a > cnt_b:
    print('Tommy wins!')
else:
    print('Tie!')