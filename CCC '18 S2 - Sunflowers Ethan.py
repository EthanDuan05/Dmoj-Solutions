import sys

N = int(input())

Grid = []
for i in range(N):
    P = list(map(int, input().split()))
    Grid.append(P)

def check(Grid):
    for i in range(N-1):
        if Grid[i][0] >= Grid[i+1][0]:
            return False

    for j in range(N):
        for s in range(N-1):
            if Grid[j][s] >= Grid[j][s+1]:
                return False

    return True

Debug = True
order = [0, 90, 180, 270]
new_grid = [[0 for i in range(N)] for j in range(N)]
ind = -1
Flag = True

if check(Grid):
    for i in Grid:
        print(' '.join(map(str, i)))
    sys.exit(0)

while Flag:
    if check(new_grid):
        Flag = False
    else:
        ind += 1
        if ind == 0:
            continue

        for j in range(N):
            for k in range(N):
                x = k
                y = j

                if ind == 1:
                    new = Grid[x][y]
                    new_grid[y][N - 1 - x] = new

                elif ind == 2:
                    new_grid[N - 1 - x][N - 1 - y] = Grid[x][y]

                elif ind == 3:
                    new_grid[N - 1 - y][x] = Grid[x][y]

for i in new_grid:
    print(' '.join(map(str, i)))

'''
new_grid = [[0 for i in range(N)] for j in range(N)]
ind = 2

for i in Grid:
    print(i)

for j in range(N):
    for k in range(N):
        x = k
        y = j

        if ind == 1:
            new = Grid[x][y]
            new_grid[y][N - 1 - x] = new

        elif ind == 2:
            new_grid[N - 1 - x][N - 1 - y] = Grid[x][y]

        elif ind == 3:
            new_grid[N - 1 - y][x] = Grid[x][y]


print('-----------')

for i in Grid:
    print(i)

print('-----------')

for i in new_grid:
    print(i)
'''