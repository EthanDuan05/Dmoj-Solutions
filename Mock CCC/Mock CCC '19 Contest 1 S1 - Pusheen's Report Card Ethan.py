N = int(input())

total = 0
for _ in range(N):
    mark = int(input())
    total += mark

print(round(total / N, 1))