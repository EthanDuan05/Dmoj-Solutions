n = int(input())
t = 0
l = 0
for i in range(n):
    k = int(input())
    if k < -k:
        l = -k
        t = t +l
    elif k > -k:
        l = k
        t = t + l
print(t)