N = int(input())
drone_now = list(map(int, input().split()))
drone_fac = list(map(int, input().split()))

frequency = {}
for i in range(N):
    difference = drone_fac[i] - drone_now[i]
    if difference in frequency:
        frequency[difference] += 1
    else:
        frequency[difference] = 1

ans = max(frequency.values())
Flag = True

if list(frequency.values()).count(ans) > 1:
    Flag = False

ans_set = []
cnt_f = 0
if not Flag:
    for i in frequency:
        if frequency[i] == ans:
            if cnt_f == 0:
                cnt_f += 1
                continue
            else:
                ans_set.append(i)

cnt = 0
for i in range(N):
    difference = drone_fac[i] - drone_now[i]
    if frequency[difference] == ans:
        if difference not in ans_set:
            cnt += 1

print(cnt)