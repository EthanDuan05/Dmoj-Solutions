import sys

N = int(input())
K = 3
Shoes = list(map(int, input().split()))

Costs = [1e9 for _ in range(N+1)]

def compare(a, b):
    if a <= b:
        return a
    else:
        return b

def Calculate_2(a , b):
    T = a + b
    T2 = T - min(a, b) * 0.5
    return T2

def Calculate_3_1(a, b, c):
    T = a + b + c

    # two pair
    T2_1 = T - min(a, b) * 0.5

    T2_2 = T - min(b, c) * 0.5

    # three pair
    T3 = T - min(a, b, c)

    return min(T2_1, T2_2, T3)

def Calculate_3(a, b, c):
    T = a + b + c

    T3 = T - min(a, b, c)

    return T3

if N == 1:
    print(float(Shoes[0]))
    sys.exit(0)

if N == 2:
    print('%.1f'%(Calculate_2(Shoes[0], Shoes[1])))
    sys.exit(0)

Costs[1] = Shoes[0]
Costs[2] = Calculate_2(Shoes[0], Shoes[1])
Costs[3] = Calculate_3_1(Shoes[0], Shoes[1], Shoes[2])

for i in range(K+1, N+1):
    ways = []
    for j in range(1, K+1):
        if j == 1:
            current_cost = Shoes[i-1] + Costs[i-1]
            ways.append(current_cost)

        if j == 2:
            current_cost = Calculate_2(Shoes[i-1], Shoes[i-1-1]) + Costs[i-2]
            ways.append(current_cost)

        if j == 3:
            current_cost = Calculate_3(Shoes[i-1], Shoes[i-1-1], Shoes[i-1-1-1]) + Costs[i-3]
            ways.append(current_cost)

    Costs[i] = min(ways)

print('%.1f'%(Costs[N]))


