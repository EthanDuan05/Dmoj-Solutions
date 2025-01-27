n = int(input())

L_f = []
L_s = []

line = input()
for s in line:
    L_f.append(s)
line_s = input()
for s in line_s:
    L_s.append(s)

cnt = 0
for k in range(0, n):
    if L_f[k] == L_s[k] and L_f[k] == 'C':
        cnt += 1
    elif L_f[k] != L_s[k]:
        cnt += 0

print(cnt)