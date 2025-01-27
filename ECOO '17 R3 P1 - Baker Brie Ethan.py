ans = []
for _ in range(10):
    f, d = map(int, input().split())

    vertical = [0]*f
    horizontal = [0]*d

    for i in range(d):
        line = list(map(int, input().split()))
        horizontal[i] += sum(line)
        for s in range(f):
            vertical[s] += line[s]

    cnt = 0
    for i in vertical:
        if i % 13 == 0:
            a = i // 13
            cnt += a
    for m in horizontal:
        if m % 13 == 0:
            k = m // 13
            cnt += k
    ans.append(cnt)

for i in ans:
    print(i)