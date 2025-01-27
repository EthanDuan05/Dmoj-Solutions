import sys
input = sys.stdin.readline

N = int(input())
B = []
for _ in range(N):
    Bubble = int(input())
    B.append(Bubble)

def calculate_2(a, b):
    Total = a+b
    if a <= b:
        Total -= a*0.25
    elif b < a:
        Total -= b*0.25
    return Total

def calculated_3(a, b, c):
    Total = a + b + c
    F = Total - min(a, b, c)*0.5
    S = calculate_2(a, b) + c
    T = calculate_2(b, c) + a
    return min(F, S, T)

Costs = [0 for _ in range(N+1)]
Costs[1] = B[0]
Costs[2] = calculate_2(B[0], B[1])
Costs[3] = calculated_3(B[0], B[1], B[2])

for i in range(3+1, N+1):
    ways = []
    way_1 = B[i-1] + Costs[i-1]
    way_2 = calculate_2(B[i-1], B[i-1-1]) + Costs[i-2]
    way_3 = calculated_3(B[i-1], B[i-1-1], B[i-1-1-1]) + Costs[i-3]
    ways.append(way_1)
    ways.append(way_2)
    ways.append(way_3)
    Costs[i] = min(ways)

print(int(Costs[N]))