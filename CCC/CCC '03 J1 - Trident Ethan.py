t = int(input())
s = int(input())
h = int(input())
t_l = ''
s_l = '*' + s * '*' + '*' + s * '*' + '*'
h_l = ''

for i in range(t):
    if i != t-1:
        line = '*' + s * ' ' + '*' + s * ' ' + '*' + '\n'
        t_l += line
    elif i == t-1:
        line = '*' + s * ' ' + '*' + s * ' ' + '*'
        t_l += line

for k in range(h):
    if k != h-1:
        line = (s+1)*' ' + '*' + '\n'
        h_l += line
    elif k == h-1:
        line = (s + 1) * ' ' + '*'
        h_l += line

if t == 0:
    if s == 0:
        if h == 0:
            print(s_l)
else:
    print(t_l)
    print(s_l)
    print(h_l)