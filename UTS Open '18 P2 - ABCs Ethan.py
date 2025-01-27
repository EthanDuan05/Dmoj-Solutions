a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(3):
    if b[i] == a[i-1]:
        if c[i] > 0:
            ans += c[i]
print(ans)