T = int(input())

for _ in range(T):
    a, b, n = map(int, input().split())
    if n % a == 0:
        print('Yes')
    else:
        max_b = n // b
        flag = True
        while flag:
            n -= max_b
            if n % a == 0:
                max_b -= 1
            else:
                flag = False
        if flag:
            print('YES')
        else:
            print('NO')

