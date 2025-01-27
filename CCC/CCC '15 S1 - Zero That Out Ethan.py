n = int(input())
L = []
for i in range(n):
    num = int(input())
    if num > 0:
        L.append(num)
    else:
        L.pop()

total = 0
for i in range(len(L)):
    total += L[i]

print(total)