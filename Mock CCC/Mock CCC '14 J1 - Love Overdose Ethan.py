import sys

A = int(input())
B = int(input())
R = int(input())

if A > R:
    print('Bob overdoses on day 1.')
    sys.exit(0)
else:
    if A / 2 + B > R:
        print('Bob overdoses on day 2.')
    else:
        print('Bob never overdoses.')