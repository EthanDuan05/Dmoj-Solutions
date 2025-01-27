p = int(input())
m = -100000000
for i in range(p):
    f = float(input())
    if f > m:
        m = f
print(format(m, '.4f'))