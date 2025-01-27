T = int(input())

for i in range(T):
    s_max, S = input().split()
    s_max = int(s_max)
    total_audience = 0
    need_audience = 0
    for j in range(s_max+1):
        if j > total_audience:
            need_audience += j-total_audience
            total_audience += need_audience

        total_audience += int(S[j])

    print('Case #' + str(i+1) + ': ' + str(need_audience))


