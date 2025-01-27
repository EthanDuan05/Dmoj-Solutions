import sys
input = sys.stdin.readline

K = int(input())

N = int(input())
People = []
Time = []

debug = False

for _ in range(N):
    name = input().strip()
    time = int(input())
    People.append(name)
    Time.append(time)

Time_Costs = [1e9 for _ in range(N+1)]
IND = [[] for _ in range(N+1)]

if debug:
    print(People)
    print(Time)

Group = []
for i in range(K):
    Group.append(Time[i])
    Time_Costs[i+1] = max(Group)
    current_group = [x for x in range(i+1)]
    IND[i+1].append(current_group)

for i in range(K+1, N+1):
    MIN = 10000000
    I = 0
    ways = []
    IIND = []
    Skip = 0
    for j in range(1, K+1):
        GGroup = []
        Current_IND = []
        for s in range(j):
            GGroup.append(Time[i-s-1: i])
            Current_IND.append([m for m in range(i-s-1, i)])

        MAX = 100000000
        Final_cost = 0
        Current_IIND = []
        LEN = len(GGroup)
        current_timecost = 0

        if debug:
            print(GGroup, 'GGroup')
            print(Current_IND, 'Current_IND')

        for w in range(LEN):
            if max(GGroup[w]) + Time_Costs[i-len(GGroup[w])] < MAX:
                MAX = max(GGroup[w]) + Time_Costs[i-len(GGroup[w])]
                Skip = len(GGroup[w])
                Final_cost = max(GGroup[w])
                Current_IIND = Current_IND[w]
                current_timecost = Final_cost + Time_Costs[i - len(GGroup[w])]

                if debug:
                    print(Current_IIND, '!!!')
                    print(Current_IND[w], '!!!')

        ways.append(current_timecost)
        IIND.append(Current_IIND)

        if debug:
            print(Current_IIND, 'Last Update')
            print(IIND, 'After Update')

    if debug:
        print(ways, 'ways')
        print(IIND, 'IIND')

    for q in range(len(ways)):
        if ways[q] < MIN:
            MIN = ways[q]
            if debug:
                print(q, 'Q')
            I = q


    Time_Costs[i] = MIN

    if debug:
        print(Skip, 'Skip')

    for a in IND[i-Skip]:
        IND[i].append(a)

    IND[i].append(IIND[I])

print('Total Time: ' + str(Time_Costs[N]))

for i in IND[N]:
    Name = []
    for ind in i:
        Name.append(People[ind])
    print(' '.join(Name))