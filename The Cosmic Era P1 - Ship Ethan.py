line = list(input())

total = ['B', 'F', 'T', 'L', 'C']

ans = []
for i in total:
    if i not in line:
        ans.append(i)

if len(ans) == 0:
    print('NO MISSING PARTS')
else:
    for i in ans:
        print(i)