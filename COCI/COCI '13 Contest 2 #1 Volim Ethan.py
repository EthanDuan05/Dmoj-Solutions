Players = ['1', '2', '3', '4', '5', '6', '7', '8']
N = int(input())

T = int(input())

Current_player = N-1
Time = 210

for _ in range(T):
    second, state = input().split()
    second = int(second)

    Time -= second

    if Time > 0:
        if state == 'T':
            if Current_player < 7:
                Current_player += 1
            else:
                Current_player = 0
    else:
        print(Players[Current_player])
        break
