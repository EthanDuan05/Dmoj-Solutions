line_1 = list(input())
line_2 = list(input())

for i in reversed(range(len(line_1))):
    for j in reversed(range(len(line_2))):
        if line_1[i] == line_2[j]:
            line_1.pop(i)
            line_2.pop(j)
            break

for i in reversed(range(len(line_2))):
    if line_2[i] == '*':
        line_2.pop(i)
        line_1.pop()

if (len(line_2) and len(line_1)) == 0:
    print('A')
else:
    print('N')