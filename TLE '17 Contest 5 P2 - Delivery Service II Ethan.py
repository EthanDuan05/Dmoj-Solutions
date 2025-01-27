N, D = map(int, input().split())
P = []

for _ in range(N):
    planet = int(input())
    P.append(planet)

P.sort()

MIN = 1e9
MAX = -1e9
flag = False

for _ in range(D):
    a, b = map(int, input().split())
    if a < MIN:
        MIN = a

    if a > MAX:
        MAX = a

    if b < MIN:
        MIN = a

    if b > MAX:
        MAX = a

    if  a or b < 0:
        flag = True

if  flag:
    print(2 *abs((P[MAX-1] - P[MIN-1])))
else:
    print(abs(P[MAX-1] - P[MIN[-1]]))