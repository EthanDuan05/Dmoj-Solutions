n = int(input())
L = []
for i in range(n):
    h = float(input())
    L.append(h)

# sort the number
L.sort()

print(L)

# calculate distance
D = []
for k in range(1, n-1):
    distant = (L[k+1]-L[k]) / 2 + (L[k] - L[k-1]) / 2
    D.append(distant)

D.sort()

print(D[0])