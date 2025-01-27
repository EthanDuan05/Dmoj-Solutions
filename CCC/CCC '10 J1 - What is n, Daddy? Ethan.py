n = int(input())
cnt = 0
for i in range(0, n+1):
    for k in range(0, n+1):
        if i <= 5 and k <= 5:
            if i + k == n and i >= k:
                cnt += 1
        elif i + k == n and i < k:
            cnt = cnt
print(cnt)