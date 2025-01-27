N = int(input())
S = list(map(int, input().split()))

A = [1 for _ in range(N)]

for i in range(1, N):
    if abs(S[i] - S[i - 1]) <= 2 and abs(S[i] - S[i - 1]) != S[i]:
        A[i - 1] += 1
        A[i] = A[i - 1]

print(max(A))