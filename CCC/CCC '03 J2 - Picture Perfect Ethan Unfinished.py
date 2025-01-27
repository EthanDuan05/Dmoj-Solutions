import math
import sys

while True:
    num = int(input())
    if num == 0:
        sys.exit(0)
    a = math.sqrt(num)
    a = math.floor(a)
    if num % a == 0:
        b = num // a
    else:
        a = a - 1
        b = num // a
    perimeter = 2*(a+b)
    print('Minimum perimeter is', perimeter, 'with dimensions', a, 'x', b)