D = int(input())
X = list(map(int, input()))

for i in range(D-1):
    if X[i] < X[i+1]:
        X[i], X[i+1] = X[i+1], X[i]
        break

print(''.join(map(str, X)))