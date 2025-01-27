d = int(input())
e = int(input())
w = int(input())
a_d = max(0.25*(d-100), 0)
a_e = 0.15*e
a_w = 0.2*w
a = a_d+a_e+a_w
b_d = max(0.45*(d-250), 0)
b_e = 0.35*e
b_w = 0.25*w
b = b_d+b_e+b_w
a = '{:.2f}'.format(a)
b = '{:.2f}'.format(b)
print('Plan A costs', a)
print('Plan B costs', b)
if a > b:
    print('Plan B is cheapest.')
if a < b:
    print('Plan A is cheapest.')
if a == b:
    print('Plan A and B are the same price.')