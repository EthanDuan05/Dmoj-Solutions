import math
N, P = map(int, input().split())

Name_min = ''
Name_max = ''
Min = 1e9
Max = 0
for _ in range(N):
    name, m, cs, e = input().split()
    m = int(m)
    cs = int(cs)
    e = int(e)
    score = math.floor(4 * math.sqrt(m) + 3 * cs**P - 4 * e)
    if score > Max:
        Max = score
        Name_max = name

    if score < Min:
        Min = score
        Name_min = name

print(Name_max, Max)
print(Name_min, Min)