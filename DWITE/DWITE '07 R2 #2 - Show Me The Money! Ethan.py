balance = 0
for _ in range(5):
    line = input().strip()
    flag = True
    for i in line:
        if balance >= 0:
            if i == '+':
                balance += 1
            elif i == '-':
                balance -= 1
        else:
            balance = 0
            print('OH NOES!')
            flag = False
            break

    if flag:
        print(balance)

