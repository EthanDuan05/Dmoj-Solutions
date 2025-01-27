k = int(input())
c = int(input())
d = int(input())
if k+c+d != 180:
    print('Error')
elif k == c == d == 60:
    print('Equilateral')
elif k == c or c == d or d ==k:
    print('Isosceles')
else:
    print('Scalene')