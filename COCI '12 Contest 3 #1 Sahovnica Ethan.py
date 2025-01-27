r, c = map(int, input().split())
a, b = map(int, input().split())

C = c*b

line1 = ''
curr = 'X'
while C:
    line1 += curr*b
    C -= b
    if curr == 'X':
        curr = '.'
    else:
        curr = 'X'

line2 = ''
for i in line1:
    if i == '.':
        line2 += 'X'
    else:
        line2 += '.'

R = r*a
previous = line1
while R:
    for i in range(a):
        print(previous)

    R -= a

    if previous == line1:
        previous = line2
    else:
        previous = line1

