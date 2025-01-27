import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    num = int(input())
    Flag = True
    while Flag:
        str_num = str(num)

        state = False
        for s in range(len(str_num) - 1, 0, -1):
            if str_num[s] < str_num[s - 1]:
                num -= 1
                state = True
                break

        if state:
            continue
        else:
            Flag = False


    print('Case ' + '#' + str(i+1) + ': ' + str(num))


