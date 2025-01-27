N = int(input())

debt = 0
days = 0

max_d = 0
max_day = 0

for i in range(N):
    a, b = input().split()
    b = int(b)
    days += 1
    if a == 'borrow':
        debt += b
    else:
        debt -= b

    if debt > max_d:
        debt = max_d
        max_day = days

print(max_day)