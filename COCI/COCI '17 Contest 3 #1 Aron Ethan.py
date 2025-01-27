N = int(input())
group = []
last = ''
for _ in range(N):
    C = input()
    if last == '':
        last = C
    else:
        if C == last:
            continue
        else:
            group.append(last)
            last = C

if len(group) == 0:
    group.append(last)

if last != group[-1]:
    group.append(last)

print(len(group)+1)