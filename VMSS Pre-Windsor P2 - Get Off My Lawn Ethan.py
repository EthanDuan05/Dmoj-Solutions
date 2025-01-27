import math

N = int(input())
distance = {}

for _ in range(N):
    x, y = map(int, input().split())
    current_distance = math.sqrt((x - 0)**2 + (y - 0)**2)
    distance[(x, y)] = current_distance

ans = max(distance.values())

for i in distance:
    if distance[i] == ans:
        print(i[0], i[1])
        break