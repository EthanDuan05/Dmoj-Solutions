n = int(input())
if n <= 1:
    print('not')
elif n > 1:
    for i in range(0, n+1):
        for k in range(0, n+1):
            if i * k == n:
                if i < k:
                    if (i != 1 and i != n) and (k != 1 and k != n):
                        print('not')
                        break
                    elif(i == 1 or i == n) and (k == 1 or k == n):
                        print('prime')