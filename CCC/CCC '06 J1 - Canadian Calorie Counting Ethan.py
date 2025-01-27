B = 0
D = 0
S = 0
De = 0
b = int(input())
if b == 1:
    B = 461
if b == 2:
    B = 431
if b == 3:
    B = 420
if b == 4:
    B = B
s = int(input())
if s == 1:
    S = 100
if s == 2:
    S = 57
if s == 3:
    S = 70
if s == 4:
    S = S
d = int(input())
if d == 1:
    D = 130
if d == 2:
    D = 160
if d == 3:
    D = 118
if d == 4:
    D = D
de = int(input())
if de == 1:
    De = 167
if de == 2:
    De = 266
if de == 3:
    De = 75
if de == 4:
    De = De
t = B+S+D+De
print(f'Your total Calorie count is {t}.')
