def checkingprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


T = int(input())
for _ in range(T):
    num = int(input())
    if checkingprime(num):
        print(1)
    else:
        print(0)