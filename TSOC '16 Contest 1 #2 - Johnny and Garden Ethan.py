line = input()
if '.' in line:
    line = list(line.split('.'))
    a = line[0]
    b = line[1]
    b = b.lower()
    print('"' + a + '"' + ' ' + '-' + ' ' + b)
elif '.' not in line:
    line_2 = input()
    line_2 = line_2.lower()
    print('"' + line + '"' + ' ' + '-' + ' ' + line_2)