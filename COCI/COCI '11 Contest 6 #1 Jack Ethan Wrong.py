N, L = map(int, input().split())
line = list(map(int, input().split()))

best_sum = 0

for i in range(N):
    for s in range(N):
        for k in range(N):
            summ = line[i] + line[s] + line[k]
            if summ >= L:
                continue
            else:
                if summ < best_sum:
                    continue
                else:
                    best_sum = summ
print(best_sum)
