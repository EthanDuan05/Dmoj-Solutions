l_1 = []
l_2 = []

for i in range(5):
    n, d = map(int, input().split())
    sum = n+d
    l_1.append(sum)

for i in range(5):
    expected = int(input())
    l_2.append(expected)

cnt = 0
for s in range(5):
    if l_1[s] == l_2[s]:
        cnt += 1

print(l_1)
print(l_2)
print(cnt)