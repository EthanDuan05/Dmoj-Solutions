L = []
n = int(input())
for i in range(n):
    a, p, s = input().split()
    a = int(a)
    p = int(p)
    s = int(s)
    if a * p == s:
        answer = 'POSSIBLE DOUBLE SIGMA'
        L.append(answer)
    elif a * p != s:
        answer = '16 BIT S/W ONLY'
        L.append(answer)

for i in L:
    print(i)