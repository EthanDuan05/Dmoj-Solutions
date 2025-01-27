import math
pi = math.pi

R = int(input())

ans1 = pi * (R**2)
print(round(ans1, 6))

ans2 = 2*R**2
print(format(ans2, '.6f'))