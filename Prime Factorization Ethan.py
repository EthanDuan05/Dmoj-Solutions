import sys
import math
input = sys.stdin.readline
T = int(input())

L = []
prime = [True for _ in range(int(10**4+200+1))]

def sieve(N):
    p = 2
    while p*p <= N:
        if prime[p]:
            for i in range(p*p, N+1, p):
                prime[i] = False

        p += 1

    for p in range(2, N+1):
        if prime[p]:
            L.append(p)

sieve(int(10**4+200))

for _ in range(T):
    num = int(input())

    if num < 10**4:
        if prime[num]:
            print(num)
            continue

    root = int(math.sqrt(num))
    if prime[root] and root**2 == num:
        print(root, root)
        continue

    i = 0
    ans = []
    current_p = L[0]
    while num > 1 and num >= current_p:
        current_p = L[i]
        if current_p > root + 1:
            break
        if num % current_p == 0:
            while num % current_p == 0 and num >= current_p:
                ans.append(current_p)
                num //= current_p
        else:
            i += 1

    if num >= root:
        ans.append(num)

    print(*ans)


