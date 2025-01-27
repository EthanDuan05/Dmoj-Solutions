N = int(input())
Frequency = [0 for _ in range(N+1)]

L = list(map(int, input().split()))
Total = sum(L)
ans = Total // N

for i in range(N):
    Frequency[L[i]-1] += 1

res = 0
for i in range(N+1):
    if i != ans - 1:
        res += Frequency[i]

print(res)