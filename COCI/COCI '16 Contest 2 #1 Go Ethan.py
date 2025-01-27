n = int(input())
total = 0
max_e = []
poke_index = []
Name = []

for i in range(n):
    e = 0
    name = input()
    k, m = map(int, input().split())
    Name.append(name)
    poke_index.append(m)
    while m >= k:
        m = m - k + 2
        e += 1
        total += 1
    max_e.append(e)

ans = 0
ind = 0
for s in range(len(max_e)):
    if max_e[s] > ans:
        ans = max_e[s]
        ind = s
    elif max_e[s] == ans:
        if ind < s:
            ans = ans
            ind = ind
        elif s < ind:
            ans = max_e[s]
            ind = s
    else:
        continue

print(total)
print(Name[ind])