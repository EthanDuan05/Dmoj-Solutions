n = int(input())
fib = [-1] * (n+1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if fib[n] >= 0:
        return fib[n]
    fib[n] = fibonacci(n-2) + fibonacci(n-1)
    return fib[n]


for i in range(n):
    print(fibonacci(i))