N = int(input())

sum_c = 0
for _ in range(N):
    c, v = map(int, input().split())

    if v > 0:
        sum_c += c

print(sum_c)