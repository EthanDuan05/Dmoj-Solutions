import math

N, D = map(int, input().split())
max_combo = 0
current_combo = 0

x = 0
y = 0

for i in range(N):
    n_x, n_y = map(int, input().split())
    if i == 1:
        x = n_x
        y = n_y
    v = (n_x - x)**2 + (n_y - y)**2
    v_t = math.sqrt(v)
    if v_t <= D:
        current_combo += 1
    else:
        if current_combo > max_combo:
            max_combo = current_combo
            current_combo = 0
        else:
            current_combo = 0

    x = n_x
    y = n_y

    if i == N-1:
        if current_combo > max_combo:
            max_combo = current_combo

print(max_combo)

