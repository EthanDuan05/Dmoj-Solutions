n1 = int(input())
n2 = int(input())

nums = 0

for x in range(n1, n2+1):
    cnt = 0
    for y in range(1, n2+1):
        if x % y == 0:
            cnt += 1
    if cnt == 4:
        nums += 1

print('The number of RSA numbers between', n1, 'and', n2, 'is', nums)