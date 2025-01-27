a, b = input().split()
length = len(a)

letter = ''
cnt = -1
for i in a:
    cnt += 1
    if i in b:
        letter = i
        break

ans = []
flag = False
for i in b:
    if i != letter:
        ans.append(('.' * cnt) + i + ('.' * (length - cnt - 1)))
    else:
        if not flag:
            ans.append(a)
            flag = True
        else:
            ans.append(('.' * cnt) + i + ('.' * (length - cnt - 1)))

for i in ans:
    print(i)
