N = int(input())

for _ in range(N):
    a, b, c = map(int, input().split())
    total = a + b*2 + c*3

    if total % 2 == 0:
        if (a + c*3) % 2 == 0 and b % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')