L = []
prime = [True for _ in range(int(5500000+2))]

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

sieve(int(5500000+1))

num = int(input())

for i in L:
    if prime[i] and i >= num:
        print(i)
        break