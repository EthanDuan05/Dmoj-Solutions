R = int(input())
Logs = input()

M = Logs.replace('X', '*')

L = ['']*(R+1)

for i in range(R):
    if M[i] == '*':
        L[i] += '*'
    if M[i] == 'O':
        L[i] += 'O'
    if i == R-1:
        L[R] += '*'

k = []

ll = ''
for m in L:
    if m != '*':
        ll += m
    if m == '*':
        k.append(ll)
        ll = ''

P = []
for i in k:
    if len(i) == 0:
        continue
    else:
        P.append(i)

print(len(P))
for i in P:
    print(i)