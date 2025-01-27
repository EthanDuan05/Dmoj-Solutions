fib = [-1] * 21


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if fib[n] >= 0:
        return fib[n]
    fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib[n]


LIST = []
for i in range(20):
    LIST.append(fibonacci(i))

N = int(input())
line = input()

determine = True
for i in range(N):
    if i+1 in LIST:
        if line[i] == 'A':
            continue
        else:
            determine = False
            break

    if line[i] == 'A':
        if i+1 in LIST:
            continue
        else:
            determine = False
            break


if determine:
    print("That's quite the observation!")
else:
    print('Bruno, GO TO SLEEP')