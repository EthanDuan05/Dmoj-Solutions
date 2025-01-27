import sys
input = sys.stdin.readline

N = int(input())
L_r = []
frequency = [0]*N

distinct = False
repeat = False

Line = list(map(int, input().split()))
Line.sort()

for i in range(len(Line)):
    frequency[Line[i]-1] += 1

for s in range(len(Line) - 1):
    if s >= 1:
        if (Line[s - 1] != Line[s]) and (Line[s] != Line[s + 1]):
            distinct = True
        else:
            distinct = False
            break

for i in range(len(frequency)):
    if frequency[i] == 1:
        repeat = True
    else:
        repeat = False
        break

if distinct and repeat:
    print('YES')
else:
    print('NO')