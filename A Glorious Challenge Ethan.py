N = int(input())
A = list(map(int, input().split()))

A_1 = []
A_2 = []
for i in range(N):
    A_1.append(A[i]+i)
    A_2.append(A[i]-i)

ans_1 = max(A_1) - min(A_1)
ans_2 = max(A_2) - min(A_2)

print(max(ans_1, ans_2))