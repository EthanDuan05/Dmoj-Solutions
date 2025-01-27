M = list(map(int, input().split()))
order = input()

L  = sorted(M)

a = L[0]
b = L[1]
c = L[2]

ans = []
for i in order:
    if i == 'A':
        ans.append(a)

    if i == 'B':
        ans.append(b)

    if i == 'C':
        ans.append(c)

print(' '.join(map(str, ans)))