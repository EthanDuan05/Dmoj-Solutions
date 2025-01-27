N, M = map(int, input().split())

line = list(map(int, input().split()))

can = []
cant = []

for i in line:
    if i >= M:
        can.append(i)
    else:
        cant.append(i)

cnt = 0

while can:
    can.pop(0)
    if len(cant) > 0:
        cant.pop(0)
        cnt += 2
    else:
        cnt += 1

print(cnt)