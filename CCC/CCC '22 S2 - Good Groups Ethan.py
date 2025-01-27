import sys
input = sys.stdin.readline

constrains_same = {}
constrains_different = {}
violation = set()

x = int(input())
for i in range(x):
    a, b = input().strip().split()
    if a not in constrains_same:
        constrains_same[a] = [b]
    else:
        constrains_same[a].append(b)
    if b not in constrains_same:
        constrains_same[b] = [a]
    else:
        constrains_same[b].append(a)

y = int(input())
for i in range(y):
    a, b = input().strip().split()
    if a not in constrains_different:
        constrains_different[a] = [b]
    else:
        constrains_different[a].append(b)
    if b not in constrains_different:
        constrains_different[b] = [a]
    else:
        constrains_different[b].append(a)

cnt = 0
G = int(input())
for i in range(G):
    a, b, c = input().strip().split()
    # a
    if a in constrains_same:
        cnt += 1
        for x in constrains_same[a]:
            if x in (b, c):
                continue
            else:
                if x < a:
                    violation.add((x, a))
                else:
                    violation.add((a, x))
    if a in constrains_different:
        if b in constrains_different[a]:
            cnt += 1
            if a < b:
                violation.add((a, b))
            else:
                violation.add((b, a))
        if c in constrains_different[a]:
            cnt += 1
            if a < c:
                violation.add((a, c))
            else:
                violation.add((c, a))

    # b
    if b in constrains_same:
        cnt += 1
        for x in constrains_same[b]:
            if x in (a, c):
                continue
            else:
                if x < b:
                    violation.add((x, b))
                else:
                    violation.add((b, x))
    if b in constrains_different:
        if a in constrains_different[b]:
            cnt += 1
            if a < b:
                violation.add((a, b))
            else:
                violation.add((b, a))
        if c in constrains_different[b]:
            cnt += 1
            if b < c:
                violation.add((b, c))
            else:
                violation.add((c, b))

    # c
    if c in constrains_same:
        cnt += 1
        for x in constrains_same[c]:
            if x in (a, b):
                continue
            else:
                if x < c:
                    violation.add((x, c))
                else:
                    violation.add((c, x))
    if c in constrains_different:
        if b in constrains_different[c]:
            cnt += 1
            if c < b:
                violation.add((c, b))
            else:
                violation.add((b, c))
        if a in constrains_different[c]:
            cnt += 1
            if a < c:
                violation.add((a, c))
            else:
                violation.add((c, a))

print(len(violation))
