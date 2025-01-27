a = int(input())
b = int(input())
T = int(input())

cnt = 0
for i in range(0, T):
    if i % a == 0 and i % b == 0:
        cnt += 1

print(cnt)