home, direction = input().split()
street_direction = {home: direction}

N = int(input())

cnt_ew = 0
cnt_ns = 0

if street_direction[home] == 'ns':
    cnt_ns += 1
else:
    cnt_ew += 1

for _ in range(N):
    street_1, street_2 = input().split()
    if street_direction[street_1] == 'ns':
        street_direction[street_2] = 'ew'
        cnt_ew += 1
    elif street_direction[street_1] == 'ew':
        street_direction[street_2] = 'ns'
        cnt_ns += 1

print(cnt_ns, cnt_ew)
