import sys

N, K = map(int, input().split())
arr = list(map(int, input()))

if sum(arr) == 0:
    if K != 0:
        print(1)
    else:
        print(0)

    sys.exit(0)

def check(S):
    for i in range(N-1):
        if S[i] == 1 and S[i+1] == 1:
            S[i] = 0
    return S

check(arr)

ind = []
for i in range(N):
    if arr[i] == 1:
        ind.append(i)

if K == 0:
    print(sum(arr))
    sys.exit(0)

D = []
for i in range(len(ind)-1):
    D.append([abs(ind[i] - ind[i+1]+1), ind[i], ind[i+1]])

D.sort(key=lambda x: x[0])

cnt = 0
for i in D:
    if K - i[0] >= 0:
        K -= i[0]
        cnt += 1
        continue
    else:
        break

D = D[0: cnt]

for i in D:
    s, e = i[1]+1, i[2]
    arr[s: e] = [1 for _ in range(i[0])]

'''
print(''.join(map(str, arr)))

print(''.join(map(str, check(arr))))
'''

print(sum(check(arr)))