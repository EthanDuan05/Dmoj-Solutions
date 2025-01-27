import math


def prime_check(num):
    if num <= 1:
        return False
    else:
        is_prime = True
        root = int(math.sqrt(num))
        for i in range(2, root + 1):
            if num % i == 0:
                is_prime = False
                break
        return is_prime


n = int(input())
cnt = 0
for _ in range(n):
    num = int(input())
    if prime_check(num):
        cnt += 1
print(n - cnt)
