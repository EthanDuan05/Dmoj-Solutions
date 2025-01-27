T = 0

for _ in range(6):
    score = int(input())
    T += score

a = int(input())

ans = int(input())

if T / 6 + a >= ans:
    print('yes')
else:
    print('no')