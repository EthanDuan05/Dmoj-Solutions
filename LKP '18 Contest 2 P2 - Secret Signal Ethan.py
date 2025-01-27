import sys
input = sys.stdin.readline

N, K = map(int, input().split())
PSA = [0]*(N+1)

line = input().split()
for i in range(N):
    PSA[i+1] += PSA[i] + int(line[i])

PSA.remove(PSA[0])
L = [0 for _ in range(50000)]
for s in range(N):
    L[PSA[s] % K] += 1

cnt = 0
cnt += L[0]
for i in range(0, 50000):
    cnt += L[i]*(L[i]-1)//2

# print(PSA)
# print(L)
print(cnt)