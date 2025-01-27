line = input()
a = 'pusheen'

cnt = 0
for i in range(7):
    if line[i] != a[i]:
        cnt += 1
print(cnt)