import sys
input = sys.stdin.readline

N, T = map(int, input().split())
Target = list(map(int, input().split()))

People = [[] for i in range(N)]

Last = [0 for _ in range(N)]

for i in range(N):
    People[Target[i]-1].append(i)
    People[Target[i]-1].sort()
    Last[i] = Target[i]

Plus = [[] for _ in range(N)]

for _ in range(T-1):
    for i in range(N):
        if People[i]:
            ind = People[i].pop(0)
            Last[i] = ind+1
            Plus[ind].append(i)
        else:
            continue

    for s in range(N):
        if Plus[s]:
            Plus[s].sort()
            People[s] = People[s] + Plus[s]

    '''
    print(Plus)
    print(People, 'People')
    '''

    Plus = [[] for _ in range(N)]

print(' '.join(map(str, Last)))