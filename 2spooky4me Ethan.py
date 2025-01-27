import sys
input = sys.stdin.readline

N, L, S = map(int, input().split())
position = []

for _ in range(N):
    a, b, scale = map(int, input().split())
    position.append((a, scale))
    if b+1 <= L:
        position.append((b+1, -scale))

position.sort()
ind = 1
spook = 0
can = 0

for p, c in position:
    if p > ind:
        if spook < S:
            can += p - ind
    ind = p
    spook += c

if ind <= L and spook < S:
    can += L - ind + 1

print(can)