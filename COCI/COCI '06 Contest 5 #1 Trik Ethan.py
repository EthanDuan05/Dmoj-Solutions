L = 'a'
M = 'b'
R = 'c'
l = input()
b_l = 'a'
f_b = 0
for i in l:
    if i == 'A':
        if b_l == 'a':
            b_l = 'b'
        elif b_l == 'b':
            b_l = 'a'
    elif i == 'B':
        if b_l == 'b':
            b_l = 'c'
        elif b_l == 'c':
            b_l = 'b'
    elif i == 'C':
        if b_l == 'c':
            b_l = 'a'
        elif b_l == 'a':
            b_l = 'c'

if b_l == 'a':
    f_b = 1
if b_l == 'b':
    f_b = 2
if b_l == 'c':
    f_b = 3
print(f_b)