n = int(input())
Line = [1, 2, 4, 6, 3, 2, 8, 5]

psa = [0]*(n+1)
for i in range(n):
    psa[i+1] = psa[i] + Line[i]

print(psa)

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    total = 0
    for j in range(a, b + 1):
        total += Line[j - 1]
    ans = psa[b] - psa[a - 1]

    print(ans)