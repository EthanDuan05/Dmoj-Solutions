T = int(input())
for _ in range(T):
    ans = True
    A, B, N = map(int, input().split())
    if N % A == 0 and N % B == 0:
        ans = True
    elif (N - A) % B == 0 or (N - B) % A == 0:
        ans = True
    elif N % B == 0:
        total = 0
        current_a = 0
        max_b = N / B
        while True:
            current_price = (A * current_a) + (B * max_b)
            current_a += 1
            max_b -= 1
            if total + current_price < N:
                total += current_price
            else:
                break

        if total == N:
            ans = True
        else:
            ans = False

    elif N % A == 0:
        total = 0
        current_b = 0
        max_a = N / A
        while True:
            current_price = (A * max_a) + (B * current_b)
            current_b += 1
            max_a -= 1
            if total + current_price < N:
                total += current_price
            else:
                break
        if total == N:
            ans = True
        else:
            ans = False

    else:
        ans = False

    if ans:
        print('YES')
    else:
        print('NO')
