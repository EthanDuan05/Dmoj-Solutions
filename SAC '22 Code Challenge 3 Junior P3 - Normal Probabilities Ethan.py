import sys
M = sys.stdin.readline

P = 1

N = int(input())
for i in range(N):
    letter = input()
    if letter == 'A':
        P *= 1.0
    elif letter == 'B':
        P *= 0.8
    elif letter == 'C':
        P *= 0.6
    elif letter == 'D':
        P *= 0.4
    elif letter == 'E':
        P *= 0.2

print('%.6f'%P)