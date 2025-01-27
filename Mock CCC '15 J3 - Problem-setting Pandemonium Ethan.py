N = int(input())
d = input().split()

Repeats = []

cnt = 0
for i in d:
    if i not in Repeats:
        Repeats.append(i)
        cnt += 1

print(cnt)