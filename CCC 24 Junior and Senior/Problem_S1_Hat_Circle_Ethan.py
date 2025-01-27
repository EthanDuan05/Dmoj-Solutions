N = int(input())
Line = []

for _ in range(N):
     num = int(input())
     Line.append(num)

cycle = N // 2

cnt = 0
for i in range(N):
    if i + cycle < N:
        if Line[i] == Line[i + cycle]:
            cnt += 1
    elif i + cycle > N:
        if Line[i] == Line[i + cycle - N]:
            cnt += 1

    elif i + cycle == N:
        if Line[i] == Line[0]:
            cnt += 1

print(cnt)
# print(cycle)
# print(Line)