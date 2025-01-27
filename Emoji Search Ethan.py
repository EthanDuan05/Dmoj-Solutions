line = list(input())
ans = []
phrase = ''

flag1 = False
flag2 = False

for i in line:
    if i == ':' and (flag1 == False and flag2 == False):
        flag1 = True
    elif i == ':' and (flag1 == True and flag2 == False):
        flag2 = True


    if flag1:
        phrase += i

    if flag2:
        ans.append(phrase)
        phrase = ''
        flag1 = False
        flag2 = False

for i in ans:
    print(i[1:len(i)-1])
