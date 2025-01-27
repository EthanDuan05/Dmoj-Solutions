n = int(input())

L = []

cnt = 0
for i in range(n):
    num = int(input())
    if num not in L:
        L.append(num)
        cnt += 1
    elif num in L:
        continue
print(cnt)
