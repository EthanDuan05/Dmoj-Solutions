n = int(input())
line = input().split()
cnt = 0
for i in line:
    if int(i) > 0:
        cnt += 1
print(cnt)