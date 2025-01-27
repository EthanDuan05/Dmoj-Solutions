left_pinky = ['1', 'Q', 'A', 'Z']
left_ring = ['2', 'W', 'S', 'X']
left_middle = ['3', 'E', 'D', 'C']
left_index = ['4', 'R', 'F', 'V',
              '5', 'T', 'G', 'B']

right_index = ['6', 'Y', 'H', 'N',
               '7', 'U', 'J', 'M']
right_middle = ['8', 'I', 'K', ',']
right_ring = ['9', 'O', 'L', '.']
right_pinky = ['0', 'P', ';', '/',
               '-', '=', '[', ']',
               "'"]

left = ['1', 'Q', 'A', 'Z', '2', 'W', 'S', 'X',
        '3', 'E', 'D', 'C', '4', 'R', 'F', 'V',
        '5', 'T', 'G', 'B']

right = ['6', 'Y', 'H', 'N', '7', 'U', 'J', 'M',
         '8', 'I', 'K', ',', '9', 'O', 'L', '.',
         '0', 'P', ';', '/', '-', '=', '[', ']',
         "'"]


def findwhich(x):
    if x in left:
        return 'left'
    elif x in right:
        return 'right'


def findfinger_left(x):
    if x in left_pinky:
        return 0
    elif x in left_ring:
        return 1
    elif x in left_middle:
        return 2
    elif x in left_index:
        return 3


def findfinger_right(x):
    if x in right_index:
        return 4
    elif x in right_middle:
        return 5
    elif x in right_ring:
        return 6
    elif x in right_pinky:
        return 7


frequency = [0]*8

line = list(input())
for i in line:
    if findwhich(i) == 'left':
        ind = findfinger_left(i)
        frequency[ind] += 1
    elif findwhich(i) == 'right':
        ind = findfinger_right(i)
        frequency[ind] += 1

for i in frequency:
    print(i)