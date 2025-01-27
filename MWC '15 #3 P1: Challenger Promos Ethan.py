import sys

N = int(input())
Players = {}

for _ in range(N):
    Name, Score = input().split()
    Score = int(Score)

    Players[Name] = Score

D = int(input())

for _ in range(N*D):
    Name, Change = input().split()
    Change = int(Change)
    Players[Name] += Change

P = int(input())
sorted_items = sorted(Players.items(), key=lambda x:x[1], reverse=True)
sorted_Players = {}
for i in sorted_items:
    sorted_Players[i[0]] = i[1]

# print(sorted_Players)

cnt = 0
for i in sorted_Players:
    cnt += 1
    if cnt == P:
        print(i)
        sys.exit(0)