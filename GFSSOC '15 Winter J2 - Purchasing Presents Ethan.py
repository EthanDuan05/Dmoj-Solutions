n = int(input())
m = float(input())
P = 0
for i in range(n):
    p = float(input())
    P = P + p
if P <= m:
    k = m-P
    print("%.2f"%k)
if P > m:
    print("Fardin's broke")