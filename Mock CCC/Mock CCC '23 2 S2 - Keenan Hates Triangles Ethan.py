import sys
input = sys.stdin.readline

length = []
N = int(input())

if N < 6:
    print(0)
    sys.exit(0)

for _ in range(N):
    a = int(input())
    length.append(a)

length.sort(reverse=True)

used = []

possible = []

for a in range(0, N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            if length[a] < length[b] + length[c] and len(possible) < 3:
                if (a, b, c) not in used:
                    sum = length[a] + length[b] + length[c]
                    possible.append(sum)
                    used.append((a, b, c))

possible.sort(reverse=True)
print(possible[0] + possible[1])