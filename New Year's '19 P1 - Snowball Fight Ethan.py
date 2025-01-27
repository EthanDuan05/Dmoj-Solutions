n_1, h_1 = input().split()
n_2, h_2 = input().split()

t_1 = int(n_1)
t_2 = int(n_2)

cnt = 0

while True:
    cnt += 1
    if cnt % int(h_1) == 0 and cnt != 0:
        t_1 -= 1
    elif cnt % int(h_2) == 0 and cnt != 0:
        t_2 -= 1

    if t_1 == 0 or t_2 == 0:
        break

print(t_1)
print(t_2)