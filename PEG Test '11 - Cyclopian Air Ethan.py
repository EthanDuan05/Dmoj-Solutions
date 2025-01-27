N = int(input())

L = []

for i in range(N):
    num = int(input())
    L.append(num)

ans = []

for s in range(N):
    product = L[s-1] * L[s]
    ans.append(product)

print(max(ans))