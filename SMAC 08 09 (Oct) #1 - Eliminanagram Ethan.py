import sys

D = {}
a = input()
b = input()

for i in a:
    if i not in D:
        D[i] = 1
    else:
        D[i] += 1

for s in b:
    if s not in D:
        D[s] = 1
    else:
        D[s] += 1

for i in D:
    if D[i] % 2 != 0:
        print('No')
        sys.exit(0)

print('Yes')