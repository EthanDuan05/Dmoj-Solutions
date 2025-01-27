N, D = map(int, input().split())

Line = list(map(int, input().split()))

max_interval = -1

for i in range(N):
    value = Line[i]
    if abs(D) % value == 0:
        if value > max_interval:
            max_interval = value

if max_interval != -1:
    print(abs(D) // max_interval)
else:
    print('This is not the best time for a trip.')