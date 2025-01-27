frequency = [0]*11

N = int(input())
for i in range(N):
    line = list(map(int, input().split()))
    M = line[0]
    line.remove(M)
    for s in range(M):
        frequency[line[s]-1] += 1

flag = True
for i in frequency:
    if i > 1:
        flag = False
        break
    else:
        continue

if flag:
    print('NO')
else:
    print('YES')