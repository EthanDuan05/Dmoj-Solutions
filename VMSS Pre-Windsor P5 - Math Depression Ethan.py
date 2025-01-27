'''
2 = 1*1 = 1
3 = 1*1*1 = 1
  = 1*2 = 2
4 = 1*1*1*1 = 1
  = 2*2 = 4
5 = 1*4 = 4
  = 2*3 = 6
6 = 2*2*2 = 8
  = 3*3 = 9
7 = 1*6 = 6
  = 1*3*3 = 9
  = 2*5 = 10
  = 3*2*2 = 12
8 = 2*2*4 = 16
  = 4*4 = 16
  = 2*3*3 = 18
10 = 3*3*3*1= 27
   = 3*3*2*2 = 36
12 = 2*3*2*3*2 = 72
   = 3*3*3*3 = 81
   = 2*2*2*2*2*2 = 64
'''
import sys

num = int(input())
factor_3 = num // 3
remainder = num % 3

if num == 2:
    print(1)
    sys.exit(0)

if num == 3:
    print(2)
    sys.exit(0)

if remainder == 1:
    factor_3 -= 1
    remainder += 3

factor_2 = remainder // 2
ans = 3**factor_3*2**factor_2
m = int(1e9) + 7
print(ans % m)

# print(factor_3)
# print(factor_2)