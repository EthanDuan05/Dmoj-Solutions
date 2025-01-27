a, b, c = map(int, input().split())
sum = 0
if a % 3 == 0:
    sum += a // 3
else:
    sum += a// 3 + 1

if b % 3 == 0:
    sum += b // 3
else:
    sum += b // 3 + 1

if c % 3 == 0:
    sum += c // 3
else:
    sum += c // 3 + 1

print(sum)