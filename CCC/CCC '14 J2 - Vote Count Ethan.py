k = int(input())
line = input()
a_n = 0
b_n = 0
for i in line:
    if i == 'A':
        a_n += 1
    if i == 'B':
        b_n += 1
if a_n > b_n:
    print('A')
elif b_n > a_n:
    print('B')
elif a_n == b_n:
    print('Tie')