a, b = map(int, input().split())

for i in range(1, a+1):
    for s in range(i, a+1):
        if i + s == a and i * s == b:
            print(i, s)
            break