import math
Debug = False

N = int(input())
STOPS_old = []
STOPS_new = []

Limit_old = 132
Limit_new = 251

for s in range(N):
    passen, percen = map(int, input().split())
    STOPS_old.append([passen, percen])
    STOPS_new.append([passen, percen])

if Debug:
    print(STOPS_old)

CNT_old = 0
while sum([i[0] for i in STOPS_old]) > 0:
    P_old = 0
    CNT_old += 1
    for i in range(N):
        pa = STOPS_old[i][0]
        pe = STOPS_old[i][1]
        P_old -= math.floor(P_old * pe/100)
        if P_old + pa <= Limit_old:
            P_old += pa
            STOPS_old[i][0] -= pa
        else:
            max_p = Limit_old - P_old
            P_old = 132
            STOPS_old[i][0] -= max_p

    if Debug:
        print(STOPS_old)

CNT_new = 0
while sum([i[0] for i in STOPS_new]) > 0:
    P_new = 0
    CNT_new += 1
    for i in range(N):
        pa = STOPS_new[i][0]
        pe = STOPS_new[i][1]
        P_new -= math.floor(P_new * pe/100)
        if P_new + pa <= Limit_new:
            P_new += pa
            STOPS_new[i][0] -= pa
        else:
            max_p = Limit_old - P_new
            P_new = 251
            STOPS_new[i][0] -= max_p

if CNT_old - CNT_new < 0:
    print(0)
else:
    print(CNT_old - CNT_new)