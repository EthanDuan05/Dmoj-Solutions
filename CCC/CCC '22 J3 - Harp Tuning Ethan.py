L = "ABCDEFGHIJKLMNOPQRST"
N = '0123456789'

s = ''
t = input()
t = list(t)

n = []

for i in range(len(t)):
    if t[i] in L:
        if i > 1 and t[i-1] in N:
            n.append('*')
        n.append(t[i])
    else:
        n.append(t[i])

t = n

for i in t:
    s += i

s = s.replace('+', ' tighten ')
s = s.replace('-', ' loosen ')
s = s.replace('*', '\n')

print(s)