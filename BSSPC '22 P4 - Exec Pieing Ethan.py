N, T = map(int, input().split())

execs = list(map(int, input().split()))

cnt = 0
MAX = execs[0]
running_sum = 0
for i in execs[1:]:
    if i > MAX:
        running_sum += MAX
        MAX = i
    else:
        running_sum += i

    if running_sum > T:
        break
    else:
        cnt += 1

print(cnt)