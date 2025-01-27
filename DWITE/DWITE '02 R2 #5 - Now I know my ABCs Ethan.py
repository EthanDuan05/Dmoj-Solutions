for _ in range(5):
    dic = {}
    line = list(input().strip())
    for i in line:
        if i.isalpha():
            if i.islower():
                i = i.upper()

            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1

    M = sorted(dic)

    ans = []
    for i in M:
        ans.append(i + '-' + str(dic[i]))

    print(':'.join(ans))
