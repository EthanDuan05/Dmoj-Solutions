n = int(input())
line = list(map(int, input().split()))
M = sorted(line)

divisor = 0
for s in range(2, M[n-1]):
    for i in M:
        if i % s == 0:
            divisor = s

L = ''
for i in line:
    ans = i // divisor
    L += str(ans)+' '

L = L.strip(L[n+1])

print(n//divisor)
print(L)