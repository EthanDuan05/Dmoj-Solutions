N = int(input())

for _ in range(N):
    a, b = input().split()
    if len(a) == 1 and len(b) == 1:
        print('NO')
    elif len(a) == 1 or len(b) == 1:
        if (a == '7' and b == '11') or (a == '11' and b == '7'):
            print('YES')
        else:
            print('NO')
    else:
        if a[-1] == '7' or b[-1] == '7':
            if a[-1] == '7':
                if b[-2] == '1' and b[-1] == '1':
                    if a[-2] != '1':
                        print('YES')
                    else:
                        print('NO')
                else:
                    print('NO')
            elif b[-1] == '7':
                if a[-2] == '1' and a[-1] == '1':
                    if b[-2] != '1':
                        print('YES')
                    else:
                        print('NO')
                else:
                    print('NO')
        else:
            print('NO')