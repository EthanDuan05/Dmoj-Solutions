Map = [['*', '*', '*', '*', '*', '*', '*', '*'],
       ['*', 'A', 'B', 'C', 'D', 'E', 'F', '*'],
       ['*', 'G', 'H', 'I', 'J', 'K', 'L', '*'],
       ['*', 'M', 'N', 'O', 'P', 'Q', 'R', '*'],
       ['*', 'S', 'T', 'U', 'V', 'W', 'X', '*'],
       ['*', 'Y', 'Z', ' ', '-', '.', 'enter', '*'],
       ['*', '*', '*', '*', '*', '*', '*', '*']]

def index(I):
    for row in range(7):
        if I in Map[row]:
            y = Map[row].index(I)
            x = row
            return x, y

string = list(input())

x_cor = 1
y_cor = 1
total = 0
while string:
    i = string.pop(0)
    x1, y1 = index(i)
    total += abs(x_cor-x1) + abs(y_cor-y1)
    x_cor = x1
    y_cor = y1

total += abs(5 - x_cor) + (6 - y_cor)
print(total)