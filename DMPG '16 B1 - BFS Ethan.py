line = [5, 10, 25, 100, 200]

amount = list(map(int, input().split()))

ans = 0
for i in range(len(amount)):
    new = amount[i] * line[i]
    ans += new

print(ans)