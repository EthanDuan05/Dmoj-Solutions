N = int(input())

ability = [0 for _ in range(5)]

for _ in range(N):
    line = list(input())
    for i in range(5):
        if line[i] == 'Y':
            ability[i] += 1
        else:
            continue

ind = max(ability)

ans = []
for i in range(5):
    if ability[i] == ind:
        ans.append(str(i+1))

print(','.join(ans))