for _ in range(5):
    n = int(input())
    total = 0
    for i in range(0, n+1):
        ans = str(i).count('0')
        total += ans
    print(total)