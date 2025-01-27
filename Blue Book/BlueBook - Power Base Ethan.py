T = int(input())

for _ in range(T):
    x, p = input().split()
    x = float(x)
    p = int(p)
    print('%.2f'%(x**p))