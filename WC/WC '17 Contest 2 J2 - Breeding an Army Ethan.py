a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
sum_a = a
sum_b = b
sum_c = c

cnt = 0
while True:
    if (sum_a <= x) and (sum_b <= y) and (sum_c <= z):
         sum_a += a
         sum_b += b
         sum_c += c
         cnt += 1
    else:
        break

print(cnt)