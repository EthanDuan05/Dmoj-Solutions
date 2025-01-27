S = input()
S += 'a'

L = []
C = ''
for i in S:
    if i.isalpha():
        L.append(C)
        C = ''
        continue
    else:
        C += i

cnt = 0
used = []
for i in L:
    if i != '' and i not in used:
        cnt += 1
        used.append(i)

print(cnt)
