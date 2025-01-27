initial = int(input())
last = int(input())

L = []

cnt = 0
for i in range(initial, last+1):
    for s in range(1, i+1):
        if s**2 == i:
            for k in range(1, i+1):
                if k**3 == i:
                    cnt += 1

print(cnt)