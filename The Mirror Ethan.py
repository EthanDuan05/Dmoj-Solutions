def checkprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
for _ in range(N):
    cnt = 0
    a, b = map(int, input().split())
    for s in range(a, b):
        if checkprime(s):
            cnt += 1
    print(cnt)