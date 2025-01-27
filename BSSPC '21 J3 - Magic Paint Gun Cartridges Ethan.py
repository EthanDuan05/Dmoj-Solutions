import sys
input = sys.stdin.readline

D = {'R': ['red'],
     'U': ['blue'],
     'Y': ['yellow'],
     'O': ['red', 'yellow'],
     'G': ['blue', 'yellow'],
     'P': ['red', 'blue'],
     'B': ['red', 'blue', 'yellow']}

col, row = map(int, input().strip().split())
Graph = []

for _ in range(row):
    line = list(input())
    Graph.append(line)

R = 0
B = 0
Y = 0

for i in range(row):
    for j in range(col):
        if Graph[i][j] == '.':
            continue
        else:
            if j == 0:
                for C in D[Graph[i][j]]:
                    if C == 'red':
                        R += 1

                    if C == 'blue':
                        B += 1

                    if C == 'yellow':
                        Y += 1

            else:
                if Graph[i][j-1] == '.':
                    for C in D[Graph[i][j]]:
                        if C == 'red':
                            R += 1

                        if C == 'blue':
                            B += 1

                        if C == 'yellow':
                            Y += 1
                else:
                    for C in D[Graph[i][j]]:
                        if C in D[Graph[i][j-1]]:
                            continue

                        else:
                            if C == 'red':
                                R += 1

                            if C == 'blue':
                                B += 1

                            if C == 'yellow':
                                Y += 1

print(R, Y, B)

