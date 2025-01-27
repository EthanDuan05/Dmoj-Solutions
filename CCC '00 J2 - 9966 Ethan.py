import sys
input = sys.stdin.readline

Applicable_Number = {'0':'0', '1':'1', '8':'8', '9':'6', '6':'9'}

a = int(input())
b = int(input())

cnt = 0
for i in range(a, b+1):
    Num = i
    S_Num = str(Num)
    New_Num = ''
    for s in S_Num:
        if s in Applicable_Number:
            New_Num += Applicable_Number[s]
        else:
            New_Num += s

    New_Num = New_Num[::-1]

    if int(New_Num) == Num:
        Flag = False
        for k in New_Num:
            if k not in Applicable_Number:
                Flag = True
                break

        if not Flag:
            cnt += 1

print(cnt)