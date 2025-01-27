N = int(input())

S = 10000
for _ in range(N):
    num = float(input())
    if num < S:
        S = num

print('%.2f'%(S))