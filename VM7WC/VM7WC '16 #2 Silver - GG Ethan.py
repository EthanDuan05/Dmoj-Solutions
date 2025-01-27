import sys
input = sys.stdin.readline
line = input()
M = [0]*(len(line))

for i in range(len(line)):
    if line[i] == 'G':
        M[i] += 1

psa = [0]*(len(line)+1)

for i in range(len(line)):
    psa[i+1] = psa[i] + M[i]

Ans = []
q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    ans = psa[b+1]-psa[a]
    Ans.append(ans)

for k in Ans:
    print(k)