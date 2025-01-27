N = int(input())

for _ in range(N):
    a, b, c  = input().split()
    if a == b or a == c or b == c:
        if a == b or a == c:
            print(a)
        else:
            print(b)
    else:
        print('???')