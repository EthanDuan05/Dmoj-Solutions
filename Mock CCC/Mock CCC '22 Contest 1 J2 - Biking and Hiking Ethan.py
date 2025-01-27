n, k = map(int, input().split())
section = input()

t_cnt = 0
s_cnt = k
for s in range(n):
    if section[s] == 'U':
        if s_cnt > 0:
            s_cnt -= 1
        if s_cnt == 0:
            t_cnt += 1
    elif section[s] == 'D':
        s_cnt += 1
    elif section[s] == 'F':
        if s_cnt == 0:
            t_cnt += 1

print(t_cnt)