import sys
input = sys.stdin.readline

N, T = map(int, input().split())

cards = []

for i in range(N):
    name, cost = input().strip().split()
    cards.append((name, int(cost)))

cards.sort()

combinations = []
for i in range(N-2):
    for s in range(i+1, N-1):
        for k in range(s+1, N):
            if cards[i][1] + cards[s][1] + cards[k][1] <= T:
                LIST = [cards[i][0], cards[s][0], cards[k][0]]
                combinations.append(LIST)

for i in combinations:
    print(' '.join(i))