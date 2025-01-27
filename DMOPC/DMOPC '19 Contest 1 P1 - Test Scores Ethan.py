N = int(input())

for _ in range(N):
    n, get, lost, want = map(int, input().split())
    if get * n < want:
        print(-1)
    else:
        ans = (want + lost * n) // (get + lost)
        print(ans+1)
