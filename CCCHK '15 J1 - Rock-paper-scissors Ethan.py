N = int(input())

a = input().split()
b = input().split()

cnt_a = 0
cnt_b = 0

for i in range(N):
    if a[i] == 'rock' and b[i] == 'scissors':
        cnt_a += 1
    elif a[i] == 'scissors' and b[i] == 'paper':
        cnt_a += 1
    elif a[i] == 'paper' and b[i] == 'rock':
        cnt_a += 1

    if b[i] == 'rock' and a[i] == 'scissors':
        cnt_b += 1
    elif b[i] == 'scissors' and a[i] == 'paper':
        cnt_b += 1
    elif b[i] == 'paper' and a[i] == 'rock':
        cnt_b += 1

print(cnt_a, cnt_b)