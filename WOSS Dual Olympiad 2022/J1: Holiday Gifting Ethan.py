N = int(input())
A, B, C = map(int, input().split())
total = A + 4*B + 7*C
if total <= N:
    print('Time to go shopping!')
else:
    print('You cannot afford them all.')