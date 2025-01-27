t = 0
n = int(input())
for i in range(n):
    s = int(input())
    f = int(input())
    if s*5-f*3 > 40:
        t = t+1
if t == n:
    print(f'{t}+')
elif t:
    print(t)