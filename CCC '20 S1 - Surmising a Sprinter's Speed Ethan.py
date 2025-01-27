T = int(input())
L = {}
Time = []

for _ in range(T):
    t, d = map(int, input().split())
    L[t] = d
    Time.append(t)

Time.sort()

MAX_SPEED = -1e9
for i in range(len(Time)-1):
    Current_Speed = abs(L[Time[i+1]] - L[Time[i]]) / (Time[i+1] - Time[i])
    if Current_Speed > MAX_SPEED:
        MAX_SPEED = Current_Speed

print(MAX_SPEED)