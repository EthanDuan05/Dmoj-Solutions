N = int(input())

ans = 0
for _ in range(N):
    num = input()
    n = num[0:-1]
    # print(n)
    p = num[-1]
    ans += int(n) ** int(p)

print(ans)