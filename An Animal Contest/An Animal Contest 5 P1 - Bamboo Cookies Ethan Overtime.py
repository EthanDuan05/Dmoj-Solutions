n = int(input())
line = input().split()

k = []
cnt = 0
for i in range(n):
    for s in range(n):
        if line[i] not in k:
            if line[s] not in k:
                if (int(line[i]) + int(line[s])) % 2 == 0 and i < s:
                    cnt += 1
                    k.append(line[i])
                    k.append(line[s])
print(cnt)
