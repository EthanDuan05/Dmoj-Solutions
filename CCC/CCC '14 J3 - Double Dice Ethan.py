n = int(input())
A = 100
D = 100
for i in range(n):
    a, d = map(int, (input()).split())
    a = int(a)
    d = int(d)
    if a > d:
        D = D-a
    if a < d:
        A = A-d
    if a == d:
        A = A
        D = D
print(A)
print(D)