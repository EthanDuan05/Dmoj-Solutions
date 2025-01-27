n = int(input())
S_t = []
T_t = []
for i in range(n):
    line = input()
    S = line.count('s') + line.count('S')
    T = line.count('t') + line.count('T')
    S_t.append(S)
    T_t.append(T)

sum_s = sum(S_t)
sum_t = sum(T_t)

if sum_t > sum_s:
    print('English')
elif sum_s > sum_t:
    print('French')
else:
    print('French')
