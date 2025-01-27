import sys
input = sys.stdin.readline

N = int(input())
line = input()
Order = [0 for _ in range(N)]
Ind_1 = []
Ind_2 = []

for i in range(N):
    if line[i] == 'R':
        Ind_1.append(i)

    if line[i] == 'G':
        Order[i] = 1

    if line[i] == 'B':
        Order[i] = 0
        Ind_2.append(i)

cnt = 0
for i in Ind_1:
    for s in Ind_2:
        Phrase = Order[i:s+1]
        if sum(Phrase) == 1:
            cnt += 1

print(cnt)