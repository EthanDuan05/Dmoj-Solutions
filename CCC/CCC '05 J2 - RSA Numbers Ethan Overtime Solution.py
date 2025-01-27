n1 = int(input())
n2 = int(input())
L = []

for i in range(n1, n2+1):
    L.append(i)

t_c = 0
for k in L:
    nums = 0
    for s in range(0, k+1):
        for l in range(0, k+1):
            if s * l == k and s < l:
                nums += 2
    if nums == 4:
        t_c += 1
    else:
        t_c = t_c

print('The number of RSA numbers between', n1, 'and', n2, 'is', t_c)