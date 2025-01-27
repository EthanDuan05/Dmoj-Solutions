initial_p, max_p = map(int, input().split())
time_paper = {}

cnt_time = -1
current_p = initial_p

N = int(input())
for _ in range(N):
    time, paper = map(int, input().split())
    time_paper[time] = paper

symbol = ''
flag = True
while flag:
    cnt_time += 1
    if current_p >= 0:
        if cnt_time in time_paper:
            if current_p + time_paper[cnt_time] <= max_p:
                current_p += time_paper[cnt_time]
            else:
                flag = False
                symbol = 'jams'
    else:
        flag = False
        symbol = 'melts'

    print(current_p)

print('The printer'+' '+symbol+' '+'at'+' '+str(cnt_time)+' '+'second(s).')