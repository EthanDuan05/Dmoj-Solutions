t_p = int(input())
n_p = int(input())
p_p = int(input())
total = int(input())
max_t = total//t_p
max_n = total//n_p
max_p = total//p_p
cnt = 0
for t in range(max_t+1):
    # print(t, 'Brown Trout,')
    for n in range(max_n+1):
        for p in range(max_p+1):
            Sum = t*t_p+n*n_p+p*p_p
            if total >= Sum > 0:
                print(t,'Brown Trout,',n,'Northern Pike,',p,'Yellow Pickerel')
                cnt = cnt+1
print('Number of ways to catch fish:', cnt)