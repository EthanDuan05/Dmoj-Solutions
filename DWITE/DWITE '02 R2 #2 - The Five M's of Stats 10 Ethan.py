N = int(input())
D = {}
Sum = 0
Max = -1000
Min = 1000
Median = 0
L = []
for i in range(N):
    num = float(input())
    if num > Max:
        Max = num

    if num < Min:
        Min = num

    if num not in D:
        D[num] = 1
    else:
        D[num] += 1

    Sum += num

    L.append(num)

L.sort()

print('%.2f'%(Sum/N))

if N % 2 == 0:
    print('%.2f'%((L[N//2 - 1] + L[N//2])/2))
else:
    print('%.2f'%(L[N//2]))

for i in D:
    if D[i] == max(D.values()):
        print('%.2f'%(i))
        break
print('%.2f'%(Max))
print('%.2f'%(Min))
