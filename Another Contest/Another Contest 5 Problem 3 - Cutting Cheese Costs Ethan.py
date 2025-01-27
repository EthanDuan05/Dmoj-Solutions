N, K = map(int, input().split())
L = []
O = {}

for _ in range(N):
    original, discount = map(int, input().split())
    L.append(original - discount)
    O[original] = original - discount

L.sort()
S = []
for i in range(K):
    delete = L.pop()
    S.append(delete)

cnt = 0
ans = 0
for i in O:
    if O.get(i) not in S:
        ans += i
    else:
        if cnt <= K-1:
            ans += i - O.get(i)
            cnt += 1
            continue
        else:
            ans += i


print(ans)
print(O)