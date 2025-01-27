N, M = map(int, input().split())

numbers = N*M

if numbers % 2 == 0:
    print(numbers//2, numbers//2)
else:
    more = min(N, M)
    ans = (numbers - more) // 2
    print(ans + more, ans)
