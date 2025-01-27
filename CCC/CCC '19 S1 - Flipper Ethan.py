line = input()
i_1 = [1, 2]
i_2 = [3, 4]
for i in range(len(line)):
    if line[i] == 'H':
        i_1, i_2 = i_2, i_1
    elif line[i] == 'V':
        i_1[0], i_1[1] = i_1[1], i_1[0]
        i_2[0], i_2[1] = i_2[1], i_2[0]

as_1 = ''
as_2 = ''
for i in i_1:
    as_1 += str(i)+' '
for i in i_2:
    as_2 += str(i)+' '

print(as_1)
print(as_2)