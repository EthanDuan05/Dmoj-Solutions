N = int(input())

L = []
frequency = {}
line = input().split()

for i in line:
    if i not in L:
        L.append(i)
        frequency[i] = 0

    frequency[i] += 1

ans = []
for i in frequency:
    if frequency.get(i) % 2 != 0:
        ans.append(int(i) // 2)
ans.sort()
cnt = 0
total = N
ANS = ''
for i in ans:
    if cnt < N-1:
        ANS += str(i) + ' '
        cnt += 1
    else:
        ANS += str(i)

print(ANS)
