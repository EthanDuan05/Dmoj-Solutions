N = int(input())
sw = list(input().split())
se = list(input().split())

s_w = 0
s_e = 0

L = []

for i in range(0, N):
    s_w += int(sw[i])
    s_e += int(se[i])
    if s_w == s_e:
        L.append(i+1)
    else:
        L.append(0)

initial = 0
for k in L:
    if int(k) >= initial:
        initial = int(k)
    elif int(k) < initial:
        initial = initial
print(initial)