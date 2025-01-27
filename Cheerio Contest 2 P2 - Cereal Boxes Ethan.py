import sys

input = sys.stdin.readline

M, C, I, Q = map(int, input().split())

current = C
total = 0

while True:
    if Q - current * M < 0:
        total += Q // current
        break
    else:
        Q -= current * M
        total += M
        current += I

print(total)
