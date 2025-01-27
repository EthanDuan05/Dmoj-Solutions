L = []
N = []
for i in range(5):
    line = L.append(input())
    num = N.append(int(input()))

for s in range(1, 6):
    for i in range(len(N)):
        if N[i] == s:
            print(L[i])