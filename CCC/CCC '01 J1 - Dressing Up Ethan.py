H = int(input())

for i in range(1, H+1, +2):
    row_1 = (i * '*') + (2 * H - 2 * i) * ' ' + (i * '*')
    print(row_1)
for i in range(H-2, 0, -2):
    row_1 = (i * '*') + (2 * H - 2 * i) * ' ' + (i * '*')
    print(row_1)