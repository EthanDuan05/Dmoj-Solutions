import sys

N = int(input())

def check_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if N == 1:
    print(2)
    sys.exit(0)

if check_prime(N):
    print(N)
else:
    while not check_prime(N):
        N += 1
    print(N)