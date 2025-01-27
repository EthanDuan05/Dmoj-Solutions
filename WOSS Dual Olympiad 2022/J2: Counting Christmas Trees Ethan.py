N = int(input())
line = list(map(int, input().split()))
line.append(0)

max_c_increase = 0
current_i = 0
last_i = 0

for i in range(N):
    if line[i] == 0:
        if current_i > max_c_increase:
            max_c_increase = current_i

    elif line[i] > last_i:
        current_i += 1
        last_i = line[i]

    else:
        if current_i > max_c_increase:
            max_c_increase = current_i
            current_i = 0
            last_i = line[i]
        else:
            current_i = 0
            last_i = line[i]

max_c_decrease = 0
current_d = 0
last_d = 201

for i in range(N):
    if line[i] == 0:
        if current_d > max_c_decrease:
            max_c_decrease = current_d

    elif line[i] < last_d:
        current_d += 1
        last_d = line[i]

    else:
        if current_d > max_c_decrease:
            max_c_decrease = current_d
            current_d = 0
            last_d = line[i]
        else:
            current_d = 0
            last_d = line[i]


print(max_c_increase)
print(max_c_decrease)
