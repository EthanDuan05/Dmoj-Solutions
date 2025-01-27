n = int(input())
LINE = ['']*n

line = input().split()
num = input().split()

for i in range(n+1):
    for k in range(n-1):
        if num[k] > num[k + 1]:
            num[k], num[k + 1] = num[k + 1], num[k]
            line[k], line[k+1] = line[k+1], line[k]

ans = ''
for i in line:
    ans += i
print(ans)