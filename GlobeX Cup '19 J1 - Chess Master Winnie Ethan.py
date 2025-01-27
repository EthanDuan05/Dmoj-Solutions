N, M, A, B, C = map(int, input().split())
w_l = input().split()
match = list(map(int, input().split()))

for i in range(C):
    if w_l[match[i] - 1] == '1':
        M += A
    else:
        M -= B

print(M)