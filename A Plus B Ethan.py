n = int(input())
a = []
for i in range(n):
    f, s = input().split()
    f = int(f)
    s = int(s)
    k = f + s
    a.append(k)

for m in a:
    print(m)