N = int(input())
X = int(input())
Value = []

for i in range(N):
    p1, p2 = map(int, input().split())
    D = 0
    Large = 0
    if p1 > p2:
        D = p1 - p2
        Large = p1
    elif p1 < p2:
        D = p2 - p1
        Large = p2
    elif p1 == p2:
        Value.append(p1)
    if D <= X:
        Value.append(Large)
    elif D > X:
        P3 = int(input())
        Value.append(P3)

Value = sum(Value)
print(Value)