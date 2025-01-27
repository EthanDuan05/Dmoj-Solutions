import sys
input = sys.stdin.readline

cnt = 0

N = int(input())

for _ in range(N):
    line = list(input().strip())
    unpaired = []
    for ch in line:
        if len(unpaired) == 0:
            unpaired.append(ch)
        else:
            last = unpaired.pop(-1)
            if last == ch:
                continue
            else:
                unpaired.append(last)
                unpaired.append(ch)

    if len(unpaired) == 0:
        cnt += 1

print(cnt)
