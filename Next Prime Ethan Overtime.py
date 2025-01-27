import sys
input = sys.stdin.readline

i_n = int(input())
n = i_n

def prime(n):
    L = []
    for i in range(1, n + 1):
        if n % i == 0:
            L.append(i)
    return L

while True:
    cnt = 0
    for i in prime(n):
        cnt += 1

    if cnt == 2 and n != i_n:
        print(n)
        break

    else:
        n += 1