n, a, r = map(int, input().split())

max_num = 0
for i in range(1, n+1):
    cost = a * i
    if r >= cost:
        max_num = i

print(max_num)