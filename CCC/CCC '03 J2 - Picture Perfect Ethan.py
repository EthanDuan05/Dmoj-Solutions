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
        b = 0
        for i in range(1, a+1):
            if num % i == 0:
                if i > b:
                    b = i
                    a = num // i

    perimeter = 2*(a+b)
    print('Minimum perimeter is', perimeter, 'with dimensions', b, 'x', a)