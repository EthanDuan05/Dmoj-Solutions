N = int(input())

line_1 = list(map(int, input().split()))
line_2 = list(map(int, input().split()))

total = line_1.count(1)*3 + line_2.count(1)*3

for i in range(N):
    if i < N-1:
        if line_1[i] == 1 and line_1[i + 1] == 1:
            total -= 2

        if line_2[i] == 1 and line_2[i + 1] == 1:
            total -= 2

    if i % 2 == 0:
        if line_1[i] == 1 and line_2[i] == 1:
            total -= 2

print(total)