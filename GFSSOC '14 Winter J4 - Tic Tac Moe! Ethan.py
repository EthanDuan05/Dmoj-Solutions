Graph = []

for _ in range(3):
    line = input()
    Graph.append(line)

O = False
X = False

# vertical
if Graph[0][0] == Graph[1][0] == Graph[2][0]:
    if Graph[0][0] == 'O':
        O = True
    elif Graph[0][0] == 'X':
        X = True

if Graph[0][1] == Graph[1][1] == Graph[2][1]:
    if Graph[0][1] == 'O':
        O = True
    elif Graph[0][1] == 'X':
        X = True

if Graph[0][2] == Graph[1][2] == Graph[2][2]:
    if Graph[0][2] == 'O':
        O = True
    elif Graph[0][2] == 'X':
        X = True

# horizontal
if Graph[0][0] == Graph[0][1] == Graph[0][2]:
    if Graph[0][0] == 'O':
        O = True
    elif Graph[0][0] == 'X':
        X = True

if Graph[1][0] == Graph[1][1] == Graph[1][2]:
    if Graph[1][0] == 'O':
        O = True
    elif Graph[1][0] == 'X':
        X = True

if Graph[2][0] == Graph[2][1] == Graph[2][2]:
    if Graph[2][0] == 'O':
        O = True
    elif Graph[2][0] == 'X':
        X = True

# diagonal
if Graph[0][0] == Graph[1][1] == Graph[2][2]:
    if Graph[0][0] == 'O':
        O = True
    elif Graph[0][0] == 'X':
        X = True

if Graph[0][2] == Graph[1][1] == Graph[2][0]:
    if Graph[0][2] == 'O':
        O = True
    elif Graph[0][2] == 'X':
        X = True

if O and X:
    print('Error, redo')
elif O:
    print('Griffy')
elif X:
    print('Timothy')
else:
    print('Tie')