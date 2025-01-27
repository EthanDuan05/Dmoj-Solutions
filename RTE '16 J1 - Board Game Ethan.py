line = list(input())

while ' ' in line:
    line.remove(' ')

last = ''
max_consecutive = 0
consecutive_current = 0
total = 0
for i in line:
    if i == 'L':
        total += 1
        if last == 'L':
            if consecutive_current == 0:
                consecutive_current += 2
            else:
                consecutive_current += 1

        if consecutive_current > max_consecutive:
                max_consecutive = consecutive_current
    else:
        if last == 'L':
            if consecutive_current > max_consecutive:
                max_consecutive = consecutive_current
                consecutive_current = 0
            else:
                consecutive_current = 0
        else:
            consecutive_current = 0
            continue
    last = i

print(total, max_consecutive)

