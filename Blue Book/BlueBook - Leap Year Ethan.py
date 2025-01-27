n = int(input())

ans = []
for i in range(n):
    year = int(input())
    if year != 0:
        if year % 4 == 0 and year % 100 != 0:
            ans.append(1)
        elif year % 400 == 0:
            ans.append(1)
        else:
            ans.append(0)
    else:
        ans.append(1)

for i in ans:
    print(i)