Flag = True
TEM = []

while Flag:
    name, tem = input().split()
    tem = int(tem)
    TEM.append((tem, name))

    if name == 'Waterloo':
        Flag = False

TEM.sort()

print(TEM[0][1])
