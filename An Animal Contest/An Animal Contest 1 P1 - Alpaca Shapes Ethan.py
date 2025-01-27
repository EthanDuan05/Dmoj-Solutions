s,c = input().split()
s = int(s)
c = int(c)
s_a = s**2
c_a = 3.14*c**2
if c_a > s_a:
    print('CIRCLE')
elif c_a < s_a:
    print('SQUARE')