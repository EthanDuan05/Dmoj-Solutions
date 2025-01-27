n = int(input())
l = []
for i in range(n):
    num = int(input())
    if num != 2:
        l.append(num-1)
    elif num == 2:
        l.append(num)
for i in l:
    print(i)