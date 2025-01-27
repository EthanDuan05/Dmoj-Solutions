n = int(input())

if n <= 1:
    print('not')
else:
    isprime = True
    for i in range(2, n):
        if n % i == 0:
            isprime = False
            break
    if isprime:
        print('prime')
    else:
        print('not')