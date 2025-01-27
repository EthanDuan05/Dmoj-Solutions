for _ in range(5):
    line = input().split()
    ans = []
    for i in line:
        if i.isdigit():
            ans.append(i)
        else:
            ans.append(i[::-1])
    ans_f = reversed(ans)
    print(' '.join(ans_f))
