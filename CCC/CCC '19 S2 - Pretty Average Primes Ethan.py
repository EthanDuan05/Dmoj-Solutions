import math

def check_if_prime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True


N = int(input())
for _ in range(N):
    num = int(input())
    num = 2*num
    for i in range(2, num-1):
        a = i
        b = num-a
        if check_if_prime(a) and check_if_prime(b):
            if a + b == num:
                print(a, b)
                break
