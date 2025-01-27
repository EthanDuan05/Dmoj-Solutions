c, n = input().split()
c = int(c)
n = int(n)

T = 1
E = 2
C = 3
M = 4

total = 0

for i in range(c):
    s = input()
    if s == 'TOK':
        s = T
        total = total + T
    if s == 'English':
        s = E
        total = total + E
    if s == 'Chemistry':
        s = C
        total = total + C
    if s == 'Math':
        s = M
        total = total + M

cnt = 0
if total > n:
    for p in range(1, 6):
        for s in range(1, 6):
            if p+s == n and p != s and p < s:
                cnt += 1
    print('Go to Metro')
    print(cnt)

elif total <= n:
    print('YEA BOI')