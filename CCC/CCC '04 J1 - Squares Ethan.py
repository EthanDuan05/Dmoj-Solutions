area = int(input())
L = []
for i in range(1, area + 1):
    if i ** 2 <= area:
        L.append(i)

cnt = 0
for i in L:
    if int(i) >= cnt:
        cnt = int(i)
print('The largest square has side length %i.' % cnt)
