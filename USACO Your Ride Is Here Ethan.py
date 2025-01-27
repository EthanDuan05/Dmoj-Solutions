"""
ID: ethandu1
LANG: PYTHON3
PROG: ride
"""
D = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
     'e': 5, 'f': 6, 'g': 7, 'h': 8,
     'i': 9, 'j': 10, 'k': 11, 'l': 12,
     'm': 13, 'n': 14, 'o': 15, 'p': 16,
     'q': 17, 'r': 18, 's': 19, 't': 20,
     'u': 21, 'v': 22, 'w': 23, 'x': 24,
     'y': 25, 'z': 26}

line_1 = input().strip().lower()
line_2 = input().strip().lower()
sum_1 = 1
sum_2 = 1
for i in line_1:
    sum_1 *= D.get(i)
for i in line_2:
    sum_2 *= D.get(i)
if (sum_1 % 47) == (sum_2 % 47):
    print('GO')
else:
    print('STAY')
