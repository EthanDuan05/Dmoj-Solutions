ans = []
for i in range(5):
    line_1 = list(input())
    line_2 = list(input())

    L_1 = len(line_1)
    L_2 = len(line_2)

    cnt = 0
    if L_2 >= L_1:
        for s in range(L_1):
            if line_1[s] == line_2[s]:
                cnt += 1
            else:
                break
    elif L_1 > L_2:
        for s in range(L_2):
            if line_1[s] == line_2[s]:
                cnt += 1
            else:
                break
    ans.append(cnt)

for i in ans:
    print(i)