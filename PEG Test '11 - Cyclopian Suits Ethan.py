n = int(input())
L = []
Distinct = []
Repeat = []

for i in range(n):
    size = int(input())
    L.append(size)
    if size not in Distinct:
        Distinct.append(size)

for i in Distinct:
    M = L.count(i)
    Repeat.append(M)

K = max(Repeat)

ans = []
for i in range(len(Distinct)):
    if Repeat[i] == K:
        ans.append(Distinct[i])

ans.sort()

print(Repeat.count(K))
for i in ans:
    print(i)