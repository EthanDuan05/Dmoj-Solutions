N = int(input())
names = []
cnt = 0
for _ in range(N):
    name = input()
    if name not in names:
        names.append(name)

M = int(input())
for _ in range(M):
    name = input()
    if name not in names:
        names.append(name)
    else:
        cnt += 1
print(cnt)