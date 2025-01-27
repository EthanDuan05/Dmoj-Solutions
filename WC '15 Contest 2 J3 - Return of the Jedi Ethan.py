S, E, R = map(int, input().split())
Location = []

for _ in range(S):
    t, x, y = map(int, input().split())
    Location.append((t, x, y))

Location.sort()

cnt = 0
for _ in range(E):
    x, y = map(int, input().split())
    used_type = []
    for i in Location:
        distance = (abs(x-i[1])**2 + abs(y-i[2])**2)**0.5
        if distance <= R:
            if i[0] not in used_type:
                used_type.append(i[0])

        if len(used_type) > 1:
            cnt += 1
            break

print(cnt)


