L = ''
for i in range(7):
    part = input()
    L += part

while 'JJ' in L:
    L = L.replace('JJ', 'J')

print(L.count('J'))