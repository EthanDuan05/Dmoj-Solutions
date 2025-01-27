h = int(input())
max_t = int(input())
for t in range(max_t):
    A = -6*(t**4)+h*(t**3)+2*(t**2)+t
    if A <= 0 and t != 0:
        f_t = t
        print('The balloon first touches ground at hour:')
        print(f_t)
        break

for k in range(max_t):
    A = -6 * (k ** 4) + h * (k ** 3) + 2 * (k ** 2) + k
    if A > 0:
        if k == max_t-1:
            print('The balloon does not touch ground in the given time.')