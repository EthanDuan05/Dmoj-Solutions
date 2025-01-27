T = int(input())

for _ in range(T):
    ans = 0
    N = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    for i in range(N):
        ans += line1[i] * line2[i]

    print(ans)