N = int(input())

for _ in range(N):
    total = 0
    num = input()
    for i in num:
        if i.isdigit():
            total += 1
    print(total)