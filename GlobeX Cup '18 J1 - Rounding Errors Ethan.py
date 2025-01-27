N = int(input())

cnt_up = 0
cnt_down = 0
for _ in range(N):
    num = float(input())
    if num % 1 >= 0.5:
        cnt_up += 1
    else:
        cnt_down += 1

print(cnt_up)
print(cnt_down)