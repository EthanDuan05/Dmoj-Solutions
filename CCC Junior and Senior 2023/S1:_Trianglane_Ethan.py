import sys
input = sys.stdin.readline

C = int(input())

Line_1 = list(map(int, input().split()))
Line_2 = list(map(int, input().split()))

sides_1 = []
sides_2 = []

debug = False

cnt = 0
# 0 represents middle, -1 represents left, 1 represents right
for i in range(C):
    if Line_1[i] == 1:
        if (i+1) % 2 != 0:
            sides_1.append((i + 1, 'middlelower'))
        else:
            sides_1.append((i + 1, 'middleupper'))

        if (i, 'right') not in sides_1:
            sides_1.append((i + 1, 'left'))  # left
        elif (i, 'right') in sides_1:
            sides_1.remove((i, 'right'))

        sides_1.append((i + 1, 'right'))  # right
        cnt += 1

for i in range(C):
    if Line_2[i] == 1:
        if (i+1) % 2 != 0:
            if (i + 1, 'middlelower') not in sides_1:
                sides_2.append((i + 1, 'middleupper'))  # middle

            elif (i + 1, 'middlelower') in sides_1:
                sides_1.remove((i + 1, 'middlelower'))
        else:
            sides_2.append((i + 1, 'middlelower'))

        if (i, 'right') not in sides_2:
            sides_2.append((i + 1, 'left'))  # left
        elif (i, 'right') in sides_2:
            sides_2.remove((i, 'right'))

        sides_2.append((i + 1, 'right'))  # right

if debug:
    print(sides_1)
    print(sides_2)

print(len(sides_1) + len(sides_2))

