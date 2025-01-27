D = 'CAMBRIDGE'

S = input()

ans = ''
for i in S:
    if i in D:
        continue
    else:
        ans += i

print(ans)
