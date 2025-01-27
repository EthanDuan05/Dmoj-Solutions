N = int(input())

young = 0
total = 0

for _ in range(N):
    age = int(input())
    if age >= 0:
        if age > 14:
            total += 1
        else:
            young += 1

if young > 0:
    if young == 1:
        print('1 person is too young to play.')
    else:
        print(str(young) + ' ' + 'people are too young to play.')

if total == 12:
    print('Time to play!')
elif total > 12:
    print('There are too many people who want to play.')
else:
    print('There are not enough people to play.')