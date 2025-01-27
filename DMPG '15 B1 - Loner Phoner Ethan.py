N = int(input())

for _ in range(N):
    number = input()
    ans = ''
    if len(number) == 10:
        ans += number[0] + number[1] + number[2]
        if ans == '416' or ans == '647':
            print('(' + ans + ')' + '-' + number[3] + number[4] + number[5]
                  + '-' + number[6] + number[7] + number[8] + number[9])
        else:
            print('not a phone number')
    else:
        print('not a phone number')