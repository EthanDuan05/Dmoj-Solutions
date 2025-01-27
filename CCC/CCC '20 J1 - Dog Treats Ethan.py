S = int(input())  # the number of small treats
M = int(input())  # the number of medium treats
L = int(input())  # the number of large treats
score = 1*S + 2*M + 3*L
if score >= 10:
    print('happy')
if score < 10:
    print('sad')