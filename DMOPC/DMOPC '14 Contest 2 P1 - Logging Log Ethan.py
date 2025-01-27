n = int(input())
ans = []
for i in range(n):
    total = 0
    num = int(input())
    for s in range(num):
        k = int(input())
        total += k
    ans.append(total)

for i in range(len(ans)):
    if ans[i] != 0:
        m = i+1
        print('Day %d:'%m, ans[i])
    else:
        print('Weekend')