initial = input()
t = int(input())

wizards = [initial]
cnt = 1
current = initial

for _ in range(t):
    w1, w2 = input().split()
    if w2 == current:
        if w1 not in wizards:
            wizards.append(w1)
            cnt += 1
            current = w1
        else:
            current = w1

print(current)
print(cnt)