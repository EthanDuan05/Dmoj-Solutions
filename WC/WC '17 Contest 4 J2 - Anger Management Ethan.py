n = int(input())
limit = 10
total = 0

last = 0
cnt = 0
for i in range(n):
    a = int(input())
    if total + a < limit:
        last += a
        total += a
    elif total + a >= limit:
        if last >= limit:
            total += a
            last += a
        else:
            cnt += 1
            total += a
            last += a
print(cnt)