dic = {'000': 0, '001': 1,
       '010': 2, '011': 3,
       '100': 4, '101': 5,
       '110': 6, '111': 7}

line = input()
k = len(line)

if k % 3 != 0:
    while k % 3 != 0:
        line = '0' + line
        k += 1

line = list(line)
ANS = []
while line:
    a = line.pop(0)
    b = line.pop(0)
    c = line.pop(0)
    ans = a + b + c
    ANS.append(dic[ans])

print(''.join(map(str, ANS)))
