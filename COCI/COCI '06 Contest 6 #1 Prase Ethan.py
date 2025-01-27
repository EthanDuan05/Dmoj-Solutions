N = int(input())
child = {}

warnings = 0
for _ in range(N):
    name = input()
    if name not in child:
        child[name] = 0

    taken_by_child = child[name]
    taken_by_others = N - taken_by_child
    if taken_by_child > taken_by_others:
        warnings += 1

    child[name] += 1

print(warnings)
