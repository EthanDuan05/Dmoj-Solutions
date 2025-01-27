N = int(input())

line = list(map(int, input().split()))
determine = [True]*N

for i in range(N):
    if line[i] == 0:
        continue
    else:
        determine[line[i]] = False

print(determine.count(True))