template = list(input())

n = int(input())
ans = []
for _ in range(n):
    T = True
    array = list(input())
    for i in template:
        if i in array:
            continue
        else:
            T = False
            break
    if T:
        ans.append('yes')
    else:
        ans.append('no')

for i in ans:
    print(i)