L = int(input())
D = int(input())
X = int(input())
MAX_M = 0
MIN_M = 0

for i in range(L, D+1):
    S = str(i)
    S = list(S)
    if sum(map(int, S)) == X:
        MIN_M = i
        break

for i in range(D, L-1, -1):
    S = str(i)
    S = list(S)
    if sum(map(int, S)) == X:
        MAX_M = i
        break

print(MIN_M)
print(MAX_M)