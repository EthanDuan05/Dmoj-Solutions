a, b, c = input().split()
t = int(a)
d = int(b)
p = int(c)

answer = ''

if t < -40:
    if d >= 15 or p > 50:
        answer = 'YES'
    else:
        answer = 'NO'

if d >= 15:
    if t < -40 or p > 50:
        answer = 'YES'
    else:
        answer = 'NO'

if p > 50:
    if t < -40 or d >= 15:
        answer = 'YES'
    else:
        answer = 'NO'

if t >= -40:
    if d >= 15 and p > 50:
        answer = 'YES'
    else:
        answer = 'NO'

if d < 15:
    if t < -40 and p > 50:
        answer = 'YES'
    else:
        answer = 'NO'

if p <= 50:
    if t < -40 and d >= 15:
        answer = 'YES'
    else:
        answer = 'NO'

print(answer)