import sys
input = sys.stdin.readline

R = int(input())
C = int(input())

def find_factors(N):
    ANS = []
    for i in range(1, int(N**0.5 + 1)):
        if N % i == 0:
            x = i
            y = N // i
            if x <= C and y <= R:
                ANS.append((y, x))
            if y <= C and x <= R:
                ANS.append((x, y))

    return ANS

Graph = dict()
Has_Exit = False
Repeated = dict()
Result = R * C
for r in range(R):
    Line = list(map(int, input().split()))
    for c in range(len(Line)):
        Number = Line[c]
        if Number == Result:
            Has_Exit = True
        if Number not in Repeated.keys():
            L = find_factors(Number)
            Graph[(r+1, c+1)] = L
            Repeated[Number] = L
        else:
            Graph[(r+1, c+1)] = Repeated[Number]

if not Has_Exit:
    print('no')
    sys.exit(0)
def BFS(r, c):
    visited = {position: False for position in Graph.keys()}
    visited[(r, c)] = True
    queue = []
    queue.append((1, 1))

    while len(queue) > 0:
        x, y = queue.pop()
        for k in Graph[(x, y)]:
            a, b = k
            if visited[(a, b)]: continue
            visited[(a, b)] = True
            queue.append([a, b])
            if a == R and b == C:
                return True

    return False

if BFS(1, 1):
    print('yes')
else:
    print('no')

