n, c = map(int, input().split())
L = input().split()

frequency = {}

for i in L:
    if i not in frequency:
        frequency[i] = 1
    else:
        frequency[i] += 1

final = []
for i in range(n, 0, -1):
    if i in frequency.values():
        for s in frequency:
            if frequency[s] == i:
                for _ in range(i):
                    final.append(s)

print(' '.join(final))