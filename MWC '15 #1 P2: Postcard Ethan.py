r, c = map(int, input().split())
L = []

debug = False

min_x = 1001
min_y = 1001

max_x = 0
max_y = 0

for j in range(r):
    line = input().split()
    for h in range(c):
        if line[h] == '*':
            if h < min_x:
                min_x = h

            if j < min_y:
                min_y = j

            if h > max_x:
                max_x = h

            if j > max_y:
                max_y = j

    L.append(line)

if debug:
    print(min_x, max_x)
    print(min_y, max_y)

for s in range(min_y, max_y+1):
    print(' '.join((L[s][min_x:max_x+1])))
