from math import sqrt
T = int(input())

Fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
             89, 144, 233, 377, 610, 987, 1597,
             2584, 4181, 6765, 10946, 17711, 28657,
             46368, 75025]


def finding_prime(n):
    prime_flag = 0
    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return True


for _ in range(T):
    n = int(input())
    if n in Fibonacci:
        if n == 1:
            print('NO')
        elif not finding_prime(n):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')