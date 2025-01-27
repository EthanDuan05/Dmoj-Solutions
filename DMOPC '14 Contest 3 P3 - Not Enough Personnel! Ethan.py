P = int(input())
D = {}

for i in range(P):
    name, skill = input().split()
    skill = int(skill)
    D[(skill, i)] = name

Current_Pair = {}

Q = int(input())
for _ in range(Q):
    current, d = map(int, input().split())
    cnt = 0
    for skill, ind in D.keys():
        if skill in range(current, current+d+1):
            if (current, d) not in Current_Pair:
                diff = abs(skill - current)
                Current_Pair[(current, d)] = [diff, ind, D[skill, ind]]
            else:
                diff = abs(skill - current)
                if diff < Current_Pair[(current, d)][0]:
                    Current_Pair[(current, d)] = [diff, ind, D[skill, ind]]
                elif diff == Current_Pair[(current, d)][0]:
                    if ind < Current_Pair[(current, d)][1]:
                        Current_Pair[(current, d)] = [diff, ind, D[skill, ind]]

        else:
            cnt += 1

    if cnt == P:
        Current_Pair[(current, d)] = [0, 0, 'No suitable teacher!']


for i in Current_Pair.values():
    print(i[2])
