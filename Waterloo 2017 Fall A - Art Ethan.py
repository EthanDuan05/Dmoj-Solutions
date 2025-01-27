line = list(map(int, input().split(' ')))

l = len(line)
ans = []

cnt = 0
for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1,l):
            if line[i] + line[j] > line[k] and line[i] + line[k] > line[j] and line[j] + line[k] > line[i]:
                comb = (line[i], line[j], line[k])
                if comb not in ans:
                    ans.append(comb)
                    cnt += 1
print(cnt)