m = []
n = int(input())
line = input().split()
for i in range(n):
    if i >= 1 and int(line[i]) < int(line[i-1]):
        line[i], line[i-1] = line[i-1], line[i]
        ppp = ''
        for o in line:
            ppp += o + ' '
        print(ppp)
        m.append(line)

    else:
        ppp = ''
        for o in line:
            ppp += o + ' '
        print(ppp)
        m.append(line)

for s in range(len(m[n-1])):
    if s >= 1 and int(m[n-1][s]) < int(m[n-1][s-1]):
        (m[n - 1][s]), (m[n - 1][s - 1]) = (m[n - 1][s - 1]), (m[n - 1][s])
        xxx = ''
        for x in (m[n-1]):
            xxx += x + ' '
        print(xxx)
