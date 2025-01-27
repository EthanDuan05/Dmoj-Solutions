k = int(input())
ANS = []
for i in range(k):
    t, k = map(int, input().split())
    if t % k == 0:
        ans = t // k
        ANS.append(ans)
    else:
        ans = abs(t // k)+1
        ANS.append(ans)
for i in ANS:
    print(i)