d = int(input())
s = int(input())
t_d = 0
for i in range(s):
    m = int(input())
    t_d = t_d + m
if t_d >= d:
    print('Roberta wins in', s, 'strokes.')
elif d == 5281:
    print(' Roberta acknowledges defeat.')
else:
    print(' Roberta acknowledges defeat.')