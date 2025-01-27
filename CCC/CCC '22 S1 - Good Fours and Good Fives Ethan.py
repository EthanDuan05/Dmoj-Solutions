import sys
input = sys.stdin.readline

N = int(input())

four = N // 4
five = N // 5

cnt = 0
possible = []

if four >= five:
    for i in range(0, four + 1):
        left_4 = N - i * 4
        if left_4 % 5 == 0:
            left_5 = left_4 // 5
            if (i, left_5) not in possible:
                possible.append((i, left_5))
                cnt += 1
elif five > four:
    for i in range(0, five + 1):
        left_5 = N - i * 5
        if left_5 % 4 == 0:
            left_4 = left_5 // 4
            if (left_4, i) not in possible:
                possible.append((left_4, i))
                cnt += 1

print(cnt)