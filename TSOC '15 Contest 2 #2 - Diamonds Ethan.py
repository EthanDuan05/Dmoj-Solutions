N = int(input())

ans = []
for i in range(N // 2 + 1):
    if (1 + 2*i) == 1:
        ans.append('*' * N)
    else:
        line = '*' * (N // 2 - i + 1) + ' ' * (1 + (2 * (i - 1))) + '*' * (N // 2 - i + 1)
        ans.append(line)

for i in ans:
    print(i)

ans = ans[0:-1]
ans.reverse()

for i in ans:
    print(i)
