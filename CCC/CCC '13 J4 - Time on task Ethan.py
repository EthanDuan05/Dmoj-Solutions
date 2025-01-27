T = int(input())

L = []
N = int(input())
for i in range(N):
    num = int(input())
    L.append(num)

L.sort()
counter = 0
sum = 0

flag = True
while flag:
    for i in L:
        if sum + i <= T:
            counter += 1
            sum += i
        elif sum + i > T:
            break
    flag = False

print(counter)
