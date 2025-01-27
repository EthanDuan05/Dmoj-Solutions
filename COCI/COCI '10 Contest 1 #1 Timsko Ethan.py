M, N, K = map(int, input().split())

total = 0
while M >= 2 and N >= 1 and M+N >= K+3:
    total += 1
    M -= 2
    N -= 1
print(total)