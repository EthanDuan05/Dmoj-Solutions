line = list(input())
m = ''
s = ''

flag = False
for i in line:
    if i == ':':
        flag = True
    elif i != ':' and flag == False:
        m += i
    elif i != ':' and flag == True:
        s += i

print(int(m)*60 + int(s))