dic = {'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3',
       'f': '#', 'g': '6', 'h': '[-]', 'i': '|', 'j': '_|',
       'k': '|<', 'l': '1', 'm': '[]\/[]', 'n': '[]\[]', 'o': '0',
       'p': '|D', 'q': '(,)', 'r': '|Z', 's': '$', 't': "']['", 'u': '|_|',
       'v': '\/', 'w': '\/\/', 'x': '}{', 'y': '`/', 'z': '2'}


line = input()
line = line.lower()
list(line)

ans = ''
for i in line:
    if i in dic:
        ans += dic.get(i)
    else:
        ans += i
print(ans)