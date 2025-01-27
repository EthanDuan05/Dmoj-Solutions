n = int(input())
m = int(input())
cnt = 0
for i in range(1, n+1):
    for k in range(1, m+1):
        if i + k == 10:
            cnt += 1
if cnt == 1:
    print('There is', cnt, 'way to get the sum 10.')
if cnt > 1:
    print('There are', cnt, 'ways to get the sum 10.')
if cnt == 0:
    print('There are 0 ways to get the sum 10.')