line = int(input())
cnt = 0
day = 0

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while day < line:
    day += days[0]
    cnt += 1
    days.remove(days[0])

ans_day = 0

if cnt == 1:
    ans_day = line
elif cnt == 2:
    ans_day = line - 31
elif cnt == 3:
    ans_day = line - 59
elif cnt == 4:
    ans_day = line - 90
elif cnt == 5:
    ans_day = line - 121
elif cnt == 6:
    ans_day = line - 152
elif cnt == 7:
    ans_day = line - 182
elif cnt == 8:
    ans_day = line - 212
elif cnt == 9:
    ans_day = line - 243
elif cnt == 10:
    ans_day = line - 274
elif cnt == 11:
    ans_day = line - 304
elif cnt == 12:
    ans_day = line - 334

if len(str(cnt)) == 1:
    if len(str(ans_day)) == 1:
        print('0' + str(cnt) + '/' + '0' + str(ans_day))
    else:
        print('0' + str(cnt) + '/' + str(ans_day))
else:
    if len(str(ans_day)) == 1:
        print(str(cnt) + '/' + '0' + str(ans_day))
    else:
        print(str(cnt) + '/' + str(ans_day))