n = int(input())
m = int(input())
a = []
no =[]
for i in range(n):
    A = input()
    a.append(A)
for k in range(m):
    N = input()
    no.append(N)

for l in a:
    for t in no:
        print(l, 'as', t)